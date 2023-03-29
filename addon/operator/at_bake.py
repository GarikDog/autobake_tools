
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

from ..utility.at_utils import create_image, showMessageBox



class AT_OP_Bake(Operator):
    bl_idname = "at.bake"
    bl_label = "Bake Normal and Show"
    bl_description = "Bake map. Then show the result image"
    
    
    @classmethod
    
    def poll(cls, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        if atobjtool.prepare_statement_prop_bool == True:
            return True
        return False
    
    
    
    
    
    def execute(self, context):
        try:
            image_name = create_image("_n")
            bpy.ops.object.bake(type='NORMAL')
            
        
            
            bpy.ops.wm.window_new()
            print(bpy.context.area)
            
            for area in bpy.context.screen.areas:
                area.type = 'IMAGE_EDITOR'
                area.spaces.active.image = bpy.data.images[image_name]
        except Exception as e:
            e = ("Please check Bake Environment")
            showMessageBox(e, "Where am I?", 'ZOOM_ALL')
            
        
        
        return{'FINISHED'}
    
    