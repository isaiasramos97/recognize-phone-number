def is_phone_number(text):
    if len(text) != 15:
        return False
    if text[0] != '(' or text[3] != ')':
        return False
    for i in range(1, 3):
        if not text[i].isdecimal():
            return False
    if text[4] != ' ':
        return False
    for i in range(5, 10):
        if not text[i].isdecimal():
            return False
        if text[10] != '-':
            return False
    for i in range(11, 15):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(is_phone_number('415-555-4242'))
print('(21) 99567-2284 is a phone number:')
print(is_phone_number('(21) 99567-2284'))
