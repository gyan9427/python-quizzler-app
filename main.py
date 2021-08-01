from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
AMOUNT = 10
TYPE = 'boolean'
URL = "https://opentdb.com/api.php"

img_true='./images/true.png'
img_false='./images/false.png'

parameters = {
    'amount': AMOUNT,
    'type': TYPE
}

question_bank = []
# request to API for data
data = requests.get(URL,params=parameters)
# raise for status if any
data.raise_for_status()
# get the data in json format
question_b = data.json()
# extract required information
question_b = question_b["results"]




for question in question_b:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(img_true,img_false,quiz)
# while quiz.still_has_questions():
#     quiz.next_question()


