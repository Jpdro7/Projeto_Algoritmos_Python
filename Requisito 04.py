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