print("Bitte geben Sie die Zahlen ein, die in die Liste aufgenommen werden sollen. Drücken Sie 'q', um die Eingabe zu beenden.")
numbers = []
while True:
    user_input = input()
    if user_input == 'q':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein oder drücken Sie 'q', um die Eingabe zu beenden.")

numbers.sort()
print("Sortierte Liste:", numbers)
