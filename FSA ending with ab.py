def ends_with_ab(input_string):
    state = 0

    for char in input_string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    return state == 2


test_strings = ["ab", "cab", "aaab", "abc", "aabx", "babab"]

for s in test_strings:
    if ends_with_ab(s):
        print(f"'{s}' is accepted (ends with 'ab')")
    else:
        print(f"'{s}' is rejected")
