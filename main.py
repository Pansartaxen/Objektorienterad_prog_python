#Marius Stokkedal
import random
import time
class Accident_generator:
    def accident_check(self):
        """Används för att se om en olycka sker eller ej"""
        accident = random.randint(1,10)
        return(accident > 6)

class Diner:
    def __init__(self, inRoad, inBarn, outRoad):
        self._pickup_worker = inRoad
        self._pickup_food = inBarn
        self._dropoff_worker = outRoad
        self._worker = []
        self._food = []
    
    def set_in_worker(self, inRoad):
        """Ändrar in-vägen för arbetare"""
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        """Ändrar ut-vägen för arbetare"""
        self._dropoff_worker = outRoad
    
    def set_in_food(self, inBarn):
        """Ändrar in-vägen för mat"""
        self._pickup_food = inBarn

    def connections(self):
        """Returnerar en lista innehållande alla in och utvägar"""
        return([self._pickup_worker,self._pickup_food,self._dropoff_worker])

    def action(self):
        """Hämtar samt matar arbetaren"""
        self._worker.append(self._pickup_worker.remove_worker())
        self._food.append(self._pickup_food.remove_food())
        if self._worker[0] != None and self._food[0] != None:
            quality = self._food[0].quality()
            self._worker[0].change_hp(quality)
            self._dropoff_worker.add_worker(self._worker[0])
            self._worker.pop(0)
            self._food.pop(0)

class Barn:
    def __init__(self):
        self._queue = []
    
    def add_food(self):
        """FIFO"""
        self._queue.append(Food())

    def remove_food(self):
        """FIFO"""
        try:
            return(self._queue.pop(0))
        except:
            return(None)
    
    def que_length(self):
        """Returnerar längden på self._queue"""
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
        self._worker = []
        self._accident = Accident_generator()

    def set_in_worker(self, inRoad):
        """Ändrar in-vägen för arbetare"""
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        """Ändrar ut-vägen för arbetare"""
        self._dropoff_worker = outRoad

    def set_out_food(self, outBarn):
        """Ändrar ut-vägen för mat"""
        self._dropoff_food = outBarn

    def connections(self):
        """Returnerar en lista innehållande alla in och utvägar"""
        return([self._pickup_worker,self._dropoff_food,self._dropoff_worker])

    def action(self):
        """Hämtar arbetare samt skapar mat"""
        self._worker.append(self._pickup_worker.remove_worker())
        if self._worker[0] != None:
            if self._accident.accident_check():
                hp = -0.75 * self._worker[0].health()
                self._worker[0].change_hp(hp)
            else:
                self._dropoff_food.add_food()
            self._dropoff_worker.add_worker(self._worker[0])
            self._worker.pop(0)

class House:
    def __init__(self, inRoad, inStorage, outRoad):
        self._pickup_worker = inRoad
        self._pickup_product = inStorage
        self._dropoff_worker = outRoad
        self._worker = []
        self._product = []

    def set_in_worker(self, inRoad):
        """Ändrar in-vägen för arbetare"""
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        """Ändrar ut-vägen för arbetare"""
        self._dropoff_worker = outRoad

    def set_in_product(self, inStorage):
        """Ändrar in-vägen för produkter"""
        self._pickup_product = inStorage

    def connections(self):
        """Returnerar en lista innehållande alla in och utvägar"""
        return([self._pickup_worker,self._pickup_product,self._dropoff_worker])

    def action(self):
        """Skpar arbetare eller vilar upp arbetare beroende på hur många som finns i in-vägen"""
        create = self._pickup_worker.que_length() >= 2
        if self._pickup_worker.que_length() < 100 and create:
            self._worker.append(self._pickup_worker.remove_worker())
            self._worker.append(self._pickup_worker.remove_worker())
            self._product.append(self._pickup_product.remove_product())
            for i in range(len(self._worker)):
                self._dropoff_worker.add_worker(self._worker[i])
            self._worker = []
            for _ in range(random.randint(1,2)):
                self._dropoff_worker.add_worker(Worker())
        elif self._pickup_worker.que_length() >= 100 or not create:
            self._worker.append(self._pickup_worker.remove_worker())
            if self._worker[0] != None:
                self._product.append(self._pickup_product.remove_product())
                self._worker[0].change_hp(50)
                self._dropoff_worker.add_worker(self._worker[0])
            self._worker = []
            self._product = []

