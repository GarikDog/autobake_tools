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

from ..utility.at_utils import create_image


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
        
        image_name = create_image()
        
        bpy.ops.object.bake(type='NORMAL')
        
       
        
        bpy.ops.wm.window_new()
        print(bpy.context.area)
        
        for area in bpy.context.screen.areas:
            area.type = 'IMAGE_EDITOR'
            area.spaces.active.image = bpy.data.images[image_name]
        
        
        return{'FINISHED'}