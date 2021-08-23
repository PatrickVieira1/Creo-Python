import creopyson


c = creopyson.Client()
c.connect()
c.creo_cd("C:\\Users\\patrick.vieira\\Documents\\Creo\\TKZ")
	

file = "asm0001.asm"
cb = "ef379609p001.prt"


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
Bmod = 1550
Hmod = 1240
Lmod1 = 2170
Lmod2 = 1240


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
		Fib = lista2[l].get('Desenho')
	else:
		pass
for l in range(19):
	if lista2[l].get('L') == Hmod:
		Fih = lista2[l].get('Desenho')
	else:
		pass
for l in range(19):
	if lista2[l].get('L') == Lmod1:
		Fil1 = lista2[l].get('Desenho')
	else:
		pass


Fech_inter_100 = {'Desenho': 'EF380838P001.prt', 'L': 100}
Fech_inter_310 = {'Desenho': 'EF380838P002.prt', 'L': 310}
Fech_inter_620 = {'Desenho': 'EF380838P003.prt', 'L': 620}
Fech_inter_930 = {'Desenho': 'EF380838P004.prt', 'L': 930}
Fech_inter_1240 = {'Desenho': 'EF380838P005.prt', 'L': 1240}
Fech_inter_1550 = {'Desenho': 'EF380838P006.prt', 'L': 1550}
Fech_inter_1860 = {'Desenho': 'EF380838P007.prt', 'L': 1860}
Fech_inter_2170 = {'Desenho': 'EF380838P008.prt', 'L': 2170}
Fech_inter_2480 = {'Desenho': 'EF380838P009.prt', 'L': 2480}
Fech_inter_2790 = {'Desenho': 'EF380838P010.prt', 'L': 2790}
Fech_inter_3100 = {'Desenho': 'EF380838P011.prt', 'L': 3100}
Fech_inter_3410 = {'Desenho': 'EF380838P012.prt', 'L': 3410}
Fech_inter_3720 = {'Desenho': 'EF380838P013.prt', 'L': 3720}
Fech_inter_4030 = {'Desenho': 'EF380838P014.prt', 'L': 4030}
Fech_inter_4340 = {'Desenho': 'EF380838P015.prt', 'L': 4340}
Fech_inter_4650 = {'Desenho': 'EF380838P016.prt', 'L': 4650}
Fech_inter_4960 = {'Desenho': 'EF380838P017.prt', 'L': 4960}
Fech_inter_5270 = {'Desenho': 'EF380838P018.prt', 'L': 5270}
Fech_inter_5580 = {'Desenho': 'EF380838P019.prt', 'L': 5580}
Fech_inter_5890 = {'Desenho': 'EF380838P020.prt', 'L': 5890}

lista3 = [Fech_inter_100,Fech_inter_310,Fech_inter_620,Fech_inter_930,Fech_inter_1240,Fech_inter_1550,Fech_inter_1860,Fech_inter_2170,Fech_inter_2480,Fech_inter_2790,Fech_inter_3100,Fech_inter_3410,Fech_inter_3720,Fech_inter_4030,Fech_inter_4340,Fech_inter_4650,Fech_inter_4960,Fech_inter_5270,Fech_inter_5580,Fech_inter_5890]

for q in range(20):
	if lista3[q].get('L') == Hmod:
		Fech_canto_H = lista3[q].get('Desenho')
	else:
		pass
for q in range(20):
	if lista3[q].get('L') == Bmod:
		Fech_canto_B = lista3[q].get('Desenho')
	else:
		pass
for q in range(20):
	if lista3[q].get('L') == Lmod1:
		Fech_canto_L1 = lista3[q].get('Desenho')
	else:
		pass

cte_cubo = 23.921

if Bmod == 620:
	P2 = lista[0].get('desenho')
	P1 = lista[7].get('desenho')
	Div = 620
	Div2 = 310
elif Bmod == 930:
	P3 = lista[1].get('desenho')
	P2 = lista[8].get('desenho')
	P1 = lista[14].get('desenho')
	Div = 930
	Div2 = 620
elif Bmod == 1240:
	P3 = lista[2].get('desenho')
	P2 = lista[9].get('desenho')
	P1 = lista[15].get('desenho')
	Div = 930
	Div2 = 620
	n1 = 2 #nº de paineis de 620 em H
	n2 = 0 #nº de paineis de 310 em H
