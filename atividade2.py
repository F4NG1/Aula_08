def valor_total(p1,q2):
    t=(p1*q2)
    # print(f'Total: {t}')
    return t


for v in range(3):
    ven=float(input('Preço: '))
    quan=float(input('Quantidade: '))
    total=valor_total(ven,quan)
    print(f'Total: {total}')
        