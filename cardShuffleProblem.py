# Describe a method for performing a card shuffle of a list of 2n elements, by converting it into two lists, L1 and L2, where L1 is the first half of L and L2 is second half of L, and then these two lists are merged into one by taking the first element in L1, then the first element in L2, followed by second elementi in L1, the second element in L2 and so on.


# Input list (must have even number of elements)
L = [1, 2, 3, 4, 5, 6, 7, 8]

# Find the middle index
n = len(L) // 2

# Divide the list into two halves
L1 = L[:n]
L2 = L[n:]

# Shuffle by taking one element from each list
result = []

for i in range(n):
    result.append(L1[i])
    result.append(L2[i])

# Print the shuffled list
print("Original List:", L)
print("Shuffled List:", result)