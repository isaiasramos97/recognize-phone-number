def is_phone_number(text):
    """
    This function was made to recognize a Brazilian phone number
    :param text: number
    :return:
    """
    # normally, brazilians use the format +00 (00) 00000-0000   the brazilian code is +55, in the beginning
    disallowed_characters = '+() -'

    for character in disallowed_characters:
        text = text.replace(character, '')
    if text[0] == '5' and text[1] == '5':
        text = text[2:]
    if len(text) != 11:
        return False
    return True


print(is_phone_number('2191111-1111'))
print(is_phone_number('248888-9999'))
