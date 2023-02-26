class BasicWord:
    def __init__(self, current_word, valid_words):
        """Исходное слово, Список составленный слов из исходного"""
        self.current_word = current_word
        self.valid_words = valid_words

    def word_check(self, user_answer) -> bool:
        """проверку введенного слова в списке допустимых подслов (вернет bool)"""
        if user_answer is self.valid_words:
            return True
        return False

    def quantity_valid_words(self) -> int:
        """подсчет количества подслов (вернет int)"""
        return len(self.valid_words)

    def __repr__(self):
        return self.valid_words


class Player:
    def __init__(self, user_name):
        """Имя пользователя , Использованые слова пользователя"""
        self.user_name = user_name
        self.used_words = []

    def quantity_used_words(self) -> int:
        """получение количества использованных слов (возвращает int)"""
        return len(self.used_words)

    def add_word(self, user_word):
        """добавление слова в использованные слова (ничего не возвращает)"""
        self.used_words.append(user_word)

    def check_used_words(self, user_word) -> bool:
        """проверка использования данного слова до этого (возвращает bool)"""
        if user_word is self.used_words:
            return True
        return False

    def __repr__(self):
        return self.user_name







