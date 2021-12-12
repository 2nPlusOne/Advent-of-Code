import os

# Part 1: count the number of output digits that represent a digit with a unique number of segments.
# Part 2: figure out which unique signal patterns correspond to each digit.

# Consider the following output: acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

# We know the signal patterns for 1, 4, 7, and 8, because they have unique segment counts.
# For the 1, we don't know which letter is which segment, but we can find the top segment of 7 using this information.
# For 7, it shares both segments of 1, so we know the third letter is the top segment.

def main():
    with open(os.path.join(os.path.dirname(__file__), 'sample.txt'), 'r') as f:
        input = [line.split("|") for line in f.readlines()]
        f.close()

    input = [[part.split() for part in line] for line in input]
    outputs = [line[1] for line in input]

    sum = 0
    lengths = [2, 4, 3, 7]

    for output in outputs:
        for digit in output:
            if len(digit) in lengths:
                sum += 1
    print(f"Part 1: {sum}")


if __name__ == "__main__":
    main()