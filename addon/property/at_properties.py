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

from ..utility.at_utils import bevel_samples_setting, bevel_radius_setting, ao_distance_setting, ao_exponentiation_setting, ao_samples_setting, change_to_glossy_shader, dx_normal_setting

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
        
        
def get_at_ao_distance(self):
    return self.id_data.get("at_ao_distance", float(0.1))


def get_at_glossy_preview(self):
    return self.id_data.get("at_glossy_preview", bool(False))

def set_at_glossy_preview(self, value):
    self.id_data["at_glossy_preview"]=value
    try:
        change_to_glossy_shader(value)
    except:
        print("there are no Nodes by now")

def set_at_ao_distance(self, value):
    self.id_data["at_ao_distance"]=value
    try:
        ao_distance_setting()
        set_at_glossy_preview(self, False)
    except:
        print("there are no Nodes by now")
        
def get_at_ao_exponentiation(self):
    return self.id_data.get("at_ao_exponentiation", float(1))

def set_at_ao_exponentiation(self, value):
    self.id_data["at_ao_exponentiation"]=value
    try:
        ao_exponentiation_setting()
        set_at_glossy_preview(self, False)
    except:
        print("there are no Nodes by now")
        
        
def get_at_ao_samples(self):
    return self.id_data.get("at_ao_samples", int(8))

def set_at_ao_samples(self, value):
    self.id_data["at_ao_samples"]=value
    try:
        ao_samples_setting()
        set_at_glossy_preview(self, False)
    except:
        print("there are no Nodes by now")
        
def get_dx_normal(self):
    return self.id_data.get("at_dx_normal", bool(False))

def set_dx_normal(self, value):
    self.id_data["at_dx_normal"]=value
    try:
        dx_normal_setting()
    except:
        pass
        


class AT_Properties(bpy.types.PropertyGroup):
    bevel_samples_prop_int : bpy.props.IntProperty(name="Bevel Samples", soft_min=2, soft_max=32, default=8, get=get_bevel_value, set=set_bevel_value)
    bevel_radius_prop_float : bpy.props.FloatProperty(name="Bevel Radius", soft_min=0.001, soft_max=0.5, default=0.02, step=0.001, precision=3, get=get_bevel_radius, set=set_bevel_radius)
    image_width_prop_int : bpy.props.IntProperty(name="Image Width", soft_min=2, soft_max=32768, default=2048)
    image_height_prop_int : bpy.props.IntProperty(name="Image Height", soft_min=2, soft_max=32768, default=2048)
    at_image_name : bpy.props.StringProperty(default="")
    at_ao_distance : bpy.props.FloatProperty(name="AO Distance", soft_min=0.001, soft_max=10, default=0.1, step=0.001, precision=3, get=get_at_ao_distance, set=set_at_ao_distance)
    at_ao_exponentiation : bpy.props.FloatProperty(name="AO Exponentiation", soft_min=0.1, soft_max=10, default=1, step=0.001, precision=3, get=get_at_ao_exponentiation, set=set_at_ao_exponentiation)
    at_ao_samples : bpy.props.IntProperty(name="AO Samples", soft_min=2, soft_max=32, default=8, get=get_at_ao_samples, set=set_at_ao_samples)
    at_glossy_preview : bpy.props.BoolProperty(name="Glossy Preview", default=False, get=get_at_glossy_preview, set=set_at_glossy_preview)
    at_dx_normal : bpy.props.BoolProperty(name="DX normal", default=False, get=get_dx_normal, set=set_dx_normal)
