import math

print('Hva er lengden i centimeter?')
x = input()
print('lengden er ' + x + 'cm')

print('Hva er bredden i centimeter?')
z = input()
print('Bredden er ' + z + 'cm')

print('Hva er tykkelsen i centimeter?')
y = input()
print('Tykkelsen er ' + y + 'cm')
print(' ')

x = int(x)
z = int(z)
y = int(y)

areal = (x * z)/10000
print('Arealet er ' + str(areal) + ' kvadratmeter')

volum = (x * z * y)/1000
print('Volumet er ' + str(volum) + ' liter')
print(' ')

print('Vet du hva trykkstyrke betyr?')
vetdu = input()
if vetdu == 'ja':
    print('Ok')
else:
    print('Fasthetsklassen til betong har ofte benevnelser B20, B30, B35, B45 og lignende. Dette beskriver trykkfastheten målt i MPa (megapascal) – jo høyere tall jo større trykkstyrke.')

print(' ')
print('Hvilken trykkstyrke ønsker du å bruke?')
print('B20, B25, B30, B35 eller B40')
b = input()
print(' ')
print('Du bruker ' + b)


if b == 'B20':
    # 2kg = 1 liter
    # pris per kg = 1,4kr
    kg = volum * 2
    pris = kg * 1.4
    prisFK = "{:.2f}".format(pris)
    sekker = kg / 25
    sekkerFK = math.ceil(sekker)
    print('Du må kjøpe ' + str(sekker) + ' 25kg sekker')
    print('Det vil koste ' + str(prisFK) + ' kroner')

if b == 'B25':
    # 2kg = 1 liter
    # pris per kg = 2,196kr
    kg = volum * 2
    pris = kg * 2.196
    prisFK = "{:.2f}".format(pris)
    sekker = kg / 25
    sekkerFK = math.ceil(sekker)
    print('Du må kjøpe ' + str(sekker) + ' 25kg sekker')
    print('Det vil koste ' + str(prisFK) + ' kroner')

if b == 'B30':
    # 2kg = 1 liter
    # pris per kg = 2,36kr
    kg = volum * 2
    pris = kg * 2.36
    prisFK = "{:.2f}".format(pris)
    sekker = kg / 25
    sekkerFK = math.ceil(sekker)
    print('Du må kjøpe ' + str(sekkerFK) + ' 25kg sekker')
    print('Det vil koste ' + str(prisFK) + ' kroner')

if b == 'B35':
    # 2kg = 1 liter
    # pris per kg = 2,558kr
    kg = volum * 2
    pris = kg * 2.558
    prisFK = "{:.2f}".format(pris)
    sekker = kg / 25
    sekkerFK = math.ceil(sekker)
    print('Du må kjøpe ' + str(sekker) + ' 25kg sekker')
    print('Det vil koste ' + str(prisFK) + ' kroner')

if b == 'B40':
    # 2kg = 1 liter
    # pris per kg = 3,72kr
    kg = volum * 2
    pris = kg * 3.72
    prisFK = "{:.2f}".format(pris)
    sekker = kg / 25
    sekkerFK = math.ceil(sekker)
    print('Du må kjøpe ' + str(sekker) + '  25kg sekker')
    print('Det vil koste ' + str(prisFK) + ' kroner')


