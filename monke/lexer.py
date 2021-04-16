from dataclasses import dataclass
from monke import token

# Source Code -> Tokens -> AST


def is_letter(ch: str) -> bool:
    """
    Why bother with this when isalpha is already a std lib function?
    Well, this way we can control exactly what is allowed in our
    identifiers and not.
    """
    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")
    char = ord(ch)

    return (a <= char <= z) or (A <= char <= Z) or ch == "_"


def is_digit(ch: str) -> bool:
    zero = ord("0")
    nine = ord("9")

    return zero <= ord(ch) <= nine


@dataclass
class Lexer:
    input: str = ""
    position: int = 0  # current position in input
    read_position: int = 0  # current reading position in input
    ch: str = ""  # current char under examination

    def read_char(self):
        """Give us the next character and advance our position in the input string"""
        if self.read_position >= len(self.input):
            self.ch = "\x00"
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def peek_char(self):
        """Peek ahead in the input and return the character"""
        if self.read_position >= len(self.input):
            return "\x00"
        else:
            return self.input[self.read_position]

    def read_identifier(self) -> str:
        """Read a contiguous identifier from the input string"""
        pos = self.position
        while is_letter(self.ch):
            self.read_char()

        return self.input[pos : self.position]

    def read_number(self) -> str:
        """Read a number from the input string"""
        pos = self.position
        while is_digit(self.ch):
            self.read_char()

        return self.input[pos : self.position]

    def skip_whitespace(self):
        while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
            self.read_char()

    def next_token(self) -> token.Token:
        tok = ""

        self.skip_whitespace()

        if self.ch == "=":
            tok = token.new_token(token.ASSIGN, self.ch)
        elif self.ch == "+":
            tok = token.new_token(token.PLUS, self.ch)
        elif self.ch == "-":
            tok = token.new_token(token.MINUS, self.ch)
        elif self.ch == "!":
            tok = token.new_token(token.BANG, self.ch)
        elif self.ch == "/":
            tok = token.new_token(token.SLASH, self.ch)
        elif self.ch == "*":
            tok = token.new_token(token.ASTERISK, self.ch)
        elif self.ch == "<":
            tok = token.new_token(token.LT, self.ch)
        elif self.ch == ">":
            tok = token.new_token(token.GT, self.ch)
        elif self.ch == "(":
            tok = token.new_token(token.LPAREN, self.ch)
        elif self.ch == ")":
            tok = token.new_token(token.RPAREN, self.ch)
        elif self.ch == "{":
            tok = token.new_token(token.LBRACE, self.ch)
        elif self.ch == "}":
            tok = token.new_token(token.RBRACE, self.ch)
        elif self.ch == ",":
            tok = token.new_token(token.COMMA, self.ch)
        elif self.ch == ";":
            tok = token.new_token(token.SEMICOLON, self.ch)
        elif self.ch == "\x00":
            tok = token.new_token(token.EOF, "")
        else:
            if is_letter(self.ch):
                tok_literal = self.read_identifier()
                tok_type = token.lookup_ident(tok_literal)
                return token.new_token(tok_type, tok_literal)
            elif is_digit(self.ch):
                return token.new_token(token.INT, self.read_number())
            else:
                tok = token.new_token(token.ILLEGAL, self.ch)

        self.read_char()
        return tok


def new(input: str) -> Lexer:
    l = Lexer(input=input)
    l.read_char()
    return l
