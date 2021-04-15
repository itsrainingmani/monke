from ast import Str
from dataclasses import dataclass
from monke import token

# Source Code -> Tokens -> AST


@dataclass
class Lexer:
    input: str = ""
    position: int = 0  # current position in input
    read_position: int = 0  # current reading position in input
    ch: str = ""  # current char under examination

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> token.Token:
        ch = self.ch

        if ch == "=":
            tok = token.new_token(token.ASSIGN, ch)
        elif ch == ";":
            tok = token.new_token(token.SEMICOLON, ch)
        elif ch == "(":
            tok = token.new_token(token.LPAREN, ch)
        elif ch == ")":
            tok = token.new_token(token.RPAREN, ch)
        elif ch == ",":
            tok = token.new_token(token.COMMA, ch)
        elif ch == "+":
            tok = token.new_token(token.PLUS, ch)
        elif ch == "{":
            tok = token.new_token(token.LBRACE, ch)
        elif ch == "}":
            tok = token.new_token(token.RBRACE, ch)
        elif ch == 0:
            tok = token.new_token(token.EOF, "")

        self.read_char()
        return tok


def new(input: str) -> Lexer:
    l = Lexer(input=input)
    l.read_char()
    return l
