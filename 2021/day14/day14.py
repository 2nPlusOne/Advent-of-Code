import os
from itertools import cycle, chain, zip_longest

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        input = [part for part in f.read().partition("\n\n") if part != "\n\n"]
        f.close()

    template = list(input[0].strip())
    rules = [rule.strip().split(" -> ") for rule in input[1].split("\n")]
    rules_dict = {rule[0]: rule[1] for rule in rules}
    
    polymer_chain = perform_polymerization(template, rules_dict, 10)
    part1_sum = part1(polymer_chain)
    print("Part 1:", part1_sum)

def part1(polymer_chain):
    most_common_quantity = max(polymer_chain.count(x) for x in set(polymer_chain))
    least_common_quantity = min(polymer_chain.count(x) for x in set(polymer_chain))
    return most_common_quantity - least_common_quantity

def perform_polymerization(template, rules_dict, steps):
    for i in range(steps):
        insertions = get_insertions(template, rules_dict)
        template = [x for x in chain(*zip_longest(template, insertions)) if x is not None]
    return template


def get_insertions(template, rules_dict):
    insertions = []
    for i in range(len(template) - 1):
        pair = ''.join(template[i:i+2])
        if pair in rules_dict:
            insertions.append(rules_dict[pair])
    return insertions


if __name__ == "__main__":
    main()