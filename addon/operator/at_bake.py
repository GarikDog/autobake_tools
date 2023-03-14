import bpy
from bpy.types import Operator

from ..utility.at_utils import create_image


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
        
        image_name = create_image()
        
        bpy.ops.object.bake(type='NORMAL')
        
       
        
        bpy.ops.wm.window_new()
        print(bpy.context.area)
        
        for area in bpy.context.screen.areas:
            area.type = 'IMAGE_EDITOR'
            area.spaces.active.image = bpy.data.images[image_name]
        
        
        return{'FINISHED'}