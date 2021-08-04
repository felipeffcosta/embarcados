'''
Nome e N°USP:
Felipe Ferreira Costa: 10308885

Aplicação servidora que conecta com o cliente na placa e troca mensagens
'''

import socket

IP_Host = '127.0.0.1'  # IP onde será hosteado o server
Port = 1025  # Porta que o cliente ira conectar

socket_comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criando o socket

socket_comm.bind((IP_Host, Port)) #Socket a disposição

print('Esperando conexão do Client...')
socket_comm.listen() #Socket aguardando conexão
socket_conectado, addr = socket_comm.accept()

if socket_conectado: #Só entra se socket_comm não é nulo
    print('Conectado por: ', addr)
    while True:
        
        #Recebe o dado do usuario e envia ao cliente
        SendData = input("Escreva a mensagem para o Cliente: ")
        socket_conectado.sendall(SendData.encode()) #Enconde para transformar string em byte
        print('Mensagem enviada, aguarde a resposta do cliente \n')

        #Recebe o dado do cliente e printa na tela do usuario
        data = socket_conectado.recv(1024).decode('UTF-8') #decode decodifica a mensagem em bytes e transforma em string
        print('Recebido do cliente [' + data + ']')

        #Caso nao receba NULL do cliente ele desliga
        if not data:
            print ('Conexao desligada pelo cliente')
            break
else:
    print('Conexão falhou')
