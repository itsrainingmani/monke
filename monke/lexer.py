from ast import Str
from dataclasses import dataclass

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


def new(input: str) -> Lexer:
    l = Lexer(input=input)
    l.read_char()
    return l