import creopyson


c = creopyson.Client()
c.connect()

c.creo_cd("C:\\Users\\patrick.vieira\\Documents\\Creo\\cubo")
#c.start_creo("C:\\Program Files\\PTC\\Creo 6.0.5.1\\Parametric\\bin\\nitro_proe_remote.bat")

# Lista de arquivos no atual working directory
# listfiles = c.creo_list_files()
# print(listfiles)

# Pegar o current working directory
#current_directory = c.creo_pwd()
#print(current_directory)


file = "asm0001.asm"
cubo = "ef317079.prt"
csys = "ASM_DEF_CSYS"
perfil_15_B = "ef416987_b.prt"
perfil_15_H = "ef416987_h.prt"
perfil_15_L = "ef416987_l.prt"
perfil_15_BS = "ef416987_bs.prt"
perfil_15_HS = "ef416987_hs.prt"
perfil_15_LS = "ef416987_ls.prt"
perfil_15_BV = "ef416987_bv.prt"
perfil_15_HV = "ef416987_hv.prt"
perfil_15_LV = "ef416987_lv.prt"





# print(c.file_get_transform(asm=file, path=None, csys=None))
# print(c.file_get_transform(asm=file, path=None, csys=csys))

#{'y_rot': -0.0, 'origin': {'x': 0.0, 'z': 0.0, 'y': 0.0}, 'z_axis': {'x': 0.0, 'z': 1.0, 'y': 0.0}, 'y_axis': {'x': 0.0, 'z': 0.0, 'y': 1.0}, 'x_axis': {'x': 1.0, 'z': 0.0, 'y': 0.0}, 'x_rot': -0.0, 'z_rot': -0.0}

#{'type': 'csys', 'asmref':'ABCD1','compref':'PRT_CSYS_DEF'},

Bmaq = 1190
Hmaq = 790
Lmaq = 490
Lserp = 790


Tcubo = 19

Bpos = Bmaq - Tcubo
Hpos = Hmaq - 2*Tcubo
Lpos = Lmaq	- 2*Tcubo



maq = "ICV"

if maq == "ICH":
	xv = Lserp + Lmaq
	yv = 0
	HVpos = Hpos
	Hvent = Hmaq
	Lvent = 790
elif maq == "ICV":
	xv = Lmaq
	yv = Hmaq
	Lvent = Lserp
	Hvent = 790
	HVpos = Hvent - 2*Tcubo

else:
	print ("Máquina não faz sentido")

LVpos = Lvent - 2*Tcubo

Bperf = Bmaq - 76
Hperf = Hmaq - 76
Lperf = Lmaq - 76
LSperf = Lserp - 76
LVperf = Lvent - 76
HVperf = Hvent - 76


#Dimensionar perfis CM conforme máquina

c.file_open(perfil_15_B, display=True)
c.dimension_set("d50", Bperf, perfil_15_B)
c.file_close_window(perfil_15_B)

c.file_open(perfil_15_H, display=True)
c.dimension_set("d50", Hperf, perfil_15_H)
c.file_close_window(perfil_15_H)

c.file_open(perfil_15_L, display=True)
c.dimension_set("d50", Lperf, perfil_15_L)
c.file_close_window(perfil_15_L)

#Dimensionar perfis SERP conforme máquina

c.file_open(perfil_15_BS, display=True)
c.dimension_set("d50", Bperf, perfil_15_BS)
c.file_close_window(perfil_15_BS)

c.file_open(perfil_15_HS, display=True)
c.dimension_set("d50", Hperf, perfil_15_HS)
c.file_close_window(perfil_15_HS)

c.file_open(perfil_15_LS, display=True)
c.dimension_set("d50", LSperf, perfil_15_LS)
c.file_close_window(perfil_15_LS)

#Dimensionar perfis VENT conforme máquina

c.file_open(perfil_15_BV, display=True)
c.dimension_set("d50", Bperf, perfil_15_BV)
c.file_close_window(perfil_15_BV)

c.file_open(perfil_15_HV, display=True)
c.dimension_set("d50", HVperf, perfil_15_HV)
c.file_close_window(perfil_15_HV)

c.file_open(perfil_15_LV, display=True)
c.dimension_set("d50", LVperf, perfil_15_LV)
c.file_close_window(perfil_15_LV)


#Teste de save as --- ESTUDAR CONTINUAÇÃO DO SAVE AS (COLOCAR NO DIRETÓRIO CORRETO)

# c.file_open(perfil_15_B, display=True)
# c.interface_mapkey("~ Close `main_dlg_cur` `appl_casc`;~ Command `ProCmdModelSaveAs`;", delay=0)
# link = "C:\Users\patrick.vieira\Documents\Creo\cubo\"

c.file_open(file, display=True)

