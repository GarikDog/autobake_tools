import bpy

from .at_create_env import AT_OP_Create_Environment
from .at_bake import AT_OP_Bake
from .at_node_value_setter import AT_OP_node_value_setter

classes = (
AT_OP_Create_Environment, AT_OP_Bake, AT_OP_node_value_setter
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)