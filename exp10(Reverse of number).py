#Reverse of numbers
def print_reverse(n, i=None):
    if i is None:
        i = len(n) - 1

    if i < 0:
        return

    print(n[i])
    print_reverse(n, i - 1)

# Sample input
n = [1, 2, 3, 4, 5]

# Call the recursive function
print_reverse(n)
