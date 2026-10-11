print('=== PAINEL DA ATOS ===')
mes=input('qual mes estamos analisando?')
alunos_ativos = int(input('quantos alunos ativos temos?'))
mensalidade_media = float(input('qual a mensalidade media? R$'))
#calcula quantidade de alunos x mensalidade media
receita_estimada = alunos_ativos* mensalidade_media
meta_receita=float(input('qual a meta de receita do mes?R$'))
falta_meta=meta_receita-receita_estimada
if falta_meta>0:
              print(f'Faltam R${falta_meta:.2f}, para atingir a meta.')
elif falta_meta==0:
              print('Meta atingida exatamente!')
else:
              excedente=falta_meta*-1
              print(f'Meta superada em R${excedente:.2f}!')
print(f'receita mensal estimada: R${receita_estimada:.2f}')
aluguel= float(input('qual o valor do aluguel?R$'))
outras_despesas=float(input('qual o total das outras_despesas?R$'))
energia=float(input('qual o valor da conta de energia?R$'))
#soma aluguel, energia e outras despesas
despesas=aluguel+energia+outras_despesas
print(f'total de despesas:R${despesas:.2f}')
#calcula saldo entre receita estimada menos despesa
saldo_estimado = receita_estimada - despesas
if receita_estimada>0:
              percentual_despesas=despesas/receita_estimada*100
              print(f'despesas representam{percentual_despesas:.1f}% da receita.')
print(f'saldo mensal estimado: R${saldo_estimado:.2f}')
if saldo_estimado<0:
              print('atencao as despesas superam a receita!')
elif saldo_estimado ==0:
              print('empatou: a receita e igual as despesas.')
else:
              print('o balanco e positivo esse mes.')
print('mes analisado:', mes)
print(f'\n=== RESUMO DE {mes} ===')
print(f'A meta de receita esse mes foi: R${meta_receita:.2f}!')
print('alunos ativos:', alunos_ativos)
print(f'mensalidade media:R${mensalidade_media:.2f}')
print(f'receita estimada:R${receita_estimada:.2f}')
print(f'total de despesas:R${despesas:.2f}')
print(f'saldo estimado:R${saldo_estimado:.2f}')
input('\npressione enter para fechar...')

