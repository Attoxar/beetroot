def word_count(some_text):
    words = some_text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1

        else:
            word_dictionary[word] = 1
    return word_dictionary


sentence = input("enter sentence here: ")
word_frequency = word_count(sentence)
print("word Frequency: ")
print(word_frequency)
