from itertools import permutations, combinations
from datetime import datetime
import os

def generate_wordlist(inputs, min_len=4, max_len=12):
    wordlist = set()

    # Clean the input
    inputs = [item.strip() for item in inputs if item.strip()]

    # Generate combinations of input items (up to all of them)
    for r in range(1, len(inputs)+1):
        for combo in combinations(inputs, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if min_len <= len(word) <= max_len:
                    wordlist.add(word)

    # Create output folder and file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"wordlist_{timestamp}.txt"
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)

    with open(filepath, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    return len(wordlist), filepath
