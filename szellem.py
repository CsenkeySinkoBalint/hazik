import random
szint = 5
for i in range(5):
        ajto = int(input("melyik ajton mesz be?"))
        if ajto > 3:
            print("nincs ennyi ajto.")
        else:
         szellem = random.randint(0,3)
         if ajto == szellem:
             print("vége a játéknak.")
             exit()
         else:
            print("tovabbjutottal.",szint)
            szint = szint-1
    

       
