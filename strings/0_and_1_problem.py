def count_binary_substrings(s):
    n = len(s)
    if n < 2:
        return 0

    # Initialize counts
    prev_count = 0
    curr_count = 1
    total_count = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            curr_count += 1
        else:
            # Add the minimum of the previous and current counts to the total count
            total_count += min(prev_count, curr_count)
            # Update prev_count to be the current count and reset curr_count
            prev_count = curr_count
            curr_count = 1
    
    # Add the last pair of counts
    total_count += min(prev_count, curr_count)

    return total_count

# Example usage
s = "00110011"
print(count_binary_substrings(s))  # Output: 6
s = "0011"
print(count_binary_substrings(s))  # Output: 2
s = "001100"
print(count_binary_substrings(s))  # Output: 4
