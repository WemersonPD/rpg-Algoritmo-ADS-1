#Importações de modulos
from sistema_de_cores.cores import vermelho, verde, amarelo, azul, inverte
from limpa_tela import limpa
from sleep import espere
from sistema_de_cores.animação_inicio import animação
from instrucoes import instrucoes
limpa()
#Inicio do jogo
animação()
instrucoes()


def jogo():
	
	def inicio():
		print(amarelo('INICIAR NOVO JOGO?'))
		print(amarelo('1 - SIM, 2 - NÃO: '))

		request = input(verde('Resposta: '))
		while not(request == '1' or request == '2'):
			print(vermelho('OPÇÃO INVÁLIDA!!!'))
			print(amarelo('1 - SIM, 2 - NÃO: '))
			request = input(verde('Resposta: '))
		espere(0.5)
		
		if request == '1':
			limpa()
			print(vermelho('=' * 80))
			print(vermelho("                                 VAMOS JOGAR!!!"))
			print(vermelho('=' * 80))

			locais = {
				'a1' : {'nome' : 'corredor1' , 'baixo' : 'b1' , 'direita' : 'a2'}, 
				'a2' : {'nome' : 'corredor2' , 'esquerda' : 'a1' , 'direita' : 'a3'} , 
				'a3' : {'nome' : 'quarto' , 'esquerda' : 'a2' , 'item' : 'escudo'} , 
				'a4' : {'nome' : 'corredor3' , 'baixo' : 'b4' , 'direita' : 'a5'} , 
				'a5' : {'nome' : 'saída' , 'esquerda' : 'a4'} , 
				'b1' : {'nome' : 'corredor4' , 'cima' : 'a1' , 'baixo' : 'c1'} , 
				'b4' : {'nome' :'corredor5' , 'esquerda' : 'c2' , 'cima' : 'a4'} , 
				'b5' : {'nome' : 'quarto' , 'baixo' : 'c5' , 'inimigo' : 'monstro' , 'item' : 'poção'} , 
				'c1' : {'nome' : 'corredor6' , 'cima' : 'b1' , 'baixo' : 'd1' , 'direita' : 'c2' , 'inimigo' : 'monstro superior'} , 
				'c2' : {'nome' : 'salão principal' , 'esquerda' : 'c1' , 'direita' : 'b4' , 'inimigo' : 'O CHEFÃO' , 'item' : 'chave'} , 
				'c4' : {'nome' : 'corredor7' , 'baixo' : 'd4' , 'direita' : 'c5'} , 
				'c5' : {'nome' : 'corredor8' , 'cima' : 'b5' , 'esquerda' : 'c4' , 'baixo' : 'd5'} , 
				'd1' : {'nome' : 'corredor9' , 'cima' : 'c1' , 'baixo' : 'e1' , 'direita' : 'd2'} , 
				'd2' : {'nome' : 'corredor10' , 'direita' : 'd3' , 'esquerda' : 'd1' , 'baixo' : 'e2'} , 
				'd3' : {'nome' : 'corredor11' , 'esquerda' : 'd2' , 'direita' : 'd4' , 'baixo' : 'e3'} , 
				'd4' : {'nome' : 'corredor12' , 'esquerda' : 'd3' , 'cima' : 'c4'} , 
				'd5' : {'nome' : 'corredor13' , 'cima' : 'c5' , 'baixo' : 'e5'} , 
				'e1' : {'nome' : 'quarto' , 'cima' : 'd1' , 'inimigo' : 'monstro'} , 
				'e2' : {'nome' : 'corredor14' , 'cima' : 'd2' , 'baixo' : 'f2'} , 
				'e3' : {'nome' : 'corredor15' , 'cima' : 'd3' , 'baixo' : 'f3' , 'direita' : 'e4'} , 
				'e4' : {'nome' : 'corredor16' , 'esquerda' : 'e3' , 'baixo' : 'f4'} , 
				'e5' : {'nome' : 'depósito' , 'cima' : 'd5' , 'item' : 'guarda'} , 
				'f1' : {'nome' : 'escritório' , 'direita' : 'f2'} , 
				'f2' : {'nome' : 'corredor17' , 'esquerda' : 'f1' , 'cima' : 'e2', 'direita': 'f3'} , 
				'f3' : {'nome' : 'corredor18' , 'esquerda' : 'f2' , 'cima' : 'e3', 'direita': 'f4'} , 
				'f4' : {'nome' : 'corredor19' , 'cima' : 'e4' , 'direita' : 'f5'} , 
				'f5' : {'nome' : 'quarto' , 'esquerda' : 'f4' , 'item' : 'lâmina'}}


			posicao_atual = locais['f1']
			inventario = set()
			#limpa()
			while True:
					print()
					print(amarelo('Você está no(a)'), posicao_atual['nome'])
					print(amarelo('inventario ='), inventario)
					print()
					comando = input(verde('> ')).split(' ')
					
					if comando[0] == 'ir':
							direcao = comando[1]
							
							
							if direcao in posicao_atual.keys():
									proximo_local = posicao_atual[direcao]
									posicao_atual = locais[proximo_local]
									limpa()
							else:
									limpa()
									print(vermelho('VOCÊ NÃO PODE IR POR ESTE CAMINHO!'))
									
					
					elif comando[0] == 'pegar':
							item = comando[1]
							
							if item in posicao_atual.values():
									item_atual = posicao_atual['item']
									inventario.add(item_atual)
									limpa()
							
							else:
									limpa()
									print(vermelho('NESTE LOCAL NÃO EXISTE UM ITEM COM ESTE NOME!'))
									

					else:
							limpa()
							print(vermelho('COMANDO INVÁLIDO!'))


			
		
	inicio()
jogo()















