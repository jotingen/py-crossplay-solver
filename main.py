import random

from collections import Counter

letter_count = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 1,
        'F': 4,
        'G': 4,
        'H': 3,
        'I': 8,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 5,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 5,
        'T': 6,
        'U': 2,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1,
}
letter_weight = {
        'A': 1,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 4,
        'H': 3,
        'I': 1,
        'J': 10,
        'K': 6,
        'L': 2,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 2,
        'V': 6,
        'W': 5,
        'X': 8,
        'Y': 4,
        'Z': 10,
}

def load_list():
    words = set()
    with open("words/NSWL2023.txt", "r") as file:
        for line in file:
            words.add(line.split()[0])
    return words

def can_construct_word(letters, word):
    return not (Counter(word) - Counter(letters))

def main():
    word_list = load_list()
    print("Hello from crossplay-solver!")
    print(len(word_list))
    for word in word_list:
        score = 0
        for char in word:
            score += letter_weight[char]
        print(f"{score}: {word}")

    pool = []
    for char, count in letter_count.items():
        print(char, count)
        pool = pool + [char] * count
    print(pool)

    selected = random.sample(pool, 7)
    # Remove them from the original list
    for item in selected:
        pool.remove(item)

    print(pool)
    print(selected)

    for word in word_list:
        if can_construct_word(selected, word):
            score = 0
            for char in word:
                score += letter_weight[char]
            print(f"{score}: {word}")
    print(selected)


if __name__ == "__main__":
    main()
