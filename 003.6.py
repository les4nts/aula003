litros = float(input("quantos litros voce abasteceu?"))
combustivel = input("qual o tipo de combustivel?(G - galosina, E- etanol) ")
gasolina = 5.8
etanol = 4.9

if combustivel == 'g' or combustivel == 'G':
    valor = litros*gasolina
    print(f"o valor final foi : RS {valor:.2f}")
elif combustivel == 'e' or combustivel == 'O':
    valor = litros*etanol
    print(f"o valor final foi : RS {valor:.2f}")
else:
    print("desculpa, não entendi, escolha G ou E! ")