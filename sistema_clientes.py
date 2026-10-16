# PROJETO 1 — SISTEMA DE CADASTRO DE CLIENTES

# LISTA PRINCIPAL DE CLIENTES


# Cria uma lista vazia.
# É dentro dessa lista que vamos guardar os clientes.
clientes = list()



# ------------------------------------------------------------
# VARIÁVEL DA OPÇÃO DO MENU
# ------------------------------------------------------------

# Criamos a variável opcao e colocamos 0 inicialmente.

# Por que 0?
# Porque ainda não escolhemos nenhuma opção do menu.
# Depois ela receberá o número digitado pelo usuário.

opcao = 0


# ============================================================
# FUNÇÃO: EXIBIR MENU
# ============================================================

# "def" serve para criar uma função.
#
# O nome da função será exibir_menu.
# Tudo que estiver indentado abaixo da função
# pertence a ela.

def exibir_menu():

    # Mostra uma linha na tela.
    print("======================")

    # Mostra o título do sistema.
    print("SISTEMA DE CLIENTES")

    # Mostra outra linha.
    print("======================\n")

    # Mostra as opções disponíveis.
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Pesquisar cliente")
    print("4 - Excluir cliente")
    print("5 - Quantidade de cliente")
    print("6 - Alterar cliente")
    print("7 - Sair\n")


# ============================================================
# FUNÇÃO: VERIFICAR CLIENTE
# ============================================================

# Essa função recebe duas informações:

# clientes → a lista de clientes
# nome     → o nome que queremos procurar
#
# Exemplo:
#
# verificar_cliente(clientes, "Matheus")

def verificar_cliente(clientes, nome):

    # Percorre todos os clientes da lista.
    
    # A cada repetição, a variável "cliente"
    # representa um cliente diferente.
    for cliente in clientes:

        # .lower() transforma o texto em letras minúsculas.
        
        # Assim:
        
        # "Matheus" == "matheus"
        
        # será considerado verdadeiro.

        if cliente.lower() == nome.lower():

            # return True significa:
            # "Sim, encontrei o cliente."
            
            # Quando o Python encontra return,
            # ele encerra imediatamente a função.
            return True



    # Se o for terminar sem encontrar o cliente,
    # chegamos aqui.
    #
    # False significa:
    # "Não encontrei."
    return False


# ============================================================
# FUNÇÃO: VERIFICAR SE EXISTE ALGUM CLIENTE
# ============================================================

# Recebe a lista de clientes.
def cliente_cadastrado(clientes):

    # Uma lista vazia é considerada False.
    #
    # Uma lista com algum elemento é considerada True.
    #
    # Portanto:
    #
    # []                  → False
    # ["Matheus"]         → True
    #
    if clientes:

        # Se existe pelo menos um cliente,
        # retorna True.
        return True

    # Se a lista estiver vazia,
    # retorna False.
    return False


# ============================================================
# FUNÇÃO: BUSCAR NOME
# ============================================================

# Recebe:

# clientes → lista
# nome     → nome que queremos procurar
def buscar_nome(clientes, nome):

    # Percorre todos os clientes.
    for cliente in clientes:

        # Compara o cliente atual com o nome pesquisado.
        
        # lower() deixa a comparação independente
        # de letras maiúsculas/minúsculas.
        if cliente.lower() == nome.lower():

            # Se encontrou, devolve o próprio cliente.
            #
            # Exemplo:
            #
            # cliente = "Matheus"
            #
            # return cliente
            #
            # significa que a função vai devolver "Matheus".
            return cliente

    # Se terminar o for sem encontrar,
    # retorna None.
    
    # None significa que não encontramos nenhum valor.
    return None


# ============================================================
# FUNÇÃO: CADASTRAR CLIENTE
# ============================================================

