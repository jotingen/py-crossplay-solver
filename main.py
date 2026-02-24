def load_list():
    words = set()
    with open("words/NSWL2023.txt", "r") as file:
        for line in file:
            words.add(line.split()[0])
    return words

def main():
    word_list = load_list()
    print("Hello from crossplay-solver!")
    print(len(word_list()))


if __name__ == "__main__":
    main()
