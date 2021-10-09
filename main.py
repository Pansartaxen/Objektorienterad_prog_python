#Marius Stokkedal
import random

class Diner:
    def __init__(self):
        self._pickup_worker = None
        self._pickup_food = None
        self._dropoff_worker = None
        self._has_worker = False
        self._has_food = False
    
    def set_in_worker():
        pass

    def set_out_worker():
        pass

    def set_in_food():
        pass

    def change_hp():
        #worker.change_hp()
        pass

class Barn:
    def __init__(self):
        self._queue = []
    
    def add_food(self, food):
        self._queue.append(food)

    def remove_food(self):
        return(self._queue.pop(0))

class Food:

    def __init__(self):
        self._quality = random.randfloat(1,100)
    
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
    def __init__(self):
        self._pickup_worker = None
        self._pick_food = None
        self._dropoff_worker = None
        self._has_worker = False
        self._has_product = False
    
    def set_in_worker(self, inRoad):
        pass
    
    def set_out_worker(self, outRoad):
        pass
    
    def set_in_product(self, inBarn):
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
        self._queue = []

    def remove_worker(self):
        return(self._queue.pop(0))

    def add_worker(self, worker):
        worker.change_hp(-(len(self._queue)))
        if worker.is_alive():
            self._queue.append(worker)

class Worker:
    def __init__(self):
        self._hp = 100
    
    def change_hp(self, change):
        pass

    def is_alive(self):
        return(self._hp > 0)

    def helth(self):
        return(self._hp)

class Factory:
    def __init__(self):
        self._pickup_worker = None
        self._pickup_food = None
        self._dropoff_worker = None
        self._has_worker = False

    def set_in_worker(self):
        pass

    def set_out_worker(self):
        pass

    def set_out_product(self):
        pass

    def change_lifepower(self):
        pass

    def create_product(self):
        pass

class Storage:
    def __init__(self):
        self._queue = []

    def add_product(self, product):
        self._queue.append(product)

    def remove_product(self):
        return(self._queue.pop(-1))

class Product:
    def __init__(self):
        pass