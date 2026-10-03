import datetime
while True:
    kaam = input("log / retrieve / exit ?")
    if kaam == "exit":
        print("Bye! band kar diya. ")
        break

    if kaam == "log":
        name = input("Name batao:- ")
        kya = input("diet ya exercise:- ")
        cheez = input("kya kiya: ")
        time = datetime.datetime.now()
        with open(f"{name}_{kya}.txt", "a") as f:
            f.write(f"[{time}] {cheez}\n")
        print("Ho gya save !")

    if kaam == "retrieve":
        print("Kiska data padhna hai ?")
        name = input("name bata: ")
        kya = input("diet ya exercise: ")
        try:
            with open(f"{name}_{kya}.txt", "r") as f:
                print(f.read())
        except:
            print("File mili hi nahi!")
