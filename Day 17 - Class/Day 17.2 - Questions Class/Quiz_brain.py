class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def show_question(self):
        question = self.question_list[
            self.question_number]  # show binary code, so need to add " .text" in question_init
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {question.text} (True/ False): ")
        self.check_answer(user_answer, question.answer)  # use .answer from question_init

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("you're right")

        else:
            print("you're wrong")
        print(f"the correct answer was: {question_answer}")
        print(f"your score is: {self.score} / {self.question_number}")
