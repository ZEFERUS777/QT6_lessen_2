import re


def validate_phone_number(phone):
    cleaned_phone = re.sub(r'\s+', '', phone)
    if cleaned_phone.count('(') != cleaned_phone.count(')'):
        return "error"
    if '--' in cleaned_phone or cleaned_phone.startswith('-') or cleaned_phone.endswith('-'):
        return "error"
    cleaned_phone = re.sub(r'\(|\)', '', cleaned_phone)
    cleaned_phone = re.sub(r'-', '', cleaned_phone)
    if cleaned_phone.startswith('8'):
        cleaned_phone = cleaned_phone.replace('8', '+7', 1)
    elif not cleaned_phone.startswith('+7'):
        return "error"
    digits_only = re.sub(r'[^0-9]', '', cleaned_phone)
    if len(digits_only) != 11:
        return "error"
    return digits_only


number = input()
result = validate_phone_number(number)
result = '+' + result if result != "error" else 'error'
print(result)