
def word_count(sentence: str) -> int:
    words = [word.split("-") for word in sentence.split()]
    return len(words)
