import bpy
from bpy.types import Operator

from ..utility.at_utils import (bevel_samples_setting)

class AT_OP_node_value_setter(Operator):
    bl_idname = "at.node_value_setter"
    bl_label = "Set Node values"
    bl_description = "Setting up node values"
    
    def execute(self, context):
        #bevel_samples_setting()
        return{'FINISHED'}