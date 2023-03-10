import bpy
from bpy.types import Menu, Panel, UIList


class VIEW3D_PT_Autobake(Panel):
    bl_idname = "VIEW3D_PT_Atobake"
    bl_label = "Atobake Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Autobake Tools"
    
    

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")

'''    def draw(self, context):
        self.layout.label(text="Autobake HERE!")'''