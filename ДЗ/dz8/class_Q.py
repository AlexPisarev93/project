class Question:
    def __init__(self, text: str, difficult: int, correct_answer: str):
        self.text = text
        self.difficult = difficult
        self.correct_answer = correct_answer
        self.question = False
        self.answer_user = str or None
        self.points: int = int(self.difficult) * 10

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
            Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
            """
        return self.points

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
            с верным ответов иначе False.
            """
        return self.correct_answer.lower() == self.answer_user

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
            Вопрос: What do people often call American flag?
            Сложность 4/5
            """
        return f"Вопрос: {self.text}\n Сложность: {self.difficult}/5"

    def build_positive_feedback(self) -> str:
        """Возвращает :
           Ответ верный, получено __ баллов
           """

        return f"Ответ верный, получено {self.points} баллов"

    def build_negative_feedback(self) -> str:
        """Возвращает :
            Ответ неверный, верный ответ __
            """
        return f"Ответ неверный, верный ответ {self.correct_answer}"



