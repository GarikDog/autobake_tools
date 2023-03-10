import bpy
from bpy.types import Menu, Panel, UIList
from ..property.at_properties import AT_Properties


class VIEW3D_PT_Autobake(Panel):
    bl_idname = "VIEW3D_PT_Atobake"
    bl_label = "Atobake Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Autobake Tools"
    
    
    @classmethod
    
    def poll(cls, context):
        if context.active_object != None:
            if context.active_object.type == 'MESH':
                return True
        return False
    


    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        attool = scene.at_tool
        
        obj = context.object
        bevel_samples = int(8)
        bevel_radius = float(0.05)
        image_width = int(2048)
        image_height = int(2048)
        
        box = layout.box()
        row = layout.split(factor=0.5, align=False)
        
        box.operator("at.create_environment")

        box.column().prop(attool, "bevel_samples_prop_int", text="Bevel Samples")
        box.column().prop(attool, "bevel_radius_prop_float", text="Bevel Radius (n)")
        box.column().prop(attool, "image_width_prop_int", text="Image Width")
        box.column().prop(attool, "image_height_prop_int", text="Image Height")
        