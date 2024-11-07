nombre1 = input("como se llama jugador1? ")
nombre2 = input("como se llama jugador2? ")

jugador1 = input("Hola jugador1 Que eliges piedra papel o tijera?:  ")
jugador2 = input("Hola jugador2 Que eliges piedra papel o tijera?:  ")

condicion1 = jugador1 == "Piedra" and jugador2 == "Tijera"
condicion2 = jugador1 == "Papel" and jugador2 == "Piedra"
condicion3 = jugador1 == "Tijera" and jugador2 == "Papel"
if jugador1 == jugador2:
    print("empate")
elif condicion1 or condicion2 or condicion3:
    print("gana: ", nombre1)
else:
    print("ha ganado: ", nombre2)