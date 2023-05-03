import random as rdm
from ursina import *

app = Ursina()
Sky()
ground = Entity(model='plane',
                scale=(10000, 1, 10000),
                collider='mesh',
                texture='grass',
                texture_scale=(500, 500),
                color=color.rgb(10, 60, 10),
                y=-2)

camera.z = -20
camera.y = 3

car: object = Entity(model='m/Porsche991',
                     texture='textures/dots.jpg',
                     scale=(1, 1, 1),
                     texure_scale=(5, 10, 10),
                     color=color.rgb(246, 0, 37), y=-1)

parc1 = Entity(model='cube',texture='textures/P.PNG',
               scale=(5,5,0),x=15,y=10,z=1499.5)
parc2 = Entity(model='cube', texture='textures/P.PNG',
               scale=(5,5,0),x=15,y=10,z=1500.5,rotation_y=180)
stick3 = Entity(model='cube',scale=(1,20,-1),
                x=15,y=0,z=1500,color=color.rgb(200,200,200))

parking = vv1 = Entity(model='cube', texture='textures/asphalt.jpg',
                       scale=(40,0,-80),x=30,y=-1,z=1541)

roud = Entity(model='plane',
              texture='textures/asphalt.jpg',
              scale=(20,1,10000),
              y=-1)
line = -2000
lll = Entity(model='cube',x=1,scale=(2,.5,1),z=line)
while line < 10000:
    lll = Entity(model='cube',y=-1,scale=(.5,.1,8),
                 z=line,x=3.45)
    line = line + 20
line = -2000
while line < 10000:
    lll = Entity(model='cube',y=-1,scale=(.5, .1, 8),
                 z=line,x=-3.45)
    line = line + 20
lll=Entity(model='cube',y=-1,scale=(1,.5,10000),
             x=-10,color=color.rgb(128,128,20))
lll=Entity(model='cube',y=-1,scale=(1,.5,10000),
             x=10,color=color.rgb(150,140,20))

roud1 = Entity(model='plane',
               texture='textures/asphalt.jpg',
               scale=(10000, 1, 20),
               y=-1,  z=2000 )
line = -2000
lll = Entity(model='cube',y=1,z=2000,
             scale=(2, .5, 1),x=line)
while line < 10000:
    lll = Entity(model='cube',y=-1,
                 scale=(8, .1, .5),
                 x=line, z=2003.45)
    line = line + 20
line = -2000
while line < 10000:
    lll = Entity(model='cube',y=-1,scale=(8,.1,.5),
                 x=line,z=1996.55)
    line = line + 20

lll=Entity(model='cube',y=-1,scale=(10000,.5,1),
             z=1990,color=color.rgb(128,128,20))
lll=Entity(model='cube',y=-1,scale=(10000,.5,1),
             z=2010,color=color.rgb(150,140,20))

line = -2000
while line < 10000:
    ccc = rdm.randint(3, 5)
    deg = rdm.randint(0, 90)
    sonic = Entity(model='cube',
                   texture='textures/panelka.PNG',
                   scale=(20, 10 * ccc, 2 * ccc),
                   y=-.5, x=-25, z=line,
                   rotation_y=deg,
                   color=color.rgb(255, 255, 255))
    line = line + 60

a = 0
val = 0
delta = 0
L = 0.5258
l_r = L/2
dt = time.dt
beta = math.atan((l_r * math.tan(delta)) / L)
w = dt*(val*math.tan(math.degrees(delta))
        * math.cos(math.degrees(beta))) / L

