male = ["Erik", "Lars", "Karl", "Johan"]

female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva"]

print(male , female)
taBort=str(input("Vilket namn ska tas bort? "))
if taBort in male:
    male.remove(taBort)
    print("Namnet " '"' + taBort + '"' + " har tagits bort.")
    print(male, female)
elif taBort in female:
    female.remove(taBort)
    print("Namnet " '"' + taBort + '"' + " har tagits bort.")
    print(male, female)
else:
    print("Namnet " + '"' + taBort + '"' + " finns inte i listan.")
