from main import Factory


print(1>0)
lst = [1,None]

print(lst)

r1 = Road()
r2 = Road()
s1 = Storage()
b1 = Barn()
b2 = Barn()

for _ in range(100):
    r1.add_worker(Worker())
    r2.add_worker(Worker())
    s1.add_product(Product())
    b1.add_food()
    b2.add_food()

roads = [r1,r2]
storages = [s1]
barns = [b1, b2]

f1 = Factory(r1,s1,r1)
f2 = Factory(r2,s1,r2)
d1 = Diner(r1,b1,r1)
d2 = Diner(r1,b2,r2)
d3 = Diner(r2,b2,r1)
fiel1 = Field(r1,b1,r1)
fiel2 = Field(r2,b2,r2)
h1 = House(r1,s1,r1)
h2 = House(r1,s1,r2)
h3 = House(r2,s1,r2)
h4 = House(r2,s1,r1)

transitions = [f1,h1,f2,d1,d2,h2,d3,fiel1,h3,fiel2,h4]

count = 0

while r1.que_length() > 0 or r2.que_length() > 0:
    print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, s1:{s1.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')
    for i in transitions:
        i.action()
        count += 1
    
    minSaldoStorage = 0
    maxSaldoStorage = 0
    minStorage = storages[0]
    maxStorage = storages[0]
    for i in storages:
        if i.que_length() > maxSaldoStorage:
            maxSaldoStorage = i.que_length()
            maxStorage = i
        elif i.que_length() < minSaldoStorage:
            minSaldoStorage = i.que_length()
            minStorage = i

    minSaldoBarn = 0
    maxSaldoBarn = 0
    minBarn = barns[0]
    maxBarn = barns[0]
    for i in barns:
        if i.que_length() > maxSaldoBarn:
            maxSaldoBarn = i.que_length()
            maxBarn = i
        elif i.que_length() < minSaldoBarn:
            minSaldoBarn = i.que_length()
            minBarn = i

    for i in roads:
        if i.que_length() < 10:
            transitions.append(House(i,maxStorage,i))
        elif i.que_length() > 200:
            if minStorage < 200:
                transitions.append(Factory(i,minStorage,i))
            elif minStorage > 200:
                for x in transitions:
                    if type(x).__name__ == 'House':
                        if x.connections()[0] == i:
                            index = transitions.index(x)
                            transitions.pop(index)
                            
    print('---')
print(f'-------- count: {count} -------')
print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, s1:{s1.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')