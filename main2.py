
while True:
    num1 = input("digite seu nome: ")
    if num1.lower() == "sair":
        print("Ok, brincaremos mais tarde. Encerrando a brincadeira...")
        break

    num2 = input("digite seu sobrenome: ")
    if num2.lower() == "sair":
        print("Ok, brincaremos mais tarde. Encerrando a brincadeira...")
        break

    num3 = input("quantas letras tem seu nome?: ")
    if num3.lower() == "sair":
        print("Ok, brincaremos mais tarde. Encerrando a brincadeira...")
        break

    if len(num1.replace(" ", "")) + len(num2.replace(" ", "")) == int(num3):
        print("ok, está certo!")
    else:
        print("errado, conte novamente!")

    continuar = input("Deseja jogar novamente? (sair para encerrar): ")
    if continuar.lower() == "sair":
        print("Ok, brincaremos mais tarde. Encerrando a brincadeira...")
        break