class LL1Parser:
    def __init__(self, input_string):
        self.input_string = input_string + '$'  # Append end-of-input symbol
        self.position = 0
        self.stack = ['$', 'S']  # Initialize stack with start symbol

    def current_symbol(self):
        return self.input_string[self.position]

    def parse(self):
        while self.stack:
            top = self.stack.pop()
            current = self.current_symbol()

            if top == current:  # Match
                if top == '$':
                    print("Input successfully parsed!")
                    return True
                self.position += 1  # Move to next symbol
            elif top == 'S':
                self.stack.extend(['B', 'A'])  # S -> AB
            elif top == 'A':
                if current == 'a':
                    self.stack.append('A')  # A -> aA
                    self.stack.append('a')
                else:
                    self.stack.append('A')  # A -> ε (do nothing)
            elif top == 'B':
                if current == 'b':
                    self.stack.append('B')  # B -> bB
                    self.stack.append('b')
                else:
                    self.stack.append('B')  # B -> ε (do nothing)
            else:
                print(f"Error: unexpected symbol '{current}'")
                return False

        print("Error: stack is empty before input is completely consumed.")
        return False

# Example usage
input_string = "aaabbb"  # Example input
parser = LL1Parser(input_string)
parser.parse()
