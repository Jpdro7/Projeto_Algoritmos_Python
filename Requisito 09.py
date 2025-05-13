if(opcao == '8'):
                email_motorista = input('\nEmail: ')
                data_carona2 = input('Data: ')
                print()
                for c in cadastro:
                    if(email_motorista in c["email"]):
                        for c2 in carona:
                            if(data_carona2 in c2["data"]):
                                verify1 = True
                                carona_cadastrada = []
                                carona_cadastrada2 = {
                                    "origem": local_origem,
                                    "destino": destino,
                                    "hora": horario,
                                    "vagas_restantes":carona2["vagas"],
                                    "passageiros": quantidade,
                                    "valor": valor
                                    }
                                verify1 = True
                                carona_cadastrada.append(carona_cadastrada2)

                                for i in carona_cadastrada:
                                    for chave, vetor in i.items():
                                        print(chave, vetor)
                                break
                                              
                if(not verify1):
                    print('Informações não encontradas.')
