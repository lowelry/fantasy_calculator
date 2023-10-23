import re


def is_valid_input_str(input_str):

    valid_numbers = re.findall(r'\d', input_str)
    if valid_numbers:
        return ''.join(valid_numbers)
    else:
        return ''
