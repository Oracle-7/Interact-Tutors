# Contact Emails
contact_email_default = """\
%s has sent the following message from the email %s through the Interact Tutors website contact form:

%s

Please respond to them within 1-2 days :)
"""

contact_email_html = """\
<html>
    <head>
        <style>
            .content, .im {
                color: #000 !important;
                font-family: Arial, sans-serif;
                font-size: 15px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <b>%s</b> has sent the following message from the email <b>%s</b> through the Interact Tutors website contact form:<br><br>

            <i>%s</i><br><br>

            Please respond to them within 1-2 days :)
        </div>
    </body>
</html>
"""

# Acceptance Emails
acceptance_email_default = """\
Dear %s, 

Thanks for registering as a tutor for Interact Tutors; we loved your application and are glad to have you with us! This program was designed to give back to our community during these 
difficult times whilst allowing tutors and tutees to meet new people, and so we’re extremely thankful that you’ve decided to join us in our path to achieving this goal. 

As of now, your profile is displayed on our website 
at interacttutors.com/find-a-tutor, and tutees who wish to schedule sessions with you will email you with a request. If you would like to tutor them, you are to email 
them back with questions you may have (such as their experience with the subject, when and how often they want tutoring sessions, etc) and/or schedule a date for a possible 
test session over Zoom. If they enjoy the test session, you may begin scheduling additional sessions that fit both 
your schedules. For each session (including the test session), it is your responsibility to ensure that the tutee fills out the confirmation form at interacttutors.com/confirm so you can 
receive the appropriate volunteer hours. To view your hours, visit interacttutors.com/hours.

Some pieces of advice: 

1. Be Flexible
All tutees have different needs and backgrounds, and so it's your job as a tutor to be flexible with whatever they might request. For example, some students may simply 
want you to help guide them through their homework while others might want you to teach them a subject they've had no prior experience with. You should always be open 
to their requests and adapt accordingly.

2. Be Prepared
There's nothing more embarrassing than going ten minutes into a lesson and realizing you don't have any more material to teach — prepare for lessons beforehand! This 
could be as simple as asking them to send a few pictures of their homework for you to preview, or it could be planning out specific topics to go over if you're teaching 
them new material. We highly advise that you plan more material than you think you have time to cover; this way, you won't encounter any issues even if your tutee is 
speeding through your lesson. Additionally, being prepared includes being early to meetings; besides giving you time to prepare for the session, it also sets a good 
example and shows your commitment to helping your tutee learn. Make sure to try out zoom host controls beforehand to get a feel for the process; if you're unfamiliar with 
host controls, feel free to check out support.zoom.us/hc/en-us/articles/206618765-Zoom-video-tutorials or email us with further questions.

3. Be Patient
Sometimes it may be frustrating when your tutee doesn't seem to understand a topic no matter how many different ways you try to explain it. In these cases, it's always 
important to remember that all tutees learn at a different rate. As long as you're trying your best and staying positive, it's perfectly fine if your tutee doesn't understand at first; after 
all, tutoring is a learning process that you'll only get better at over time.

4. Be Proactive
As a tutor, you should always try to adopt a proactive approach when solving problems. If you and your tutee are having issues, be sure to contact their parents to try and 
resolve the situation immediately; if you think we could help as well, you may contact us for assistance. Also, we recommend you provide parents with a weekly or biweekly update 
on what you and your tutee have covered in your lessons to ensure they are up-to-date with their child's academic progress.

5. Have Fun!
Ultimately, this tutoring experience is meant to be enjoyable and help you and your tutee grow both individually and academically, so don't take things too seriously! We 
highly encourage you to connect with your tutee personally as well as academically, as your sessions will be far more enjoyable and the overall process more rewarding when 
you can form interpersonal connections with your tutees.

If you have any questions or concerns, want to change your picture/responses on our website, or simply want some more guidance, feel free to email us or contact us at 
interacttutors.com/contact and we'll be happy to help :)

Have fun tutoring! 

Best,
Interact Tutors
Service Over Self
21840 McClellan Rd · Cupertino, CA 95014
www.interacttutors.com
"""

