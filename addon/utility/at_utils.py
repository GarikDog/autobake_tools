import bpy


def create_render_env():
    scn = bpy.context.scene
    # Set cycles render engine if not selected
    if not scn.render.engine == 'CYCLES':
        scn.render.engine = 'CYCLES'
    print ("Render engine setted to", scn.render.engine)
    
    # Set features set to Supported if not selected
    if not scn.cycles.feature_set == 'SUPPORTED':
        scn.cycles.feature_set = 'SUPPORTED'
    print ("Feature Set setted to", scn.cycles.feature_set)
    
    # Set Render Device to GPU Compute if not selected
    if not scn.cycles.device == 'GPU':
        scn.cycles.device = 'GPU'
    print ("Render Device setted to", scn.cycles.device)
    
    

    
        
        
    
    
    

   
