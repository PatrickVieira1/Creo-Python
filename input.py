import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


import creopyson


c = creopyson.Client()
c.connect()

c.creo_cd("C:\\Users\\patrick.vieira\\Documents\\Creo\\TKZ")

file = "asm0001.asm"
Bmod = 1550
Hmod = 1240
Lmod1 = 2170
Lmod2 = 1240

Div = 930

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





Porta_620x620 = {'desenho':'EF380792C001.asm', 'x':620, 'y':620}
Porta_620x930 = {'desenho':'EF380792C002.asm', 'x':620,'y':930}
Porta_620x1240 = {'desenho':'EF380792C003.asm', 'x':620,'y':1240}
Porta_620x1550 = {'desenho':'EF380792C004.asm', 'x':620,'y':1550}
Porta_620x1860 = {'desenho':'EF380792C005.asm', 'x':620,'y':1860}

lista_porta = [Porta_620x620,Porta_620x930,Porta_620x1240,Porta_620x1550,Porta_620x1860]


# come??o da GUI
window = tk.Tk()
window.title("Posicionamento de portas")


frame1 = tk.Frame(borderwidth=3,relief = "raised")
frame1.grid()


#Quantidade de portas

p1 = tk.Label(frame1,text='Quantidade de portas',wraplength=230,justify='center')
p1.grid(column=0,row=0)

#Regra para apenas n??meros

def callback(S):
	
    if S in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
	    p2.bell() # .bell() plays that ding sound telling you there was invalid input
	    return False


p2 = tk.Entry(frame1, width = 5)
p2.grid(column=1,row=0)

reg = window.register(callback)
p2.config(validate="key", validatecommand=(reg,'%S'))
#Valores alternaveis entres os bot??es que ser??o criados

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var1.set(0)
var2.set(0)
var3.set(0)

#Comando do bot??o para aparecer op????es do visor

def janela_visor():
	global frame4
	frame4 = tk.LabelFrame(borderwidth = 3, text="Visor", relief = "raised",width = 40)
	frame4.place(x=150,y=110)
	rv1 = tk.Radiobutton(frame4, text="Com Visor", value = 1, variable=var3)
	rv2 = tk.Radiobutton(frame4, text="Sem Visor", value = 2, variable=var3)
	rv1.grid()
	rv2.grid()

#Op????o das portas

frame2 = tk.LabelFrame(borderwidth = 3, text="Tamanho das portas", relief = "raised")
frame2.place(x=10,y=50)
r1 = tk.Radiobutton(frame2, text=("Porta","-","620","x",str(Hmod)), value = 1, variable=var1, command=janela_visor)
r2 = tk.Radiobutton(frame2, text=("Porta","-","465","x",str(Hmod)), value = 2, variable=var1)
r3 = tk.Radiobutton(frame2, text=("Porta","-","310","x",str(Hmod)), value = 3, variable=var1)
r1.grid()
r2.grid()
r3.grid()

#Op????o das dobradi??as

frame3 = tk.LabelFrame(borderwidth = 3, text="Dobradi??as", relief = "raised", width = 40)
frame3.place(x=150,y=30)
r3 = tk.Radiobutton(frame3, text="Direita", value = 1, justify = "left", variable=var2)
r4 = tk.Radiobutton(frame3, text="Esquerda", value = 2,justify = "left", variable=var2)
r3.grid()
r4.grid()

frame5 = tk.LabelFrame(borderwidth = 3, relief = "raised")
frame5.grid(row=0,column=3)

# Valor de entrada - Posi????o das portas


op????es_posi????es = [0,310, 620, 930, 1240, 1550, 1860, 2170, 2480, 2790, 3100]

var_opt = tk.StringVar()
var_opt.set(op????es_posi????es[0])

lbl = tk.Label(frame5,text='Posi????o da porta', justify = 'center',wraplength=125 )

entry1 = ttk.Combobox(frame5, textvariable=var_opt, values = op????es_posi????es, state='readonly', width = 5)
#entry1['values'] = op????es_posi????es
lbl.grid(column=3,row=0)
entry1.grid(column=4,row=0)

#Bot??o de reset e apaga todos os dados

def reset():
	var1.set(0)
	var2.set(0)
	var3.set(0)
	frame4.destroy()
	Posi????es_passadas.clear()
	Tamanho_portas_passadas.clear()
	


reset_button = tk.Button(text="Reset", command=reset,width = 10)
reset_button.place(x=244, y=50)

#Defini????o de lado conforme a manuten????o

Manutencao = 'esquerda'

Pos_z = Bmod/2
xmanut = 90
xmanut_fech = 0
Pos_z_fech = Bmod/2+45
Rota????o_porta_manut_y = 180

