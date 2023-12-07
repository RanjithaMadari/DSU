def length_of_last_word(s):
    # Remove trailing and leading whitespaces
    s = s.strip()


    # Split the string into words
    words = s.split()


    # Check if there are any words in the string
    if not words:
        return 0


    # Return the length of the last word
    return len(words[-1])


# Example usage:
s = input()
output1 = length_of_last_word(s)
print(output1)