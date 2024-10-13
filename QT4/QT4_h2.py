table_alphabet = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
                  "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
                  "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
                  "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
                  "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
                  "б": "b", "ю": "ju", "ё": "jo"
                  }


def translate(text):
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in table_alphabet:
            replacement = table_alphabet[lower_char]
            if char.isupper():
                replacement = replacement.capitalize() if len(replacement) > 1 else replacement.upper()
            result.append(replacement)
        else:
            result.append(char)
    return "".join(result)


input_file = "cyrillic.txt"
output_file = "transliteration.txt"
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()
translated_content = translate(content)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(translated_content)
