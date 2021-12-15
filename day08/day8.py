import os

# Part 1: count the number of output digits that represent a digit with a unique number of segments.
# Part 2: figure out which unique signal patterns correspond to each digit.

# What we need is a unique identifier for each unknown digit based on information we have already.
# We know how many segments a digit has, and we already know the pattern for digits 1, 4, 7, and 8.
# Combining the number of segments a digit has with the number of segments it shares with 1 and 4 gives
#     us a unique identifier for each digit.

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = [line.split("|") for line in f.readlines()]
        f.close()

    lines = [[part.split() for part in line] for line in lines]

    num_easy_digits = count_easy_digits(lines)
    output_sum = sum_outputs(lines)

    print(f"Part 1: The total number of easy digits in the outputs values is {num_easy_digits}.")
    print(f"Part 2: The sum of the output digits is {output_sum}.")

def count_easy_digits(lines):
    easy_lengths = [2, 4, 3, 7]
    return sum([sum([1 for val in output[1] if len(val) in easy_lengths]) for output in lines])
  
def sum_outputs(lines):
    explicit_digits = {2: 1, 4: 4, 3: 7, 7: 8}
    output_sum = 0
    for line in lines:
        digits_map = {} # Map of digit -> pattern
        patterns = line[0]
        output_values = line[1]
        map_easy_digits(explicit_digits, digits_map, patterns) # Map the digits with unique numbers of segments

        def decode_digit(num_segments, num_common_one, num_common_four):
            # Identify a pattern's digit based on the # of segments, # in common with 1, and # in common with 4.
            def filter_func(pattern):
                return (
                len(pattern) == num_segments and
                len(set(pattern) & set(digits_map[1])) == num_common_one and
                len(set(pattern) & set(digits_map[4])) == num_common_four)
            return list(filter(filter_func, patterns))[0]
        
        # Sort each pattern to prevent KeyErrors when accessing the digit of pattern in output
        digits_map[0] = "".join(sorted(decode_digit(6, 2, 3))) # six segments, two in common with 1, three in common with 4
        digits_map[2] = "".join(sorted(decode_digit(5, 1, 2))) # five segments, one in common with 1, two in common with 4
        digits_map[3] = "".join(sorted(decode_digit(5, 2, 3))) # five segments, two in common with 1, three in common with 4
        digits_map[5] = "".join(sorted(decode_digit(5, 1, 3))) # five segments, one in common with 1, three in common with 4
        digits_map[6] = "".join(sorted(decode_digit(6, 1, 3))) # six segments, one in common with 1, three in common with 4
        digits_map[9] = "".join(sorted(decode_digit(6, 2, 4))) # six segments, two in common with 1, four in common with 4

        # Swap keys and values to get a map of pattern -> digit
        digits_map = {v: k for k, v in digits_map.items()}
        
        output_num = "".join([str(digits_map["".join(sorted(val))]) for val in output_values]) 
        output_sum += int(output_num)
    return output_sum
    

def map_easy_digits(explicit_digits, digits_map, patterns):
    for pattern in patterns:
        if len(pattern) in explicit_digits.keys():
            digits_map[explicit_digits[len(pattern)]] = "".join(sorted(pattern)) # Sort to prevent KeyErrors


if __name__ == "__main__":
    main()