# Recebe a lista de clientes.
def cadastrar_cliente(clientes):

    # Mostra qual operação estamos realizando.
    print("\n1 - Cadastrar cliente")

    # Pede o nome do cliente.
    #
    # .strip() remove espaços extras no começo e no final.
    #
    # Exemplo:
    #
    # "   Matheus   "
    #
    # vira:
    #
    # "Matheus"
    #variavel cliente vazio para fazer a validação do loop
    cliente = ""
    nome_encontrado = buscar_nome(clientes, cliente)
    #enquanto a variavel cliente for vazio ele entra no while e informa erro nome vazio e volta a pedir nome do cliente
    while cliente == "" or nome_encontrado is not None:
        cliente = input("Digite o nome do cliente: ").strip()
        
        
        nome_encontrado = buscar_nome(clientes, cliente)
        

        #se nome for vazio informa erro
        if cliente == "" or nome_encontrado is not None:
            print("Erro: Nome vazio ou já cadastrado.")
            

    else:

        # Se não encontrou, adiciona o cliente na lista.
        clientes.append(cliente)

        # Mostra mensagem de sucesso.
        print(f"\nCliente {cliente} cadastrado com sucesso.\n")

    


# ============================================================
# FUNÇÃO: LISTAR CLIENTES
# ============================================================

# Recebe a lista de clientes.
def listar_clientes(clientes):

    # Mostra o título da operação.

    print("\n2 - Lista de clientes cadastrados.")

    #saida informando cliente cadastrado
    print("Clientes cadastrados: ")
    # Verifica se existe pelo menos um cliente.
    if cliente_cadastrado(clientes):
    
        # Percorre todos os clientes.
        for cliente in clientes:

            # Mostra cada cliente.
            print(cliente)

    else:

        # Se a lista estiver vazia,
        # mostra esta mensagem.
        print("Não há cliente na cadastrado.\n")



# ============================================================
# FUNÇÃO: PESQUISAR CLIENTE
# ============================================================

# Recebe a lista de clientes.
def pesquisar_cliente(clientes):

    # Mostra o título da operação.
    print("\n3 - Pesquisa de nome.")

    # Pede o nome que será pesquisado.
    #
    # strip() remove espaços extras.
    cliente = input("Digite o nome do cliente desejado para pesquisar: ").strip()

    # Procura o nome na lista.
    nome_encontrado = buscar_nome(clientes, cliente)

    # Se encontrou:
    if nome_encontrado:

        # Mostra o cliente encontrado.
        print(f"Cliente {nome_encontrado} encontrado.\n")

    # Se não encontrou:
    else:

        # Mostra que não existe.
        print(f"Cliente {cliente} não está na lista.\n")


# ============================================================
# FUNÇÃO: REMOVER CLIENTE
# ============================================================

# Recebe a lista de clientes.
def remover_cliente(clientes):

    # Mostra o título da operação.
    print("\n4 - Remover cliente.")

    # Pede o nome que será removido.
    # strip() remove espaços extras.
    cliente = input("Digite o nome do cliente para remover: ").strip()

    # Primeiro procuramos o cliente.
    nome_encontrado = buscar_nome(clientes, cliente)

    # Se encontramos:
    if nome_encontrado:

        # remove() retira o cliente da lista.
        clientes.remove(nome_encontrado)

        # Mostra mensagem de sucesso.
        print(f"Cliente {nome_encontrado} removido com sucesso.\n")

    # Se não encontramos:
    else:

        # Mostra mensagem informando que não existe.
        print(f"Cliente {cliente} não encontrado.\n")


# ============================================================
# FUNÇÃO: CONTAR CLIENTES
# ============================================================

# Essa função deveria mostrar a quantidade de clientes.
def contar_clientes(clientes):

    # len(clientes) retorna a quantidade de elementos
    # existentes na lista.
    quantidade = len(clientes)

    # Mostra a quantidade.
    print(f"Quantidade de clientes cadastrados: {quantidade}")


#===================================================
# FUNÇÃO: ALTERAR CLIENTE
#===================================================

