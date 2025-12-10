alunos=[]

for a in range(2):
    print(f'\n----- Aluno{a+1} -----')
    nome=input('informe o nome do Aluno: ')

    notas=[]
    for n in range(2):
        nota=float(input(f'Informe a nota{n+1}: '))
        notas.append(nota)
    media=sum(notas)/len(notas)
    aluno={
        'Nome':nome,
        'Notas':notas,
        'Média':media
    }    
    alunos.append(aluno)

for estudante in alunos:
    print(f'Nome: {estudante["Nome"]}')
    print(f'Notas: {estudante["Notas"]}')
    print(f'Média: {estudante["Média"]}')
    print('------------------')


    