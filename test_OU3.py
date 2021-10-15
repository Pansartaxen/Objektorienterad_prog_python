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

while r1.que_length() > 0 or r2.que_length() > 0: #and run == True:
        input('x-x-x-x-x-x-x-x-x-x-x-x Tryck enter förr att köra 200 rundor x-x-x-x-x-x-x-x-x-x-x-x')
        for _ in range(200):
            if count % 100 == 0:
                time.sleep(2)
            for t in transitions:
                t.action()
                count += 1
            
            minSaldoStorage = 0
            maxSaldoStorage = 0
            minStorage = storages[0]
            maxStorage = storages[0]
            for i in storages:
                if i.que_length() > maxSaldoStorage:
                    maxSaldoStorage = i.que_length()
                    maxStorage = i
                elif i.que_length() <= minSaldoStorage:
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
                elif i.que_length() <= minSaldoBarn:
                    minSaldoBarn = i.que_length()
                    minBarn = i

            minSaldoRoad = 0
            maxSaldoRoad = 0
            minRoad = roads[0]
            maxRoad = roads[0]
            for i in roads:
                if i.que_length() > maxSaldoRoad:
                    maxSaldoRoad = i.que_length()
                    maxRoad = i
                elif i.que_length() <= minSaldoRoad:
                    minSaldoRoad = i.que_length()
                    minRoad = i

            for i in roads:
                if i.que_length() < 300:
                    transitions.append(House(i,maxStorage,i))
                    for x in transitions:
                            if type(x).__name__ == 'House':
                                if x.connections()[2] == i:
                                    x.change_priority(True)
                elif i.que_length() > 10000:
                    for x in transitions:
                        if type(x).__name__ == 'House':
                            if x.connections()[2] == i:
                                x.change_priority(False)
            
            for i in barns:
                if i.que_length() < 30:
                    transitions.append(Field(maxRoad,i,minRoad))
                elif i.que_length() > 300:
                    transitions.append(Diner(minRoad,i,minRoad))
                    for x in transitions:
                            if type(x).__name__ == 'Field':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)

            for i in storages:
                if i.que_length() < 50:
                    transitions.append(Factory(maxRoad,i,minRoad))
                elif i.que_length() > 500:
                    for x in transitions:
                            if type(x).__name__ == 'Factory':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)
                                    break

            x = []
            print(f'-----------------------------------------------------------transitioner--{len(transitions)}')
            for i in transitions:
                x.append(type(i).__name__)
            print('----------------------------------------------------------------------------------------',set(x))
            print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, r3:{r3.que_length()}, s1:{s1.que_length()}, s2:{s2.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')