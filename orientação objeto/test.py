def criaConta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta
conta = criaConta(123, 'Nico', 55.0, 1000.0 )
print(conta['numero'])
