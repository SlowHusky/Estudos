"""for i in range(25):
    walk = random_walk_v2(10)
    print(walk, "Distancia de casa = ", abs(walk[0]) + abs(walk[1]))
"""
import random
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

number_of_walks = 20000
for walk_length in range(1, 31):
    no_transport = 0 #numero de caminhadas de 4 ou menos de absoluto
    for i in range(number_of_walks):
        (x,y) = random_walk_v2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport)/ number_of_walks
    print("distancia do caminhar = ", walk_length,
          " / % sem transporte = ", 100*no_transport_percentage)