elif Bmod == 1550:
	P3 = lista[3].get('desenho')
	P2 = lista[10].get('desenho')
	P1 = lista[16].get('desenho')
	Div = 930
	Div2 = 620
	n1 = 2
	n2 = 1
elif Bmod == 1860:
	P3 = lista[4].get('desenho')
	P2 = lista[11].get('desenho')
	P1 = lista[17].get('desenho')
	Div = 930
	Div2 = 620
	n1 = 3 #nº de paineis de 620 em H
	n2 = 0 #nº de paineis de 310 em H
elif Bmod == 2170:
	P2 = lista[5].get('desenho')
	P1 = lista[12].get('desenho')
	Div = 620
	Div2 = 310
	n1 = 3 
	n2 = 1
elif Bmod == 2480:
	P2 = lista[6].get('desenho')
	P1 = lista[13].get('desenho')
	Div = 620
	Div2 = 310
	n1 = 4 
	n2 = 0
else:
	print("Dimensão em B não suportada")
	pass

Manutencao = 'esquerda'

Pos_z = Bmod/2
xmanut = 90
xmanut_fech = 0
Pos_z_fech = Bmod/2+45

if Manutencao == 'direita':
	Pos_z = -Pos_z
	xmanut = -90
	xmanut_fech = 180
	Pos_z_fech = -Bmod/2-45
else:
	pass


if Lmod1 == 930 and Div == 930:
	
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 1
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 930 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div-Div2/2, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 1
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div-Div2/2, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 1240 and Div == 930:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div-Div2/2, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P3, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 2
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div-Div2/2, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P3, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div2/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 1240 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 2
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

