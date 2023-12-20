def rnl(list):
    return [i for i in list if i != "\n"]


def escape_characters(text):
    escape_chars = [
        "_",
        "*",
        "[",
        "]",
        "(",
        ")",
        "~",
        "`",
        ">",
        "#",
        "+",
        "-",
        "=",
        "|",
        "{",
        "}",
        ".",
        "!",
    ]

    escaped_text = "".join(
        ["\\" + char if char in escape_chars else char for char in text]
    )
    return escaped_text


if __name__ == "__main__":
    pass
