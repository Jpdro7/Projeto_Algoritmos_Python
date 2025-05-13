elif opcao == '3':
                for r in reservas:
                    print('-' * 50)
                    for chave, valor in r.items():
                        print(f"{chave.capitalize()}: {valor}")
                    remover_verify = True
                    print('-' * 50)

                if not reserva_verify:    
                    print('\nReserva não encontrada.')
