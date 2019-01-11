def dict_file_txt():
    f = open("dict_text.txt", "r")
    l_dict = {}
    for line in f:
        (key, val) = line.split()
        l_dict[str(key)] = int(val)
    f.close()
    return l_dict


def ASL_words():
    import random
    words = list(dict_file_txt())
    wrong_words = []
    try:
        for _ in words:
            word = words.pop(random.randrange(0, len(words)))
            inp = input(word + ": ")
            if inp == "exit":
                break
            elif inp != "":
                wrong_words.append(word)

    finally:
        print("\n--------------------------------\nYou got these wrong:\n")
        for wword in wrong_words:
            print(wword)
