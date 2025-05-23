import random

num_trials = 10000

stay_wins = 0
switch_wins = 0

for _ in range(num_trials):
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    choice = random.randint(0, 2)
    host_options = [i for i, prize in enumerate(doors) if i != choice and prize == "goat"]
    host_open = random.choice(host_options)
    remaining = [i for i in range(3) if i not in (choice, host_open)]
    switch_choice = remaining[0]
    if doors[choice] == "car":
        stay_wins += 1
    if doors[switch_choice] == "car":
        switch_wins += 1

print("Total trials:", num_trials)
print("Wins by staying:", stay_wins)
print("Wins by switching:", switch_wins)

stay_rate = stay_wins / num_trials
switch_rate = switch_wins / num_trials

print(f"Stay win rate: {stay_rate:.2%}")
print(f"Switch win rate: {switch_rate:.2%}")

# ASCII visualization
bar_length = 50
stay_bar = "#" * int(bar_length * stay_rate)
switch_bar = "#" * int(bar_length * switch_rate)

print("\nResults (ASCII visualization):")
print(f"Stay    : {stay_bar}")
print(f"Switch  : {switch_bar}")
