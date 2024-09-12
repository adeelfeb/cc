def h(current_state, ch):
    n = 3

    if current_state == 0:
        if ch == '@':
            return 1
        else:
            return -1
    elif current_state == 1:
        if ch == '@':
            return 1
        elif ch.isdigit():
            return 2
        else:
            return -1
    elif current_state == 2:
        if ch.isdigit() or ch.isalpha() or ch == '_':
            return 2
        elif ch == '?':
            return n
        else:
            return -1
    elif current_state == n:
        return n

    return -1

def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression





file_path = 'expression.txt'
content = read_expression_from_file(file_path)

current_state = 0

for ch in content:
    next_state = h(current_state, ch)
    if next_state == -1:
        print("Invalid regex")
        break
    current_state = next_state

if current_state == 3:
    print("Valid regex")
else:
    print("Invalid regex")