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

lista = []
indice = 0

class Usuario:
    def __init__(self, nome):
        self.nome = nome

def novo():
    nome = input("Digite o nome do usuario: ")
    user = Usuario(nome)

    lista.append(user)
    matriz = [[ 0 * j * i for j in range(len(lista))] for i in range(len(lista))]
    print(matriz)
    return matriz


##########################################################################

matriz = novo()
matriz = novo()
matriz = novo()



x = 0
Login = input("Digite o usuario que deseja se logar: ")
for i in lista:
    if i.nome == Login:
       atual = x
    x += 1

x = 0
nome = input("Digite o nome do usuario que deseja seguir: ")
for i in lista:
    if i.nome == nome:
        Seguir = x
    x += 1
        

matriz[atual][Seguir] = 1

for linha in matriz:
    print(linha)
