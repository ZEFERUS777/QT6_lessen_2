import re


def validate_phone_number(phone):
    try:
        cleaned_phone = re.sub(r'\s+', '', phone)

        if cleaned_phone.count('(') != cleaned_phone.count(')'):
            raise ValueError("Несоответствующие скобки")

        if '--' in cleaned_phone or cleaned_phone.startswith('-') or cleaned_phone.endswith('-'):
            raise ValueError("Некорректный формат")

        cleaned_phone = re.sub(r'\(|\)', '', cleaned_phone)
        cleaned_phone = re.sub(r'-', '', cleaned_phone)

        if cleaned_phone.startswith('8'):
            cleaned_phone = cleaned_phone.replace('8', '+7', 1)
        elif not cleaned_phone.startswith('+7'):
            raise ValueError("Номер не начинается с +7")

        digits_only = re.sub(r'[^0-9]', '', cleaned_phone)

        if len(digits_only) != 11:
            raise ValueError("Некорректное количество цифр")

        return digits_only

    except (ValueError, IndexError) as e:
        return "error"


number = input()
result = validate_phone_number(number)
result = '+' + result if result != "error" else 'error'
print(result)
