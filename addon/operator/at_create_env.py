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

from ..utility.at_utils import (create_mat_env, create_render_env_n,
                                create_shader_editor_env, bevel_samples_setting, viewport_shading_setting)



class AT_OP_Create_Environment(Operator):
    bl_idname = "at.create_environment"
    bl_label = "Create Bake Environment"
    bl_description = "Prepares the scene and object for baking"
    
    
    def execute(self, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        light_intensity = 1
        
        
        viewport_shading_setting(light_intensity)
        create_render_env_n()
        create_mat_env()
        create_shader_editor_env()
        
        
        # Setting the value for custom statement property
        atobjtool.prepare_statement_prop_bool = True
        return{'FINISHED'}
    
    
    


