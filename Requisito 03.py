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