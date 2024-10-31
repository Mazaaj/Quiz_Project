class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"P.{self.question_number}: {current_question.text}. (Verdad✔️/Falso❌): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("️️✔️Respuesta correcta!")
        else:
            print("❌Respuesta incorrecta!")
        print(f"🕹️Tu puntuacion actual es: {self.score}/{self.question_number}")
        print(f"🌍La respuesta correcta era: {correct_answer}")
        print("\n")
