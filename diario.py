import os, readline
from datetime import datetime, date

comidas = ['arroz integral', 'pipoca', 'farelo de aveia', 'abobrinha', 'acelga', 'aelga', 'ameixa', 'batata doce', 'beterraba', 'biscoito de polvilho', 'bolinho de polvilho', 'bolo de caneca', 'brócolis', 'caqui', 'carambola', 'castanhas', 'cenoura', 'chocolate quente', 'chá de jasmim', 'chá oolong', 'chá preto com chocolate', 'creme de leite', 'chá preto maple', 'chá verde com jasmim', 'chá verde', 'couve-flor', 'manteiga vegana', 'creme de ricota sem lactose', 'croutons', 'doce de leite de amendoim', 'espinafre', 'goiaba', 'grão-de-bico', 'hamburguer de cogumelo', 'hamburguer de soja', 'kiwi', 'laranja', 'leite com cacau', 'lentilha', 'magic toast', 'mamão', 'manga', 'manjericão', 'maçã', 'mingau de farelo de aveia', 'morango', 'nata sem lactose', 'ovo', 'pera', 'picolé de leite e cacau', 'pimentão', 'pão de batata doce', 'pão low carb', 'pão sem glúten', 'quibe de abóbora', 'salada de frutas', 'salada', 'sopa', 'tomate']

def completer(text, state):
	options = [x for x in comidas if x.startswith(text)]
	try:
		return options[state]
	except IndexError:
		return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

refeicoes = ['Café da manhã', 'Lanche da manhã', 'Almoço', 'Lanche da manhã', 'Jantar']
today = date.today()
refeicao = {}
refeicao['data_refeicao'] = today.strftime('%d/%m')
refeicao['hora_refeicao'] = str(datetime.now().time())[:5]
refeicao['item_refeicao'] = []
linhas = []