if Manutencao == 'direita':
	Pos_z = -Pos_z
	xmanut = -90
	xmanut_fech = 180
	Pos_z_fech = -Bmod/2-45
	Rota????o_porta_manut_y = 0
else:
	pass

#----------------------------

if Div == 930:
	P0 = -155
else:
	P0 = 0


#Lista para guardar os valores conforme inputs

Posi????es_passadas = []
Tamanho_portas_passadas = []

#fun????o posicionar a porta

def posicionar_porta():

	if int(var1.get()) == 1: 
		p = 620
	elif int(var1.get()) == 2:
		p = 465
	elif int(var1.get()) == 3:
		p = 310

	if int(var2.get()) == 1:
		Dobradi??a = 'direita'
	elif int(var2.get()) == 2:
		Dobradi??a = 'esquerda'
	else:
		pass
	if Manutencao == 'direita':
		if Dobradi??a == 'esquerda':
			y_dob = 135
			x_dob = 0
			adicional_porta = 0
		elif Dobradi??a == 'direita':
			y_dob = 45
			x_dob = 180
			adicional_porta = p
	elif Manutencao == 'esquerda':
		if Dobradi??a == 'esquerda':
			y_dob = 135
			x_dob = 0
			adicional_porta = p
		elif Dobradi??a == 'direita':
			y_dob = 45
			x_dob = 180
			adicional_porta = 0

	for i in range(5):
		mi = lista_porta[i].get('x')
		ni = lista_porta[i].get('y')	
		if mi == p and ni == Hmod:
			Porta_Selecionada = lista_porta[i].get('desenho')
			print(Porta_Selecionada)
		else:
			pass
	# Para esta versao nao tem portas de 310 e 465
	if p == 465 or p == 310:
		tk.messagebox.showinfo("ERROU", "Porta n??o est?? nessa vers??o do software")
	else:
	#Capturou os inputs do usu??rio para as itera????es
		Posi????es_passadas.append(var_opt.get())
		Tamanho_portas_passadas.append(p)
	#Primeira porta
		if len(Posi????es_passadas) == 1:
			Trans1 = {'origin': {'x': -Div/2+adicional_porta+int(var_opt.get()), 'z': -Pos_z, 'y': Hmod/2}, 'y_rot': y_dob+Rota????o_porta_manut_y,'z_rot': 0,'x_rot': x_dob }
	 
			c.file_assemble(Porta_Selecionada, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
			if int(var_opt.get()) != 0:
				for j in range(18):
					if lista[j].get('x') == int(var_opt.get()) and lista[j].get('y') == Hmod:
						PainelAntesPorta1 = lista[j].get('desenho')
						Desloc_painel1 = -Div/2+int(var_opt.get())/2
						Rota????o_Z1 = 0
					else:
						pass
				for k in range(18):
					if lista[k].get('x') == Hmod and lista[k].get('y') == int(var_opt.get()) :
						PainelAntesPorta1 = lista[k].get('desenho')
						Desloc_painel1 = -Div/2+Hmod/2 
						Rota????o_Z1 = 90
					else:
						pass

				Transl1 = {'origin': {'x': Desloc_painel1, 'z': -Pos_z, 'y': Hmod/2}, 'y_rot': 0,'z_rot':0,'x_rot': -xmanut }

				c.file_assemble(PainelAntesPorta1, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Transl1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

	#Restri????es de porta colada na outra e posicionamento da porta fora do m??dulo
		elif (len(Posi????es_passadas) > 1 and int(var_opt.get())==0) or sum(map(int,Posi????es_passadas))+sum(map(int,Tamanho_portas_passadas))>Lmod1:
			tk.messagebox.showinfo("Posi????o", "Imposs??vel posicionar porta nesta posi????o")
			Posi????es_passadas.pop()
			Tamanho_portas_passadas.pop()

	#Posicionamento da segunda porta em diante
		elif len(Posi????es_passadas) > 1 and int(var_opt.get())!=0:
			Trans1 = {'origin': {'x':-Div/2+adicional_porta+int(var_opt.get())+sum(map(int,Posi????es_passadas))+sum(map(int,Tamanho_portas_passadas))-int(Tamanho_portas_passadas[-1])-int(Posi????es_passadas[-1]), 'z': -Pos_z, 'y': Hmod/2}, 'y_rot': y_dob+Rota????o_porta_manut_y,'z_rot': 0,'x_rot': x_dob }
	 
			c.file_assemble(Porta_Selecionada, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


porta_button = tk.Button(bg = "light blue", text="Posicionar porta", command=posicionar_porta,width = 10, height = 2, wraplength = 80)

porta_button.place(x=244, y=120)


window.geometry("350x200")
tk.mainloop()

 