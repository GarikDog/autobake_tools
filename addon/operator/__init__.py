import bpy

from .at_create_env import AT_OP_Create_Environment
from .at_bake import AT_OP_Bake

classes = (
AT_OP_Create_Environment, AT_OP_Bake
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)