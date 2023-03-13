import bpy

from .at_properties import AT_Properties
from .at_obj_properties import AT_Obj_Properties

classes = (
    AT_Properties, AT_Obj_Properties
)


def register_property():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.at_tool = bpy.props.PointerProperty(type=AT_Properties)
    bpy.types.Object.at_objtool = bpy.props.PointerProperty(type=AT_Obj_Properties)


def unregister_property():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.at_tool
    del bpy.types.Object.at_objtool