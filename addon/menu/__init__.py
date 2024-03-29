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

from .at_ui_panel import VIEW3D_PT_Autobake, VIEW3D_PT_Sampling, VIEW3D_PT_sampling_viewport, VIEW3D_PT_sampling_viewport_denoise, VIEW3D_PT_sampling_render, VIEW3D_PT_sampling_render_denoise

classes = (
    VIEW3D_PT_Autobake,
    VIEW3D_PT_Sampling,
    VIEW3D_PT_sampling_viewport,
    VIEW3D_PT_sampling_viewport_denoise,
    VIEW3D_PT_sampling_render,
    VIEW3D_PT_sampling_render_denoise
)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)