import bpy

from .ui_panel import VIEW3D_PT_Autobake

classes = (
    VIEW3D_PT_Autobake,
)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)