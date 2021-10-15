#Marius Stokkedal
import random
import time
class Accident_generator:
    def accident_check(self):
        accident = random.randint(1,10)
        return(accident > 6)

class Diner:
    def __init__(self, inRoad, inBarn, outRoad):
        self._pickup_worker = inRoad
        self._pickup_food = inBarn
        self._dropoff_worker = outRoad
        #self._has_worker = False
        #self._has_food = False
        self._worker = []
        self._food = []
        self._prio = True
    
    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad
    
    def set_in_food(self, inBarn):
        self._pickup_food = inBarn

    def change_priority(self, prio):
        self._prio = prio

    def connections(self):
        return([self._pickup_worker,self._pickup_food,self._dropoff_worker])

    def action(self):
        if self._prio:
            self._worker.append(self._pickup_worker.remove_worker())
            self._food.append(self._pickup_food.remove_food())
            #if self._has_worker:
            if self._worker[0] != None and self._food[0] != None:
            #if self._has_food and self._has_worker:
                quality = self._food[0].quality()
                self._worker[0].change_hp(quality)
                self._dropoff_worker.add_worker(self._worker[0])
                self._worker.pop(0)
                self._food.pop(0)
                self._has_worker = False
                self._has_food = False

class Barn:
    def __init__(self):
        #self._queue = [Food() for _ in range(100)]
        self._queue = []
    
    def add_food(self):
        # x = random.randint(1,1000)
        # if x > 600:
        #     for _ in range(2):
        #         self._queue.append(Food())
        # else:
        self._queue.append(Food())

    def remove_food(self):
        try:
            return(self._queue.pop(0))
        except:
            return(None)
    
    def que_length(self):
        return(len(self._queue))

class Food:
    def __init__(self):
        self._quality = random.randint(-15,15)
    
    def quality(self):
        return(self._quality)

class Field:
    def __init__(self, inRoad, outBarn, outRoad):
        self._pickup_worker = inRoad
        self._dropoff_food = outBarn
        self._dropoff_worker = outRoad
        #self._has_worker = False
        self._worker = [] #Ny
        self._accident = Accident_generator()

    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad

    def set_out_food(self, outBarn):
        self._dropoff_food = outBarn

    def connections(self):
        return([self._pickup_worker,self._dropoff_food,self._dropoff_worker])

    def action(self):
        self._worker.append(self._pickup_worker.remove_worker())
        #if self._has_worker:
        if self._worker[0] != None:
            if self._accident.accident_check():
                hp = -0.65 * self._worker[0].health()
                self._worker[0].change_hp(hp)
            else:
                self._dropoff_food.add_food()
            self._dropoff_worker.add_worker(self._worker[0])
            #self._dropoff_food.add_food()
            self._worker.pop(0)
            self._has_worker = False

class House:
    def __init__(self, inRoad, inStorage, outRoad):
        self._pickup_worker = inRoad
        self._pickup_product = inStorage
        self._dropoff_worker = outRoad
        self._create_worker = False
        self._worker = [] #Ny
        self._product = []

    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad

    def set_out_product(self, inStorage):
        self._pickup_product = inStorage

    def connections(self):
        return([self._pickup_worker,self._pickup_product,self._dropoff_worker])

    def change_priority(self,create):
        self._create_worker = create

    def action(self):
        if self._create_worker == True and self._pickup_worker.que_length() >= 2: #self._worker[1] != None:
            self._worker.append(self._pickup_worker.remove_worker())
            self._worker.append(self._pickup_worker.remove_worker())
            self._product.append(self._pickup_product.remove_product())
            for i in range(len(self._worker)):
                self._dropoff_worker.add_worker(self._worker[i])
            self._worker = []
            for _ in range(random.randint(1,2)):
                self._dropoff_worker.add_worker(Worker()) #Creates new worker
        #elif self._worker[0] != None:
        elif self._pickup_worker.que_length() == 1:#self._worker[0] != None:
            self._worker.append(self._pickup_worker.remove_worker())
            self._product.append(self._pickup_product.remove_product())
            self._worker[0].change_hp(50)
            self._dropoff_worker.add_worker(self._worker[0])
            self._worker.pop(0)
            self._product.pop(0)
        else:
            return(False)

class Road:
    def __init__(self):
        self._queue = [Worker() for _ in range(100)]
        #self._queue = []

    def remove_worker(self):
        try:
            return(self._queue.pop(0))
        except:
            return(None)

    def add_worker(self, worker):
        worker.change_hp(-((len(self._queue)))/1000)
        if worker.is_alive():
            self._queue.append(worker)
    
    def que_length(self):
        return(len(self._queue))

class Worker:
    def __init__(self):
        self._hp = 100
    
    def change_hp(self, change):
        self._hp += change

    def is_alive(self):
        return(self._hp > 0)

    def health(self):
        return(self._hp)

