import bpy

from ..utility.at_utils import bevel_samples_setting

def get_bevel_value(self):
    return self.id_data.get("at_tool.bevel_samples_prop_int", 1)

def set_bevel_value(self, value):
    self.id_data["at_tool.bevel_samples_prop_int"]=value
    bevel_samples_setting()
    

    

class AT_Properties(bpy.types.PropertyGroup):
    bevel_samples_prop_int : bpy.props.IntProperty(name="Bevel Samples", soft_min=2, soft_max=32, default=8, get=get_bevel_value, set=set_bevel_value)
    bevel_radius_prop_float : bpy.props.FloatProperty(name="Bevel Radius", soft_min=0.001, soft_max=0.5, default=0.02, step=0.001, precision=3)
    image_width_prop_int : bpy.props.IntProperty(name="Image Width", soft_min=2, soft_max=32768, default=2048)
    image_height_prop_int : bpy.props.IntProperty(name="Image Height", soft_min=2, soft_max=32768, default=2048)
    at_image_name : bpy.props.StringProperty(default="")
