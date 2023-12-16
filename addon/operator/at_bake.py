
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

from ..utility.at_utils import create_image, showMessageBox, change_bake_normal



class AT_OP_Bake(Operator):
    bl_idname = "at.bake"
    bl_label = "Bake Normal and Show"
    bl_description = "Bake map. Then show the result image"
    
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        if bpy.app.is_job_running('OBJECT_BAKE'):
            return False
        elif atobjtool.prepare_statement_prop_bool:
            return True
        return False

    
    
    def execute(self, context):
        try:
            change_bake_normal()
            image_name = create_image("_n")
            bpy.ops.object.bake('INVOKE_DEFAULT',  type='NORMAL')
            

                
                
            def timer_to_create_image_window():
                if (bpy.app.is_job_running('OBJECT_BAKE') == False):
                    bpy.ops.wm.window_new()
                    print(bpy.context.area)
                    
                    for area in bpy.context.screen.areas:
                        area.type = 'IMAGE_EDITOR'
                        area.spaces.active.image = bpy.data.images[image_name]
                    bpy.app.timers.unregister(timer_to_create_image_window)
                return 0.1

            bpy.app.timers.register(timer_to_create_image_window)
                
            
           
    
            
            

            
        except Exception as e:
            e = ("Please check Bake Environment. Please select an Object if it's not selected")
            showMessageBox(e, "Where am I?", 'ZOOM_ALL')
            
        
        return{'FINISHED'}
    
    
    
    