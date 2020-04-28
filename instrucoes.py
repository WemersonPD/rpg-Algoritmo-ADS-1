from sistema_de_cores.cores import vermelho, verde, amarelo, azul, inverte
from limpa_tela import limpa
from sleep import espere


def instrucoes():
	print()
	print(azul('                              COMANDOS DO JOGO:'))
	print(vermelho('                         (ANOTE OS COMANDOS DO JOGO!)'))
	print()
	print(amarelo('                                ir [direcao]'))
	print(amarelo('                                pegar [item]'))
	print()
	input(verde('DIGITE ENTER PARA CONTINUAR!'))
	print()
	espere(0.5)
	print('=' * 80)
	print()
	print(azul('                    LISTA DO QUE VOCÊ PODE FAZER NO JOGO:'))
	print(vermelho('                    (ANOTE OQUE VOCÊ PODE FAZER NO JOGO!)'))
	print()
	print(amarelo('                   DIREÇÕES:'), 'esquerda, direita, cima, baixo')
	print(amarelo('                     ITENS:'), 'escudo, lâmina, guarda, poção')
	print()
	print('=' * 80)
	print()
	input(verde('DIGITE ENTER PARA CONTINUAR!'))
	espere(0.5)
	limpa()