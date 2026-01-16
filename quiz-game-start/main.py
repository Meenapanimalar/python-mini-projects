from question_model import Question
from  data import question_data
from quiz_brain import QuizBrain

question_bank=[]


for q_data in question_data:
    question = Question(q_data['question'],q_data['correct_answer'])
    question_bank.append(question)


quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_question():

    quizbrain.next_question()

print(f"your final score is {quizbrain.score} out of {quizbrain.question_number}")