#/////---------////////////////-----------------/////////////
#cubo1
Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo2
Trans2 = {'origin': {'x': 0, 'z': 0, 'y': Hpos}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo3
Trans3 = {'origin': {'x': -Lpos, 'z': 0, 'y': Hpos}, 'y_rot': 0,'z_rot': -180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo4
Trans4 = {'origin': {'x': -Lpos-19, 'z': 19, 'y': 0}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo5
Trans5 = {'origin': {'x': 0, 'z': Bpos, 'y': -19}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans5, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo6
Trans6 = {'origin': {'x': 19, 'z': Bpos, 'y': Hpos}, 'y_rot': 0,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans6, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo7
Trans7 = {'origin': {'x': -Lpos, 'z': Bpos+19, 'y': Hpos}, 'y_rot': -90,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans7, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#cubo8
Trans8 = {'origin': {'x': -Lpos, 'z': Bpos, 'y': -19}, 'y_rot': -90,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans8, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

 
#/////------PRONTO---////////////////--------PRONTO---------/////////////



# perfil B 


PBTrans1 = {'origin': {'x': -9, 'z': 38, 'y': -1}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBTrans2 = {'origin': {'x': -1 - Lpos, 'z': 38, 'y': 9}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBTrans3 = {'origin': {'x': 1, 'z': 38, 'y': -9 + Hpos}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(perfil_15_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBTrans4 = {'origin': {'x': 9 - Lpos, 'z': 38, 'y': 1 + Hpos}, 'y_rot': 0,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_B, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#/////------PRONTO---////////////////--------PRONTO---------/////////////

# perfil L

PLTrans1 = {'origin': {'x': -19, 'z': 18, 'y': 9}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_L, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLTrans2 = {'origin': {'x': -19, 'z': 28, 'y': 1+Hpos}, 'y_rot': -90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_L, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLTrans3 = {'origin': {'x': -19, 'z': -9+Bpos, 'y': -1}, 'y_rot': -90,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_L, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLTrans4 = {'origin': {'x': 19 - Lpos, 'z': -9+Bpos, 'y': 1+Hpos}, 'y_rot': 90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_L, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#/////------PRONTO---////////////////--------PRONTO---------/////////////

#perfil H

PHTrans1 = {'origin': {'x': -9, 'z': 18, 'y': -19+Hpos}, 'y_rot': -90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHTrans2 = {'origin': {'x': -1-Lpos, 'z': 28, 'y': -19+Hpos}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHTrans3 = {'origin': {'x': 1, 'z': -9+Bpos, 'y': -19+Hpos}, 'y_rot': 180,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHTrans4 = {'origin': {'x': 9-Lpos, 'z': 1+Bpos, 'y': -19+Hpos}, 'y_rot': 90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_H, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

# #/////------PRONTO---////////////////--------PRONTO---------/////////////


# # Módulo Serpentina
# Cubo Serp1



Trans_serp1 = {'origin': {'x': -Lmaq, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp2
Trans_serp2 = {'origin': {'x': -Lmaq, 'z': 0, 'y': Hpos}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp3
Trans_serp3 = {'origin': {'x': -Lpos-Lserp, 'z': 0, 'y': Hpos}, 'y_rot': 0,'z_rot': -180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp4
Trans_serp4 = {'origin': {'x': -Lpos-19-Lserp, 'z': 19, 'y': 0}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp5
Trans_serp5 = {'origin': {'x': -Lmaq, 'z': Bpos, 'y': -19}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp5, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp6
Trans_serp6 = {'origin': {'x': 19-Lmaq, 'z': Bpos, 'y': Hpos}, 'y_rot': 0,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp6, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp7
Trans_serp7 = {'origin': {'x': -Lpos-Lserp, 'z': Bpos+19, 'y': Hpos}, 'y_rot': -90,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp7, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo Serp8
Trans_serp8 = {'origin': {'x': -Lpos-Lserp, 'z': Bpos, 'y': -19}, 'y_rot': -90,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_serp8, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#/////------PRONTO---////////////////--------PRONTO---------/////////////


#Módulo serpentina - Perfis

# perfil B 


PBSTrans1 = {'origin': {'x': -9-Lmaq, 'z': 38, 'y': -1}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_BS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBSTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBSTrans2 = {'origin': {'x': -1 - Lpos-Lserp, 'z': 38, 'y': 9}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_BS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBSTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBSTrans3 = {'origin': {'x': 1-Lmaq, 'z': 38, 'y': -9 + Hpos}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(perfil_15_BS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBSTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBSTrans4 = {'origin': {'x': 9 - Lpos-Lserp, 'z': 38, 'y': 1 + Hpos}, 'y_rot': 0,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_BS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBSTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

# #/////------PRONTO---////////////////--------PRONTO---------/////////////

# # perfil L

PLSTrans1 = {'origin': {'x': -19-Lmaq, 'z': 18, 'y': 9}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_LS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLSTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLSTrans2 = {'origin': {'x': -19-Lmaq, 'z': 28, 'y': 1+Hpos}, 'y_rot': -90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLSTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLSTrans3 = {'origin': {'x': -19-Lmaq, 'z': -9+Bpos, 'y': -1}, 'y_rot': -90,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLSTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLSTrans4 = {'origin': {'x': +57-Lmaq-Lserp, 'z': -9+Bpos, 'y': 1+Hpos}, 'y_rot': 90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLSTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



# #perfil H

PHSTrans1 = {'origin': {'x': -9-Lmaq, 'z': 18, 'y': -19+Hpos}, 'y_rot': -90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHSTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHSTrans2 = {'origin': {'x': -1-Lpos-Lserp, 'z': 28, 'y': -19+Hpos}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHSTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHSTrans3 = {'origin': {'x': 1-Lmaq, 'z': -9+Bpos, 'y': -19+Hpos}, 'y_rot': 180,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHSTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHSTrans4 = {'origin': {'x': 9-Lpos-Lserp, 'z': 1+Bpos, 'y': -19+Hpos}, 'y_rot': 90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HS, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHSTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#/////------PRONTO---////////////////--------PRONTO---------/////////////

# Módulo Ventilador
# Cubo vent1

Trans_vent1 = {'origin': {'x': -xv, 'z': 0, 'y': yv}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Cubo vent2
Trans_vent2 = {'origin': {'x': -xv, 'z': 0, 'y': HVpos+yv}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Cubo vent3
Trans_vent3 = {'origin': {'x': -xv-LVpos, 'z': 0, 'y': HVpos+yv}, 'y_rot': 0,'z_rot': -180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Cubo vent4
Trans_vent4 = {'origin': {'x': -19-xv-LVpos, 'z': 19, 'y': yv}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Cubo vent5
Trans_vent5 = {'origin': {'x': -xv, 'z': Bpos, 'y': -19+yv}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent5, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo vent6
Trans_vent6 = {'origin': {'x': 19-xv, 'z': Bpos, 'y': HVpos+yv}, 'y_rot': 0,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent6, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#Cubo vent7
Trans_vent7 = {'origin': {'x': -xv-LVpos, 'z': Bpos+19, 'y': HVpos+yv}, 'y_rot': -90,'z_rot': -90,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent7, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
# #Cubo vent8
Trans_vent8 = {'origin': {'x': -xv-LVpos, 'z': Bpos, 'y': -19+yv}, 'y_rot': -90,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_vent8, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)
#/////------PRONTO---////////////////--------PRONTO---------/////////////

#Módulo serpentina - Perfis

# perfil B 


PBVTrans1 = {'origin': {'x': -9-xv, 'z': 38, 'y': -1+yv}, 'y_rot': 0,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_BV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBVTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBVTrans2 = {'origin': {'x': -1 - xv-LVpos, 'z': 38, 'y': 9+yv}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_BV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBVTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBVTrans3 = {'origin': {'x': 1-xv, 'z': 38, 'y': -9 + HVpos+yv}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(perfil_15_BV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBVTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PBVTrans4 = {'origin': {'x': 9 - xv-LVpos, 'z': 38, 'y': 1 + HVpos+yv}, 'y_rot': 0,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_BV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PBVTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

# # #/////------PRONTO---////////////////--------PRONTO---------/////////////

# perfil L

PLVTrans1 = {'origin': {'x': -19-xv, 'z': 18, 'y': 9+yv}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(perfil_15_LV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLVTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLVTrans2 = {'origin': {'x': -19-xv, 'z': 28, 'y': 1+HVpos+yv}, 'y_rot': -90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLVTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLVTrans3 = {'origin': {'x': -19-xv, 'z': -9+Bpos, 'y': -1+yv}, 'y_rot': -90,'z_rot': -90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLVTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PLVTrans4 = {'origin': {'x': +57-xv-Lvent, 'z': -9+Bpos, 'y': 1+HVpos+yv}, 'y_rot': 90,'z_rot': 90,'x_rot': 0 }
 
c.file_assemble(perfil_15_LV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PLVTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



# #perfil H

PHVTrans1 = {'origin': {'x': -9-xv, 'z': 18, 'y': -19+HVpos+yv}, 'y_rot': -90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHVTrans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHVTrans2 = {'origin': {'x': -1-xv-LVpos, 'z': 28, 'y': -19+HVpos+yv}, 'y_rot': 0,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHVTrans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHVTrans3 = {'origin': {'x': 1-xv, 'z': -9+Bpos, 'y': -19+HVpos+yv}, 'y_rot': 180,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHVTrans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

PHVTrans4 = {'origin': {'x': 9-xv-LVpos, 'z': 1+Bpos, 'y': -19+HVpos+yv}, 'y_rot': 90,'z_rot': 0,'x_rot': 90 }
 
c.file_assemble(perfil_15_HV, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=PHVTrans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



#Modificar o valor da dimensão




#c.dimension_set("d1", 300, file)

#Regenerar e enquadrar
c.file_regenerate(file)
c.file_refresh(file)