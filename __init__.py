bl_info = {
    "name": "Autobake",
    "description": "Autobake Tools",
    "author": "Igor Subachev",
    "version": (1,0),
    "blender": (3,4,1),
    "location": "View3D",
    "category": "3D View"}



def register():
    from .addon.register import register_addon
    register_addon()



def unregister():
    from .addon.register import unregister_addon
    unregister_addon()