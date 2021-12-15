import string

lines = []
with open('Braun.txt') as f:
    contents = f.read()
    print(contents)

with open('Braun.txt') as f:
    lines = f.readlines()


totalcap = str(lines[0])
Ethan= str(lines[1])
David = str(lines[2])

'''
print(totalcap, Ethan, David)
EthanClean = ''
DavidClean = ''
for element in range(0, len(Ethan)):
  if element.isdigit():
    EthanClean += (Ethan[element])
for element in range(0, len(David)):
  if element.isdigit():
    DavidClean += (David[element])
print(Ethan,David)
'''





'''EthanClean = ''
DavidClean = ''
for element in range(0, len(Ethan)):
  if element.isdigit():
    EthanClean += (Ethan[element])
for element in range(0, len(David)):
  if element.isdigit():
    DavidClean += (David[element])

print(EthanClean , DavidClean)
  '''
'''receiverint = int(input('Who will get money? 1=Ethan , 2=David'))
if receiverint == 1:
  giver = David
  receiver = Ethan
else:
  giver = Ethan
  receiver = David

Amount = int(input('How much?'))
giver - Amount
receiver + Amount

print(Ethan,David)'''

