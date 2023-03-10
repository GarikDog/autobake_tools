

def register_addon():
    #register
    from ..menu import register_menus
    register_menus()
    return


def unregister_addon():
    #unregister
    from ..menu import unregister_menus
    unregister_menus()
    return 