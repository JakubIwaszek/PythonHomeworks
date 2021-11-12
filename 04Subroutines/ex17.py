def letterCounter(letter, text):
    counter = 0
    for singleLetter in text:
        if singleLetter == letter:
            counter += 1
    return counter

print(letterCounter("e", "You never get a second chance to make a first impression"))