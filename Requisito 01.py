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