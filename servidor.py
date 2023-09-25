#importações necessarias pra criar e rodar o server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random

#classe inicial
class RPCGame:
    #contrutor
    def __init__(self):
        #apenas salva a escolha do servidor, quando o jogo rodar sera preenchido com a escolha do servidor
        self.server_choice = None


    def play(self, choice):
        options = ['Pedra', 'Papel', 'Tesoura']
        #servidor escolhe sua jogada
        self.server_choice = random.choice(options)
        #verifica quem ganhou o jogo
        if choice == self.server_choice:
            return f'Empate! Ambos escolheram {choice}'
        elif (choice == 'Pedra' and self.server_choice == 'Tesoura') or \
             (choice == 'Papel' and self.server_choice == 'Pedra') or \
             (choice == 'Tesoura' and self.server_choice == 'Papel'):
            return f'Você ganhou! {choice} vence {self.server_choice}'
        else:
            return f'Você perdeu! {self.server_choice} vence {choice}'

    def get_server_choice(self):
        return self.server_choice


# Configuração do servidor
server = SimpleXMLRPCServer(
    #cria o server e diz qual porta ele roda
    ('localhost', 3000), requestHandler=SimpleXMLRPCRequestHandler)
#instancia o server agora pode ser chamado pelo usuario
server.register_instance(RPCGame())

print("Servidor iniciado na porta 3000...") 
server.serve_forever() #mantem o server rodando sempre
