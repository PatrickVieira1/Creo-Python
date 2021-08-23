import creopyson


c = creopyson.Client()
c.connect()

c.creo_cd("C:\\Users\\patrick.vieira\\Documents\\Creo\\TKZ")

Bmod = 1240
print('Insira a quantidade de módulos')
Numero_modulos_str = input()
Numero_modulos = int(Numero_modulos_str)
lista_Lmodulos = []

for n in range(Numero_modulos):
	print('insira o Tamanho do módulo',n+1)
	lista_Lmodulos.append(int(input()))	

print(lista_Lmodulos)



file = "asm0001.asm"

Painel_310x620= {'desenho':'ef380789C001.asm', 'x':310, 'y':620}
Painel_310x930= {'desenho':'ef380789C002.asm', 'x':310, 'y':930}
Painel_310x1240= {'desenho':'ef380789C003.asm', 'x':310, 'y':1240}
Painel_310x1550= {'desenho':'ef380789C004.asm', 'x':310, 'y':1550}
Painel_310x1860= {'desenho':'ef380789C005.asm', 'x':310, 'y':1860}
Painel_310x2170= {'desenho':'ef380789C006.asm', 'x':310, 'y':2170}
Painel_310x2480= {'desenho':'ef380789C007.asm', 'x':310, 'y':2480}
Painel_620x620= {'desenho':'ef380789C008.asm', 'x':620, 'y':620}
Painel_620x930= {'desenho':'ef380789C009.asm', 'x':620, 'y':930}
Painel_620x1240= {'desenho':'ef380789C010.asm', 'x':620, 'y':1240}
Painel_620x1550= {'desenho':'ef380789C011.asm', 'x':620, 'y':1550}
Painel_620x1860= {'desenho':'ef380789C012.asm', 'x':620, 'y':1860}
Painel_620x2170= {'desenho':'ef380789C013.asm', 'x':620, 'y':2170}
Painel_620x2480= {'desenho':'ef380789C014.asm', 'x':620, 'y':2480}
Painel_930x930= {'desenho':'ef380789C015.asm', 'x':930, 'y':930}
Painel_930x1240= {'desenho':'ef380789C016.asm', 'x':930, 'y':1240}
Painel_930x1550= {'desenho':'ef380789C017.asm', 'x':930, 'y':1550}
Painel_930x1860= {'desenho':'ef380789C018.asm', 'x':930, 'y':1860}

lista = [Painel_310x620,Painel_310x930,Painel_310x1240,Painel_310x1550,Painel_310x1860,Painel_310x2170,Painel_310x2480,Painel_620x620,Painel_620x930,Painel_620x1240,Painel_620x1550,Painel_620x1860,Painel_620x2170,Painel_620x2480,Painel_930x930,Painel_930x1240,Painel_930x1550,Painel_930x1860]


Fech_inter_310 = {'Desenho': 'EF380837P001.prt', 'L': 310}
Fech_inter_620 = {'Desenho': 'EF380837P002.prt', 'L': 620}
Fech_inter_930 = {'Desenho': 'EF380837P003.prt', 'L': 930}
Fech_inter_1240 = {'Desenho': 'EF380837P004.prt', 'L': 1240}
Fech_inter_1550 = {'Desenho': 'EF380837P005.prt', 'L': 1550}
Fech_inter_1860 = {'Desenho': 'EF380837P006.prt', 'L': 1860}
Fech_inter_2170 = {'Desenho': 'EF380837P007.prt', 'L': 2170}
Fech_inter_2480 = {'Desenho': 'EF380837P008.prt', 'L': 2480}
Fech_inter_2790 = {'Desenho': 'EF380837P009.prt', 'L': 2790}
Fech_inter_3100 = {'Desenho': 'EF380837P010.prt', 'L': 3100}
Fech_inter_3410 = {'Desenho': 'EF380837P011.prt', 'L': 3410}
Fech_inter_3720 = {'Desenho': 'EF380837P012.prt', 'L': 3720}
Fech_inter_4030 = {'Desenho': 'EF380837P013.prt', 'L': 4030}
Fech_inter_4340 = {'Desenho': 'EF380837P014.prt', 'L': 4340}
Fech_inter_4650 = {'Desenho': 'EF380837P015.prt', 'L': 4650}
Fech_inter_4960 = {'Desenho': 'EF380837P016.prt', 'L': 4960}
Fech_inter_5270 = {'Desenho': 'EF380837P017.prt', 'L': 5270}
Fech_inter_5580 = {'Desenho': 'EF380837P018.prt', 'L': 5580}
Fech_inter_5890 = {'Desenho': 'EF380837P019.prt', 'L': 5890}

