from bottle import post, request
import re
import datetime

@post('/home')
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')

    if not quest or not mail or not username:
        return "Please fill in all fields of the form"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        return "Invalid email address format"

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    return "Thanks, %s! The answer will be sent to the email %s. Access Date: %s" % (username, mail, current_date)