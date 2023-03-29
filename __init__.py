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

bl_info = {
    "name": "Autobake Tools",
    "description": "Autobake Tools",
    "author": "Igor Subachev (GarikDog)",
    "version": (1,1,0),
    "blender": (3,0,1),
    "location": "View3D",
    "category": "3D View"}



def register():
    from .addon.register import register_addon
    register_addon()



def unregister():
    from .addon.register import unregister_addon
    unregister_addon()