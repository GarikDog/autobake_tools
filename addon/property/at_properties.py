import bpy



class AT_Properties(bpy.types.PropertyGroup):
    bevel_samples_prop_int : bpy.props.IntProperty(name="Bevel Samples", soft_min=2, soft_max=32, default=8)
    bevel_radius_prop_float : bpy.props.FloatProperty(name="Bevel Radius", soft_min=0.01, soft_max=0.5, default=0.05)
    image_width_prop_int : bpy.props.IntProperty(name="Image Width", soft_min=2, soft_max=32768, default=2048)
    image_height_prop_int : bpy.props.IntProperty(name="Image Height", soft_min=2, soft_max=32768, default=2048)
    at_image_name : bpy.props.StringProperty(default="")
