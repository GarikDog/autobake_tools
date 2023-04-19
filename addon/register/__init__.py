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

def register_addon():
    #register
    from ..menu import register_menus
    register_menus()
    
    from ..operator import register_operators
    register_operators()
    
    from ..property import register_property
    register_property()
    
    
    return



def unregister_addon():
    #unregister
    from ..menu import unregister_menus
    unregister_menus()
    
    from ..operator import unregister_operators
    unregister_operators()
    
    from ..property import unregister_property
    unregister_property()
    
    
    return 