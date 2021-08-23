import creopyson


c = creopyson.Client()
c.connect()

c.creo_cd("C:\\Users\\patrick.vieira\\Documents\\Creo\\cubo")

file = "asm0001.asm"
template = "drw0001.drw"
desenho = 'icv_teste_desenho2.drw'

creopyson.drawing.create(c, template, model=file, drawing="icv_teste_desenho2", scale=1, display=True, activate=True, new_window=True)

c.file_open(desenho, display=True)
point1 = {'x': 60, 'y':240}
model_view1 = 'Default Orientation'


creopyson.drawing.create_gen_view(c, model_view1, point1, drawing=desenho, view=None, sheet=None, model=None, scale=None, display_data=None, exploded=None)

point2 = {'x': 200, 'y':200}
model_view2 = 'front'


creopyson.drawing.create_gen_view(c, model_view2, point2, drawing=desenho, view=None, sheet=None, model=None, scale=None, display_data=None, exploded=None)

# parent_view = 'new_view_13'
# point3 = {'x': 50}
# creopyson.drawing.create_proj_view(c, parent_view, point3, drawing=desenho, view=None, sheet=None, display_data=None, exploded=None)


#print (creopyson.drawing.list_views(c, view=None, drawing=desenho))