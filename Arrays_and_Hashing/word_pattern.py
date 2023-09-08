def word_pattern(pattern, s):
    words = s.split(" ")
    if len(words) != len(pattern):
        return False
    wordtoChar, chartoWord = {}, {}

    for c,w in zip(pattern, words):
        if c in chartoWord and chartoWord[c]!=w:
            return False
        if w in chartoWord and wordtoChar[w]!=c:
            return False
        chartoWord[c] = w
        wordtoChar[w] = c
    return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    val =  word_pattern(pattern, s)
    print(val)