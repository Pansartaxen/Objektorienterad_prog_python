#Marius Stokkedal
import random
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
    
    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad
    
    def set_in_food(self, inBarn):
        self._pickup_food = inBarn

    def action(self):
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
        x = random.randint(1,1000)
        if x > 500:
            for _ in range(2):
                self._queue.append(Food())
        #self._queue.append(Food())

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

    def action(self):
        self._worker.append(self._pickup_worker.remove_worker())
        #if self._has_worker:
        if self._worker[0] != None:
            if self._accident.accident_check():
                hp = -0.75 * self._worker[0].health()
                self._worker[0].change_hp(hp)
            self._dropoff_worker.add_worker(self._worker[0])
            self._dropoff_food.add_food()
            self._worker.pop(0)
            self._has_worker = False

class House:
    def __init__(self, inRoad, inStorage, outRoad):
        """Används en product när två arbetare existerar?"""
        self._pickup_worker = inRoad
        self._pickup_product = inStorage
        self._dropoff_worker = outRoad
        #self._has_worker = False
        self._worker = [] #Ny
        self._product = []

    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad

    def set_out_product(self, inStorage):
        self._pickup_product = inStorage

    def action(self):
        self._worker.append(self._pickup_worker.remove_worker())
        self._worker.append(self._pickup_worker.remove_worker())
        self._product.append(self._pickup_product.remove_product())
        if self._worker[0] and self._worker[1] != None:
            for i in range(len(self._worker)):
                self._dropoff_worker.add_worker(self._worker[i])
            self._worker = []
            self._dropoff_worker.add_worker(Worker()) #Creates new worker
            #print('Hooray! New worker')
        elif self._worker[0] != None:
            self._worker[0].change_hp(20)
            self._dropoff_worker.add_worker(self._worker[0])
            self._worker.pop(0)
            self._product.pop(0)

class Road:
    def __init__(self):
        #self._queue = [Worker() for _ in range(100)]
        self._queue = []

    def remove_worker(self):
        try:
            return(self._queue.pop(0))
        except:
            return(None)

    def add_worker(self, worker):
        worker.change_hp(-((len(self._queue))))
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

    def action(self):
        #if self._has_worker:
        self._worker.append(self._pickup_worker.remove_worker())
        if self._worker[0] != None:
            prod = Product()
            self._dropoff_product.add_product(prod)
            if self._accident.accident_check():
                hp = -1 * self._worker[0].health()
                self._worker[0].change_hp(hp) #Kills worker
                print('Worker died. #Sad')
                self._worker.pop(0)
                #self._has_worker = False
            else:
                #hp = -0.75 * self._worker[0].health()
                self._worker[0].change_hp(self._damage)
                self._dropoff_worker.add_worker(self._worker[0])
                self._dropoff_product.add_product(prod)
                self._worker.pop(0)
                #self._has_worker = False

class Storage:
    def __init__(self):
        #self._queue = [Product() for _ in range(100)]
        self._queue = []

    def add_product(self, product):
        x = random.randint(1,1000)
        if x > 400:
            for _ in range(2):
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
    s1 = Storage()
    b1 = Barn()
    b2 = Barn()

    for _ in range(100):
        r1.add_worker(Worker())
        r2.add_worker(Worker())
        s1.add_product(Product())
        b1.add_food()
        b2.add_food()

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
        print('---')
    print(f'-------- count: {count} -------')
    print(f'r1:{r1.que_length()}, r2:{r2.que_length()}, s1:{s1.que_length()}, b1:{b1.que_length()}, b2:{b2.que_length()}')