horario1 = int(input("digite o primeiro horario:"))
minuto1 = int (input("digite o minuto1:"))
horario2 = int(input("digite o segundo horario:"))
minuto2 = int(input("digite o horario 2:"))

horasaida = horario1+horario2
minutosaida = minuto1+minuto2

if horasaida >= 24:
    horasaida = horasaida - 24

#if horasaida >= 12:
    #horasaida = horasaida -12


if horasaida >12:
    horasaida = horasaida -12

if minutosaida >= 60:
    horasaida = horasaida -12
    horasaida = horasaida +1
    minutosaida = minutosaida -60



print(f"o horario de saida foi : {horasaida}:{minutosaida}")
