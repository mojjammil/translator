def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation


print((translator(input("Enter phrase to translate to language X: "))))
