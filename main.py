##############
##Funcao menu#
##############

def interface_Menu():
    print('''1-)Adicionar um novo usuario
    2-)Excluir usuario
    3-)Logar
    4-)Desconectar
    
    ''')

def interface_conta():
    print('''1-)Seguidores
    2-)Seguindo
    3-)Seguir um novo usuario
    4-)Deixar de seguir um usuario
    5-)Deslogar
    ''')

listaUsers = []
matriz = []
index = -1
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.index = index + 1

def adicionar():
    nome = input("Digite o nome do usuario: ")
    user = Usuario(nome)
    listaUsers.append(user)
    matriz.append([user][0])


adicionar()

def seguir_usuario(matriz):
    nome = input("Digite o nome do usuario que deseja seguir: ")

    for i in len(listaUsers):
      if listaUsers[i] == nome :
        index = listaUsers[i].

    for i in len(matriz):
        for j in len(matriz):
            if matriz[i][j] 


# Criando uma matriz 3x3 inicialmente preenchida com zeros
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Acessando e modificando elementos da matriz
matriz[0][0] = 1
matriz[1][1] = 2
matriz[2][2] = 3

# Imprimindo a matriz
for linha in matriz:
    print(linha)


    matriz[lista1]





lista = []
indice = -1

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.indice = indice + 1

def novo():
    nome = input("Digite o nome do usuario: ")
    user = Usuario(nome)

    lista.append(user)
    matriz = [[ 0 * j * i for j in range(len(lista))] for i in range(len(lista))]
    print(matriz)


##########################################################################

novo()
novo()

Login = input("Digite o usuario que deseja se logar: ")
for i in lista:
    if i.nome == Login:
        atual = i.indice

nome = input("Digite o nome do usuario que deseja seguir: ")

for i in lista:
    if i.nome == nome:
        Seguir = i.indice

matriz[atual][Seguir] = 1

print




# nome = input("Digite o nome do usuario que deseja seguir: ")

# for i in range(len(lista)):
#     if lista[i].nome == nome :
#         print(lista[i].nome)


