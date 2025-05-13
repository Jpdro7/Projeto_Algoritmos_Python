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