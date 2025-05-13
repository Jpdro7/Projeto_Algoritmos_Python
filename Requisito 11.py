elif opcao == '10':
                if len(reservas) == 0:
                    print("\nNenhum passageiro encontrado !")
                else:
                    print('\nInforme as datas inicial e final para filtrar.')
                    filtrar_periodo1 = input('Data inicial: ')
                    filtrar_periodo2 = input('Data final: ')

                    verificacao1 = filtrar_periodo1[0:2] + filtrar_periodo1[2:4] + filtrar_periodo1[4:8]
                    verificacao2 = filtrar_periodo2[0:2] + filtrar_periodo2[2:4] + filtrar_periodo2[4:8]

                    nome = []
                    passageiros = []
                    
                    for r in reservas:
                        data_reservada = r["data"]

                        reorganizar = data_reservada[4:8] + data_reservada[2:4] + data_reservada[0:2]

                        if verificacao1 <= data_reservada <= verificacao2:
                            nome.append(r["usuario"])
                            passageiros.append(r["vagas_reservadas"])

                    if len(nome) == 0:
                        print('Reserva não encontrada.')
                    else:
                        plt.bar(nome, passageiros, color='blue')
                        plt.xlabel('Usuário(s)')
                        plt.ylabel('Número De Vagas Reservadas')
                        plt.title('Gráfico De Caronas Reservadas')
                        plt.yticks(range(0, max(passageiros) + 1))
                        plt.xticks(rotation=40)
                        plt.tight_layout()
                        plt.show()
                continue