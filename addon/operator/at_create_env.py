import bpy
from bpy.types import Operator

from ..utility.at_utils import (create_mat_env, create_render_env_n,
                                create_shader_editor_env, create_image)



class AT_OP_Create_Environment(Operator):
    bl_idname = "at.create_environment"
    bl_label = "Create Bake Environment"
    bl_description = "Prepares the scene and object for baking"
    
    
    def execute(self, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        create_render_env_n()
        create_mat_env()
        create_shader_editor_env()
        create_image()
        
        # Setting the value for custom statement property
        atobjtool.prepare_statement_prop_bool = True
        return{'FINISHED'}
    
    


