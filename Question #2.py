# Question 2 | Nested Dictionary from Strings - Define a function that receives a list of
# strings and returns a dictionary with the following structure:
    # • Each key is a string from the list.
    # • Each value is another dictionary containing:
        # – The length of the string
        # – Whether the length is even or odd

def list_of_strings(strings):
    dictionary = {}

    for s in strings:
        dictionary[s] = {
            "length": len(s),
            "even or odd": "even" if len(s) % 2 == 0 else "odd"
        }

    return dictionary

words = ['data', 'science', 'tulip']

print(list_of_strings(words))
