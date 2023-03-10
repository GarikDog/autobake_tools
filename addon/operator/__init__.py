import bpy

from .at_create_env import AT_OP_Create_Environment

classes = (
AT_OP_Create_Environment,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)