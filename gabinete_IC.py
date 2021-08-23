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

perfil = 15

if perfil == 15:
	cubo = "ef317079.prt"
	perfil_B = "ef416987_b.prt"
	perfil_H = "ef416987_h.prt"
	perfil_L = "ef416987_l.prt"
	perfil_BS = "ef416987_bs.prt"
	perfil_HS = "ef416987_hs.prt"
	perfil_LS = "ef416987_ls.prt"
	perfil_BV = "ef416987_bv.prt"
	perfil_HV = "ef416987_hv.prt"
	perfil_LV = "ef416987_lv.prt"
	dim = "d50"
	Folgaperf = 76
elif perfil == 25:
	cubo = "cubo_25.prt"
	perfil_B = "perfil_25_B.prt"
	perfil_H = "perfil_25_H.prt"
	perfil_L = "perfil_25_L.prt"
	perfil_BS = "perfil_25_BS.prt"
	perfil_HS = "perfil_25_HS.prt"
	perfil_LS = "perfil_25_LS.prt"
	perfil_BV = "perfil_25_BV.prt"
	perfil_HV = "perfil_25_HV.prt"
	perfil_LV = "perfil_25_LV.prt"
	dim = "d22"
	Folgaperf = 60.5*2
else: 
	print("Espessura de perfil não suportada")



MTG_CM = "MTG_CM.asm"
MTG_SERP = "MTG_SERP.asm"
MTG_VENT = "MTG_VENT.asm"


# print(c.file_get_transform(asm=file, path=None, csys=None))
# print(c.file_get_transform(asm=file, path=None, csys=csys))

#{'y_rot': -0.0, 'origin': {'x': 0.0, 'z': 0.0, 'y': 0.0}, 'z_axis': {'x': 0.0, 'z': 1.0, 'y': 0.0}, 'y_axis': {'x': 0.0, 'z': 0.0, 'y': 1.0}, 'x_axis': {'x': 1.0, 'z': 0.0, 'y': 0.0}, 'x_rot': -0.0, 'z_rot': -0.0}

#{'type': 'csys', 'asmref':'ABCD1','compref':'PRT_CSYS_DEF'},

Bmaq = 2000
Hmaq = 900
Lmaq = 490
Lserp = 790



maq = "ICH"

if maq == "ICH":
	xv = Lserp + Lmaq
	yv = 0
	Hvent = Hmaq
	Lvent = 790
elif maq == "ICV":
	Hvent = 640
	xv = Lmaq
	yv = Hvent
	Lvent = Lserp
	
else:
	print ("Máquina não faz sentido")

Bperf = Bmaq - Folgaperf
Hperf = Hmaq - Folgaperf
Lperf = Lmaq - Folgaperf
LSperf = Lserp - Folgaperf
LVperf = Lvent - Folgaperf
HVperf = Hvent - Folgaperf


#Dimensionar perfis CM conforme máquina

c.file_open(perfil_B, display=True)
c.dimension_set(dim, Bperf, perfil_B)
c.file_close_window(perfil_B)

c.file_open(perfil_H, display=True)
c.dimension_set(dim, Hperf, perfil_H)
c.file_close_window(perfil_H)

c.file_open(perfil_L, display=True)
c.dimension_set(dim, Lperf, perfil_L)
c.file_close_window(perfil_L)

#Dimensionar perfis SERP conforme máquina

c.file_open(perfil_BS, display=True)
c.dimension_set(dim, Bperf, perfil_BS)
c.file_close_window(perfil_BS)

c.file_open(perfil_HS, display=True)
c.dimension_set(dim, Hperf, perfil_HS)
c.file_close_window(perfil_HS)

c.file_open(perfil_LS, display=True)
c.dimension_set(dim, LSperf, perfil_LS)
c.file_close_window(perfil_LS)

#Dimensionar perfis VENT conforme máquina

c.file_open(perfil_BV, display=True)
c.dimension_set(dim, Bperf, perfil_BV)
c.file_close_window(perfil_BV)

c.file_open(perfil_HV, display=True)
c.dimension_set(dim, HVperf, perfil_HV)
c.file_close_window(perfil_HV)

c.file_open(perfil_LV, display=True)
c.dimension_set(dim, LVperf, perfil_LV)
c.file_close_window(perfil_LV)


#MONTAGEM CAIXA DE MISTURA

c.file_open(MTG_CM, display=True)

#/////---------////////////////-----------------/////////////

