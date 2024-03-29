 ###############################################################################
#   Copyright 2023 Igor Subachev (GarikDog)                                     #
#                                                                               #
#   Licensed under the Apache License, Version 2.0 (the "License");             #
#   you may not use this file except in compliance with the License.            #
#   You may obtain a copy of the License at                                     #
#                                                                               #
#       http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                               #
#   Unless required by applicable law or agreed to in writing, software         #
#   distributed under the License is distributed on an "AS IS" BASIS,           #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
#   See the License for the specific language governing permissions and         #
#   limitations under the License.                                              #
 ###############################################################################
# SPDX-FileCopyrightText: 2011-2022 Blender Foundation
#
# SPDX-License-Identifier: Apache-2.0


# Igor Subachev (GarikDog) :

import bpy


def create_render_env_n():
    scn = bpy.context.scene
    attool = scn.at_tool
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
    
    # Set custom bool dx property to correct value from Y channel
    try:
        if bpy.context.scene.render.bake.normal_g == 'NEG_Y':
            attool.at_dx_normal = True
        elif bpy.context.scene.render.bake.normal_g == 'POS_Y':
            attool.at_dx_normal = False
    except:
        pass
    

        
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



def create_image(suffix):
    
    scene = bpy.context.scene
    attool = scene.at_tool
    
    # Get image size from custom properties
    im_width = attool.image_width_prop_int
    im_height = attool.image_height_prop_int
    
    
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes:
        print (("node type is:"), (node.type))
        if node.type == "TEX_IMAGE":
            image_texture_node = node
    
    obj = bpy.context.active_object
    images = bpy.data.images
    image_names = []
    count_suffix = 1
    image_name = f'{obj.name}'
    
    
    for image in images:
        image_name = f'{obj.name}_{count_suffix}{suffix}'
        image_names.append(image.name)
        
        if image_name in image_names:
            count_suffix += 1
            image_name = f'{obj.name}_{count_suffix}{suffix}'
        
        
        
        
            
    bpy.ops.image.new(name=(image_name),width=im_width, height=im_height, generated_type='COLOR_GRID', alpha=False)
    
    
    print(("Image name is  - "), (image_name))
    # Set current texture name to the custom property
    attool.at_image_name = image_name
    
    # Link texture by name from custom property
    image_texture_node.image = bpy.data.images.get(attool.at_image_name)
    
    return image_name


    
    
# set node location

def setNodeLocation(node, x, y):
    if node.location:
        node.location = x, y
    

def change_to_glossy_shader(statement: bool):
    links = bpy.context.active_object.active_material.node_tree.links
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes:
        if node.type == 'BSDF_DIFFUSE':
            diffuse_node = node
        if node.type == 'BSDF_GLOSSY':
            glossy_node = node
        if node.type == 'OUTPUT_MATERIAL':
            output_node = node
        
    
    if statement:
        links.new(glossy_node.outputs[0], output_node.inputs[0])
    else:
        links.new(diffuse_node.outputs[0], output_node.inputs[0])


def create_shader_editor_env():
    
    
    scene = bpy.context.scene
    attool = scene.at_tool
    # Get nodes from node tree and clear
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    nodes.clear()
    
    
   
    

    # Create nodes
    shader_node = nodes.new("ShaderNodeBsdfDiffuse")
    shader_node_glossy = nodes.new("ShaderNodeBsdfGlossy")
    mat_output = nodes.new('ShaderNodeOutputMaterial')
    bevel_node = nodes.new("ShaderNodeBevel")
    image_texture_node = nodes.new("ShaderNodeTexImage")
    ambient_occulusion_node = nodes.new("ShaderNodeAmbientOcclusion")
    math_node = nodes.new("ShaderNodeMath")
    
    # Place nodes in correct position
    setNodeLocation(shader_node_glossy, 0, 200)
    setNodeLocation(mat_output, 300, 25)
    setNodeLocation(bevel_node, -300, -565)
    setNodeLocation(image_texture_node, -900, 0)
    setNodeLocation(ambient_occulusion_node, -600, 0)
    setNodeLocation(math_node, -300, 0)

    # Get node links
    links = bpy.context.active_object.active_material.node_tree.links
    
    # Default glossy for glossy bsdf shader
    default_glossy = 0.2 
    
    # Link nodes
    links.new(bevel_node.outputs['Normal'], shader_node.inputs['Normal'])
    links.new(bevel_node.outputs['Normal'], shader_node_glossy.inputs['Normal'])
    links.new(shader_node.outputs[0], mat_output.inputs[0])
    math_node.operation = 'POWER' # make power operation in the Math node (it always have Add by default)
    shader_node_glossy.inputs['Roughness'].default_value = default_glossy
    math_node.inputs[1].default_value = attool.at_ao_exponentiation
    bevel_node.inputs['Radius'].default_value = attool.bevel_radius_prop_float
    bevel_node.samples = attool.bevel_samples_prop_int
    ambient_occulusion_node.samples = attool.at_ao_samples
    ambient_occulusion_node.inputs['Distance'].default_value = attool.at_ao_distance
    links.new(ambient_occulusion_node.outputs['Color'], math_node.inputs[0])
    links.new(math_node.outputs[0], shader_node.inputs['Color'])
    links.new(math_node.outputs[0], shader_node_glossy.inputs['Color'])
    
    
    attool.at_glossy_preview = False
    
    for node in nodes:
        print (("I have this node:"), (node))
        
    return image_texture_node
    
    
        
