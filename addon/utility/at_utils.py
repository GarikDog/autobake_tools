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
    try:
        if not scn.cycles.device == 'GPU':
            scn.cycles.device = 'GPU'
    except:
        print ("Current device is", scn.cycles.device)
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



def create_image():
    
    scene = bpy.context.scene
    attool = scene.at_tool
    
    # Get image size from custom properties
    im_width = attool.image_width_prop_int
    im_height = attool.image_height_prop_int
    
    
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    image_texture_node = nodes.get("Image Texture")
    
    obj = bpy.context.active_object
    images = bpy.data.images
    image_names = []
    count_suffix = 1
    image_name = f'{obj.name}'
    
    
    for image in images:
        image_name = f'{obj.name}_{count_suffix}_n'
        image_names.append(image.name)
        
        if image_name in image_names:
            count_suffix += 1
            image_name = f'{obj.name}_{count_suffix}_n'
        
        
        
        
            
    bpy.ops.image.new(name=(image_name),width=im_width, height=im_height, generated_type='COLOR_GRID')
    
    # Set current texture name to the custom property
    attool.at_image_name = image_name
    
    # Link texture by name from custom property
    image_texture_node.image = bpy.data.images.get(attool.at_image_name)
    
    return image_name


    
    
# set node location

def setNodeLocation(node, x, y):
    if node.location:
        node.location = x, y
    
def create_shader_editor_env():
    
    
    scene = bpy.context.scene
    attool = scene.at_tool
    # Get nodes from node tree and clear
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    nodes.clear()
    
    
        
    # Create nodes
    shader_node = nodes.new("ShaderNodeBsdfPrincipled")
    mat_output = nodes.new('ShaderNodeOutputMaterial')
    bevel_node = nodes.new("ShaderNodeBevel")
    image_texture_node = nodes.new("ShaderNodeTexImage")
    
    # Place nodes in correct position
    setNodeLocation(mat_output, 300, 25)
    setNodeLocation(bevel_node, -300, -565)
    setNodeLocation(image_texture_node, -600, 0)

    # Get node links
    links = bpy.context.active_object.active_material.node_tree.links
    
    # Link nodes
    links.new(bevel_node.outputs[0], shader_node.inputs[22])
    links.new(shader_node.outputs[0], mat_output.inputs[0])
    
    
        
def bevel_samples_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    bevel_node = nodes.get("Bevel")
    scene = bpy.context.scene
    attool = scene.at_tool
    attool = scene.at_tool
    bevel_node.samples = attool.bevel_samples_prop_int
    
def bevel_radius_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    bevel_node = nodes.get("Bevel")
    scene = bpy.context.scene
    attool = scene.at_tool
    attool = scene.at_tool
    bevel_node.inputs[0].default_value = attool.bevel_radius_prop_float
    
    
def viewport_shading_setting (intensity: float):
    
    bpy.context.space_data.shading.type = 'RENDERED'
    bpy.context.space_data.shading.studio_light = 'city.exr'
    
    if bpy.context.space_data.shading.studiolight_intensity != intensity:
        bpy.context.space_data.shading.studiolight_intensity = intensity

    if bpy.context.space_data.shading.use_scene_world_render:
        bpy.context.space_data.shading.use_scene_world_render = False
        


