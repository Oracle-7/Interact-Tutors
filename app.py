from flask import Flask, flash, request, redirect, url_for, render_template, Markup

import os
from datetime import datetime
import secrets
import sqlite3
from mysql import connector
from database import Db
from werkzeug.utils import secure_filename
from hashlib import md5
from helpers import allowed_file, send_email, merge_list, subject_dict, subject_display_names
from helpers import questions_dict, print_inventory, is_string, image_transpose_exif
from email_templates import contact_email_default, contact_email_html, acceptance_email_default, acceptance_email_html
from forms import TutorApplicationForm, ContactForm, SessionConfirmationForm, HoursForm
from PIL import Image

from flask_basicauth import BasicAuth


IMG_UPLOAD_FOLDER = os.path.abspath("./static/img/tutors/")

app = Flask("__name__")
app.secret_key = secrets.token_urlsafe(32)
app.jinja_env.filters['is_string'] = is_string
app.config["IMG_UPLOAD_FOLDER"] = IMG_UPLOAD_FOLDER
app.config["BASIC_AUTH_USERNAME"] = os.getenv("BASIC_AUTH_USER")
app.config["BASIC_AUTH_PASSWORD"] = os.getenv("BASIC_AUTH_PASS")

basic_auth = BasicAuth(app)


# Home page
@app.route("/")
def index():
    return render_template("index.html", subject_dict=subject_dict, subject_display_names=subject_display_names)


# Tutors page
@app.route("/find-a-tutor", methods=["GET", "POST"])
def tutors():

    if request.method == "POST":
        className = request.form.get("subject-search")
        
        if not className:
            flash("Please select a subject.", "error")
            return redirect(url_for("tutors"))

        subject = [k for k,v in subject_dict.items() if className in v][0]

        DB = Db()
        query = ("SELECT tutors.tutorID, name, email, grade, image, status, questionName, answerText "
                "FROM tutors JOIN answers ON tutors.tutorID = answers.tutorID JOIN questions on answers.questionID = questions.questionID "
                "WHERE status = 1 AND tutors.tutorID IN (SELECT DISTINCT tutorID from answers WHERE answerText = %s) "
                "AND (questionName = 'description' OR questionName = 'motivation' OR questionName = %s);")
        arguments = (className, subject + "Experience")
        tutors = DB.execute(query, arguments)

        if tutors:
            for tutor in tutors:
                tutor[tutor["questionName"]] = tutor["answerText"]
                tutor.pop("questionName")
                tutor.pop("answerText")
        
            tutors = merge_list(tutors, "tutorID")

            tutors = sorted(tutors, key=lambda k: k['name'].lower())

        
        DB.close_connection()
        return render_template("tutors.html", tutors=tutors, className=className, subject=subject, subject_dict=subject_dict, subject_display_names=subject_display_names)


    DB = Db()
    query = ("SELECT tutors.tutorID, name, email, grade, image, status, questionName, answerText "
                "FROM tutors JOIN answers ON tutors.tutorID = answers.tutorID JOIN questions on answers.questionID = questions.questionID "
                "WHERE status = 1;")
    tutors = DB.execute(query)
    
    for tutor in tutors:
        tutor[tutor["questionName"]] = tutor["answerText"]
        tutor.pop("questionName")
        tutor.pop("answerText")

    tutors = merge_list(tutors, "tutorID")
    tutors = sorted(tutors, key=lambda k: k['name'].lower()) # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

    # Define list of subjects
    subjects = subject_dict.keys()

    DB.close_connection()
    return render_template("tutors.html", tutors=tutors, subjects=subjects, subject_dict=subject_dict, subject_display_names=subject_display_names)


