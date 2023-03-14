bl_info = {
    "name": "Autobake Tools",
    "description": "Autobake Tools",
    "author": "Igor Subachev (Garik_Dog)",
    "version": (1,01),
    "blender": (3,4,1),
    "location": "View3D",
    "category": "3D View"}



def register():
    from .addon.register import register_addon
    register_addon()



def unregister():
    from .addon.register import unregister_addon
    unregister_addon()