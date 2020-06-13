def reverse_words_order_and_swap_cases(sentence):
    my_word = sentence.split()

    my_word = list(reversed(my_word))

    result = " ".join(my_word)
    return result.swapcase()
