import bpy

from .at_properties import AT_Properties

classes = (
    AT_Properties,
)


def register_property():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        bpy.types.Scene.at_tool = bpy.props.PointerProperty(type=AT_Properties)


def unregister_property():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        del bpy.types.Scene.at_tool