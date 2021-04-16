from monke import token
from monke import lexer
import getpass
import sys

PROMPT = ">🐵> "


def start():
    username = getpass.getuser()
    print("Hello {}! This is the Monké programming language!\n".format(username))
    print("Feel free to type in commands\n")

    try:
        while (line := input(PROMPT)) :
            l = lexer.new(line)

            while (tok := l.next_token()) :
                if tok.type == token.EOF:
                    break
                else:
                    print("{}".format(tok))
    except (EOFError, KeyboardInterrupt):
        sys.exit("All things must come to an end 🙈")


if __name__ == "__main__":
    start()
