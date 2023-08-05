from question_init import Questions
from data import question_data
from Quiz_brain import QuizBrain

question_blank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text, question_answer)
    question_blank.append(new_question)

quiz = QuizBrain(question_blank)
while quiz.still_has_question:
    quiz.show_question()

print("you complete the quiz")
print(f"your final score is: {quiz.score}/{quiz.question_number}")


