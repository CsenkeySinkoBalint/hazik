def min(be):
  ki = be[0]
  for i in range(1,len(be)):
    if be[i] < ki:
      ki=be[i]
  return ki    

def max(be):
  ki = be[0]
  for i in range(1,len(be)):
    if be[i] > ki:
      ki=be[i]
  return ki    

def atlag(be):
  asd = 0
  for i in range(len(be)):
    asd +=be[i]
  return asd/len(be)

d=[['a',2],['b',3],['c',5]]
valasz=[]

for i in range(len(d)):
  valasz.append(d[i][1])
  print('Legnagyobb elem:' + str(max(valasz)))
  print('Legkisebb elem:' + str(min(valasz)))
  print('Átlagos érték:' + str(atlag(valasz)))
