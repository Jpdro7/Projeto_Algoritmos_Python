elif opcao == '0':
                print('\nLogout...')
                email_senha_verify = False
                log_verify = False
                usuario_log = ''
                time.sleep(1.50)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('='* 50)
                print(f'Bem Vindo'.center(50))
                print('='* 50)
                break
