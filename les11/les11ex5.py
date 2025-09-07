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

class SuperStr(str):

    def is_repeatance(self, s):
        if not s:
            return False
        if len(self) % len(s) != 0:
            return False
        if s * (len(self) // len(s)) == self:
            return True
        return False

    def is_palindrom(self):
        if len(self) == 0:
            return True
        normalized = self.lower()
        return normalized == normalized[::-1]


# --- Примеры использования ---
word1 = SuperStr("abcabcabc")
print(word1.is_repeatance("abc"))
print(word1.is_repeatance("ab"))

word2 = SuperStr("Level")
print(word2.is_palindrom())

word3 = SuperStr("Привет")
print(word3.is_palindrom())

empty_str = SuperStr("")
print(empty_str.is_palindrom())
