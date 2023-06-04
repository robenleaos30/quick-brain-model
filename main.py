from data import question_data
from html import unescape
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    q_text = unescape(question["question"])
    q_answer = question["correct_answer"]
    item = (q_text, q_answer)
    question_bank.append(item)

quiz = QuizBrain(question_bank)

while quiz.still_question():
    quiz.next_question()

print(f"You try very well. Have a nice day bro!\nYour final score is {quiz.score}/10.")
