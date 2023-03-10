

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