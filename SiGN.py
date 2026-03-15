# Função que calcula a média de uma lista de notas
def media(notas):
    return sum(notas) / len(notas)  # soma todas as notas e divide pela quantidade

# Dicionário que armazena os alunos
# Cada aluno possui uma lista de notas e sua frequência
alunos = {
    "Ana": {"notas": [8, 7, 9], "frequencia": 90},
    "Bruno": {"notas": [5, 6, 4], "frequencia": 75},
    "Carlos": {"notas": [9, 9, 10], "frequencia": 95},
    "Daniela": {"notas": [6, 5, 7], "frequencia": 80}
}

# Texto do menu que será exibido ao usuário
cabecalho = '''Olá, professor! Seja bem vindo ao 'SiGN'. O que você deseja fazer hoje?

1) - Visualizar alunos da turma
2) - Ranking da turma
3) - Frequência
4) - Aprovados
5) - Recuperação
6) - Gerar relatório
7) - Sair
'''

# Loop principal do programa (repete até o usuário escolher sair)
while True:
    try:
        print(cabecalho)  # imprime o menu
        opcao = int(input("Selecione a opção desejada: "))  # usuário escolhe uma opção

        # Opção 1 - Mostrar todos os alunos da turma
        if opcao == 1:
            print("\nAlunos da turma:\n")
            for aluno in alunos:  # percorre todos os alunos do dicionário
                print(aluno)  # imprime o nome do aluno
            print("")
        # Opção 2 - Mostrar o ranking da turma baseado na média das notas
        elif opcao == 2:
            print("\nRanking da turma:\n")

            # sorted organiza os alunos pela média das notas (do maior para o menor)
            ranking = sorted(alunos.items(),
                             key=lambda x: media(x[1]["notas"]),
                             reverse=True)

            # enumerate cria a posição do ranking (1º, 2º, 3º...)
            for pos, (nome, dados) in enumerate(ranking, start=1):
                print(f"{pos}º - {nome} | Média: {media(dados['notas']):.2f}")
            print("")
        # Opção 3 - Mostrar a frequência de cada aluno
        elif opcao == 3:
            print("\nFrequência dos alunos:")

            # percorre todos os alunos e seus dados
            for nome, dados in alunos.items():
                print(f"{nome}: {dados['frequencia']}%")  # mostra a frequência

        # Opção 4 - Mostrar os alunos aprovados
        elif opcao == 4:
            print("\nAlunos aprovados:\n")

            for nome, dados in alunos.items():
                # aluno é aprovado se média >= 7 e frequência >= 75%
                if media(dados["notas"]) >= 7 and dados["frequencia"] >= 75:
                    print(f"{nome} | Média: {media(dados['notas']):.2f}")
            print("")

        # Opção 5 - Mostrar alunos em recuperação
        elif opcao == 5:
            print("\nAlunos em recuperação:\n")

            for nome, dados in alunos.items():
                # aluno entra em recuperação se média < 7
                if media(dados["notas"]) < 7:
                    print(f"{nome} | Média: {media(dados['notas']):.2f}")
            print("")

        # Opção 6 - Gerar relatório geral da turma
        elif opcao == 6:
            print("\nRelatório da turma:\n")

            todas_notas = []  # lista que armazenará todas as notas da turma

            # percorre os dados dos alunos
            for dados in alunos.values():
                todas_notas.extend(dados["notas"])  # adiciona todas as notas na lista

            # calcula estatísticas da turma
            maior = max(todas_notas)  # maior nota
            menor = min(todas_notas)  # menor nota
            media_turma = sum(todas_notas) / len(todas_notas)  # média geral

            # exibe os resultados
            print(f"Média geral da turma: {media_turma:.2f}\n")
            print(f"Maior nota da turma: {maior}\n")
            print(f"Menor nota da turma: {menor}\n")

        # Opção 7 - Encerrar o programa
        elif opcao == 7:
            print("Programa encerrado.")
            break  # encerra o loop

        # Caso o usuário digite um número que não existe no menu
        else:
            print("Informe uma opção válida!")

    # Tratamento de erro caso o usuário digite algo que não seja número
    except ValueError:
        print("\nErro! Digite apenas números.\n")