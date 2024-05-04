from tkinter.messagebox import QUESTION
from bottle import post, request
import re
import datetime
import json

#Пустой словарь
question = {}

#Функция для проверки вопроса
def check_question_validity(quest):
    if len(quest) > 3 and re.match(r"[a-zA-Z0-9]", quest):
        question_marks = quest.count('?')
        #Проверка на наличие знака вопроса
        if question_marks == 1 and '?' in quest:
            return True
        return False

#Функция для обновления файла json
def update_json_file(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

#Функция для загрузки данных из файла json
def load_json_file():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def correct_mail(mail):
     if not re.match(r"[\w\.\-?%]{2,30}@[a-zA-Z]{1,9}(\.[a-zA-Z]{2,7}(\.[a-zA-Z]{2,7}))?", mail):
        return True
     else:
        return False

@post('/home')
#Функция для обработки полей формы
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')

    #Проверка, что поля не пустые
    if not quest or not mail or not username:
        return "Please fill in all fields of the form"

    #Паттерн для обработки email
    if not re.match(r"[\w\.\-?%]{2,30}@[a-zA-Z]{1,9}(\.[a-zA-Z]{2,7}(\.[a-zA-Z]{2,7}))?", mail):
        return "Invalid email address format"

    #Получение сегодняшней даты
    if not check_question_validity(quest):
        return "Invalid question format. Make sure that your question consists not only of numbers, but more than three letters and is there a one question mark."

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    #Загрузка данных из файла json
    data = load_json_file()

    #Привод вопрос к нижнему регистру
    quest_lower = quest.lower()

    #Обновление данных в файле json в зависимости от наличия email в словаре data
    if mail in data:
        if quest_lower not in [q.lower() for q in data[mail]]:
            data[mail].append(quest)
    else:
        data[mail] = [username, quest]

    update_json_file(data)

    return "Thanks, %s! The answer will be sent to the email %s. Access Date: %s" % (username, mail, current_date)
