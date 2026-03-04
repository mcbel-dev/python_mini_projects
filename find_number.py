import random 
number = random.randint(1,100)

while True:
    try:
        choice = int(input("hadaj cislo od 1 - 100: "))
        if choice < number:
            print("prilis nizke")
        elif choice > number:
            print("prilis vysoke")
        else:
            print("uhadol si spravne cislo.")
            break 
    except ValueError:
        print("zadaj len validne cislo")
