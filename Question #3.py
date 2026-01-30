# Question 3 | Nested Dictionary from Strings - Safe Function Application | Define a function that computes
# xy. Then, given a list of pairs (x, y):
    # • Use a for loop with argument unpacking to call the function.
    # • Skip any pair where the exponent y is negative.
    # • Store the valid results in a list and print the list.

def power(x, y):
    return x ** y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

results = []

for x, y  in pairs:
    if y >= 0:
        results.append(power(x, y))

print(results)