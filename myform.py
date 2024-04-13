from tkinter.messagebox import QUESTION
from bottle import post, request
import re
import datetime
import json

question = {}

def check_question_validity(quest):
    if len(quest) > 3 and not quest.isdigit():
        return True
    return False

def update_json_file(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_json_file():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

@post('/home')
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')

    if not quest or not mail or not username:
        return "Please fill in all fields of the form"

    if not re.match(r"[\w\.\\\-/?%]{2,30}@[a-zA-Z\.-]{1,9}.[a-zA-Z]{2,7}", mail):
        return "Invalid email address format"

    if not check_question_validity(quest):
        return "Invalid question format"

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = load_json_file()

    if mail in data:
        if quest not in data[mail]:
            data[mail].append(quest)
    else:
        data[mail] = [username, quest]

    update_json_file(data)

    return "Thanks, %s! The answer will be sent to the email %s. Access Date: %s" % (username, mail, current_date)
