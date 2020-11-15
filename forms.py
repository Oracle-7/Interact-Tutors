from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SelectMultipleField, RadioField, TextAreaField, TextField, FileField, DateField, DecimalField, HiddenField, SubmitField, widgets
from wtforms.validators import DataRequired, Email, Optional, ValidationError, NumberRange
from flask_wtf.file import FileRequired
import decimal

from helpers import subject_dict


subjectLimit = 3
studentGradeLimit = 5

# Helper classes

# Code from wtforms documentation
class Length(object):
    def __init__(self, min=-1, max=-1, minMessage=None, maxMessage=None):
        self.min = min
        self.max = max
        if not minMessage:
            minMessage = 'Field must be at least %i characters long' % (min)
        if not maxMessage:
            maxMessage = 'Field cannot be longer than %i characters' % (max)
        self.minMessage = minMessage
        self.maxMessage = maxMessage

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min:
            raise ValidationError(self.minMessage)
        elif self.max != -1 and l > self.max:
            raise ValidationError(self.maxMessage)

length = Length

# Field with multiple checkboxes
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Decimal field with rounding, taken from https://stackoverflow.com/questions/27781926/decimal-field-rounding-in-wtforms
class BetterDecimalField(DecimalField):
    """
    Very similar to WTForms DecimalField, except with the option of rounding
    the data always.
    """
    def __init__(self, label=None, validators=None, places=2, rounding=None,
                 round_always=False, **kwargs):
        super(BetterDecimalField, self).__init__(
            label=label, validators=validators, places=places, rounding=
            rounding, **kwargs)
        self.round_always = round_always

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = decimal.Decimal(valuelist[0])
                if self.round_always and hasattr(self.data, 'quantize'):
                    exp = decimal.Decimal('.1') ** self.places
                    if self.rounding is None:
                        quantized = self.data.quantize(exp)
                    else:
                        quantized = self.data.quantize(
                            exp, rounding=self.rounding)
                    self.data = quantized
            except (decimal.InvalidOperation, ValueError):
                self.data = None
                raise ValueError(self.gettext('Not a valid decimal value'))


# Tutor Application Form
class TutorApplicationForm(FlaskForm):
    name = StringField("Full Name", [
        DataRequired("Please enter your name"),
        length(min=3, max=50),
    ])

    email = StringField("Email", [
        DataRequired("Please enter your email"),
        Email("Please enter a valid email"),
        length(max=50)
    ])  

    grade = RadioField("Grade", [DataRequired("Must choose a grade")], choices=[
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ] , default="9")

    math = MultiCheckboxField("Math subjects", choices=[
        (className, className) for className in subject_dict["math"]
    ])
    
    science = MultiCheckboxField("Science subjects", choices=[
        (className, className) for className in subject_dict["science"]
    ])

    english = MultiCheckboxField("English subjects", choices=[
        (className, className) for className in subject_dict["english"]
    ])

    history = MultiCheckboxField("History subjects", choices=[
        (className, className) for className in subject_dict["history"]
    ])

    cs = MultiCheckboxField("Computer Science subjects", choices=[
        (className, className) for className in subject_dict["cs"]
    ])

    language = MultiCheckboxField("World Language subjects", choices=[
        (className, className) for className in subject_dict["language"]
    ])

    business = MultiCheckboxField("Business/Economics subjects", choices=[
        (className, className) for className in subject_dict["business"]
    ])

    speech = MultiCheckboxField("Speech and Debate subjects", choices=[
        (className, className) for className in subject_dict["speech"]
    ])

    # Experience textfields
    mathExperience = TextAreaField("Describe your past math experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    scienceExperience = TextAreaField("Describe your past science experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    englishExperience = TextAreaField("Describe your past English experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    historyExperience = TextAreaField("Describe your past history experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    csExperience = TextAreaField("Describe your past CS experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    languageExperience = TextAreaField("Describe your past language experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    businessExperience = TextAreaField("Describe your past business and/or economics experience, including classes, grades, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})

    speechExperience = TextAreaField("Describe your past speech and debate experience, including classes, clubs, and/or achievements.",
        [Optional(), length(max = 300)], render_kw={"disabled": "true", "placeholder": "Field will be enabled when you check a box under this subject."})


    # Additional fields
    description = TextAreaField("Provide a 4-5 sentence description of who you are in first person.", [DataRequired("Please enter a description"), length(max = 300)])

    motivation = TextAreaField("Describe some of the reasons you would like to tutor, as well as your experience with tutoring (if any).",
        [DataRequired("Please describe your motivations for tutoring"), length(max = 300)])

    referral = TextAreaField("How did you hear about us?", [Optional(), length(max = 300)])

    extra = TextAreaField("Anything else you want to let us know?", [Optional(), length(max = 300)])

    image = FileField("Please attach a image of yourself in good lighting (you may see our website's tutor page for examples). Allowed formats are .jpg, .jpeg, and .png.",
        [FileRequired("Please attach an image of yourself")])

    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()


# Contact Form
class ContactForm(FlaskForm):
    name = StringField("Name", [
        DataRequired("Please enter your name"),
        length(min=3, max=50)
    ], render_kw={"placeholder": "Your Name"})

    email = StringField("Email", [
        DataRequired("Please enter your email address"),
        Email(message="Not a valid email address"),
        length(max=50)
    ], render_kw={"placeholder": "Email"})

    subject = StringField("Subject", [
        DataRequired("Please enter a subject")
    ], render_kw={"placeholder": "Subject"})

    message = TextAreaField("Message", [
        DataRequired("Please enter your message")
    ], render_kw={"placeholder": "Message"})


class SessionConfirmationForm(FlaskForm):
    name = StringField("Your Name", [
        DataRequired("Please enter your name"),
        length(min=3, max=50)
    ])

    tuteeEmail = StringField("Your Email", [
        DataRequired("Please enter your email address"),
        Email(message="Not a valid email address"),
        length(max=50)
    ])

    tutorEmail = StringField("Tutor Email", [
        DataRequired("Please enter your tutor's email address"),
        Email(message="Not a valid email address"),
        length(max=50)
    ])

    sessionDate = DateField("Date (format: MM-DD-YYYY)", [
        DataRequired("Not a valid date value")
    ], format="%m-%d-%Y")

    hours = BetterDecimalField("Hours", [
        DataRequired("Not a valid decimal value"),
        NumberRange(min=0, max=5, message="Value must be between 0 and 5 hours")
    ], places=1, round_always=True)

    comments = TextAreaField("Any feedback on the session? (Optional)", [Optional(), length(max = 300)])


class HoursForm(FlaskForm):
    email = StringField("Email", [
        DataRequired("Please enter your email address"),
        Email(message="Not a valid email address"),
        length(max=50)
    ])