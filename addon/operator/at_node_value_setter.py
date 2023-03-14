import bpy
from bpy.types import Operator

from ..utility.at_utils import (bevel_samples_setting)

class AT_OP_node_value_setter(Operator):
    bl_idname = "at.node_value_setter"
    bl_label = "Set Node values"
    bl_description = "Setting up node values"
    
    
    

    
    
    def modal(self, context, event):
        if event.type == 'LEFTMOUSE':
            print("eeeeeeeeeeeeeeeeeeeeeee")