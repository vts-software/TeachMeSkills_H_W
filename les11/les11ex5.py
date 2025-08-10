# Разработать класс SuperStr, который наследует
# функциональность стандартного типа str и содержит два
# новых метода:
# ● метод is_repeatance(s), который принимает некоторую
# строку и возвращает True или False в зависимости от того,
# может ли текущая строка быть получена целым
# количеством повторов строки s. Считать, что пустая
# строка не содержит повторов
# ● метод is_palindrom(), который возвращает True или False в
# зависимости от того, является ли строка палиндромом вне
# зависимости от регистра. Пустую строку считать
# палиндромом

class SuperStr(str):  # 1

    def is_repeatance(self, s):  # 2
        if not s:  # 3
            return False  # 4
        if len(self) % len(s) != 0:  # 5
            return False  # 6
        if s * (len(self) // len(s)) == self:  # 7
            return True  # 8
        return False  # 9

    def is_palindrom(self):  # 10
        if len(self) == 0:  # 11
            return True  # 12
        normalized = self.lower()  # 13
        return normalized == normalized[::-1]  # 14


# --- Примеры использования ---  # 15
word1 = SuperStr("abcabcabc")  # 16
print(word1.is_repeatance("abc"))  # True  # 17
print(word1.is_repeatance("ab"))   # False  # 18

word2 = SuperStr("Level")  # 19
print(word2.is_palindrom())  # True  # 20

word3 = SuperStr("Привет")  # 21
print(word3.is_palindrom())  # False  # 22

empty_str = SuperStr("")  # 23
print(empty_str.is_palindrom())  # True  # 24
