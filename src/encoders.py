import base64
import urllib.parse
import html


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base32_encode(text):
    return base64.b32encode(text.encode()).decode()


def base85_encode(text):
    return base64.b85encode(text.encode()).decode()


def hex_encode(text):
    return text.encode().hex()


def binary_encode(text):
    return " ".join(f"{b:08b}" for b in text.encode())


def octal_encode(text):
    return " ".join(f"{b:03o}" for b in text.encode())


def decimal_encode(text):
    return " ".join(str(b) for b in text.encode())


def url_encode(text):
    return urllib.parse.quote(text)


def html_encode(text):
    return html.escape(text)


def unicode_encode(text):
    return "".join(f"\\u{ord(c):04x}" for c in text)
