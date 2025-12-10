vendedores=[]

for n in range(5):
    print(f'Vendedor {n+1}: ')
    nome=input('Informe seu nome: ')

    vendas=[]
    for v in range(5):
        venda=float(input(f'Informa o valor {v+1}: '))
        vendas.append(venda)
        total=sum(vendas)
        media=sum(vendas)/len(vendas)
        
    vendors={
        'Nome':nome,
        'Vendas':vendas,
        'Total':total,
        'Média':media
    }
    vendedores.append(vendors)

for vendors2 in vendedores:
    print('-----------')
    print(f'Nome: {vendors2["Nome"]}')
    print(f'Vendas: {vendors2["Vendas"]}') 
    print(f'Total: {vendors2["Total"]}') 
    print(f'Média: {vendors2["Média"]}')
    print('-----------')       