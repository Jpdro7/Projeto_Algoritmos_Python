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