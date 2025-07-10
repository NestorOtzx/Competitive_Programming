from sys import stdin
from collections import deque

casosJugados = {}

def main():
    cartas = list(map(int, stdin.readline().split()))
    count = 0

    deck_cartas = deque()
    
    while (cartas != ""):
        for x in cartas:
            if (x == 0):
                return
            count += 1
            deck_cartas.appendleft(x)
            
            if count == 52:
                juego(deck_cartas)
                deck_cartas.clear()
                count = 0
        cartas = list(map(int, stdin.readline().split()))
    
def juego(deck):
    global casosJugados
    casosJugados.clear()

    pilas = []

    for x in range(0, 7):
        pilas.append(deque())

    pilaActual = 0
    jugada = 0
    draw = False
    comprobarDraw = False
    while (True):
        pilas[pilaActual].append(deck.pop())
        jugada+=1

        if (comprobarDraw == True):
            stringDatos = str(pilaActual)+"|"+str(deck)+"|"+str(pilas)
            if (comprobarEmpate(stringDatos, jugada)):
                print("Draw:",jugada-1)
                break

        
        while(True): 
            tamanioPila = len(pilas[pilaActual])
            
            if (tamanioPila>2): 
                
                primeraCarta = pilas[pilaActual][0]
                segundaCarta = pilas[pilaActual][1]
                ultimaCarta = pilas[pilaActual][tamanioPila-1]
                penultimaCarta = pilas[pilaActual][tamanioPila-2]
                antePenultimaCarta = pilas[pilaActual][tamanioPila-3]

                if (comprobarSuma(primeraCarta, segundaCarta, ultimaCarta)):
                    comprobarDraw = True
                    primeraCarta = pilas[pilaActual].popleft()
                    segundaCarta = pilas[pilaActual].popleft()
                    ultimaCarta = pilas[pilaActual].pop()
    
                
                    deck.appendleft(primeraCarta)
                    deck.appendleft(segundaCarta)
                    deck.appendleft(ultimaCarta)
                    continue
                    
                elif (comprobarSuma(primeraCarta, penultimaCarta, ultimaCarta)): 
                    comprobarDraw = True
                    primeraCarta = pilas[pilaActual].popleft()
                    ultimaCarta = pilas[pilaActual].pop()
                    penultimaCarta = pilas[pilaActual].pop()
                
                    deck.appendleft(primeraCarta)
                    deck.appendleft(penultimaCarta)
                    deck.appendleft(ultimaCarta)
                    continue 
                
                elif (comprobarSuma(antePenultimaCarta, penultimaCarta, ultimaCarta)):
                    comprobarDraw = True
                    ultimaCarta = pilas[pilaActual].pop()
                    penultimaCarta = pilas[pilaActual].pop()
                    antePenultimaCarta = pilas[pilaActual].pop()

                    deck.appendleft(antePenultimaCarta)
                    deck.appendleft(penultimaCarta)
                    deck.appendleft(ultimaCarta)
                    continue 
                else:
                    break

            elif (tamanioPila == 0):
                pilas.remove(pilas[pilaActual])
                pilaActual -= 1
                break
            else: 
                break

        pilaActual += 1
        if (pilaActual >= len(pilas)):
            pilaActual = 0

        if (draw == True):
            print("Draw:",jugada)
            break
        if (len(deck) < 1):
            print("Loss:",jugada)
            break
        if (len(pilas) < 1):
            print("Win :",jugada)
            break
        
def comprobarEmpate(datos, linea_jugada):
    global casosJugados
    
    if datos in casosJugados:
        return True
    casosJugados[datos] = linea_jugada

def comprobarSuma(a, b, c):
    return (a + b + c) == 10 or (a + b + c) == 20 or (a + b + c) == 30

main()