acceptance_email_html = """\
<html>
    <head>
        <style>
            .content, .im {
                color: #000 !important;
                font-family: Arial, sans-serif;
                font-size: 15px;
            }

            .advice {
                font-weight: bold;
            }

            .advice span {
                font-weight: normal;
            }
        </style>
    </head>
    <body>
        <div class="content">
            Dear %s,<br><br>
                    
            Thanks for registering as a tutor for Interact Tutors; we loved your application and are glad to have you with us! This program was designed to give back to our 
            community during these difficult times whilst allowing tutors and tutees to meet new people, and so we’re extremely thankful that you’ve decided to join us in our 
            path to achieving this goal.<br><br>

            As of now, your profile is displayed on our website 
            <a href="interacttutors.com/find-a-tutor">here</a>, and tutees who wish to schedule sessions with you will email you with a request. If you would like to tutor them, you are to email 
            them back with questions you may have (such as their experience with the subject, when and how often they want tutoring sessions, etc) and/or schedule a date for a possible 
            test session over Zoom. If they enjoy the test session, you may begin scheduling additional sessions that fit both 
            your schedules. <strong>For each session (including the test session), it is your responsibility to ensure that the tutee fills out the confirmation form at 
            <a href="interacttutors.com/confirm">interacttutors.com/confirm</a> so you can receive the appropriate volunteer hours.</strong> To view your hours, visit 
            <a href="interacttutors.com/hours">interacttutors.com/hours</a>.<br><br>

            Some pieces of advice: 
            <ol class="advice">
                <li>Be Flexible<br>
                    <span>
                        All tutees have different needs and backgrounds, and so it's your job as a tutor to be flexible with whatever they might request. For example, some students may simply 
                        want you to help guide them through their homework while others might want you to teach them a subject they've had no prior experience with. You should always be open 
                        to their requests and adapt accordingly.
                    </span>
                </li><br>

                <li>Be Prepared<br>
                    <span>
                        There's nothing more embarrassing than going ten minutes into a lesson and realizing you don't have any more material to teach — prepare for lessons beforehand! This 
                        could be as simple as asking them to send a few pictures of their homework for you to preview, or it could be planning out specific topics to go over if you're teaching 
                        them new material. We highly advise that you plan more material than you think you have time to cover; this way, you won't encounter any issues even if your tutee is 
                        speeding through your lesson. Additionally, being prepared includes being early to meetings; besides giving you time to prepare for the session, it also sets a good 
                        example and shows your commitment to helping your tutee learn. Make sure to try out zoom host controls beforehand to get a feel for the process; if you're unfamiliar with 
                        host controls, feel free to check out <a href="support.zoom.us/hc/en-us/articles/206618765-Zoom-video-tutorials">this link</a> or email us with further questions.
                    </span>
                </li><br>

                <li>Be Patient<br>
                    <span>
                        Sometimes it may be frustrating when your tutee doesn't seem to understand a topic no matter how many different ways you try to explain it. In these cases, it's always 
                        important to remember that all tutees learn at a different rate. As long as you're trying your best and staying positive, it's perfectly fine if your tutee doesn't understand at first; after 
                        all, tutoring is a learning process that you'll only get better at over time.
                    </span>
                </li><br>

                <li>Be Proactive<br>
                    <span>
                        As a tutor, you should always try to adopt a proactive approach when solving problems. If you and your tutee are having issues, be sure to contact their parents to try 
                        and resolve the situation immediately; if you think we could help as well, you may contact us for assistance. Also, we recommend you provide parents with a weekly or 
                        biweekly update on what you and your tutee have covered in your lessons to ensure they are up-to-date with their child's academic progress.
                    </span>
                </li><br>

                <li>Have Fun!<br>
                    <span>
                        Ultimately, this tutoring experience is meant to be enjoyable and help you and your tutee grow both individually and academically, so don't take things too seriously! We 
                        highly encourage you to connect with your tutee personally as well as academically, as your sessions will be far more enjoyable and the overall process more rewarding when 
                        you can form interpersonal connections with your tutees.
                    </span>
                </li>
            </ol>
            
            If you have any questions or concerns, want to change your picture/responses on our website, or simply want some more guidance, feel free to email us or contact us at 
            <a href="interacttutors.com/contact">interacttutors.com/contact</a> and we'll be happy to help :)<br><br>
            
            Have fun tutoring!<br><br>

            Best,<br>
            Interact Tutors<br>
            <span style="color: #777">Service Over Self<br>
            21840 McClellan Rd · Cupertino, CA 95014</span><br>
            <a href="www.interacttutors.com">www.interacttutors.com</a>
        </div>
    </body>
</html>
"""

# Mass Emails
mass_email_default = """\
Hey tutors,

To provide some guidance to all of you who may need some advice and suggestions on tutoring, we've asked guest speaker Hung Wei to give a short 
presentation on important aspects of tutoring that will help you form better relationships with your tutees. Hung Wei is a former School Board 
President and now a member of the Cupertino City Council; the three points she will be focusing on are time commitment, building trust, and being 
a tutor of the heart. Below is the Zoom invitation:

https://fuhsd-org.zoom.us/j/4575165295?pwd=eG9YRHg1alY3SGIyRmlOd3dSM1JFdz09
Meeting ID: 457 516 5295
Passcode: 323930

The meeting will be on Monday, 10/9 at 4PM. We highly encourage all of you to attend to improve your tutoring skills!

Best,
Interact Tutors
Service Over Self
21840 McClellan Rd · Cupertino, CA 95014
www.interacttutors.com
"""

mass_email_html = """\
<html>
    <head>
        <style>
            .content, .im {
                color: #000 !important;
                font-family: Arial, sans-serif;
                font-size: 15px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            Hey tutors,<br><br>
                    
            To provide some guidance to all of you who may need some advice and suggestions on tutoring, we've asked guest speaker Hung Wei to give a short 
            presentation on important aspects of tutoring that will help you form better relationships with your tutees. Hung Wei is a former School Board 
            President and now a member of the Cupertino City Council; the three points she will be focusing on are time commitment, building trust, and being 
            a tutor of the heart. Below is the Zoom invitation:<br><br>

            <a href="https://fuhsd-org.zoom.us/j/4575165295?pwd=eG9YRHg1alY3SGIyRmlOd3dSM1JFdz09">https://fuhsd-org.zoom.us/j/4575165295?pwd=eG9YRHg1alY3SGIyRmlOd3dSM1JFdz09</a><br>
            Meeting ID: 457 516 5295<br>
            Passcode: 323930<br><br>
            
            The meeting will be on Monday, 10/9 at 4PM. We highly encourage all of you to attend to improve your tutoring skills!<br><br>
            
            Best,<br>
            Interact Tutors<br>
            <span style="color: #777">Service Over Self<br>
            21840 McClellan Rd · Cupertino, CA 95014</span><br>
            <a href="www.interacttutors.com">www.interacttutors.com</a>
        </div>
    </body>
</html> 
"""