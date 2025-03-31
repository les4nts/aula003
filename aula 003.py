nome = input("qual o seu nome?")
idade = int(input("qual a sua idade?"))
salario = float(input("agora me informe o seu salario:"))
porcentagem= float ( input("quanto voce recebeu de aumento em porcentagem ultimo ajuste:"))
conta = (porcentagem*salario)/100
somaaumento = (salario+conta)
print (f"olá, {nome} você atualmente tem {idade} e recebia cerca de {salario} , por mês , antes do aumento. ")
print (f" voce teve um aumento de {conta} no seu salario que era {salario}, então seu salário agora é {somaaumento}")