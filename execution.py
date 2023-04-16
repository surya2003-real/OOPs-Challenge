import object as oj
from object import Car
Car.from_csv()
Car.list_cars()
oj.all_cars[3].accelerate(12, 12, 3)
print(oj.all_cars[3].speedx)
oj.all_cars[4].brake(1, 1, 1)
print(oj.all_cars[4].speedx)
oj.all_cars[2].move(1)
print(oj.all_cars[2].x)
print(oj.all_cars[2].y)
print(oj.all_cars[2].z)
oj.all_cars[3].detect_collision(oj.all_cars[4])
oj.all_cars[0].time_to_collision(oj.all_cars[1])
