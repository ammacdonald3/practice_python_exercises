def word_reversal():
    print("This function will reverse the words that you input.")
    input_string = input("Please enter a sentence. ")
    input_list = input_string.split()
    output_list = input_list[::-1]
    output_string = " ".join(output_list)

    return output_string

print(word_reversal())