import bpy
from bpy.types import Operator

from ..utility.at_utils import create_render_env


class AT_OP_Create_Environment(Operator):
    bl_idname = "at.create_environment"
    bl_label = "Create Bake Environment"
    bl_description = "Prepares the scene and object for baking"
    
    
    def execute(self, context):
        create_render_env()
        return{'FINISHED'}