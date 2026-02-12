def vowels(word):
    letters = list(word)
    count = 0
    for x in letters:
        if x in ["a","e","i","o","u"]:
            count = count + 1
            continue
            return count
        else:
            continue
    return count

    
w = input("Give me a word")
print(vowels(w))

