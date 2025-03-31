n1 = float(input(" nota 1:"))
n2 = float(input(" nota 2:"))
n3 = float(input(" nota 3:"))

media = (n1+n2+n3)/3
if media>=6.0:
    print (f"aprovado. a sua media é {media}")
else:
    if media<=6.0:
        print(f"reprovado. sua media foi {media}")
