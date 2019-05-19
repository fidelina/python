#ф-ию to_title: принимает строчку, ищет пробелы, первые буквы после них делает заглавными:
from typing import List

def to_title(s: List):
    s = s.strip(" ")
    if not (s.istitle()):
        for i in range(0, len(s)):
            if s[i] in " ":
                s = s[:i+1] + s[i+1].upper() + s[i+2:]

        return s
    else:
        return "Строка уже соответствует формату"

s = "String str lol trololo"
print(to_title("   String str lol trololo   "))
