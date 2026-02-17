def word_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Number of words:", len(words))
    print("Number of characters:", len(sentence))
word_counter()
