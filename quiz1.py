class SyntaxError(Exception):
    pass

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.tokens = []

    def error(self):
        raise SyntaxError("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def variable(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return Token('ID', result)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('NUM', int(result))

    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isalpha():
                return self.variable()
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '=':
                self.advance()
                return Token('ASSIGN', '=')
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            if self.current_char == '*':
                self.advance()
                return Token('MUL', '*')
            if self.current_char == '/':
                self.advance()
                return Token('DIV', '/')
            if self.current_char == 'i' and self.text[self.pos:self.pos + 2] == 'if':
                self.advance()
                self.advance()
                return Token('IF', 'if')
            if self.current_char == 't' and self.text[self.pos:self.pos + 4] == 'then':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return Token('THEN', 'then')
            if self.current_char == 'e' and self.text[self.pos:self.pos + 4] == 'else':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return Token('ELSE', 'else')
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            self.error()

        return Token('EOF', None)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def error(self, message):
        raise SyntaxError(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            self.error(f"Expected '{token_type}', found '{self.current_token.type}'.")

    def parse(self):
        try:
            self.statement()
            if self.current_token.type != 'EOF':
                self.error("Extra input after valid statement.")
            print("Parse Successful: The input conforms to the grammar.")
        except SyntaxError as e:
            print(f"Error: {e}")

    def statement(self):
        if self.current_token.type == 'IF':
            self.e_if()
        elif self.current_token.type == 'ID':
            self.assignment()
        else:
            self.error("Expected 'if' or 'id' at the beginning of the statement.")

    def e_if(self):
        self.eat('IF')
        self.condition()
        self.eat('THEN')
        self.statement()
        if self.current_token.type == 'ELSE':
            self.eat('ELSE')
            self.statement()
        else:
            self.error("Missing 'else' clause in nested if statement.")

    def assignment(self):
        self.eat('ID')
        self.eat('ASSIGN')
        self.expression()

    def condition(self):
        self.eat('ID')
        self.eat('ASSIGN')
        self.expression()

    def expression(self):
        self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            self.current_token.type
            if self.current_token.type == 'PLUS':
                self.eat('PLUS')
            elif self.current_token.type == 'MINUS':
                self.eat('MINUS')
            self.term()

    def term(self):
        self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            if self.current_token.type == 'MUL':
                self.eat('MUL')
            elif self.current_token.type == 'DIV':
                self.eat('DIV')
            self.factor()

    def factor(self):
        if self.current_token.type == 'ID':
            self.eat('ID')
        elif self.current_token.type == 'NUM':
            self.eat('NUM')
        elif self.current_token.type == 'LPAREN':
            self.eat('LPAREN')
            self.expression()
            self.eat('RPAREN')
        else:
            self.error("Invalid factor.")

# Sample input
input_programs = [
    "if id = num then if id = num then id = num",
    "if = num then id = num",
    "if id = num then id = id * num else id = num / id"
]

for program in input_programs:
    print(f"Input: {program}")
    lexer = Lexer(program)
    parser = Parser(lexer)
    parser.parse()
    print()
