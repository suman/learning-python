class QuizBrain:
    def __init__(self, question_bank):
        self.qn_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.qn_number+1} {self.question_bank[self.qn_number]['text']}. (True/False)")
        self.check_answer(answer, self.question_bank[self.qn_number]['answer'])
        self.qn_number += 1
        print(f"Your current score is {self.score} / {self.qn_number+1}")

    def still_has_question(self):
        return len(self.question_bank) > self.qn_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1