while True:
	os.system('clear')
	print(f'     DIÁRIO ALIMENTAR - {refeicao["data_refeicao"]} - {refeicao["hora_refeicao"]}')
	print('-'*43)
	diario = open('diario.txt', 'r')
	todasLinhas = diario.read()
	linhas = todasLinhas.split('\n')
	print('Registros mais recentes: ') 
	for j in range(2, 7):
		if len(linhas)-1 >= j-1:
			mostra_linha = eval(linhas[-j])
			lista_alimentos = ''
			for a in mostra_linha["item_refeicao"]:
				lista_alimentos += a + ', '
			mostra_alimentos = lista_alimentos.strip(', ')
			# print(f'{j-1} - {mostra_linha["data_refeicao"]}, {mostra_linha["hora_refeicao"]}, {mostra_alimentos}')
			print(f'{j-1} - {mostra_linha["data_refeicao"]}, {refeicoes[(mostra_linha["tipo_refeicao"])-1]}, {mostra_linha["hora_refeicao"]}, {mostra_alimentos}')
	diario.close()

	print('-'*43)
	print('1 ADICIONAR   2 EDITAR   3 EXCLUIR   4 SAIR')
	print('-'*43)
	opcao = int(input('Digite sua opção: '))

	if opcao == 1:
		print('\n1 Café da manhã, 2 Lanche da manhã, 3 Almoço, 4 Lanche da manhã, 5 Jantar\n')
		refeicao['tipo_refeicao'] = int(input('Digite o tipo de refeição: '))

		while True:
			item_comida = input('Digite o alimento (TAB p/completar, ENTER p/encerrar): ')
			if item_comida == '':
				break
			refeicao['item_refeicao'].append(item_comida)

		while True:
			os.system('clear')
			print(f'\n1: {refeicao["data_refeicao"]}\n2: {refeicoes[refeicao["tipo_refeicao"]-1]}\n3: {refeicao["hora_refeicao"]}')
			for item in range(4,4+len(refeicao['item_refeicao'])):
				print(f'{item}: {refeicao["item_refeicao"][item-4]}')
			confirmacao = input('\nEstá correto? (S/N) ').lower()
			if confirmacao == 's':
				diario = open('diario.txt', 'a')
				diario.write(f'{refeicao}\n')
				diario.close()
				refeicao['item_refeicao'] = []
				break
			elif confirmacao == 'n':
				edicao = int(input('Digite o número da linha para corrigir: '))
				if edicao == 1:
					refeicao['data_refeicao'] = input('Nova data: ')
				elif edicao == 2:
					print('1 Café da manhã, 2 Lanche da manhã, 3 Almoço, 4 Lanche da manhã, 5 Jantar')
					refeicao['tipo_refeicao'] = int(input('Nova refeição (1 a 5): '))
				elif edicao == 3:
					refeicao['hora_refeicao'] = input('Nova hora: ')
				elif edicao > len(refeicao['item_refeicao'])+4:
					print('Número incorreto, tente de novo')
				elif edicao >= 4 and edicao < len(refeicao['item_refeicao'])+4:
					refeicao['item_refeicao'][edicao-4] = input('Novo alimento: ')
	
	elif opcao == 2:
		print()
		editar_registro = int(input('Selecione um número entre os registros mais recentes acima: '))
		mostra_linha = eval(linhas[-(editar_registro+1)])
		lista_alimentos = ''
		for a in mostra_linha["item_refeicao"]:
			lista_alimentos += a + ', '
		mostra_alimentos = lista_alimentos.strip(', ')
		print(f'\n{editar_registro} - {mostra_linha["data_refeicao"]}, {refeicoes[mostra_linha["tipo_refeicao"]-1]}, {mostra_linha["hora_refeicao"]}, {mostra_alimentos}\n')
		while True:
			confirma_edicao = input('Editar este registro? (S/N) ').lower()
			if confirma_edicao == 's':
				itens_edicao = str(linhas[-(editar_registro+1)])
				itens_dic = eval(itens_edicao)
				print(f'\n1: {itens_dic["data_refeicao"]}\n2: {refeicoes[itens_dic["tipo_refeicao"]-1]}\n3: {itens_dic["hora_refeicao"]}')
				num_item = 4
				for item in itens_dic['item_refeicao']:
					print(f'{num_item}: {item}')
					num_item += 1
				edicao = int(input('\nDigite o número da linha para corrigir: '))
				if edicao == 1:
					refeicao['data_refeicao'] = input('Nova data: ')
				elif edicao == 2:
					print('1 Café da manhã, 2 Lanche da manhã, 3 Almoço, 4 Lanche da manhã, 5 Jantar')
					refeicao['tipo_refeicao'] = int(input('Nova refeição (1 a 5): '))
				elif edicao == 3:
					refeicao['hora_refeicao'] = input('Nova hora: ')
				elif edicao > len(itens_edicao)+4:
					print('Número incorreto, tente de novo')
				elif edicao >= 4 and edicao < len(itens_edicao)+4:
					refeicao['item_refeicao'][edicao-4] = input('Novo alimento: ')
				for editado in refeicao['item_refeicao']:
					if editado == '':
						refeicao['item_refeicao'].pop(editado)
				for a in mostra_linha["item_refeicao"]:
					lista_alimentos += a + ', '
				mostra_alimentos = lista_alimentos.strip(', ')
				print(f'\n{editar_registro} - {mostra_linha["data_refeicao"]}, {refeicoes[mostra_linha["tipo_refeicao"]-1]}, {mostra_linha["hora_refeicao"]}, {mostra_alimentos}\n')
				diario = open('diario.txt', 'r')
				linhas = diario.readlines()
				linhas[-(editar_registro+1)] = (f'{refeicao}\n')
				diario = open('diario.txt', 'w')
				diario.writelines(linhas)
				diario.close()
			elif confirma_edicao == 'n':
				break
	elif opcao == 3:
		excluir_registro = int(input('Selecione um número entre os registros mais recentes acima: '))
		# print(f'\n{linhas[-(excluir_registro+1)]}\n')
		mostra_linha = eval(linhas[-(excluir_registro+1)])
		lista_alimentos = ''
		for a in mostra_linha["item_refeicao"]:
			lista_alimentos += a + ', '
		mostra_alimentos = lista_alimentos.strip(', ')
		print(f'\n{excluir_registro} - {mostra_linha["data_refeicao"]}, {refeicoes[mostra_linha["tipo_refeicao"]-1]}, {mostra_linha["hora_refeicao"]}, {mostra_alimentos}\n')
		while True:
			confirma_exclusao = input('Excluir este registro? (S/N) ').lower()
			if confirma_exclusao == 's':
				excluiDiario = open('diario.txt', 'r')
				diarioNovo = open('diarioNovo.txt', 'w')
				linhas = excluiDiario.readlines()
				for linha in range(0, len(linhas)):
					if linha != len(linhas)-(excluir_registro):
						diarioNovo.write(linhas[linha])
				excluiDiario.close()
				diarioNovo.close()
				os.remove('diario.txt')
				os.rename('diarioNovo.txt', 'diario.txt')
				break

	elif opcao == 4:
		print('Fim do programa')
		break
	else:
		print('Opção inválida, digite outra')