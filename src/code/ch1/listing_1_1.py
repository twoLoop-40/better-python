from collections.abc import Generator


def get_word(src: str) -> str:
    pass


def word_number(word: str) -> int:
    magic = 0
    for letter in word:
        magic += 1 + ord(letter) + ord('a')
    return magic


def word_numbers(src: str) -> Generator[int, None, None]:
    while (word := get_word(src=src)) is not None:
        yield word_number(word)
