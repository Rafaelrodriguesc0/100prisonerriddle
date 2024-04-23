import random

def prisoner_protocol(num_prisoners, block_size):
    days = 0
    visited = set()
    counter_visited = set()

    while True:
        days += 1
        prisoner = random.randint(1, num_prisoners)

        # If it is day 1 for the current block
        if days % block_size == 1:
            if prisoner not in visited:
                visited.add(prisoner)
                if days > block_size:
                    counter_visited.add(prisoner)
                    if len(counter_visited) == num_prisoners:
                        break
            else:
                if days > block_size:
                    counter_visited.add(prisoner)
                    if len(counter_visited) == num_prisoners:
                        break
                    visited.remove(prisoner)
        elif days % block_size == 2:
            # If it is your second time visiting the room during the current block
            if prisoner in visited:
                visited.remove(prisoner)
            else:
                visited.add(prisoner)

    return days

# Simulate the protocol multiple times to get an average
num_simulations = 1000
total_days = 0
num_prisoners = 100
block_size = 3

for _ in range(num_simulations):
    total_days += prisoner_protocol(num_prisoners, block_size)

average_days = total_days / num_simulations
print(f"Average number of days needed: {average_days}")
