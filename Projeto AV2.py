import matplotlib.pyplot as plt
import time
import os

email_senha_verify = False
log_verify = False
caronas_verify = False
carona = []
cadastro = []
condicao_data = 0
usuario_log = ''
filtrar_verify = False
email_existente_verify = False
reserva_verify = False
reserva_verify2 = False
remover_verify = False
verify1 = False
reservas = []
quantidade = 0

print('='* 50)
print('Bem - Vindo'.center(50))
print('='*50)

while True:
    print(
        '\n[1] Cadastro' \
        '\n[2] Login')
    opcao = input('\nOpção: ')

    if opcao == '1':
        usuario = input('\nNome de usuario: ')

        email1 = input('\nEmail: ')
        email2 = input('Confirmar Email: ')

        while email2 != email1:
            print("\nEmail's diferente !")
            print("Verifique os email's e tente novamente.")
            email1 = input('\nEmail: ')
            email2 = input('Confirmar Email: ')
 
        while len(email1) < 1 or "@gmail.com" not in email1:
            print('\nEmail invalido.')
            print('Digite o email com nome de dominio do gmail.')
            email1 = input('\nEmail: ')
            email2 = input('Confirmar Email: ')

        for c in cadastro:
            while c["email"] == email1:
                print('\nEsse email já esta cadastrado, cadastre outro.')
                email1 = input('\nEmail: ')
                email2 = input('Confirmar Email: ')
        
        print('\nCadastre sua senha, ela deve conter sete ou mais caracteres !')
        senha1 = input('Senha: ')
        senha2 = input('Confirmar Senha: ')

        while senha2 != senha1 or len(senha1) < 7:
            print('\nAs senhas não conferem ou tem menos de sete caracteres !')
            print('Verifique as senhas e tente novamente.')
            senha1 = input('\nSenha: ')
            senha2 = input('Confirmar Senha: ')

        print('\nEmail e Senha cadastrados com sucesso.')
        print('Cadastro concluido !')

        cadastro2 = {
            "usuario": usuario,
            "email": email2,
            "senha": senha2
        }
        cadastro.append(cadastro2)
        
        print('...')
        time.sleep(1.50)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='* 50)
        print('Bem - Vindo'.center(50))
        print('='*50)
        continue
    
    elif opcao == '2':
        login_email = input('\nEmail: ')
        login_senha = input('Senha: ')
        for c in cadastro:
            if login_email == c["email"] and login_senha == c["senha"]: 
                print('...')
                time.sleep(1.50) 
                os.system('cls' if os.name == 'nt' else 'clear')  
                print('='* 50)
                print(f'Bem Vindo {c["usuario"]}'.center(50))
                print('='* 50)
                usuario_log = c["usuario"]
                log_verify = True 
                email_senha_verify = True

        if not email_senha_verify:
            print('\nDados não encontrados !')
            continue

        while True:
            print(
            '\n[1] Cadastrar Carona' \
            '\n[2] Listar Caronas Disponiveis' \
            '\n[3] Listar Caronas Reservadas' \
            '\n[4] Procurar Caronas' \
            '\n[5] Reservar Carona' \
            '\n[6] Cancelar Reserva' \
            '\n[7] Remover Carona' \
            '\n[8] Detalhes Da Carona' \
            '\n[9] Caronas Cadastradas Pelo Usuario' \
            '\n[10] Vizualizar Grafico De Reservas' \
            '\n[0] Logout')
            opcao = input('\nOpção: ')

            if opcao == '1':
                local_origem = input('\nOrigem: ').title()
                destino = input('Destino: ').title()
                data_carona = input('Data: ')

                dia = int(data_carona[0:2])
                mes = int(data_carona[3:5])
                ano = int(data_carona[6:10])

                if mes in [1, 3, 5, 7, 8, 10, 12]:
                    condicao_data = 31

                elif mes in [4, 6, 9, 11]:
                    condicao_data = 30

                elif mes == 2:
                    condicao_data = 28

                if dia > condicao_data or mes > 12 or ano < 2025 or ano > 2025:
                    while True:
                        print('\nData invalida !')
                        data_carona = input('\nDigite novamente: ')

                        dia = int(data_carona[0:2])
                        mes = int(data_carona[3:5])
                        ano = int(data_carona[6:10])

                        if dia <= condicao_data and mes <= 12 and ano == 2025:
                            break
                        if dia > condicao_data and mes > 12 and ano < 2025 and ano > 2025:
                            continue

                horario = input('Hora: ') 

                while len(horario) > 5 or horario[2] != ':':
                    print('\nHora invalida !')
                    horario = input('\nDigite novamente: ')

                vagas = int(input('Vaga(s) disponivel: '))
                valor = input('Valor por vaga: ')

                carona2 = {
                    "usuario": usuario_log,
                    "origem": local_origem,
                    "destino": destino,
                    "data": data_carona,
                    "hora": horario,
                    "vagas": vagas,
                    "valor": valor
                    }
                carona.append(carona2)
                print('\nCarona cadastrada com sucesso.')
                print('...')

                time.sleep(1.50)
                os.system('cls' if os.name == 'nt' else 'clear')  
                print('='* 50)
                print(f'Bem Vindo {c["usuario"]}'.center(50))
                print('='* 50)

            elif opcao == '2':
                os.system('cls' if os.name == 'nt' else 'clear')  
                print('='* 50)
                print(f'Bem Vindo {c["usuario"]}'.center(50))
                print('='* 50)
                
                contador = 1
                for c in carona:
                    print('-' * 50)
                    print(f'\nCarona nº {contador}\n')
                    for chave, valor in c.items():
                        print(f"{chave.capitalize()}: {valor}")
                    caronas_verify = True
                    contador += 1
                    print('-' * 50)
                    
                if not caronas_verify:
                    print('\nRegistro de carona não encontrado.')

            elif opcao == '4':
                filtrar_origem = input('\nOrigem: ').title()
                filtrar_destino = input('Destino: ').title()
                os.system('cls' if os.name == 'nt' else 'clear')  
                print('='* 50)
                print(f'Bem Vindo {c["usuario"]}'.center(50))
                print('='* 50)
                print()
                for c in carona:
                    if 'origem' in c and 'destino' in c:
                        if filtrar_origem in c['origem'] and filtrar_destino in c['destino']:
                            print('-' * 50)
                            for chave, valor in c.items():
                                print(f"{chave.capitalize()}: {valor}")
                            filtrar_verify = True
                            print('-' * 50)

                if not filtrar_verify:
                    print('\nNenhuma carona encontrada.')
                
            elif opcao == '5':
                reserva1 = input('\nEmail: ')
                reserva2 = input('Data: ')
                reserva_verify = False
                for c in cadastro:
                    if reserva1 in c["email"]:
                        for c in carona:
                            if reserva2 in c["data"]:
                                if c["vagas"] > 0:
                                    reserva_verify = True
                                    print('\nVaga disponivel.')
                                    reserva3 = input('Reservar ? ').lower()
                                    if reserva3 == 's':
                                        quantidade = int(input('Quantas Vagas ? '))
                                        if quantidade > c["vagas"]:
                                            print('\nQuantidade de vagas não disponiveis.')
                                        else:
                                            c["vagas"] -= quantidade
                                            
                                            reserva = {
                                                "usuario": usuario_log,
                                                "origem": local_origem,
                                                "destino": destino,
                                                "data": data_carona,
                                                "hora": horario,
                                                "vagas_reservadas": quantidade,
                                                "valor": valor
                                                }
                                            reservas.append(reserva)
                                            reserva_verify = True

                                            print('\nVaga reservada.')
                                            print('...')

                                            time.sleep(1.50)
                                            os.system('cls' if os.name == 'nt' else 'clear')  
                                            print('='* 50)
                                            print(f'Bem Vindo {c["usuario"]}'.center(50))
                                            print('='* 50)
                                        break
                                
                if not reserva_verify:
                    print('\nCarona não encontrada.')
                
            elif opcao == '3':
                for r in reservas:
                    print('-' * 50)
                    for chave, valor in r.items():
                        print(f"{chave.capitalize()}: {valor}")
                    remover_verify = True
                    print('-' * 50)

                if not reserva_verify:    
                    print('\nReserva não encontrada.')

            elif opcao == '6':
                reserva_cancelamento2 = input('Data: ')
                for c in carona:
                    if reserva_cancelamento2 in c["data"]:
                        for r in reservas:
                            if r["data"] == c["data"]:
                                reserva_verify2 = True
                                print('\nReserva encontrada.')
                                cancelar = input('Cancelar ? ')
                                if cancelar == 's':
                                    c["vagas"] += r["vagas_reservadas"]
                                    print('\nReversa cancelada.')
                                    r["vagas"] = 0
                                    reservas.remove(r)

                                    print('...')
                                    time.sleep(1.50)
                                    os.system('cls' if os.name == 'nt' else 'clear')  
                                    print('='* 50)
                                    print(f'Bem Vindo {c["usuario"]}'.center(50))
                                    print('='* 50)
                                    
                if not reserva_verify2:
                    print('\nReserva não encontrada.')

            elif opcao == '7':
                remover_carona = input('\nData: ')
                for c in carona:
                    if remover_carona in c["data"]:
                        remover_verify = True
                        carona.remove(carona2)
                        print('\nCarona removida.')
                        print('...')

                        time.sleep(1.50)
                        os.system('cls' if os.name == 'nt' else 'clear')  
                        print('='* 50)
                        print(f'Bem Vindo {c["usuario"]}'.center(50))
                        print('='* 50)
                        break

                if not remover_verify:
                    print('\nCarona não encontrada.')
                 
            if(opcao == '8'):
                email_motorista = input('\nEmail: ')
                data_carona2 = input('Data: ')
                print()
                for c in cadastro:
                    if(email_motorista in c["email"]):
                        for c2 in carona:
                            if(data_carona2 in c2["data"]):
                                verify1 = True
                                carona_cadastrada = []
                                carona_cadastrada2 = {
                                    "origem": local_origem,
                                    "destino": destino,
                                    "hora": horario,
                                    "vagas_restantes":carona2["vagas"],
                                    "passageiros": quantidade,
                                    "valor": valor
                                    }
                                verify1 = True
                                carona_cadastrada.append(carona_cadastrada2)

                                for i in carona_cadastrada:
                                    for chave, vetor in i.items():
                                        print(chave, vetor)
                                break
                                              
                if(not verify1):
                    print('Informações não encontradas.')

            if(opcao == '9'):
                print()
                for c in carona:
                    if(c["usuario"] == usuario_log):
                        minhas_caronas_verify = True
                        
                        carona_cadastrada = []
                        carona_cadastrada2 = {
                            "origem": local_origem,
                            "destino": destino,
                            "hora": horario,
                            "vagas_restantes":carona2["vagas"],
                            "passageiros": quantidade,
                            "valor": valor
                            }
                        carona_cadastrada.append(carona_cadastrada2)

                        for i in carona_cadastrada:
                            for chave, vetor in i.items():
                                print(chave, vetor)
                        break

                if(not minhas_caronas_verify):
                    print('Carona não encontrada.')

            elif opcao == '10':
                if len(reservas) == 0:
                    print("\nNenhum passageiro encontrado !")
                else:
                    print('\nInforme as datas inicial e final para filtrar.')
                    filtrar_periodo1 = input('Data inicial: ')
                    filtrar_periodo2 = input('Data final: ')

                    verificacao1 = filtrar_periodo1[0:2] + filtrar_periodo1[2:4] + filtrar_periodo1[4:8]
                    verificacao2 = filtrar_periodo2[0:2] + filtrar_periodo2[2:4] + filtrar_periodo2[4:8]

                    nome = []
                    passageiros = []
                    
                    for r in reservas:
                        data_reservada = r["data"]

                        reorganizar = data_reservada[4:8] + data_reservada[2:4] + data_reservada[0:2]

                        if verificacao1 <= data_reservada <= verificacao2:
                            nome.append(r["usuario"])
                            passageiros.append(r["vagas_reservadas"])

                    if len(nome) == 0:
                        print('Reserva não encontrada.')
                    else:
                        plt.bar(nome, passageiros, color='blue')
                        plt.xlabel('Usuário(s)')
                        plt.ylabel('Número De Vagas Reservadas')
                        plt.title('Gráfico De Caronas Reservadas')
                        plt.yticks(range(0, max(passageiros) + 1))
                        plt.xticks(rotation=40)
                        plt.tight_layout()
                        plt.show()
                continue

            elif opcao == '0':
                print('\nLogout...')
                email_senha_verify = False
                log_verify = False
                usuario_log = ''
                break
