 ###############################################################################
#   Copyright 2023 Igor Subachev (GarikDog)                                     #
#                                                                               #
#   Licensed under the Apache License, Version 2.0 (the "License");             #
#   you may not use this file except in compliance with the License.            #
#   You may obtain a copy of the License at                                     #
#                                                                               #
#       http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                               #
#   Unless required by applicable law or agreed to in writing, software         #
#   distributed under the License is distributed on an "AS IS" BASIS,           #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
#   See the License for the specific language governing permissions and         #
#   limitations under the License.                                              #
 ###############################################################################

import bpy

from ..utility.at_utils import bevel_samples_setting, bevel_radius_setting

def get_bevel_value(self):
    return self.id_data.get("at_tool.bevel_samples_prop_int", int(8))

def set_bevel_value(self, value):
    self.id_data["at_tool.bevel_samples_prop_int"]=value
    try:
        bevel_samples_setting()
    except:
        print("there are no Nodes by now")
    
def get_bevel_radius(self):
    return self.id_data.get("at_tool.bevel_radius_prop_float", float(0.02))
    
def set_bevel_radius(self, value):
    self.id_data["at_tool.bevel_radius_prop_float"]=value
    try:
        bevel_radius_setting()
    except:
        print("there are no Nodes by now")

class AT_Properties(bpy.types.PropertyGroup):
    bevel_samples_prop_int : bpy.props.IntProperty(name="Bevel Samples", soft_min=2, soft_max=32, default=8, get=get_bevel_value, set=set_bevel_value)
    bevel_radius_prop_float : bpy.props.FloatProperty(name="Bevel Radius", soft_min=0.001, soft_max=0.5, default=0.02, step=0.001, precision=3, get=get_bevel_radius, set=set_bevel_radius)
    image_width_prop_int : bpy.props.IntProperty(name="Image Width", soft_min=2, soft_max=32768, default=2048)
    image_height_prop_int : bpy.props.IntProperty(name="Image Height", soft_min=2, soft_max=32768, default=2048)
    at_image_name : bpy.props.StringProperty(default="")
