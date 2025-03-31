time1 = input("time 1:")
time2 = input("time 2:")
gols1 = input(f"quantos gols fez o {time1} :")
gols2 = input(f"quantos gols fez {time2} :")

if gols1>gols2:
    print(f"{time1} vencedor na contagem de {gols1}.")
else:
    if gols2>gols1:
        print(f"{time2} vencedor na contagem de {gols2}.")
    else:
        print(f"empate.")