def bevel_samples_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    for node in nodes:
        if node.type == 'BEVEL':
            bevel_node = node
            pass
    scene = bpy.context.scene
    
    attool = scene.at_tool
    bevel_node.samples = attool.bevel_samples_prop_int
    
def bevel_radius_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes:
        if node.type == 'BEVEL':
            bevel_node = node
            pass
    scene = bpy.context.scene
    
    attool = scene.at_tool
    bevel_node.inputs[0].default_value = attool.bevel_radius_prop_float
    
def ao_distance_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    for node in nodes:
        if node.type == 'AMBIENT_OCCLUSION':
            ao_node = node
            pass
        
    scene = bpy.context.scene
    attool = scene.at_tool
    
    ao_node.inputs[1].default_value = attool.at_ao_distance
    
def ao_exponentiation_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    for node in nodes:
        if node.type == 'MATH' and node.operation == 'POWER':
            power_node = node
            pass
    scene = bpy.context.scene
    attool = scene.at_tool
    
    power_node.inputs[1].default_value = attool.at_ao_exponentiation
    
def ao_samples_setting ():
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    
    for node in nodes:
        print("node type is: ", node.type)
        if node.type == 'AMBIENT_OCCLUSION':
            ao_node = node
            pass
        
    scene = bpy.context.scene
    attool = scene.at_tool
    
    ao_node.samples = attool.at_ao_samples
    
    

    
    
def viewport_shading_setting (intensity: float):
    
    bpy.context.space_data.shading.type = 'RENDERED'
    bpy.context.space_data.shading.studio_light = 'city.exr'
    
    if bpy.context.space_data.shading.studiolight_intensity != intensity:
        bpy.context.space_data.shading.studiolight_intensity = intensity

    if bpy.context.space_data.shading.use_scene_world_render:
        bpy.context.space_data.shading.use_scene_world_render = False
        
        
def showMessageBox(message='', title='Message box', icon='INFO'):

        def draw(self, context):
            self.layout.label(text=message)

        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


def change_bake_normal():
    scn = bpy.context.scene
    # Set Bake Type to Normal
    if not scn.cycles.bake_type == 'NORMAL':
        scn.cycles.bake_type = 'NORMAL'
    print ("Bake type setted to", scn.cycles.bake_type)
       
    # Set Selected to Active to False
    if not scn.render.bake.use_selected_to_active == False:
        scn.render.bake.use_selected_to_active = False
    print ("Selected to Active setted to", scn.render.bake.use_selected_to_active)

def change_bake_ao():
    scn = bpy.context.scene
    # Set Bake Type to AO
    if not scn.cycles.bake_type == 'DIFFUSE':
        scn.cycles.bake_type = 'DIFFUSE'
    print ("Bake type setted to", scn.cycles.bake_type)
    
    if not scn.render.bake.use_pass_direct == False:
        scn.render.bake.use_pass_direct = False
        
    if not scn.render.bake.use_pass_indirect == False:
        scn.render.bake.use_pass_indirect = False
        
        
def dx_normal_setting():
    scene = bpy.context.scene
    attool = scene.at_tool
    if attool.at_dx_normal:
        bpy.context.scene.render.bake.normal_g = 'NEG_Y'
    else:
        bpy.context.scene.render.bake.normal_g = 'POS_Y'
    


#Blender Foundation:

def get_effective_preview_denoiser(context):
    scene = context.scene
    cscene = scene.cycles

    if cscene.preview_denoiser != "AUTO":
        return cscene.preview_denoiser

    return 'OIDN'