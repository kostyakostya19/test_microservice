def word_counter(sentence):
    words = sentence.split()
    new_tuple = {
        "sentence": sentence,
        "count of words": len(words)
    }
    return new_tuple

def space_counter(sentence):
    space = " "
    spaces = sentence.count(space)
    return spaces

def upper_lower_counter(sentence):
    upper_count = 0
    lower_count = 0
    for char in sentence:
        if char.uppeer:
            upper_count += 1
        elif char.lower:
            lower_count += 1
        else:
            print("error")
    return upper_count, lower_count

def sentence_x(sentence):
    basic_array = sentence.split()
    count_of_array = len(basic_array)
    print("first v")
    for elem in basic_array:
        print(elem, "- ", len(elem))

    for i in range(count_of_array - 1):
        for j in range(count_of_array - 1 - i):
            if len(basic_array[j]) > len(basic_array[j + 1]):
                basic_array[j], basic_array[j + 1] = basic_array[j + 1], basic_array[j]

    for elem in basic_array:
        print(elem, "- ", len(elem))

#sent = "my word is bond"
#sentence_x(sent)