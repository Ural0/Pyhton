
n =input("Geben Sie bitte einen Text ein: ")

for i in range(0,len(n)):
	#print(ord(n[i]), end=",")
    if i < len(n) - 1: #Das „if“ und „else“ wird verwendet, damit am Ende kein Komma erscheint.
        print(ord(n[i]), end=",")
    else:
        print(ord(n[i]))