def update():
    global val # Скорость
    global w # Тета
    global delta # Дельта
    global dt # Дельта времени
    global a # Скорость пешего хода
    global beta # Бета

    car.rotation_y = 0
    car.rotation_z = 0

    if held_keys['e'] and \
            car.parent != camera.ui:
        car.parent = camera.ui # Привязка камеры к машине
        car.scale = (0.15, 0.15, -0.15)
        car.y = -.3
        car.z = 20
    if not held_keys['e']: # Пеший ход
        car.z = 5
        if held_keys['d']: # Поворот (пеший ход)
            if a != 0:
                camera.rotation_y += 1
                car.rotation_y = 0
                car.rotation_z = 0
            elif val != 0:
                camera.rotation_y += 1
                car.rotation_y = 0
                car.rotation_z = 0
            else:
                camera.rotation_y = 0

        if held_keys['a']: # Поворот (пеший ход)
            if a != 0:
                camera.rotation_y -= 1
                car.rotation_y = 0
                car.rotation_z = 0
            elif val != 0:
                camera.rotation_y -= 1
                car.rotation_y = 0
                car.rotation_z = 0
            else:
                camera.rotation_y = 0

    if held_keys['w']:
        if car.parent != camera.ui: # Для пешего хода
            if a < .7:
                a = .7
            camera.x += a *\
                        math.sin(3.14 * camera.rotation_y / 180)
            camera.z += a *\
                        math.cos(3.14 * camera.rotation_y / 180)
            camera.y=.3 * \
                     abs(math.sin(.35 *(camera.x+camera.z)))+1
        else: # Для машины
            if val < 3.5:
                val += 0.1
            camera.x += val *\
                        math.sin(3.14 * camera.rotation_y / 180)
            camera.z += val *\
                        math.cos(3.14 * camera.rotation_y / 180)
    elif val > 0:
        val -= 0.01
        camera.x += val *\
                    math.sin(3.14 * camera.rotation_y / 180)
        camera.z += val *\
                    math.cos(3.14 * camera.rotation_y / 180)
    elif val < 0:
        val = 0

    if held_keys['s']:
        if car.parent != camera.ui: # Для пешего хода
            camera.x -= 1 *\
                        math.sin(3.14 * camera.rotation_y / 180)
            camera.z -= 1 *\
                        math.cos(3.14 * camera.rotation_y / 180)
            camera.y = .3 *\
                       abs(math.sin(.35*(camera.x+camera.z)))+1
        else: # Для машины
            if val > -1:
                val -= 0.25
            camera.x -= 1 *\
                        math.sin(3.14 * camera.rotation_y / 180)
            camera.z -= 1 *\
                        math.cos(3.14 * camera.rotation_y / 180)

    if held_keys['d']: # Привязка кинематической модели велосипеда
        if val != 0:
            if delta < math.pi / 6:
                delta += math.pi / 180 # Наращивание угла дельта
                car.rotation_y = -math.degrees(delta)
                car.rotation_x = cos(-w + beta)
                car.rotation_z = sin(-w + beta)
            elif delta >= math.pi / 6:
                delta = math.pi / 6
                car.rotation_y = -math.degrees(delta)
                car.rotation_x = cos(-w + beta)
                car.rotation_z = sin(-w + beta)
    elif delta > 0: # Возвращение угла дельта в 0
        delta -= math.pi / 90
        car.rotation_y = -math.degrees(delta)

    if held_keys['a']:# Привязка кинематической модели велосипеда
        if val != 0:
            if delta > -math.pi / 6:
                delta -= math.pi / 180
                car.rotation_y = -math.degrees(delta)  # дельта
                car.rotation_x = cos(w + beta)
                car.rotation_z = sin(w + beta)
            elif delta <= math.pi / 6:
                delta = -math.pi / 6
                car.rotation_y = -math.degrees(delta)  # дельта
                car.rotation_x = cos(w + beta)
                car.rotation_z = sin(w + beta)
    elif delta < 0:
        delta += math.pi / 90
        car.rotation_y = -math.degrees(delta)

    if held_keys['p']: # Автономная парковка
        g = time.perf_counter()
        if g <= 1:
            camera.z -=1 *\
                       math.cos(3.14 * camera.rotation_y / 180)
            camera.x -=1 *\
                       math.sin(3.14 * camera.rotation_y / 180)
            car.rotation_y = -3
            camera.rotation_y -= 0.3
        elif g <= 2:
            camera.z -=1 *\
                       math.cos(3.14 * camera.rotation_y / 180)
            camera.x -=1 *\
                       math.sin(3.14 * camera.rotation_y / 180)
            car.rotation_y = -6
            camera.rotation_y -= 0.6
        elif g <= 3:
            camera.z -= 1 *\
                        math.cos(3.14 * camera.rotation_y / 180)
            camera.x -= 1 *\
                        math.sin(3.14 * camera.rotation_y / 180)
            car.rotation_y = -9
            camera.rotation_y -= 0.9
        elif g <= 4:
            camera.z -= 1 *\
                        math.cos(3.14 * camera.rotation_y / 180)
            camera.x -= 1 *\
                        math.sin(3.14 * camera.rotation_y / 180)
            car.rotation_y = -15
            camera.rotation_y -= 1.5
        elif g <= 4.30:
            camera.z -= 1 *\
                        math.cos(3.14 * camera.rotation_y / 180)
            camera.x -= 1 *\
                        math.sin(3.14 * camera.rotation_y / 180)
            car.rotation_y = -20
            camera.rotation_y -= 1.5

    # Дополнительные функции
    if held_keys['q']:
        quit()
    if held_keys['1']:
        val = 0.5
    if held_keys['8']:
        camera.rotation_x += .3
    if held_keys['2']:
        camera.rotation_x -= .3
    if held_keys['i']:
        camera.y += 1
    if held_keys['k']:
        camera.y -= 1
    if held_keys['6']:
        camera.rotation_z += 1
    if held_keys['4']:
        camera.rotation_z -= 1

app.run()

#print(round(camera.x, 1), round(camera.z + 20, 1))