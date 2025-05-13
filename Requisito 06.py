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