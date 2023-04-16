import csv
e=0.001
all_cars=[]
class Car:
    i=0
    def __init__(self, make: str, model: str, year: int, speedx=0, speedy=0, speedz=0, x=0, y=0, z=0):
        self.make=make
        self.model=model
        self.year=year
        self.speedx=speedx
        self.speedy=speedy
        self.speedz=speedz
        self.x=x
        self.y=y
        self.z=z
        self.i=Car.i
        Car.i+=1
        all_cars.append(self)
    def __repr__(self):
        return f"{self.i}. {self.make} {self.model} {self.year}"
    def accelerate(self, dx, dy):
        self.speedx+=dx
        self.speedy+=dy
        self.speedz+=dz
    def brake(self, dx, dy):
        self.speedx-=dx
        self.speedy-=dy
        self.speedz+=dz
    def move(self, time):
        self.x+=self.speedx*time
        self.y+=self.speedy*time
        self.z+=self.speedz*time
    @staticmethod
    def list_cars():
        print(all_cars)
    def detect_collision(self, car2):
        if (abs(self.x-car2.x)<e and (self.y-car2.y)<e and (self.z-car2.z)<e):
            print(f"Car {self.i} collided with Car {car2.i}")
        else:
            print("No Collision")
    @classmethod
    def from_csv(cls):
        with open('cars.csv', 'r') as f:
            items=list(csv.DictReader(f))
        for item in items:
            Car(item['make'], item['model'], item['year'], int(item['speedx']), int(item['speedy']), int(item['speedz']), int(item['x']), int(item['y']), int(item['z']))
    def time_to_collision(self, car2):
        itr=1
        x1, y1, z1=self.x, self.y, self.z
        x2, y2, z2=car2.x, car2.y, car2.z
        dist=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
        k=0.001
        x1, y1, z1=self.x+self.speedx*k, self.y+self.speedy*k, self.z+self.speedz*k
        x2, y2, z2=car2.x+car2.speedx*k, car2.y+car2.speedy*k, car2.z+car2.speedz*k
        while(dist>e and dist>(x1-x2)**2+(y1-y2)**2+(z1-z2)**2):
            dist=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
            x1, y1, z1=x1+self.speedx*k, y1+self.speedy*k, z1+self.speedz*k
            x2, y2, z2=x2+car2.speedx*k, y2+car2.speedy*k, z2+car2.speedz*k
            itr+=1
        if(dist<=e):
            print(f"Car {self.i} and Car {car2.i} will collide in {k*itr} hours")
        else:
            print(f"Car {self.i} and Car {car2.i} will not collide")
            
Car.from_csv()
print(all_cars[1].speedx)
Car.list_cars()
all_cars[0].time_to_collision(all_cars[1])