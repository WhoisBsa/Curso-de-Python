"""
Faca um minisistema que utilize o IH do python. O usuario vai digitar 
o comando e o manual vai aparecer. Quando o usuario digitar a palavra 
'FIM', o programa se encerrara.
obs: use cores
"""

def interactiveHelp():
	print('\033[33;7m')
	print('~' * 27)
	print(f'  SISTEMA DE AJUDA PYHELP')
	print('~' * 27, '\033[m')
	while True:
		hlp = str(input('\033[32;1;6mFuncao ou Biblioteca >>> \033[m')).lower()
		if hlp in 'fim':
			print('\033[31;5m <<< Fim do Programa >>> \033[m')
			break
		print('\033[36;7;3m')
		print('~' * (36 + len(hlp)))
		print(f"  Acessando o manual do comando '{hlp}'")
		print('~' * (36 + len(hlp)), '\033[m')
		print('\033[7m')
		help(hlp)
		print('\033[m')
	
interactiveHelp()
	