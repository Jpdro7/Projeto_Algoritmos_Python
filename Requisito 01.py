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
