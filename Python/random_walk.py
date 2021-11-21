import random

def random_walk_v1(n):
    """Retorna coordenadas depois de 'n' blocos andados aleatoriamente"""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','L','O'])
        if step == 'N':y+=1
        elif step == 'S':y-=1
        elif step == 'L':x+=1
        else: x-=1
    #print(f"Eixo x: {x}, Eixo y: {y}")
    return x,y

"""for i in range(25):
    walk = random_walk_v1(10)
    print(walk, "Distancia de casa = ", abs(walk[0]) + abs(walk[1]))
"""

def random_walk_v2(n):
    """Retorna coordenadas depois de 'n' blocos andados aleatoriamente
    de modo pythonico
    """
    (x, y) = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return x,y

"""for i in range(25):
    walk = random_walk_v2(10)
    print(walk, "Distancia de casa = ", abs(walk[0]) + abs(walk[1]))
"""
        