# Volunteer page
@app.route("/volunteer", methods=["GET", "POST"])
def volunteer():
    form = TutorApplicationForm()

    if form.validate_on_submit():

        # Get form data
        data = form.data
        for value in data:
            value = value.strip()

        # Get form values
        name = data["name"]
        email = data["email"]
        grade = data["grade"]

        # Connect to database
        DB = Db()

        # Test if user is already registered as a tutor/potential tutor
        result = DB.execute("SELECT * from tutors WHERE email = %s", (email, ))
        if result:
            if result[0]["status"] == 1:
                flash("This email is already registered as a tutor.", "error")
            else:
                flash("This email is already registered as a potential tutor.", "error")
            return render_template("volunteer.html", form=form)

        # Get user responses

        # Get classes
        subjects = subject_dict.keys()
        classes = []
        for subject in [data[i] for i in subjects]:
            for className in subject:
                classes.append(className)

        # Get experiences
        mathExperience = data["mathExperience"]
        scienceExperience = data["scienceExperience"]
        englishExperience = data["englishExperience"]
        historyExperience = data["historyExperience"]
        csExperience = data["csExperience"]
        languageExperience = data["languageExperience"]
        businessExperience = data["businessExperience"]
        speechExperience = data["speechExperience"]

        description = data["description"]
        motivation = data["motivation"]
        referral = data["referral"]
        extra = data["extra"]
        image = data["image"]
        x = data["x"]
        y = data["y"]
        w = data["w"]
        h = data["h"]

        # Store tutor profile information
        if allowed_file(image.filename):

            # Protect against forged filenames
            filename = secure_filename(image.filename)

            # Hash the file
            filename = secrets.token_urlsafe(16) + ".jpeg"

            # Save image to images folder
            image_path = os.path.join(app.config["IMG_UPLOAD_FOLDER"], filename)
            image.save(image_path)

            # If user used JCrop, crop the image
            if w:
                x = float(x)
                y = float(y)
                w = float(w)
                h = float(h)
                temp = Image.open(image_path)
                temp = image_transpose_exif(temp)
                
                # Get dpi of image
                dpi = (300, 300)
                if 'dpi' in temp.info:
                    dpi = temp.info['dpi']

                # Modify crop width to fit image size (instead of the size displayed in the browser)
                height = temp.size[1]
                browserH = 300 # The height of the image in the browser

                # Resize image to match browser dimensions * scale
                scale = height / browserH
                temp = temp.crop((x * scale, y * scale, (x + w) * scale, (y + h) * scale)) # Crop image using JCrop browser dimensions
                temp.thumbnail((692, 400)) # Make image smaller while maintaining 1.73 aspect ratio (for browser)
                temp = temp.convert('RGB')
                temp.save(image_path, 'jpeg', quality=90, dpi=dpi)

            # Define query and arguments
            date = datetime.now().strftime("%Y-%m-%d")
            query = "INSERT INTO tutors (name, email, grade, image, hours, applyDate) VALUES(%s, %s, %s, %s, %s, %s)"
            arguments = (name, email, grade, filename, 0, date)
            
            # Connect to DB & execute insert query
            DB.execute(query, arguments)
        else:
            flash("Invalid image format (only .jpg, .jpeg, and .png are allowed). Please try again.", "error")
            DB.close_connection()
            return render_template("volunteer.html", form=form)


        # Store tutor answers

        tutorID = DB.execute("SELECT LAST_INSERT_ID() AS id")[0]["id"]

        # Store subjects they want to teach
        for className in classes:
            if className:
                query = "INSERT INTO answers(formID, questionID, tutorID, answerText) VALUES(%s, %s, %s, %s)"
                arguments = (1, 1, tutorID, className)
                DB.execute(query, arguments)

        # Store other answers
        for questionName in questions_dict:
            if questionName != "subjects":
                query = "INSERT INTO answers(formID, questionID, tutorID, answerText) VALUES(%s, %s, %s, %s)"
                arguments = (1, questions_dict[questionName], tutorID, locals()[questionName])
                DB.execute(query, arguments)

        flash("Thanks for applying! The application process typically takes up to 1 week; if you're accepted, we'll send you an email with further details on the tutoring process.")
        DB.close_connection()
        return redirect(url_for("volunteer"))

    return render_template("volunteer.html", form=form, subject_dict=subject_dict, subject_display_names=subject_display_names)


# Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        send_email("charles.zhu04@gmail.com", "Interact Tutors: " + subject, contact_email_default % (name, email, message),
            contact_email_html % (name, email, message))
        flash("Thanks for your message! We usually respond within 1-2 days.")

        return redirect(url_for("contact"))
        
    return render_template("contact.html", form=form)


