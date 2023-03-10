import bpy


def create_at_env():
    scn = bpy.context.scene
    # Set cycles render engine if not selected
    if not scn.render.engine == 'CYCLES':
        scn.render.engine = 'CYCLES'
        print ("Render engine setted to", scn.render.engine)
        
    
    
    

   
