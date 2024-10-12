#QUESTÃO 2
entrada = str(input("Digite algo: "))
contador = entrada.lower().count("a")
if contador == 0:
    print("Nenhuma letra A digitada.")
else:
    print("Foram digitadas", contador, "letras A.")