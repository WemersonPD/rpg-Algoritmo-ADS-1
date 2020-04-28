
def animação():
	from sistema_de_cores.cores import vermelho, verde, amarelo, azul
	from random import choice
	from limpa_tela import limpa
	from sleep import espere
	cores = [vermelho, azul, amarelo, verde]
	for i in range(10):
		cor = choice(cores)
		print(cor('=' * 80))
		print(cor("                               CORREDORES DO MEDO "))
		print(cor('=' * 80))
		espere(0.2)
		limpa()
	
	print(cor('=' * 80))
	print(cor("                             CORREDORES DO MEDO "))
	print(cor('=' * 80))


