from tkinter.messagebox import QUESTION
from bottle import post, request
import re
import datetime
import pdb

question = {}

@post('/home')
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    
    if not quest or not mail or not username:
        return "Please fill in all fields of the form"

    if not re.match(r"[\w\.\\\-/?%]{2,30}@[a-zA-Z\.-]{1,9}.[a-zA-Z]{2,7}", mail):
        return "Invalid email address format"

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    question[mail] = [username, quest]
    
    pdb.set_trace()  

    
    return "Thanks, %s! The answer will be sent to the email %s. Access Date: %s" % (username, mail, current_date)

print(question)