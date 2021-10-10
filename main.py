#Marius Stokkedal
import random

class Accident_generator:
    def accident_check(self):
        accident = random.randint(1,10)
        return(accident > 7)

class Diner:
    def __init__(self):
        self._pickup_worker = None
        self._pickup_food = None
        self._dropoff_worker = None
        self._has_worker = False
        self._has_food = False
        self._worker = []
        self._food = []
    
    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad
    
    def set_in_food(self, inBarn):
        self._pickup_food = inBarn

    # def change_hp():
    #     #worker.change_hp()
    #     pass

    def _get_worker(self):
        worker = self._pickup_worker.remove_worker()
        if worker != None:
            self._worker.append(worker)
            self._has_worker = True
    
    def _get_food(self):
        food = self._pickup_food.remove_food()
        if food != None:
            self._food.append(food)
            self._has_food = True

    def _feed_worker(self):
        if self._has_food and self._has_worker:
            #food = self._pickup_food.remove_food()
            quality = self._food[0].quality()
            self._worker[0].change_hp(quality)
            self._dropoff_worker.add_worker(self._worker[0])
            self._worker.pop(0)
            self._food.pop(0)
            self._has_worker = False
            self._has_food = False

class Barn:
    def __init__(self):
        self._queue = [Food() for _ in range(100)]
    
    def add_food(self, food):
        self._queue.append(food)

    def remove_food(self):
        try:
            return(self._queue.pop(0))
        except:
            return(None)

class Food:
    def __init__(self):
        self._quality = random.randint(1,100)
    
    def quality(self):
        return(self._quality)

class Field:
    def __init__(self):
        self._pickup_worker = None
        self._dropoff_food = None
        self._dropoff_worker = None
        self._has_worker = False
    
    def set_in_worker(self):
        pass

    def set_out_worker(self):
        pass

    def set_out_food(self):
        pass

    def accident_generator(self):
        pass

    def change_hp(self):
        pass

    def produce(self):
        pass

class House:
    def __init__(self, inRoad, inBarn, outRoad):
        self._pickup_worker = inRoad
        self._pick_food = inBarn
        self._dropoff_worker = outRoad
        self._has_worker = False
        self._has_product = False
    
    def set_in_worker(self, inRoad):
        pass
    
    def set_out_worker(self, outRoad):
        pass
    
    def set_in_food(self, inBarn):
        pass
    
    def _worker_check(self):
        pass

    def _product_check(self):
        pass

    def create_worker(self):
        pass

    def execute():
        pass

class Road:
    def __init__(self):
        self._queue = [Worker() for _ in range(100)]

    def remove_worker(self):
        try:
            return(self._queue.pop(0))
        except:
            return(None)

    def add_worker(self, worker):
        worker.change_hp(-((len(self._queue)))/10)
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
    def __init__(self, inRoad, outFactory, outRoad):
        self._pickup_worker = inRoad
        self._dropoff_product = outFactory
        self._dropoff_worker = outRoad
        self._has_worker = False
        self._worker = [] #Ny
        self._accident = Accident_generator()

    def set_in_worker(self, inRoad):
        self._pickup_worker = inRoad
    
    def set_out_worker(self, outRoad):
        self._dropoff_worker = outRoad

    def set_out_product(self, outFactory):
        self._dropoff_product = outFactory

    def get_worker(self):
        worker = self._pickup_worker.remove_worker()
        self._worker.append(worker)
        self._has_worker = True

    def create_product(self):
        if self._has_worker:
            prod = Product()
            self._dropoff_product.add_product(prod)
            if self._accident.accident_check():
                hp = -1 * self._worker[0].health()
                self._worker[0].change_hp(hp) #Kills worker
                print('Worker died. #Sad')
            else:
                self._worker[0].change_hp(-10)
                self._dropoff_worker.add_worker(self._worker[0])
                self._dropoff_product.add_product(prod)
                self._worker.pop(0)
                self._has_worker = False

class Storage:
    def __init__(self):
        self._queue = [Product() for _ in range(100)]

    def add_product(self, product):
        self._queue.append(product)

    def remove_product(self):
        try:
            return(self._queue.pop(-1))
        except:
            return(None)

class Product:
    def __init__(self):
        pass


if __name__ == "__main__":
    r1 = Road()
    s1 = Storage()
    f1 = Factory(r1,s1,r1)

    f1.set_in_worker(r1)
    f1.set_out_worker(r1)
    f1.set_out_product(s1)

    while r1.que_length() > 0:
        f1.get_worker()
        f1.create_product()
        print(r1.que_length())
        #print(len(s1._queue))