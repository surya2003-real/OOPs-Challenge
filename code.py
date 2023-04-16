import csv
all_cars=[]
class Car:
    i=0
    def __init__(self, make: str, model: str, year: int, speedx=0, speedy=0, x=0, y=0):
        self.make=make
        self.model=model
        self.year=year
        self.speedx=speedx
        self.speedy=speedy
        #self.speedz=speedz
        self.x=x
        self.y=y
        #self.z=z
        self.i=Car.i
        Car.i+=1
        all_cars.append(self)
    def __repr__(self):
        return f"{self.i}. {self.make} {self.model} {self.year}"
    def accelerate(self, dx, dy):
        self.speedx+=dx
        self.speedy+=dy
    def brake(self, dx, dy):
        self.speedx-=dx
        self.speedy-=dy
    def move(self, time):
        self.x+=speedx*time
        self.y+=speedy*time
    @staticmethod
    def list_cars():
        print(all_cars)
    def detect_collision(self, car2):
        if (self.x==car2.x and self.y==car2.y):
            print(f"Car {self.i} collided with Car {car2.i}")
        else:
            print("No Collision")
    @classmethod
    def from_csv(cls):
        with open('cars.csv', 'r') as f:
            items=list(csv.DictReader(f))
        for item in items:
            Car(item['make'], item['model'], item['year'], item['speedx'], item['speedy'], item['x'], item['y'])

Car.from_csv()
print(all_cars)