def alterar_cliente(clientes):
    print("6 - Alterar cliente")


    cliente = ""
    #enquanto cliente for vazio o loop continua voltando com erro nome vazio e pedindo o cliente que deseja alterar
    while cliente == "":
        
        
        # Solicitando cliente que será alterado.
        cliente = input("Qual cliente deseja alterar: ").strip()
        if cliente == "":
            print("Erro: Nome vazio")
    #procurar cliente
    cliente_alterar = buscar_nome(clientes, cliente)

    # se cliente tiver na busca
    if cliente_alterar:
        print(f"Cliente {cliente_alterar} encontrado.")
        # cadastrar novo cliente
        novo_cliente = ""
        while novo_cliente == "":
            novo_cliente = input("Digite o nome do novo cliente: ").strip()
            if novo_cliente == "":
                print("Erro: Nome Vazio")

        novo_nome_encontrado = buscar_nome(clientes, novo_cliente)
    
        if novo_nome_encontrado and novo_cliente != cliente_alterar:
            print(f"Cliente {novo_nome_encontrado} já cadastrado.")

        else:
            #pecorrendo na lista clientes os indices e nome cadastrados
            for indice, nome in enumerate(clientes):
            
            #se condição nome for igual ao novo cliente informa que novo cliente já possui cadastro
                if nome == cliente_alterar:
                    clientes[indice] = novo_cliente
                    print(f"Cliente alterado de {cliente_alterar} para {novo_cliente} com sucesso.")
                    break
                    
               
            
     
    else:
        
        #saida de que o cliente não está na lista
        print(f"Cliente {cliente} não está cadastrado.")
        opcao = input("Deseja cadastrar um novo cliente? S/N ").lower().strip()
        if opcao == 's':
            print("Estamos te enviando para cadastrar um novo cliente.")
            return cadastrar_cliente(clientes)
        


# ============================================================
# LOOP PRINCIPAL DO PROGRAMA
# ============================================================

# Enquanto a opção for diferente de 5,
# o programa continuará funcionando.
#
# No começo:
#
# opcao = 0
#
# 0 != 5 → True
#
# Portanto o while começa.
while opcao != 7:

    # Chama a função que mostra o menu.
    exibir_menu()

    # --------------------------------------------------------
    # TENTAR RECEBER A OPÇÃO DO USUÁRIO
    # --------------------------------------------------------

    # try significa:
    # "Tente executar este código."
    try:

        # input() recebe um texto.
        #
        # int() transforma esse texto em número inteiro.
        #
        # Exemplo:
        #
        # "1" → 1
        #
        opcao = int(input("Digite a opção: "))

    # Se o usuário digitar algo que não pode virar inteiro,
    # acontece um ValueError.
    #
    # Exemplo:
    #
    # Digite a opção: abc
    #
    # "abc" não pode virar int.
    except ValueError:

        # Mostra uma mensagem de erro.
        print("Digite apenas números.")

        # continue faz o while voltar para o começo.
        #
        # Portanto:
        #
        # mostra o menu novamente
        # e pede a opção novamente.
        continue


    # ========================================================
    # OPÇÃO 1 — CADASTRAR
    # ========================================================

    # Verifica se o usuário digitou 1.
    if opcao == 1:

        # Chama a função cadastrar_cliente.
        #
        # Passamos a lista "clientes" para a função.
        cadastrar_cliente(clientes)


    # ========================================================
    # OPÇÃO 2 — LISTAR
    # ========================================================

    # Se não foi 1, verifica se foi 2.
    elif opcao == 2:

        # Chama a função de listar.
        listar_clientes(clientes)


    # ========================================================
    # OPÇÃO 3 — PESQUISAR
    # ========================================================

    # Se não foi 1 nem 2, verifica se foi 3.
    elif opcao == 3:

        # Chama a função de pesquisa.
        pesquisar_cliente(clientes)


    # ========================================================
    # OPÇÃO 4 — EXCLUIR
    # ========================================================

    # Verifica se a opção escolhida foi 4.
    elif opcao == 4:

        # Chama a função de remover.
        remover_cliente(clientes)


    # ========================================================
    # OPÇÃO 5 — CONTAR CLIENTE
    # ========================================================

    elif opcao == 5:

        # chama a função para saber quantidade de clientes está cadastrados.
        contar_clientes(clientes)

    elif opcao == 6:

        #chamar a função alterar cliente
        alterar_cliente(clientes)

    # ========================================================
    # OPÇÃO 7 — SAIR
    # ========================================================

    # Verifica se a opção foi 7.
    elif opcao == 7:

        # Mostra mensagem de encerramento.
        print("\nObrigado por usar nosso sistema.\n")

        # break encerra imediatamente o while.
        break


    # ========================================================
    # QUALQUER OUTRO NÚMERO
    # ========================================================

    # Se o usuário digitou algo como:
    #
    # 
    # 7
    # 10
    #
    # nenhuma das condições anteriores será verdadeira.
    #
    # Então chegamos ao else.
    else:

        # Mostra que a opção não existe.
        print("\nOpcao inválida. Tente novamente.\n")
