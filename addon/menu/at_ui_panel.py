import bpy
from bpy.types import Menu, Panel, UIList


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
    

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.operator("at.create_environment")
        box.operator("material.new")


'''    def draw(self, context):
        self.layout.label(text="Autobake HERE!")'''