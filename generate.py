import os
import random
import itertools


characters = "abcdefghijklmnopqrstuvwxyz0123456789"
prefix = "PLDTWIFI"
output_file = "data/pldt_passwords.txt"

# Generate all unique passwords
print("Generating passwords...")
passwords = ["".join((prefix + "".join(combo))) for combo in itertools.product(characters, repeat=5)]

# Shuffle the list
print("Shuffling passwords...")
random.shuffle(passwords)

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save to file
print("Saving to file...")
with open(output_file, "w") as f:
    f.write("\n".join(passwords))

print(f"Shuffled {len(passwords)} passwords saved to {output_file}")
