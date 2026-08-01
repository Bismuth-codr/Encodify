import sys

from src.encoders import *

OPERATIONS = {
    "-64": base64_encode,
    "--base64": base64_encode,

    "-32": base32_encode,
    "--base32": base32_encode,

    "-85": base85_encode,
    "--base85": base85_encode,

    "-x": hex_encode,
    "--hex": hex_encode,

    "-b": binary_encode,
    "--binary": binary_encode,

    "-o": octal_encode,
    "--octal": octal_encode,

    "-d": decimal_encode,
    "--decimal": decimal_encode,

    "-u": url_encode,
    "--url": url_encode,

    "-H": html_encode,
    "--html": html_encode,

    "-U": unicode_encode,
    "--uni": unicode_encode,
}


HELP = """
ECode v2

Usage:
    ecode [operations] TEXT

Operations

Encoding
    -64 --base64
    -32 --base32
    -85 --base85

    -x  --hex
    -b  --binary
    -o  --octal
    -d  --decimal

    -u  --url
    -H  --html
    -U  --uni

Examples

    ecode -64 hello
    ecode -x hello
    echo hello | ecode -85
"""


def get_text(args):
    if args:
        return " ".join(args)

    if not sys.stdin.isatty():
        return sys.stdin.read().rstrip("\n")

    print("ecode: no input")
    sys.exit(1)


def main():

    argv = sys.argv[1:]

    if not argv or "--help" in argv or "-h" in argv:
        print(HELP)
        return

    operations = []
    text_parts = []
    for arg in argv:
        if arg in OPERATIONS:
            operations.append(OPERATIONS[arg])

        elif arg.startswith("-"):
            print(f"ecode: unknown option '{arg}'")
            print("Try 'ecode --help' for usage.")
            sys.exit(1)

        else:
            text_parts.append(arg)

    text = get_text(text_parts)

    if not operations:
        print("ecode: no operation specified")
        print("Try 'ecode --help' for usage.")
        sys.exit(1)

    print(text)

    for op in operations:
        text = op(text)

    print(text)