Trans1 = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans1, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans2 = {'origin': {'x': -Lmaq, 'z': Bmaq, 'y': 0}, 'y_rot': 180,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans2, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans3 = {'origin': {'x': 0, 'z': Bmaq, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 0,'x_rot': -180 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans3, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans4 = {'origin': {'x': -Lmaq, 'z': 0, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans4, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_B, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_B','compref':'CSYS_B'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_L, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_L','compref':'CSYS_L'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_H, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_H','compref':'CSYS_H'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans5 = {'origin': {'x': -Lmaq, 'z': 0, 'y': 0}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans5, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans6 = {'origin': {'x': 0, 'z': Bmaq, 'y': 0}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans6, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans7 = {'origin': {'x': 0, 'z': 0, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans7, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



Trans8 = {'origin': {'x': -Lmaq, 'z': Bmaq, 'y': -Hmaq}, 'y_rot': -180,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_CM, path=None, ref_model=None, transform=Trans8, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


c.file_close_window(MTG_CM)

#-----------------#----------#

#MONTAGEM SERPENTINA

c.file_open(MTG_SERP, display=True)

#/////---------////////////////-----------------/////////////

Trans1S = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans1S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans2S = {'origin': {'x': -Lserp, 'z': Bmaq, 'y': 0}, 'y_rot': 180,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans2S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans3S = {'origin': {'x': 0, 'z': Bmaq, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 0,'x_rot': -180 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans3S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans4S = {'origin': {'x': -Lserp, 'z': 0, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans4S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_BS, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_B','compref':'CSYS_B'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_LS, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_L','compref':'CSYS_L'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_HS, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_H','compref':'CSYS_H'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans5S = {'origin': {'x': -Lserp, 'z': 0, 'y': 0}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans5S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans6S = {'origin': {'x': 0, 'z': Bmaq, 'y': 0}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans6S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans7S = {'origin': {'x': 0, 'z': 0, 'y': -Hmaq}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans7S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



Trans8S = {'origin': {'x': -Lserp, 'z': Bmaq, 'y': -Hmaq}, 'y_rot': -180,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_SERP, path=None, ref_model=None, transform=Trans8S, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


c.file_close_window(MTG_SERP)

#-----------------#----------#

#MONTAGEM VENTILADOR

c.file_open(MTG_VENT, display=True)

#/////---------////////////////-----------------/////////////

Trans1V = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans1V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans2V = {'origin': {'x': -Lvent, 'z': Bmaq, 'y': 0}, 'y_rot': 180,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans2V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans3V = {'origin': {'x': 0, 'z': Bmaq, 'y': -Hvent}, 'y_rot': 0,'z_rot': 0,'x_rot': -180 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans3V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans4V = {'origin': {'x': -Lvent, 'z': 0, 'y': -Hvent}, 'y_rot': 0,'z_rot': 180,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans4V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_BV, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_B','compref':'CSYS_B'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_LV, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_L','compref':'CSYS_L'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

c.file_assemble(perfil_HV, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=cubo, transform=None, constraints={'type': 'csys', 'asmref':'CSYS_H','compref':'CSYS_H'}	, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans5V = {'origin': {'x': -Lvent, 'z': 0, 'y': 0}, 'y_rot': 90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans5V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


Trans6V = {'origin': {'x': 0, 'z': Bmaq, 'y': 0}, 'y_rot': -90,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans6V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans7V = {'origin': {'x': 0, 'z': 0, 'y': -Hvent}, 'y_rot': 0,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans7V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)



Trans8V = {'origin': {'x': -Lvent, 'z': Bmaq, 'y': -Hvent}, 'y_rot': -180,'z_rot': 0,'x_rot': -90 }
 
c.file_assemble(cubo, dirname=None, generic=None, into_asm=MTG_VENT, path=None, ref_model=None, transform=Trans8V, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)


c.file_close_window(MTG_VENT)

c.file_open(file, display=True)

Trans_MTG_CM = {'origin': {'x': 0, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(MTG_CM, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_MTG_CM, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_MTG_SERP = {'origin': {'x': -Lmaq, 'z': 0, 'y': 0}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(MTG_SERP, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_MTG_SERP, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

Trans_MTG_VENT = {'origin': {'x': -xv, 'z': 0, 'y': yv}, 'y_rot': 0,'z_rot': 0,'x_rot': 0 }
 
c.file_assemble(MTG_VENT, dirname=None, generic=None, into_asm=file, path=None, ref_model=None, transform=Trans_MTG_VENT, constraints={'type': 'fix'}, package_assembly=None, walk_children=None, assemble_to_root=None, suppress=None)

#Regenerar e enquadrar
c.file_regenerate(file)
c.file_refresh(file)