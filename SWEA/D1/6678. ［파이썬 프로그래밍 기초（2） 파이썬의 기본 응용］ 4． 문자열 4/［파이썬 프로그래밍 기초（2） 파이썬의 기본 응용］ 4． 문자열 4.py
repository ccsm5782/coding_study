n = []
while True:
    try:
        string = input()
        if string == "":
            break
        else:
            n.append(string.upper())
    except EOFError:
        break

for i in range(len(n)):
    print(f">> {n[i]}")