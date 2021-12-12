import os

bracket_dict = {'{': '}', '[': ']', '(': ')', '<': '>'}

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    f.close()

    