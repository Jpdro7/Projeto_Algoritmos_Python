if(opcao == '9'):
                print()
                for c in carona:
                    if(c["usuario"] == usuario_log):
                        minhas_caronas_verify = True
                        
                        carona_cadastrada = []
                        carona_cadastrada2 = {
                            "origem": local_origem,
                            "destino": destino,
                            "hora": horario,
                            "vagas_restantes":carona2["vagas"],
                            "passageiros": quantidade,
                            "valor": valor
                            }
                        carona_cadastrada.append(carona_cadastrada2)

                        for i in carona_cadastrada:
                            for chave, vetor in i.items():
                                print(chave, vetor)
                        break

                if(not minhas_caronas_verify):
                    print('Carona não encontrada.')
