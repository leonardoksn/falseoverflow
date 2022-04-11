from collections import deque
from inspect import stack
from turtle import st

from sqlalchemy import true

d = deque()

status = 0

# Insere um novo elemento na fila de dados.


def NovoElemento(status: int,tam):
    if status < tam:

        d.append(int(input("Digite um elemento para a fila:  ")))
        print("Elemento incluido com sucesso!")
        print(status)
    else:
        print('Fila cheia irmão')
    return status


# Apaga um elemento na fila de dados.


def ApagaElemento():
    x = d.popleft()
    print(f"Elemento {x} excluido com sucesso!")

# Consulta se um elemento está na fila.


def ConsultaElemento(a: int):
    try:
        x = d.index(a)
        print(f"Elemento {a} encontrado na posiçâo: {x}")
    except:
        print(f"Elemento {a} não encontrado")

def TamanhoFila():
    value = int(input('Tamanho da fila: '))
    return value

status = 0
while True:
    Opcao = 0
    print(" 0 - SAIR\n 1 - Novo \n 2 - Exibe os elemento da fila \n 3 - Remove elemento da fila\n 4 - Encontra elemento na fila\n 5 - Determinar tamanho da fila\n")
    Opcao = (input("Escolha uma Opção:  "))

    if Opcao == "0":
        break
    elif Opcao == "1":
        NovoElemento(status,tam)
        #Aqui é feito o encremento porém como pode ver na opção 3 não temos uma lógica de decremento na variavel de controle "status", causando assim um overflow
        status += 1
    elif Opcao == "2":
        print(d)
        print()
    elif Opcao == "3":
        if len(d) == 0:
            print("Underflow.... Fila Vazia\n")
        else:
            ApagaElemento()
            print()
            print(d)
            print()
    elif Opcao == "4":
        procura = int(
            input("Informe o elemento que deseja verificar se está na fila:  "))
        ConsultaElemento(procura)
    elif Opcao == "5":
        tam = TamanhoFila()
    else:
        print("Esta não é uma opção válida")
        print()
