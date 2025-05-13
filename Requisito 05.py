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