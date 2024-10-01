def current_symbol(input_string, position):
    return input_string[position] if position < len(input_string) else '$'

def parse(input_string):
    input_string += '$'  # Append end-of-input symbol
    position = 0
    stack = ['$']  # Initialize stack with end symbol
    stack.append('S')  # Push start symbol

    while stack:
        top = stack.pop()
        current = current_symbol(input_string, position)

        if top == current:  # Match
            if top == '$':
                print("Input successfully parsed!")
                return True
            position += 1  # Move to the next symbol
        elif top == 'S':
            stack.append('B')  # S -> AB (push B first to process A last)
            stack.append('A')
        elif top == 'A':
            if current == 'a':
                stack.append('A')  # A -> aA
                stack.append('a')
            else:
                stack.append('A')  # A -> ε (do nothing)
        elif top == 'B':
            if current == 'b':
                stack.append('B')  # B -> bB
                stack.append('b')
            else:
                stack.append('B')  # B -> ε (do nothing)
        else:
            print(f"Error: unexpected symbol '{current}'")
            return False

    print("Error: stack is empty before input is completely consumed.")
    return False

# Example usage
input_string = "aaabbb"  # Example input
parse(input_string)