# Confirm Tutors page
@app.route("/confirm-tutors", methods=["GET", "POST"])
@basic_auth.required
def confirm_tutors():
    if request.method == "POST":
        decision = request.form.get("submit-btn")
        tutorID = request.form.get("tutorID")
        DB = Db()

        if decision == "Accept":
            status = 1
        elif decision == "Move to Pending":
            status = 0
        elif decision == "Reject":
            status = -1
        elif decision == "Remove":
            status = -2
        else:
            flash(Markup(f"ERROR: Invalid Status. Please report this incident <a href={ url_for('contact') }>here</a>."), "error")
            return redirect(url_for("confirm_tutors"))    

        # Remove tutor
        if status == -2:
            tutor = DB.execute("SELECT * from tutors WHERE tutorID = %s", (tutorID,))[0]

            DB.execute("INSERT INTO removedTutors (name, email, grade, image, hours, applyDate) VALUES (%s, %s, %s, %s, %s, %s)",
                (tutor['name'], tutor['email'], tutor['grade'], tutor['image'], tutor['hours'], tutor['applyDate']))
            DB.execute("DELETE FROM answers WHERE tutorID = %s", (tutorID,))
            DB.execute("DELETE FROM tutors WHERE tutorID = %s", (tutorID,))

        # Change tutor status
        else:
            # If accepted, send acceptance email
            if status == 1:
                tutor = DB.execute("SELECT name, email from tutors WHERE tutorID = %s", (tutorID,))[0]
                first_name = tutor['name'].split()[0]
                send_email(tutor['email'], "Interact Tutors Acceptance", acceptance_email_default % (first_name),
                acceptance_email_html % (first_name))

            DB.execute("UPDATE tutors SET status = %s WHERE tutorID = %s", (status, tutorID))

        flash("Status updated!")
        DB.close_connection()
        return redirect(url_for("confirm_tutors"))

    DB = Db()
    query = ("SELECT tutors.tutorID, name, email, grade, image, hours, applyDate, status, questionName, answerText "
                "FROM tutors JOIN answers ON tutors.tutorID = answers.tutorID JOIN questions on answers.questionID = questions.questionID;")
    tutors = DB.execute(query)
    
    for tutor in tutors:
        tutor[tutor["questionName"]] = tutor["answerText"]
        tutor.pop("questionName")
        tutor.pop("answerText")

    tutors = merge_list(tutors, "tutorID")

    tutors = sorted(tutors, key=lambda k: k['name'].lower()) # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

    # Define list of subjects
    subjects = subject_dict.keys()

    DB.close_connection()
    return render_template("confirmTutors.html", tutors=tutors, subjects=subjects)


# Confirm Session page
@app.route("/confirm", methods=["GET", "POST"])
def confirm_session():
    form = SessionConfirmationForm()

    if form.validate_on_submit():
        name = form.name.data
        tuteeEmail = form.tuteeEmail.data
        tutorEmail = form.tutorEmail.data
        date = str(form.sessionDate.data)
        hours = form.hours.data
        comments = form.comments.data

        # Connect to database        
        DB = Db()

        # Make sure tuteeEmail isn't the same as tutorEmail
        if tuteeEmail == tutorEmail:
            flash("Your email can't be the same as your tutor's email. Please try again.", "error")
            return render_template("confirmSession.html", form=form)

        # Check if tutor exists
        tutor = DB.execute("SELECT * from tutors WHERE email = %s AND status = 1", (tutorEmail, ))
        if not tutor:
            flash(Markup(f"The email you entered doesn't seem to be registered as a tutor. Please check to make sure you typed it correctly, \
                or <a href={ url_for('contact') }>contact us</a> if you think this is an error."), "error")
            return render_template("confirmSession.html", form=form)

        # Log tutee name and email if they don't exist in the database, then get their ID
        tutee = DB.execute("SELECT * from tutees where email = %s", (tuteeEmail, ))
        tuteeID = -1
        if tutee:
            tuteeID = tutee[0]["tuteeID"]
        else:
            DB.execute("INSERT INTO tutees (name, email, status) VALUES (%s, %s, %s)", (name, tuteeEmail, 0))
            tuteeID = DB.execute("SELECT LAST_INSERT_ID() AS id")[0]["id"]

        # Log session in database
        DB.execute("INSERT INTO sessionLogs (sessionDate, hours, comments, tutorID, tuteeID) VALUES (%s, %s, %s, %s, %s)", 
            (date, hours, comments, tutor[0]["tutorID"], tuteeID))

        # Give tutor the appropriate hours
        DB.execute("UPDATE tutors SET hours = hours + %s WHERE email = %s", (hours, tutorEmail))

        flash("Thank you for confirming! We've given your tutor their volunteer hours.")
        return redirect(url_for("confirm_session"))

    return render_template("confirmSession.html", form=form)


# View Tutoring Hours page
@app.route("/hours", methods=["GET", "POST"])
def hours():
    form = HoursForm()

    if form.validate_on_submit():
        email = form.email.data

        DB = Db()
        tutor = DB.execute("SELECT tutorID, hours FROM tutors WHERE email = %s AND status = 1", (email,)) 

        # Check if email is registered as a tutor
        if not tutor:
            flash(Markup(f"This email doesn't seem to be registered as a tutor. Please check to make sure you typed it correctly, \
                or <a href={ url_for('contact') }>contact us</a> if you think this is an error."), "error")
            return render_template("hours.html", form=form)

        # Convert hours to integer if hours is a whole number
        hours = tutor[0]['hours']
        hours = hours if hours % 1 != 0 else int(hours)

        if hours == 1:
            flash(Markup(f"You currently have 1 volunteer hour. Please <a href={ url_for('contact') }>contact us</a> if you think this is an error."))
        else:
            flash(Markup(f"You currently have { hours } volunteer hours. Please <a href={ url_for('contact') }>contact us</a> if you think this is an error."))

        return redirect(url_for("hours"))
        

    return render_template("hours.html", form=form)


# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404