lista2 = [Fech_inter_310,Fech_inter_620,Fech_inter_930,Fech_inter_1240,Fech_inter_1550,Fech_inter_1860,Fech_inter_2170,Fech_inter_2480,Fech_inter_2790,Fech_inter_3100,Fech_inter_3410,Fech_inter_3720,Fech_inter_4030,Fech_inter_4340,Fech_inter_4650,Fech_inter_4960,Fech_inter_5270,Fech_inter_5580,Fech_inter_5890]



for l in range(19):
	if lista2[l].get('L') == Bmod:
		FechamentoIntermediarioB = lista2[l].get('Desenho')
	else:
		pass

# Liberar só quando tiver Hmod		
# for l in range(19):
# 	if lista2[l].get('L') == Hmod:
# 		FechamentoIntermediarioH = lista2[l].get('Desenho')
# 	else:
# 		pass


for k in range(Numero_modulos):
	if int(lista_Lmodulos[k])>=1240 and Bmod>=1240:
		for i in range(18):
			if lista[i].get('x') == 930 and lista[i].get('y') == Bmod:
				print(lista[i].get('desenho'))
				PainelPrincipalInferior = lista[i].get('desenho')
				Numero_paineis = int(lista_Lmodulos[k]) // 930
				Painel_restante = int(lista_Lmodulos[k]) % 930
				print('Encontrou_930')
				Encontrou_930 = True
				Metade_painel = 930/2
				break
			else:
				Encontrou_930 = False
		if Encontrou_930 == True:
			pass
		else:
			for i in range(18):
				#Pq tá gerando apenas paineis de 620??
				if lista[i].get('x') == 620 and lista[i].get('y') == Bmod:
					PainelPrincipalInferior = lista[i].get('desenho')	
					Numero_paineis = int(lista_Lmodulos[k]) // 620
					Painel_restante = int(lista_Lmodulos[k]) % 620
					Metade_painel = 620/2
					print('Encontrou_620')
				else:
					pass
		for n in range(Numero_paineis):
			
			Trans1 = {'origin': {'x': Metade_painel+Metade_painel*2*n+int(sum(lista_Lmodulos[0:k])), 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
			 
			c.file_assemble(PainelPrincipalInferior, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
			if not n == Numero_paineis-1:
				Trans_fech_inf = {'origin': {'x': 2*Metade_painel+Metade_painel*2*n+int(sum(lista_Lmodulos[0:k])), 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
		 
				c.file_assemble(FechamentoIntermediarioB, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
			else:
				pass

		if Painel_restante != 0:
			for i in range(18):
				if lista[i].get('x') == Painel_restante and lista[i].get('y') == Bmod:
					PainelRestanteInferior = lista[i].get('desenho')
				else:
					pass
			
			Trans2 = {'origin': {'x': Numero_paineis*Metade_painel*2+Painel_restante/2+int(sum(lista_Lmodulos[0:k])), 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
			 
			c.file_assemble(PainelRestanteInferior, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

			Trans_fech_inf = {'origin': {'x': Numero_paineis*Metade_painel*2+int(sum(lista_Lmodulos[0:k])), 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
		 
			c.file_assemble(FechamentoIntermediarioB, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
		else:
			pass
	else:
		for i in range(18):
			Posicao1 = lista[i].get('x')
			Posicao2 = lista[i].get('y')
			if Posicao1 == int(lista_Lmodulos[k]) and Posicao2 == Bmod:
				PainelDeitadoB = lista[i].get('desenho')
				RotacaoXpainelB = 0
				RotacaoYpainelB = 0
				RotacaoZpainelB = 180
			elif  Posicao1 == Bmod and Posicao2 == int(lista_Lmodulos[k]):
				PainelDeitadoB = lista[i].get('desenho')
				RotacaoXpainelB = 0
				RotacaoYpainelB = 90
				RotacaoZpainelB = 180
			else:
				pass
		TransBunico = {'origin': {'x': int(lista_Lmodulos[k])/2+int(sum(lista_Lmodulos[0:k])), 'z': 0, 'y': 0}, 'y_rot': RotacaoYpainelB,'z_rot':RotacaoZpainelB,'x_rot': RotacaoXpainelB }
	 
		c.file_assemble(PainelDeitadoB, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=TransBunico, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Especificar restrição para Bmod < 930 e Lmod > 2170