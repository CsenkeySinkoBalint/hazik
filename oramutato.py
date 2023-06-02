szoveg = input("az időpont")
ido = list(map(int,szoveg.split(":")))
perc = 6 * ido[1]
ora = ido[0] % 12 * 30 + 0.5 * ido[1]

szog = abs(ora-perc)

if szog>180:
    sog = 360 - szog

print(szog)
    
    


