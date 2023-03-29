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

import bpy

from gpu_extras.presets import draw_texture_2d
from bpy.types import Menu, Panel, UIList

from ..utility.at_utils import bevel_samples_setting


class VIEW3D_PT_Autobake(Panel):
    bl_idname = "VIEW3D_PT_Atobake"
    bl_label = "Autobake Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Autobake Tools"
    
    
    @classmethod
    
    def poll(cls, context):
        if context.active_object != None:
            if context.active_object.type == 'MESH':
                return True
        return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    

    def draw(self, context):
        
        layout = self.layout
        scene = bpy.context.scene
        attool = scene.at_tool
       
        box = layout.box()
        box.operator("at.create_environment")
        layout.column().prop(attool, "image_width_prop_int", text="Image Width")
        layout.column().prop(attool, "image_height_prop_int", text="Image Height")
        layout.label(text="Bevel Shader:")
        layout.column().prop(attool, "bevel_samples_prop_int", text="Bevel Samples")
        layout.column().prop(attool, "bevel_radius_prop_float", text="Bevel Radius (m)")
        
        
        box = layout.box()
        row = layout.split(factor=0.5, align=False)
        
        box.operator("at.bake")
        
        layout.label(text="Ambient Occlusion:")
        layout.column().prop(attool, "at_ao_distance", text="AO Distance")
        layout.column().prop(attool, "at_ao_samples", text="AO Samples")
        layout.column().prop(attool, "at_ao_exponentiation", text="AO Exponentiation")
        
        
        box = layout.box()
        row = layout.split(factor=0.5, align=False)
        box.operator("at.bake_ao")