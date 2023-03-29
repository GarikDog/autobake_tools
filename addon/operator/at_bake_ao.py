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
from bpy.types import Operator

from ..utility.at_utils import create_image,showMessageBox, change_bake_ao


class AT_OP_Bake_ao(Operator):
    bl_idname = "at.bake_ao"
    bl_label = "Bake AO and Show"
    bl_description = "Bake Ambient Occlusion map. Then show the result image"
    
    
    @classmethod
    
    def poll(cls, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        if atobjtool.prepare_statement_prop_bool == True:
            return True
        return False
    
    
    
    
    def execute(self, context):
        try:
            scene = bpy.context.scene
            attool = scene.at_tool
            if attool.at_glossy_preview:
                glossy_statement = True
                attool.at_glossy_preview = False
            change_bake_ao()
            image_name = create_image("_ao")
            bpy.ops.object.bake(type='DIFFUSE')
  
            bpy.ops.wm.window_new()
            print(bpy.context.area)
            
            for area in bpy.context.screen.areas:
                area.type = 'IMAGE_EDITOR'
                area.spaces.active.image = bpy.data.images[image_name]
            if glossy_statement:
                attool.at_glossy_preview = True
            
        except Exception as e:
            e = ("Please check Bake Environment")
            showMessageBox(e, "Where am I?", 'ZOOM_ALL')
        
        
        return{'FINISHED'}