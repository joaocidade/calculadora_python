def menu():
    while True:
        print('1 - somar')
        print("2 - subtrair")
        print("3 - multiplicar")        
        print("4 - dividir")
        break
def retorna():
    return(menu())
def soma():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado1 = n1 + n2
    print(resultado1)

def subtrair():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado2 = n1 - n2
    print(resultado2)   

def divisao():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado2 = n1 / n2
    print(resultado2)  
    
def multiplicar():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado2 = n1 * n2
    print(resultado2)
    
menu()
escolha = input('Escolha uma opção (1/2/3/4): ')
        
if escolha == '1':
    soma()
    retorna()
elif escolha == '2':
    subtrair()
elif escolha == '3':
    multiplicar()
elif escolha == '4':
    divisao()
else:
    print('Opção inválida')