class Factory:
    def __init__(self, inRoad, outStorage, outRoad):
        self._pickup_worker = inRoad
        self._dropoff_product = outStorage
        self._dropoff_worker = outRoad
        #self._has_worker = False
        self._worker = [] #Ny
        self._accident = Accident_generator()
        self._damage = random.randint(-40,-10)

    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad

    def set_out_product(self, outStorage):
        self._dropoff_product = outStorage

    def connections(self):
        return([self._pickup_worker,self._dropoff_product,self._dropoff_worker])

    def action(self):
        #if self._has_worker:
        self._worker.append(self._pickup_worker.remove_worker())
        if self._worker[0] != None:
            if self._accident.accident_check():
                hp = -1 * self._worker[0].health()
                self._worker[0].change_hp(hp) #Kills worker
                #print('Worker died. #Sad')
                self._worker.pop(0)
                #self._has_worker = False
            else:
                #hp = -0.75 * self._worker[0].health()
                self._worker[0].change_hp(self._damage)
                #self._worker[0].change_hp(-500)
                self._dropoff_worker.add_worker(self._worker[0])
                for _ in range(random.randint(1,3)):
                    self._dropoff_product.add_product(Product())
                self._worker.pop(0)
                #self._has_worker = False

class Storage:
    def __init__(self):
        #self._queue = [Product() for _ in range(100)]
        self._queue = []

    def add_product(self, product):
        # x = random.randint(500,1000)
        # if x > 400:
        #     for _ in range(2):
        #         self._queue.append(product)
        self._queue.append(product)


    def remove_product(self):
        try:
            return(self._queue.pop(-1))
        except:
            return(None)

    def que_length(self):
        return(len(self._queue))

class Product:
    def __init__(self):
        pass

class Government:
    def __init__(self):
        self._goal_road = 100
        self._goal_barn = 100
        self._goal_storage = 100

if __name__ == "__main__":
    r1 = Road()
    r2 = Road()
    r3 = Road()
    s1 = Storage()
    s2 = Storage()
    b1 = Barn()
    b2 = Barn()

    # for _ in range(10000):
    #     r1.add_worker(Worker())
    #     r2.add_worker(Worker())
    #     s1.add_product(Product())
    #     b1.add_food()
    #     b2.add_food()
    
    roads = [r1,r2,r3]
    storages = [s1,s2]
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

    #transitions = [f1,h1,f2,d1,d2,h2,d3,fiel1,h3,fiel2,h4]
    transitions = []

    count = 0
    # while r1.que_length() > 0 or r2.que_length() > 0:
    #     print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, s1:{s1.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')
    #     for i in transitions:
    #         i.action()
    #         count += 1
    #     print('---')
    # print(f'-------- count: {count} -------')
    # print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, s1:{s1.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')
    #run = True

    while r1.que_length() > 0 or r2.que_length() > 0: #and run == True:
        #input('x-x-x-x-x-x-x-x-x-x-x-x Tryck enter förr att köra 200 rundor x-x-x-x-x-x-x-x-x-x-x-x')
        for _ in range(20000000000):
            if count % 100 == 0:
                time.sleep(2)
            for t in transitions:
                t.action()
                # if t.action() == False:
                #     run = False
                count += 1

                #print('---')
                #print(h1._create_worker,h2._create_worker,h3._create_worker,h4._create_worker)
            #print(d1._prio,d2._prio)
                #print(f'-------- count: {count} -------')
            
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
                            #transitions.append(House(i,maxStorage,i))
                elif i.que_length() > 10000:
                    # if minSaldoStorage <= 1000:
                    #     transitions.append(Factory(i,minStorage,i))
                    # elif minSaldoStorage > 1000:
                    for x in transitions:
                        if type(x).__name__ == 'House':
                            if x.connections()[2] == i:
                                index = transitions.index(x)
                                transitions.pop(index)
                                break
                                #x.change_priority(False)
            
            for i in barns:
                if i.que_length() < 30:
                    transitions.append(Field(maxRoad,i,minRoad))
                    # for x in transitions:
                    #         if type(x).__name__ == 'Diner':
                    #             if x.connections()[1] == i:
                    #                 index = transitions.index(x)
                    #                 transitions.pop(index)
                                    #x.change_priority(False)
                elif i.que_length() > 300:
                    transitions.append(Diner(minRoad,i,minRoad))
                    for x in transitions:
                            if type(x).__name__ == 'Field':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)
                                    #x.change_priority(True)

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
            # print('---')
            x = []
            #print(f'-------- count: {count} -------')
            print(f'-----------------------------------------------------------transitioner--{len(transitions)}')
            for i in transitions:
                x.append(type(i).__name__)
            print('----------------------------------------------------------------------------------------',set(x))
            #outputNames = [type(transitions[i]).__name__ for i in range(len(transitions))]
            #print(outputNames)
            print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, r3:{r3.que_length()}, s1:{s1.que_length()}, s2:{s2.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')