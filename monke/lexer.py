from ast import Str
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

    return (a <= char <= z) or (A <= char <= z) or ch == "_"


@dataclass
class Lexer:
    input: str = ""
    position: int = 0  # current position in input
    read_position: int = 0  # current reading position in input
    ch: str = ""  # current char under examination

    def read_char(self):
        """Give us the next character and advance our position in the input string"""
        if self.read_position >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def read_identifier(self) -> str:
        """Read a contiguous identifier from the input string"""
        pos = self.position
        while self.ch.isalpha():
            self.read_char

        return self.input[pos : self.position]

    def next_token(self) -> token.Token:
        tok = ""
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
        else:
            if ch.isalpha():
                tok_literal = self.read_identifier()

        self.read_char()
        return tok


def new(input: str) -> Lexer:
    l = Lexer(input=input)
    l.read_char()
    return l
