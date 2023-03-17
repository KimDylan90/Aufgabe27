print("Bitte geben Sie die Wörter ein, die in die Liste aufgenommen werden sollen. Drücken Sie 'q', um die Eingabe zu beenden.")
words = []
while True:
    user_input = input()
    if user_input == 'q':
        break
    words.append(user_input)

words.sort()
print("Sortierte Liste:", words)
