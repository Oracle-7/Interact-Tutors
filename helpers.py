# Email imports
import os
import smtplib, ssl
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from email.header import Header
from email.utils import formataddr

# Merge dict import
from collections import defaultdict

# Image transpose imports
from PIL import Image
import functools


subject_dict = {
    "math": ["1st-5th Grade Math", "Algebra 1", "Geometry", "Algebra 2", "Trigonometry", "Pre-Calculus", "Calculus", "Statistics", "AMC8/Mathcounts", "AMC10", "AMC12", "AIME"],
    "science": ["Earth Science (6th)", "Life Science (7th)", "Physical Science (8th)", "Biology", "Physiology", "Chemistry", "Physics 1", "Physics C", "Environmental Science", "Psychology", "USAPhO", "USABO"],
    "english": ["6th-8th Grade Literature/Writing", "Literature and Writing (9th)", "World Literature", "American Literature", "European Literature", "AP Literature"],
    "history": ["World History", "U.S. History", "U.S. Government", "European History"],
    "cs": ["Computer Programming Java (9th)", "AP Computer Science A (Java)", "AP Computer Science P", "Machine Learning", "Web Development", "Python", "Data Science", "USACO Bronze", "USACO Silver", "USACO Gold"],
    "language": ["Chinese", "Spanish", "French", "Japanese"], 
    "business": ["Principles of Business", "International Business", "Principles of Marketing", "Economics", "Macroeconomics", "Microeconomics", "Money and Banking", "Law"],
    "speech": ["DECA", "Model UN", "Public Speaking", "Debating"]
}

subject_display_names = {
    "math": "Math",
    "science": "Science",
    "english": "English",
    "history": "History",
    "cs": "Computer Science",
    "language": "Language",
    "business": "Business/Economics",
    "speech": "Speech and Debate"
}

questions_dict = {
    "subjects": "1",
    "description": "2",
    "motivation": "3",
    "extra": "4",
    "mathExperience": "5",
    "scienceExperience": "6",
    "englishExperience": "7",
    "historyExperience": "8",
    "csExperience": "9",
    "languageExperience": "10",
    "businessExperience": "11",
    "referral": "14",
    "speechExperience": "15"
}

ALLOWED_IMG_EXTENSIONS = {'jpg', 'png', 'jpeg'}
contact_email_counter = 0


def allowed_file(filename):
    # Inspired from Flask documentation
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_IMG_EXTENSIONS

# Crop image based on x, y, w, h
def crop_image(img, file_path, x, y, w, h):
    pass

# Code from https://realpython.com/python-send-email/#starting-a-secure-smtp-connection
def send_email(to_addrs, subject, text, html=""):
    if html:
        msg = MIMEMultipart('alternative')
    else:
        msg = MIMEMultipart()
    username = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    msg['From'] = formataddr((str(Header('Interact Tutors', 'utf-8')), username))
    msg['To'] = ", ".join(to_addrs) if isinstance(to_addrs, list) else to_addrs
    msg['Subject'] = subject
    
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(username, password)
    
    server.sendmail(msg['From'], to_addrs, msg.as_string())


# Code from https://stackoverflow.com/questions/3421906/how-to-merge-lists-of-dictionaries
def merge_list(lst, key):
    merged = {}
    for item in lst:
        if item[key] in merged:
            merged[item[key]] = merge_dict(merged[item[key]], item)
            # merged[item[key]].update(item)
        else:
            merged[item[key]] = item
    return merged.values()


# Merges two dictionaries by appending rather than overwriting keys
def merge_dict(d1, d2):
    for key,val in d2.items():
        if key in d1 and d1[key] != val:
            if not isinstance(d1[key], list):
                d1[key] = d1[key].split("%")
            d1[key].append(val)
        else: # key is not in d1
            d1[key] = val
    return d1


# Neatly prints the contents of a list of dictionaries
def print_inventory(dct_list):
    print("\n\n")
    for dct in dct_list:
        print("\nItems held:")
        for item, amount in dct.items():  # dct.iteritems() in Python 2
            print("{} ({})".format(item, amount))

    print("\n\n")


# Filter for Jinja template
def is_string(value):
    return isinstance(value, str)


# Code from https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
def image_transpose_exif(im):
    """
    Apply Image.transpose to ensure 0th row of pixels is at the visual
    top of the image, and 0th column is the visual left-hand side.
    Return the original image if unable to determine the orientation.

    As per CIPA DC-008-2012, the orientation field contains an integer,
    1 through 8. Other values are reserved.

    Parameters
    ----------
    im: PIL.Image
       The image to be rotated.
    """

    exif_orientation_tag = 0x0112
    exif_transpose_sequences = [                   # Val  0th row  0th col
        [],                                        #  0    (reserved)
        [],                                        #  1   top      left
        [Image.FLIP_LEFT_RIGHT],                   #  2   top      right
        [Image.ROTATE_180],                        #  3   bottom   right
        [Image.FLIP_TOP_BOTTOM],                   #  4   bottom   left
        [Image.FLIP_LEFT_RIGHT, Image.ROTATE_90],  #  5   left     top
        [Image.ROTATE_270],                        #  6   right    top
        [Image.FLIP_TOP_BOTTOM, Image.ROTATE_90],  #  7   right    bottom
        [Image.ROTATE_90],                         #  8   left     bottom
    ]

    try:
        seq = exif_transpose_sequences[im._getexif()[exif_orientation_tag]]
    except Exception:
        return im
    else:
        return functools.reduce(type(im).transpose, seq, im)