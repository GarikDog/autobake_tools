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
 
# SPDX-FileCopyrightText: 2011-2022 Blender Foundation
#
# SPDX-License-Identifier: Apache-2.0

import bpy

from bpy.types import Panel
from ..utility.at_utils import get_effective_preview_denoiser




class VIEW3D_PT_Autobake(Panel):
    bl_idname = "VIEW3D_PT_Atobake"
    bl_label = "Auto-bake Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"
    
    
    @classmethod
    
    def poll(cls, context):
        if context.active_object != None:
            if context.active_object.type == 'MESH':
                return True
        return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    

    def draw(self, context):
        
        layout = self.layout
        scene = bpy.context.scene
        attool = scene.at_tool
        job_statement = False
       
        box = layout.box()
        box.operator("at.create_environment")
        layout.column().prop(attool, "at_glossy_preview", text="Glossy Preview")
        layout.column().prop(attool, "image_width_prop_int", text="Image Width")
        layout.column().prop(attool, "image_height_prop_int", text="Image Height")
        layout.label(text="Bevel Shader:")
        layout.column().prop(attool, "bevel_samples_prop_int", text="Bevel Samples")
        layout.column().prop(attool, "bevel_radius_prop_float", text="Bevel Radius")
        layout.column().prop(attool, "at_dx_normal", text="DirectX Normal")
        
        box = layout.box()
        row = layout.split(factor=0.5, align=False)
        
        
        bake = box.operator("at.bake")
        
    
        
        layout.label(text="Ambient Occlusion:")
        layout.column().prop(attool, "at_ao_distance", text="AO Distance")
        layout.column().prop(attool, "at_ao_samples", text="AO Samples")
        layout.column().prop(attool, "at_ao_exponentiation", text="AO Exponentiation")
        
        
        box = layout.box()
        row = layout.split(factor=0.5, align=False)
        box.operator("at.bake_ao")
        
class VIEW3D_PT_Sampling(Panel):
    bl_idname = "VIEW3D_PT_Sampling"
    bl_label = "Sampling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"

    
    
    
    @classmethod
    
    # def poll(cls, context):
    #     if context.active_object != None:
    #         if context.active_object.type == 'MESH' and context.scene.render.engine == 'CYCLES':
    #             return True
    #     return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    

    def draw(self, context):
        layout = self.layout
        
        #scene = bpy.context.scene
        #attool = scene.at_tool
        
class VIEW3D_PT_sampling_viewport(Panel):
    bl_idname = "VIEW3D_PT_sampling_viewport"
    bl_label = "Viewport"
    bl_parent_id = "VIEW3D_PT_Sampling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"

    
    
    
    @classmethod
    
    def poll(cls, context):
        if context.active_object != None:
            if context.active_object.type == 'MESH' and context.scene.render.engine == 'CYCLES':
                return True
        return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    
        
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cscene = scene.cycles
        layout.use_property_split = True
        layout.use_property_decorate = False
        heading = layout.column(align=True, heading="Noise Threshold")
        row = heading.row(align=True)
        row.prop(cscene, "use_preview_adaptive_sampling", text="")
        sub = row.row()
        sub.active = cscene.use_preview_adaptive_sampling
        sub.prop(cscene, "preview_adaptive_threshold", text="")
        if cscene.use_preview_adaptive_sampling:
            col = layout.column(align=True)
            col.prop(cscene, "preview_samples", text="Max Samples")
            col.prop(cscene, "preview_adaptive_min_samples", text="Min Samples")
        else:
            layout.prop(cscene, "preview_samples", text="Samples")
            
class VIEW3D_PT_sampling_viewport_denoise(Panel):
    bl_idname = "VIEW3D_PT_sampling_viewport_denoise"
    bl_label = "Denoise"
    bl_parent_id = "VIEW3D_PT_sampling_viewport"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    
    # def poll(cls, context):
    #     if context.active_object != None:
    #         if context.active_object.type == 'MESH' and context.scene.render.engine == 'CYCLES':
    #             return True
    #     return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    

    def draw_header(self, context):
        scene = context.scene
        cscene = scene.cycles

        self.layout.prop(context.scene.cycles, "use_preview_denoising", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        cscene = scene.cycles

        col = layout.column()
        col.active = cscene.use_preview_denoising
        col.prop(cscene, "preview_denoiser", text="Denoiser")
        col.prop(cscene, "preview_denoising_input_passes", text="Passes")
        
        effective_preview_denoiser = get_effective_preview_denoiser(context)
        if effective_preview_denoiser == 'OPENIMAGEDENOISE':
            col.prop(cscene, "preview_denoising_prefilter", text="Prefilter")

        col.prop(cscene, "preview_denoising_start_sample", text="Start Sample")
        
        
class VIEW3D_PT_sampling_render(Panel):
    bl_idname = "VIEW3D_PT_sampling_render"
    bl_label = "Render"
    bl_parent_id = "VIEW3D_PT_Sampling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"

    
    
    
    @classmethod
    
    def poll(cls, context):
        if context.active_object != None:
            if context.active_object.type == 'MESH' and context.scene.render.engine == 'CYCLES':
                return True
        return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    
        
    def draw(self, context):
        layout = self.layout

        scene = context.scene
        cscene = scene.cycles

        layout.use_property_split = True
        layout.use_property_decorate = False

        heading = layout.column(align=True, heading="Noise Threshold")
        row = heading.row(align=True)
        row.prop(cscene, "use_adaptive_sampling", text="")
        sub = row.row()
        sub.active = cscene.use_adaptive_sampling
        sub.prop(cscene, "adaptive_threshold", text="")

        col = layout.column(align=True)
        if cscene.use_adaptive_sampling:
            col.prop(cscene, "samples", text="Max Samples")
            col.prop(cscene, "adaptive_min_samples", text="Min Samples")
        else:
            col.prop(cscene, "samples", text="Samples")
        col.prop(cscene, "time_limit")
        
class VIEW3D_PT_sampling_render_denoise(Panel):
    bl_idname = "VIEW3D_PT_sampling_render_denoise"
    bl_label = "Denoise"
    bl_parent_id = "VIEW3D_PT_sampling_render"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto-bake Tools"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    
    # def poll(cls, context):
    #     if context.active_object != None:
    #         if context.active_object.type == 'MESH' and context.scene.render.engine == 'CYCLES':
    #             return True
    #     return False
    
    
    def invoke(self, context, event):
        return {'RUNNING_MODAL'}
    
    def draw_header(self, context):
        scene = context.scene
        cscene = scene.cycles

        self.layout.prop(context.scene.cycles, "use_denoising", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        cscene = scene.cycles

        col = layout.column()
        col.active = cscene.use_denoising
        col.prop(cscene, "denoiser", text="Denoiser")
        col.prop(cscene, "denoising_input_passes", text="Passes")
        if cscene.denoiser == 'OPENIMAGEDENOISE':
            col.prop(cscene, "denoising_prefilter", text="Prefilter")