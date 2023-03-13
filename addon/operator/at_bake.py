import bpy
from bpy.types import Operator


class AT_OP_Bake(Operator):
    bl_idname = "at.bake"
    bl_label = "Bake and Show Image"
    bl_description = "Bake map. Then show the result image"
    
    
    @classmethod
    
    def poll(cls, context):
        obj = context.active_object
        atobjtool = obj.at_objtool
        if atobjtool.prepare_statement_prop_bool == True:
            return True
        return False
    
    
    
    
    def execute(self, context):
        return{'FINISHED'}