elif Lmod1 == 1550 and Div == 930: #Quando Painel 930+620
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div-Div2/4, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 2
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div-Div2/4, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 1550 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	
	Trans3 = {'origin': {'x': 2*Div-Div2/2, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 2
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
		 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup3 = {'origin': {'x': 2*Div-Div2/2, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+Div+Div2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 1860 and Div == 930:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 3
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div+Div/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 1860 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans3 = {'origin': {'x': 2*Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 3
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup3 = {'origin': {'x': 2*Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+2*Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 2170 and Div == 930:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans3 = {'origin': {'x': Div/2+Div+Div2/4, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P3, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 3
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_sup3 = {'origin': {'x': Div/2+Div+Div2/4, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P3, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+Div+Div2/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 2170 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans3 = {'origin': {'x': 2*Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans4 = {'origin': {'x': 2*Div+Div/2+Div2/2, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf3 = {'origin': {'x': Div/2+2*Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 3
	m2 = 1
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup3 = {'origin': {'x': 2*Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_sup4 = {'origin': {'x': 2*Div+Div/2+Div2/2, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+2*Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup4 = {'origin': {'x': Div/2+2*Div+Div2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 2480 and Div == 930:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans3 = {'origin': {'x': Div/2+Div+Div2/2, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	m1 = 4
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_sup3 = {'origin': {'x': Div/2+Div+Div2/2, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+Div+Div2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
elif Lmod1 == 2480 and Div == 620:
	Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans2 = {'origin': {'x': Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans3 = {'origin': {'x': 2*Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans4 = {'origin': {'x': 3*Div, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf = {'origin': {'x': Div/2, 'z': -	Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf2 = {'origin': {'x': Div/2+Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_inf3 = {'origin': {'x': Div/2+2*Div, 'z': -Bmod/2, 'y': -45}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_inf3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	m1 = 4
	m2 = 0
	Trans_sup1 = {'origin': {'x': 0, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup2 = {'origin': {'x': Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	Trans_sup3 = {'origin': {'x': 2*Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_sup4 = {'origin': {'x': 3*Div, 'z': 0, 'y': Hmod}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
	c.file_assemble(P1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_sup4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup = {'origin': {'x': Div/2, 'z': 	Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup2 = {'origin': {'x': Div/2+Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup3 = {'origin': {'x': Div/2+2*Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_sup4 = {'origin': {'x': Div/2+3*Div, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
	c.file_assemble(Fib, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_sup4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
else:
	print('nao deu')

i1 = 1
iesp = i1
i2 = 1
ip = 2

if Hmod >= 1240 and Bmod >= 1240:
	for j in range(18):
		if lista[j].get('x') == 620 and lista[j].get('y') == Hmod:
			Ph1 = lista[j].get('desenho')
			Ph1n = 620
		else:
			pass
	for k in range(18):
		if lista[k].get('x') == 310 and lista[k].get('y') == Hmod:
			Ph2 = lista[k].get('desenho')
			Ph2n = 310
		else:
			pass
	while n1>=i1:
		Transh1 = {'origin': {'x': -Div/2, 'z': Bmod/2-(310*iesp), 'y': Hmod/2}, 'y_rot': -90,'z_rot':180,'x_rot': 90 }

		c.file_assemble(Ph1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transh1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
		if n1-1 >= i1:
			Trans_fech_h1 = {'origin': {'x': -Div/2-45, 'z': Bmod/2-(310*ip), 'y': 0}, 'y_rot': -90,'z_rot':0,'x_rot': 0 }

			c.file_assemble(Fih, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_h1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
		else:
			pass

		i1 = i1 + 1
		if i1 == 2:
			iesp = 3
			ip = 4
		elif i1 == 3:
			iesp = 5
			ip = 6
		elif i1 == 4:
			iesp = 7
			ip = 8
		else:
			iesp = i1
	if 	n2 != 0:
		Transh2 = {'origin': {'x': -Div/2, 'z': -Bmod/2+155, 'y': Hmod/2}, 'y_rot': -90,'z_rot':180,'x_rot': 90 }

		c.file_assemble(Ph2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transh2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
		Trans_fech_h2 = {'origin': {'x': -Div/2-45, 'z': -Bmod/2+310, 'y': 0}, 'y_rot': -90,'z_rot':0,'x_rot': 0 }

		c.file_assemble(Fih, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_h2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	else:
		pass	
else:
	for i in range(18):
		m = lista[i].get('x')
		n = lista[i].get('y')
		if m == Hmod and n == Bmod:
			Ph = lista[i].get('desenho')
			xroth = 0
			yroth = 0
			zroth = -90
		elif  m == Bmod and n == Hmod:
			Ph = lista[i].get('desenho')
			xroth = 90
			yroth = -90
			zroth = 180
		else:
			pass
	Transh1 = {'origin': {'x': -Div/2, 'z': 0, 'y': Hmod/2}, 'y_rot': yroth,'z_rot':zroth,'x_rot': xroth }
 
	c.file_assemble(Ph, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transh1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


#Posicionar os paineis do lado oposto da manutenção
o1 = 1
o2 = 1
oesp = 0
if Div == 930:
	P0 = -155
	p0 = +155
else:
	P0 = 0
	p0 = Div/2

for o in range(18):
	if lista[o].get('x') == 620 and lista[o].get('y') == Hmod:
		Pl1 = lista[o].get('desenho')
		Pl1n = 620
	else:
		pass
for p in range(18):
	if lista[p].get('x') == 310 and lista[p].get('y') == Hmod:
		Pl2 = lista[p].get('desenho')
		Pl2n = 310
	else:
		pass
while m1>=o1:
	Transl1 = {'origin': {'x': P0+oesp*620, 'z': Pos_z, 'y': Hmod/2}, 'y_rot': 0,'z_rot':0,'x_rot': xmanut }

	c.file_assemble(Pl1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transl1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_lat = {'origin': {'x': p0+oesp*620, 'z': Pos_z_fech, 'y': 0}, 'y_rot': xmanut_fech,'z_rot':0,'x_rot': 0 }

	c.file_assemble(Fih, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_lat, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	o1 = o1 + 1
	if o1 == 2:
		oesp = 1
		
	elif o1 == 3:
		oesp = 2
		
	elif o1 == 4:
		oesp = 3
		
	else:
		oesp = o1
if 	m2 != 0:
	Transl2 = {'origin': {'x': Lmod1-Div+Div2/2, 'z': Pos_z, 'y': Hmod/2}, 'y_rot': 0,'z_rot':0,'x_rot': xmanut }

	c.file_assemble(Pl2, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transl2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
	Trans_fech_lat = {'origin': {'x': Lmod1-Div/2, 'z': Pos_z_fech, 'y': 0}, 'y_rot': xmanut_fech,'z_rot':0,'x_rot': 0 }

	c.file_assemble(Fih, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_lat, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
else:
	pass	

Trans_fech_cantoH1 = {'origin': {'x': -45-Div/2, 'z': Bmod/2+45, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
	 
c.file_assemble(Fech_canto_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoH1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoH2 = {'origin': {'x': -45-Div/2, 'z': -Bmod/2-45, 'y': 0}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
	 
c.file_assemble(Fech_canto_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoH2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoB1 = {'origin': {'x': -45-Div/2, 'z': Bmod/2, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
	 
c.file_assemble(Fech_canto_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoB1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoB2 = {'origin': {'x': -45-Div/2, 'z': Bmod/2, 'y': -45}, 'y_rot': 90,'z_rot': -90,'x_rot': 180 }
	 
c.file_assemble(Fech_canto_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoB2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoL11 = {'origin': {'x': -Div/2, 'z': Bmod/2+45, 'y': Hmod+45}, 'y_rot': 0,'z_rot': 90,'x_rot': 0 }
	 
c.file_assemble(Fech_canto_L1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoL11, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoL12 = {'origin': {'x': -Div/2, 'z': Bmod/2+45, 'y': -45}, 'y_rot': 90,'z_rot': 0,'x_rot': 90 }
	 
c.file_assemble(Fech_canto_L1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoL12, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoL21 = {'origin': {'x': -Div/2, 'z': -Bmod/2-45, 'y': Hmod+45}, 'y_rot': 90,'z_rot': 180,'x_rot': 90 }
	 
c.file_assemble(Fech_canto_L1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoL21, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fech_cantoL22 = {'origin': {'x': -Div/2, 'z': -Bmod/2-45, 'y': -45}, 'y_rot': 90,'z_rot': -90,'x_rot': 90 }
	 
c.file_assemble(Fech_canto_L1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fech_cantoL22, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_cubo1 = {'origin': {'x': -Div/2+cte_cubo, 'z': Bmod/2-cte_cubo, 'y': Hmod-cte_cubo}, 'y_rot': 0,'z_rot': 45,'x_rot': 0 }
 
c.file_assemble(cb, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_cubo1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
Trans_cubo2 = {'origin': {'x': -Div/2+cte_cubo, 'z': -Bmod/2+cte_cubo, 'y': Hmod-cte_cubo}, 'y_rot': -90,'z_rot': 45,'x_rot': 0 }
 
c.file_assemble(cb, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_cubo2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
Trans_cubo3 = {'origin': {'x': -Div/2+cte_cubo, 'z': -Bmod/2+cte_cubo, 'y': cte_cubo}, 'y_rot': -45,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(cb, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_cubo3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
Trans_cubo4 = {'origin': {'x': -Div/2+cte_cubo, 'z': Bmod/2-cte_cubo, 'y': cte_cubo}, 'y_rot': 45,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(cb, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_cubo4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


fechinho1 = Fech_inter_100.get('Desenho')

Trans_fechinho1 = {'origin': {'x': -Div/2+Lmod1+50, 'z': Bmod/2+45, 'y': -45}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(fechinho1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fechinho1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fechinho2 = {'origin': {'x': -Div/2+Lmod1-50, 'z': -Bmod/2-45, 'y': -45}, 'y_rot': 0,'z_rot': -90,'x_rot': 180 }
 
c.file_assemble(fechinho1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fechinho2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fechinho3 = {'origin': {'x': -Div/2+Lmod1+50, 'z': -Bmod/2-45, 'y': Hmod+45}, 'y_rot': 90,'z_rot': 90,'x_rot': -90 }
 
c.file_assemble(fechinho1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fechinho3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_fechinho4 = {'origin': {'x': -Div/2+Lmod1+50, 'z': Bmod/2+45, 'y': Hmod+45}, 'y_rot': 90,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(fechinho1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_fechinho4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)




#____________________________________________________________________
#--------------------------------$%$$-------------------------------|
# Finalizar o primeiro módulo com paineis em B,H,L até Bmod = 2480!!|
#--------------------------------$%$$-------------------------------|






#Regenerar e enquadrar
c.file_regenerate(file)
c.file_refresh(file)