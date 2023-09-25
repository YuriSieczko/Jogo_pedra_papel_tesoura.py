from xmlrpc.client import ServerProxy

# Conecta ao servidor
server = ServerProxy('http://localhost:3000/')

# Função para jogar o jogo
def play_game():
    print("Escolha entre Pedra, Papel ou Tesoura:")
    choice = input("> ")

    # Chama a função no servidor
    result = server.play(choice)

    print(result)

    # Recebe e exibe a escolha do servidor tentativa falha 
    server_choice = server.get_server_choice()
    print(f"Escolha do servidor: {server_choice}")

# Chama a função de jogo
play_game()
