f = open("dict_text.txt", "a")
while_bool = True
number = 0
input_number = None
while while_bool:
    input_number = input("Enter page number: ")
    if input_number == "":
        f.write("\n" + input("Enter word: ") + " " + str(number))
    else:
        number = int(input_number)