class Road:
    def __init__(self):
        self._queue = [Worker() for _ in range(2)]

    def remove_worker(self):
        """FIFO"""
        try:
            return(self._queue.pop(0))
        except:
            return(None)

    def add_worker(self, worker):
        """FIFO. Skadar arbetaren olika mycket beroende på köns längd"""
        worker.change_hp(-((len(self._queue)))/10)
        if worker.is_alive():
            self._queue.append(worker)
    
    def que_length(self):
        return(len(self._queue))

class Worker:
    def __init__(self):
        self._hp = 100
    
    def change_hp(self, change):
        """Ändrar arbetarens hälsa"""
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
        self._worker = []
        self._accident = Accident_generator()
        self._damage = random.randint(-40,-20)

    def set_in_worker(self, inRoad):
        """Ändrar in-vägen för arbetare"""
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        """Ändrar ut-vägen för arbetare"""
        self._dropoff_worker = outRoad

    def set_out_product(self, outStorage):
        """Ändrar ut-vägen för produkter"""
        self._dropoff_product = outStorage

    def connections(self):
        """Returnerar en lista innehållande alla in och utvägar"""
        return([self._pickup_worker,self._dropoff_product,self._dropoff_worker])

    def action(self):
        """Hämtar en arbetare samt skapar en produkt om arbetaren överlever"""
        self._worker.append(self._pickup_worker.remove_worker())
        if self._worker[0] != None:
            if self._accident.accident_check():
                hp = -1 * self._worker[0].health()
                self._worker[0].change_hp(hp)
                self._worker.pop(0)
            else:
                self._worker[0].change_hp(self._damage)
                self._dropoff_worker.add_worker(self._worker[0])
                for _ in range(random.randint(1,3)):
                    self._dropoff_product.add_product(Product())
                self._worker.pop(0)

class Storage:
    def __init__(self):
        self._queue = []

    def add_product(self, product):
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


if __name__ == "__main__":
    r1 = Road()
    r2 = Road()
    r3 = Road()
    s1 = Storage()
    s2 = Storage()
    b1 = Barn()
    b2 = Barn()

    roads = [r1,r2,r3]
    storages = [s1,s2]
    barns = [b1,b2]
    transitions = []
    count = 0

    while r1.que_length() > 0 or r2.que_length() > 0 or r3.que_length():
        time.sleep(0.05)
        for _ in range(1):
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
                if i.que_length() <= 100:
                    transitions.append(House(i,maxStorage,i))
                elif i.que_length() > 100:
                    for x in transitions:
                        if type(x).__name__ == 'House':
                            popCount = 0
                            if popCount == 0:
                                index = transitions.index(x)
                                transitions.pop(index)
                                popCount += 1

            for i in barns:
                if i.que_length() <= 25:
                    transitions.append(Field(maxRoad,i,minRoad))
                    for x in transitions:
                            if type(x).__name__ == 'Diner':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)
                elif i.que_length() > 25:
                    transitions.append(Diner(minRoad,i,minRoad))
                    for x in transitions:
                            if type(x).__name__ == 'Field':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)

            for i in storages:
                if i.que_length() <= 25:
                    transitions.append(Factory(maxRoad,i,minRoad))
                elif i.que_length() > 25:
                    for x in transitions:
                            if type(x).__name__ == 'Factory':
                                if x.connections()[1] == i:
                                    index = transitions.index(x)
                                    transitions.pop(index)
                                    break

            x = []
            output = f'||    Rundor: {count:<4}    ||'
            output += f'    transitioner: {len(transitions):<4}'
            for i in transitions:
                x.append(type(i).__name__)
            y = ''
            output +=f' ||   r1:{r1.que_length():<3} r2:{r2.que_length():<3} r3:{r3.que_length():<3} s1:{s1.que_length():<3} s2:{s2.que_length():<3} b1:{b1.que_length():<3} b2:{b2.que_length():<2}'
            output += f'{y:<4}||    {set(x)}'
            print(output)
            print(150*'-')
    print('Alla dog :´(')