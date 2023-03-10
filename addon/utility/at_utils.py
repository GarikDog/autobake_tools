import bpy


def create_render_env_n():
    scn = bpy.context.scene
    # Set cycles render engine if not selected
    if not scn.render.engine == 'CYCLES':
        scn.render.engine = 'CYCLES'
    print ("Render engine setted to", scn.render.engine)
    
    # Set features set to Supported if not selected
    if not scn.cycles.feature_set == 'SUPPORTED':
        scn.cycles.feature_set = 'SUPPORTED'
    print ("Feature Set setted to", scn.cycles.feature_set)
    
    # Set Render Device to GPU Compute if not selected
    if not scn.cycles.device == 'GPU':
        scn.cycles.device = 'GPU'
    print ("Render Device setted to", scn.cycles.device)
    
    # Set Bake Multires to False if not
    if not scn.render.use_bake_multires == False:
        scn.render.use_bake_multires = False
    print ("Bake Multires setted to", scn.render.use_bake_multires)
    
    # Set Bake Type to Normal if not
    if not scn.cycles.bake_type == 'NORMAL':
        scn.cycles.bake_type = 'NORMAL'
    print ("Bake type setted to", scn.cycles.bake_type)
       
    # Set Selected to Active to False if not
    if not scn.render.bake.use_selected_to_active == False:
        scn.render.bake.use_selected_to_active = False
    print ("Selected to Active setted to", scn.render.bake.use_selected_to_active)
        
def create_mat_env():
    obj = bpy.context.active_object
    
    #create new material if there are not mat on obj
    if obj.active_material == None:
        matname = 'baker_material'
        mat = bpy.data.materials.new(matname)
        obj.data.materials.append(mat)
    
    #Set Use Nodes if obj arlready have a material
    if obj.active_material != None:
       if bpy.context.active_object.active_material.use_nodes == False:
           bpy.context.active_object.active_material.use_nodes = True
        
    print ("Object active material is", obj.active_material)
