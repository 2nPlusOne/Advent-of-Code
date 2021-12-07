import os
from collections import deque

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        initial_fish_timers = [int(num) for num in f.read().split(',')]
        print(f'Part 1: {simulate_fish_growth(initial_fish_timers, 80)}')
        print(f'Part 2: {simulate_fish_growth(initial_fish_timers, 256)}')

def simulate_fish_growth(init_timers: list[int], num_days: int) -> int:
    timer_counts = [0] * 7 # Each index is a possible timer value
    for state in init_timers: # Initialize the timer counts
        timer_counts[state] += 1

    # Convert timer counts to a deque
    fish = deque(timer_counts) 

    # Initialize the deque for fry timer values
    # Fry[0] is the number of fry with timer at 8 (newly spawned)
    # Fry[1] is the number of new fry on the next day
    fry = deque([0, 0]) 

    print(f"Initial fish: {fish}")
    for day in range(num_days):
        print(f'Day {day+1} start: Fish -> {fish} Fry -> {fry}')
        fish.rotate(-1) # Age fish
        fry.append(fish[0]) # Fish[0] is the number of fry to create next day, so append to fry
        fish[0] += fry.popleft() # Add fry with timers at 7 to fish[0] to be aged next day
        print(f'Day {day+1} end: Fish -> {fish} Fry -> {fry}')
    return sum(fish) + fry.popleft()

if __name__ == '__main__':
    try:
        assert simulate_fish_growth([3, 4, 3, 1, 2], 80) == 5934
        print("Test with sample input passed!")
    except: raise(AssertionError("test with sample input failed."))
    main()