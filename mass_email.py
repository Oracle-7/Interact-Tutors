from database import Db
from helpers import send_email
from email_templates import mass_email_default, mass_email_html

DB = Db()

tutors = DB.execute("SELECT email FROM tutors WHERE status = 1")
emails = [tutor["email"] for tutor in tutors]
emails.append("mvistainteract@gmail.com")

for email in emails:
    send_email(email, "Interact Tutors Update", mass_email_default, mass_email_html)

DB.close_connection()