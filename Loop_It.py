# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Loop It",
    "description": "Different Useful Loop Presets",
    "author": "Marc Rohrer \ CultLess (cultless@gmx.ch)",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "View 3D > UI > Loop It",
    "warning": "",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/node/node_presets.html",
    "category": "3D View",
}

import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )
import math

#################################################################
###                           PROPERTIES                      ###
#################################################################



class LOOP_IT_PROPS(PropertyGroup):
    
    #############################################
    #                Displacement               #
    #############################################
    
#    use_displace_texture: BoolProperty(
#        name="Use New Texture",
#        description="Add a Texture to Displace Modifier",
#        default = True
#        )
        
#    new_loop: BoolProperty(
#        name="New Loop",
#        description="New Loop",
#        default = True
#        )

    displace_texture: EnumProperty(
        name="Texture:",
        description="Choose Displace Texture",
        #        Type      Name  Identifier
        items=[ ('WOOD', "Wood", "Wood Texture"),
                ('VORONOI', "Voronoi", "Voronoi Texture"),
                ('STUCCI', "Stucci", "Stucci Texture"),
                ('NOISE', "Noise", "Noise Texture"),
                ('MUSGRAVE', "Musgrave", "Musgrave Texture"),
                ('MARBLE', "Marble", "Marble Texture"),
                ('MAGIC', "Magic", "Magic Texture"),
                ('IMAGE_OR_MOVIE', "Image or Movie", "Image or Movie"),
                ('DISTORTED_NOISE', "Distorted Noise", "Distorted Noise"),
                ('CLOUDS', "Clouds", "Clouds Texture"),
                ('BLEND', "Blend", "Blend Texture"), 
                ], 
                default = 'DISTORTED_NOISE')

    displace_amount: IntProperty(
        name = "",
        description="Amount of Loops during Timeline",
        default = 1,
        min = 1,
        max = 100
        )

    #############################################
    #          Texture Coordinate Node          #
    #############################################

    loop_tex_coord_node: EnumProperty(
        name="Texture:",
        description="Choose Texture Node",
        #        Type                   Name     Identifier
        items=[ ('ShaderNodeTexBrick', "Brick", "Brick Texture"),
                ('ShaderNodeTexChecker', "Checker", "Checker Texture"),
                ('ShaderNodeTexEnvironment', "Environment", "Stucci Texture"),
                ('ShaderNodeTexGradient', "Gradient", "Noise Texture"),
                ('ShaderNodeTexIES', "IES", "Musgrave Texture"),
                ('ShaderNodeTexImage', "Image", "Marble Texture"),
                ('ShaderNodeTexMagic', "Magic", "Magic Texture"),
                ('ShaderNodeTexMusgrave', "Musgrave", "Musgrave Texture"),
                ('ShaderNodeTexNoise', "Noise", "Noise Texture"),
                ('ShaderNodeTexPointDensity', "Point Density", "Point Density"),
                ('ShaderNodeTexSky', "Sky", "Sky Texture"),
                ('ShaderNodeTexVoronoi', "Voronoi", "Voronoi Texture"), 
                ('ShaderNodeTexWave', "Wave", "Wave Texture"), 
                ('ShaderNodeTexWhiteNoise', "White Noise", "White Noise"), 
                ], 
                default = 'ShaderNodeTexVoronoi')

    tex_coord_axis: EnumProperty(
        name="",
        description="Choose Camera Axis",
        #        Type      Name  Identifier
        items=[ ('X_AXIS', "X", "X Axis"),
                ('Y_AXIS', "Y", "Y Axis"),
                ('Z_AXIS', "Z", "Z Axis"),
                ('XY_AXIS', "XY", "X & Y Axis"),
                ('XZ_AXIS', "XZ", "X & Z Axis"),
                ('YZ_AXIS', "YZ", "Y & Z Axis"),
                ('XYZ_AXIS', "XYZ", "X & Y & Z Axis"),
               ]
        )

    texture_amount: IntProperty(
        name = "",
        description="Amount of Loops during Timeline",
        default = 1,
        min = 1,
        max = 100
        )

    #############################################
    #                   Ocean                   #
    #############################################

    ocean_speed: FloatProperty(
        name = "Ocean Speed",
        description = "Repetitions per Second (Time used on Ocean Modifier)",
        default = 1,
        )
        
    ocean_scale: FloatProperty(
        name = "Ocean Scale",
        description = "Scale used on Ocean Modifier",
        default = 2,
        )

    #############################################
    #                   Flag                    #
    #############################################

    #############################################
    #             Camera Turnaround             #
    #############################################

    camera_turn_angle: FloatProperty(
        name = "Camera rotation angle",
        description = "Angle to turn the camera",
        default = 360,
        )

    camera_turn_offset: IntProperty(
        name = "Offset",
        description="How many frames delayed camera will turn",
        default = 0
        )
        
    camera_turnaround_return: BoolProperty(
        name="Return",
        description="Camera return",
        default = False
        )

    #############################################
    #                Camera Array               #
    #############################################

    camera_array_axis: EnumProperty(
        name="Axis:",
        description="Choose Camera Axis",
        #        Type      Name  Identifier
        items=[ ('X_AXIS', "X", "X Axis"),
                ('Y_AXIS', "Y", "Y Axis"),
                ('Z_AXIS', "Z", "Z Axis"),
               ]
        )

    camera_array_speed: IntProperty(
        name = "Speed",
        description="How many frames delayed camera will turn",
        default = 1,
        min = 1,
        max = 5 # TODO
        )

    camera_mirror_array: BoolProperty(
        name="Use Mirror Modifier",
        description="Add a Mirror Modifier before Array Modifiers",
        default = True
        )

    #############################################
    #                 Optional                  #
    #############################################
    
    my_int: IntProperty(
        name = "",
        description="Amount of Loops during Timeline",
        default = 1,
        min = 10,
        max = 100
        )

    my_float_vector: FloatVectorProperty(
        name = "Float Vector Value",
        description="Something",
        default=(0.0, 0.0, 0.0), 
        min= 0.0, # float
        max = 0.1
    ) 

    my_string: StringProperty(
        name="User Input",
        description=":",
        default="",
        maxlen=1024,
        )

    my_path: StringProperty(
        name = "Directory",
        description="Choose a directory:",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
        )

#################################################################
###                          OPERATORS                        ###
#################################################################

class DISPLACEMENT_USER_SETTINGS(bpy.types.Operator):
    """Loop an Empty following a Bezier Circle"""
    bl_idname = "loop.displacement_user_settings"
    bl_label = "Displace"
        
    def execute(self, context):

        user_props = bpy.context.scene.loop_it_ui
        
        if user_props.update_displacement_timeline == False and user_props.new_loop == True:
            
#            print("Creating all new")
            
            bpy.ops.loop.displacement_first()
        
        elif user_props.update_displacement_timeline == True and user_props.new_loop == False:
            
#            print("Update Timeline")
            
            bpy.ops.loop.displacement_timeline()
            
            pass
        
        elif user_props.update_displacement_timeline == False and user_props.new_loop == False:
            
            print("Adding new Texture")
            
            pass
        
#        else user_props.update_displacement_frame == True and user_props.add_another_displacement == True:
#                    
#            print("Upddate Timeline & add new texture")
#            
#            pass
        
        return{'FINISHED'}

class DISPLACEMENT_FIRST(bpy.types.Operator):
    """Loop an Empty following a Bezier Circle"""
    bl_idname = "loop.displacement_first"
    bl_label = "Displace"
        
    def execute(self, context):
        
        user_props = bpy.context.scene.loop_it_ui
        
        # Saving actual frame
        
        actual_frame_user = bpy.context.scene.frame_current
        
#        if context.active_object is None:
#   
#            def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

#                def draw(self, context):
#                    self.layout.label(text=message)

#            bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


##Shows a message box with a specific message 
##ShowMessageBox("This is a message") 

##Shows a message box with a message and custom title
##ShowMessageBox("This is a message", "This is a custom title")

##Shows a message box with a message, custom title, and a specific icon
#            ShowMessageBox("Select object to displace", "No object selected", 'ERROR') 

#        try:
#            
#            bpy.data.objects['Circle Turn']
#        
#        except:
#            
#            print("Nein")

#        else:
#            
#            original_name = active_object_displace
#            print("Ja")
            
        # Saving active object name and renaming
        
#        original_object = bpy.context.active_object
#        original_object_name = bpy.context.active_object.name
        
        # Saving active object
        
#        active_collection = bpy.data.collections['Collection']
        original_object = bpy.context.active_object
        original_object.name = bpy.context.active_object.name
        active_object_displace = bpy.context.active_object
        print("Saving:", original_object.name)
#        print(original_name.name)
        active_object_displace.name = "loop_it_disp"
        print("After renaming:", original_object.name)
        
#        # Creating new Collection
#        
#        collection_loop = bpy.data.collections.new("Loop Displacement")
#        bpy.context.collection.children.link(collection_loop)

        # Adding Circle and Empty
           
        bpy.ops.curve.primitive_bezier_circle_add()
        circle_displacement = bpy.context.active_object
        circle_displacement.name = "Circle Displacement"
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        empty_displacement = context.active_object
        empty_displacement.name = "Empty Displacement"
        
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        bpy.context.object.constraints["Follow Path"].name = "Follow Path Loop It"

        bpy.context.object.constraints["Follow Path Loop It"].target = bpy.data.objects["Circle Displacement"]
        bpy.context.object.constraints["Follow Path Loop It"].show_expanded = False

        # Executing keyframing Class
        
        print("Before keyframes:", original_object.name)
        
        bpy.ops.loop.displacement_keyframes()   
        
        # Making Object from beginning active again
        
        print("Beginning active again:", original_object.name)
        
        bpy.ops.object.select_all(False)
        active_object_displace.select_set(True)
        context.view_layer.objects.active = active_object_displace

        # Adding Displace Modifier to active object
        # Code from https://github.com/njanakiev/blender-scripting/blob/master/scripts/rugged_donut.py, Line 43 ff.
        
#        obj = bpy.context.active_object
        displace = active_object_displace.modifiers.new('Displace Loop It', 'DISPLACE')
        
#                                            Modifier   Texture from Props
        displacetex = bpy.data.textures.new('Displace Loop It', user_props.displace_texture)
        displace.texture = displacetex
            
        # Displace Modifier Settings
        
        bpy.context.object.modifiers["Displace Loop It"].mid_level = 0
        bpy.context.object.modifiers["Displace Loop It"].texture_coords = 'OBJECT'
        bpy.context.object.modifiers["Displace Loop It"].texture_coords_object = empty_displacement

        bpy.context.object.modifiers["Displace Loop It"].show_expanded = False
        
#        def errmsg(message = "", title = "Message Box", icon = 'INFO'):

#            def draw(self, context):
#                self.layout.label(text=message)

#            bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

#        if bpy.context.active_object is None:
#            errmsg("No Active Object", "Uh Oh!", 'ERROR')
#        else:
#            randomesh(rmp.iterations)
        
        # Renaming Object to original name & jump back to user frame

        active_object_displace.name = original_object.name
        bpy.context.scene.frame_set(actual_frame_user)
#        original_object.name = active_object_displace.name
        
        print(original_object.name)
        
        return{'FINISHED'}

class DISPLACEMENT_SUB_KEYFRAMES(bpy.types.Operator):
    """Update Settings (Keyframes)"""
    bl_idname = "loop.displacement_keyframes"
    bl_label = "Update Settings"
        
    def execute(self, context):
        
        
        user_props = bpy.context.scene.loop_it_ui
        amount = user_props.displace_amount
        
        # Saving actual frame
        
        actual_frame_user = bpy.context.scene.frame_current
        
        # Keyframing Empty to loop
        
        bpy.ops.screen.frame_jump(end=False)
        bpy.context.object.constraints["Follow Path Loop It"].offset = 0
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        bpy.data.scenes['Scene'].frame_end += 1
        bpy.ops.screen.frame_jump(end=True)
        bpy.context.object.constraints["Follow Path Loop It"].offset = 100 * amount
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        bpy.data.scenes['Scene'].frame_end -= 1
        bpy.context.scene.frame_set(actual_frame_user)
        
        # Change keyframe interpolation mode to "Linear"
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.graph.interpolation_type(type='LINEAR')
#        bpy.ops.graph.fmodifier_add(type='CYCLES')

#        bpy.data.actions["Empty DisplacementAction.005"].(null) = 'REPEAT_OFFSET'
        bpy.context.area.ui_type = 'VIEW_3D'

        return{'FINISHED'}

class DISPLACEMENT_SUB_UPDATE_TIMELINE(bpy.types.Operator):
    """Update User Pref Timeline"""
    bl_idname = "loop.displacement_timeline"
    bl_label = "Displace"
        
    def execute(self, context):
        
        # Saving original object and making Empty Displacement active object
        
        original_object = bpy.context.active_object
        bpy.ops.object.select_all(False)
        bpy.data.objects['Empty Displacement'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Empty Displacement']
        
        # Deleting all keyframes
        
        bpy.context.area.ui_type = 'TIMELINE'
        bpy.ops.action.select_all(action='SELECT')
        bpy.ops.action.delete()
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Update Timeline keyframes
        
        bpy.ops.loop.displacement_keyframes()
        
        # Making Object from beginning active again
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object
        
        return{'FINISHED'}

class DISPLACEMENT_FLIP(bpy.types.Operator):
    """Flip keyframes"""
    bl_idname = "loop.displacement_flip"
    bl_label = "Changing direction of displacement movement"
    
    def execute(self, context):
        
        # Saving original object & settings and making "Empty Displacement" active object
        
        original_object = bpy.context.active_object
        bpy.ops.object.select_all(False)
        bpy.data.objects['Empty Displacement'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Empty Displacement']
        
        # Flipping F-Curve
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.transform.resize(value=(1, -1, 1))
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Making Object from beginning active again & jump back to user timeline
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object
        
        return{'FINISHED'}

class TEXTURE_ADD_NODES(bpy.types.Operator):
    """Adding Nodes to loop Textures"""
    bl_idname = "loop.texture_add_nodes"
    bl_label = "Texture Coordinate"
        
    def execute(self, context):
        
        user_props = bpy.context.scene.loop_it_ui
        amount = user_props.texture_amount
        
        # from https://www.youtube.com/watch?v=zYi5JPmMG3w
        # Creating new material and enable use nodes
        
        loop_tex = bpy.data.materials.new(name = "Loop Texture")
        loop_tex.use_nodes = True
        
        # Creating reference to Principled BSDF Shader
        
        princ_shader = loop_tex.node_tree.nodes.get("Principled BSDF")
        print(princ_shader)
        
        # Deselecting nodes
        
#        bpy.context.area.ui_type = 'ShaderNodeTree'
#        bpy.ops.node.select_all(action='DESELECT')
#        bpy.context.area.ui_type = 'VIEW_3D'
        
#        if update_texture_coord_settings == False:
        
        # Adding Nodes and position them
        
        tex_coord_node = loop_tex.node_tree.nodes.new(type="ShaderNodeTexCoord")
        tex_coord_node.location = (-600, 200)
        mapping_node = loop_tex.node_tree.nodes.new(type="ShaderNodeMapping")
        mapping_node.name = "Mapping Loop It"
        mapping_node.location = (-400, 200)
        viewer_node = loop_tex.node_tree.nodes.new(type="ShaderNodeEmission")
        viewer_node.location = (300, 400)
        
        # from addon Node Wrangler
        
        viewer_node.hide = True
        viewer_node.label = "Viewer"
        viewer_node.name = "Emission Viewer"
        viewer_node.use_custom_color = True
        viewer_node.color = (0.6, 0.5, 0.4)
        viewer_node.select = False
        
        # Adding Texture Node according to user preferences
        
        tex_user_pref = loop_tex.node_tree.nodes.new(type=user_props.loop_tex_coord_node)
        tex_user_pref.location = (-200, 200)
        
        # Link nodes
        
        loop_tex.node_tree.links.new(tex_coord_node.outputs[3], mapping_node.inputs[0])
        loop_tex.node_tree.links.new(mapping_node.outputs[0], tex_user_pref.inputs[0])
        loop_tex.node_tree.links.new(tex_user_pref.outputs[0], viewer_node.inputs[0])
#        viewer_node.node_tree.links.new(tex_user_pref.outputs[0], .inputs[0])

        # Adding new material to active object
        
        bpy.context.object.active_material = loop_tex
        
        # Inserting start frame keyframes
        
        bpy.ops.screen.frame_jump(end=False)
        
        if user_props.tex_coord_axis == 'X_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)

        elif user_props.tex_coord_axis == 'Y_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
        
        elif user_props.tex_coord_axis == 'Z_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'XY_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
        
        elif user_props.tex_coord_axis == 'XZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'YZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'XYZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        # Applying user preferences
        
        if user_props.tex_coord_axis == 'X_AXIS':
            mapping_node.inputs[2].default_value = (2 * math.pi * amount, 0, 0)
            
        elif user_props.tex_coord_axis == 'Y_AXIS':
            mapping_node.inputs[2].default_value = (0, 2 * math.pi * amount, 0)
        
        elif user_props.tex_coord_axis == 'Z_AXIS':
            mapping_node.inputs[2].default_value = (0, 0, 2 * math.pi * amount)
        
        elif user_props.tex_coord_axis == 'XY_AXIS':
            mapping_node.inputs[2].default_value = (2 * math.pi * amount, 2 * math.pi * amount, 0)
        
        elif user_props.tex_coord_axis == 'XZ_AXIS':
            mapping_node.inputs[2].default_value = (2 * math.pi * amount, 0, 2 * math.pi * amount)
        
        elif user_props.tex_coord_axis == 'YZ_AXIS':
            mapping_node.inputs[2].default_value = (0, 2 * math.pi * amount, 2 * math.pi * amount)
        
        elif user_props.tex_coord_axis == 'XYZ_AXIS':
            mapping_node.inputs[2].default_value = (2 * math.pi * amount, 2 * math.pi, 2 * math.pi * amount)
        
        # Setting End Frame one after User Settings (for perfect loop)
        
        bpy.data.scenes['Scene'].frame_end += 1
        
        # Inserting end frame keyframes
        
        bpy.ops.screen.frame_jump(end=True)
        
        if user_props.tex_coord_axis == 'X_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)

        elif user_props.tex_coord_axis == 'Y_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
        
        elif user_props.tex_coord_axis == 'Z_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'XY_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
        
        elif user_props.tex_coord_axis == 'XZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'YZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)
        
        elif user_props.tex_coord_axis == 'XYZ_AXIS':
            mapping_node.inputs[2].keyframe_insert("default_value", 0)
            mapping_node.inputs[2].keyframe_insert("default_value", 1)
            mapping_node.inputs[2].keyframe_insert("default_value", 2)     
        
        # Setting End Frame back to User Settings & jump to Start Frame
        
        bpy.data.scenes['Scene'].frame_end -= 1
        bpy.ops.screen.frame_jump(end=False)
        
        # Change keyframe interpolation mode to "Linear"
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.graph.interpolation_type(type='LINEAR')
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Deleting keyframes
        
#        bpy.data.objects['Sphere'].material_slots['Loop Texture.002'].keyframe_delete(      
        
        # Calling Loop Nodes Class
        
#        bpy.ops.loop.texture_loop_nodes()
        
        return{'FINISHED'}

class TEXTURE_LOOP_NODES(bpy.types.Operator):
    """Loop Textures"""
    bl_idname = "loop.texture_loop_nodes"
    bl_label = "Texture Coordinate"
        
    def execute(self, context):
        
        # Looping Texture Coordinate Node
        
        bpy.ops.screen.frame_jump(end=False)
        
        # Inserting keyframes 
        
        mapping_node.inputs[2].default_value = (2 * math.pi, 0, 0)
        mapping_node.inputs[2].keyframe_insert("default_value", 0, frame = 1)
        
        return{'FINISHED'}

class OCEAN(bpy.types.Operator):
    """Loop Ocean Modifier"""
    bl_idname = "loop.ocean"
    bl_label = "Ocean"
    
    def execute(self, context):
        
        user_props = bpy.context.scene.loop_it_ui
        
        # Saving actual frame
        
        actual_frame_user = bpy.context.scene.frame_current
        
        # User Pref references
        
        ocean_speed = bpy.data.scenes['Scene'].loop_it_ui.ocean_speed
        ocean_frames = bpy.data.scenes['Scene'].frame_end 
        ocean_fps = bpy.data.scenes['Scene'].render.fps
        ocean_speed_seconds = (ocean_speed * ocean_frames) / ocean_fps       

        ocean_scale = bpy.data.scenes['Scene'].loop_it_ui.ocean_scale
        
#        print(ocean_speed_seconds)
        
        # Stopping Play Animation (for update uses, otherwise it won't work)
            
        bpy.ops.screen.animation_cancel()
        
        # Adding Plane
        
#        if user_props.update_ocean_settings == False:
        
        if bpy.data.objects.get("Ocean Loop It") is None:
            bpy.ops.mesh.primitive_plane_add()        
            active_object_ocean = bpy.context.active_object
            active_object_ocean.name = "Ocean Loop It"        
                
        # First Ocean Modifier
           
#        if user_props.update_ocean_settings == False: # Checkbox
        
        if bpy.data.objects.get("Ocean Loop It") is None:  
            bpy.ops.object.modifier_add(type='OCEAN')
            bpy.data.objects["Ocean Loop It"].modifiers["Ocean"].name = "Ocean Loop It"
        
        else:
            
            # Deleting all keyframes
            
            bpy.context.area.ui_type = 'TIMELINE'
            bpy.ops.action.select_all(action='SELECT')
            bpy.ops.action.delete()
            bpy.context.area.ui_type = 'VIEW_3D'
        
        # Setting end frame ONE AFTER user settings (for perfect loop)
        
        bpy.data.scenes['Scene'].frame_end += 1
        
        # Insert keyframes to loop
        
        bpy.ops.screen.frame_jump(end=False) 
        bpy.context.object.modifiers["Ocean Loop It"].frame_end = bpy.data.scenes['Scene'].frame_end
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It"].time = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It"].time')  
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It"].wave_scale = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It"].wave_scale')
        
        
        bpy.ops.screen.frame_jump(end=True)
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It"].time = ocean_speed
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It"].time')
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It"].wave_scale = ocean_scale
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It"].wave_scale')
#        bpy.context.object.modifiers["Ocean Loop It"].show_expanded = False
        
        
        # Second Ocean Modifier
        
#        if user_props.update_ocean_settings == True: # Checkbox

        if bpy.data.objects.get("Ocean Loop It") is not None:
            bpy.ops.object.modifier_remove(modifier="Ocean Loop It.001")
    
        bpy.ops.object.modifier_copy(modifier="Ocean Loop It")
        
        # Insert keyframes to loop
        
        bpy.ops.screen.frame_jump(end=False)
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean"].name = "Ocean Loop It.001"
        bpy.context.object.modifiers["Ocean Loop It.001"].geometry_mode = 'DISPLACE'
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It.001"].time = ocean_speed
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It.001"].time')
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It.001"].wave_scale = ocean_scale
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It.001"].wave_scale')
        
        bpy.ops.screen.frame_jump(end=True)
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It.001"].time = ocean_speed * 2
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It.001"].time')
        bpy.data.objects["Ocean Loop It"].modifiers["Ocean Loop It.001"].wave_scale = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean Loop It.001"].wave_scale')
        bpy.context.object.modifiers["Ocean Loop It.001"].show_expanded = False
        
        # Setting end frame back to user settings & jump back to user frame
        
        bpy.data.scenes['Scene'].frame_end -= 1
        bpy.context.scene.frame_set(actual_frame_user)  
        
        #change keyframe interpolation mode to "Linear"
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.graph.interpolation_type(type='LINEAR')
        bpy.context.area.ui_type = 'VIEW_3D'
#        bpy.ops.graph.fmodifier_add(type='CYCLES')
#        bpy.data.actions["PlaneAction.015"].(mode_before) = 'REPEAT_OFFSET'
        
        # Starting animation again
        
#        bpy.ops.screen.animation_play():

        return{'FINISHED'}

class CREATE_FLAG(bpy.types.Operator):
    """Loop Cloth Modifier"""
    bl_idname = "create.flag"
    bl_label = "Create Flag"

    def execute(self, context):
        
        # Enable addon needed (Export Pointcache Format)
        
        bpy.ops.preferences.addon_enable(module="io_export_pc2")
         
        # Add Wind Force Field
        
        bpy.ops.object.effector_add(type='WIND', enter_editmode=False, align='WORLD', location=(-2, 0, 0))
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Y')
        bpy.context.object.field.strength = 1000
        
        # Add Turbulance Force Field
        
        bpy.ops.object.effector_add(type='TURBULENCE', enter_editmode=False, align='WORLD', location=(-4, 0, 0))
        bpy.context.object.field.strength = 100

        # Adding single Vertex to create Plane with Vertex Group to pin
        
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.transform.translate(value=(0, 0, -2))
        
        # Extruding single Vertex and subdivide it
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 4), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.subdivide(number_cuts=18)

        
        # Assigning to Vertex Groups (later used to pin cloth)
        
        bpy.ops.object.vertex_group_add()
        bpy.ops.object.vertex_group_assign()
#        bpy.context.object.active_index = 0
#        bpy.context.object.name = "Pin"
        
        # Extruding Vertecies to a second row
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0.21053, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        
        # Removing new extruded Vertecies from Vertex Group
        
        bpy.ops.object.vertex_group_remove_from()
        
        # Extruding Vertecies to a Plane (not in Vertex Group anymore)
        
        for i in range(18):
            bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0.21053, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

        bpy.ops.object.editmode_toggle()
        bpy.ops.object.shade_smooth()

#        bpy.data.objects['Vert'].VertexGroups.active_index = "pin"

        # Adding Cloth Modifier and pin Vertex Group

        bpy.ops.object.modifier_add(type='CLOTH')
        bpy.context.object.modifiers["Cloth"].settings.vertex_group_mass = "Group"
        bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True


        return{'FINISHED'}

# from https://blender.stackexchange.com/questions/6249/setting-the-context-for-cloth-bake

class BAKE_FLAG(bpy.types.Operator):
    """Bake Flag"""
    bl_idname = "bake.flag"
    bl_label = "Bake"

    def execute(self, context):
        
        
        for scene in bpy.data.scenes:
            for object in scene.objects:
                for modifier in object.modifiers:
                    if modifier.type == 'CLOTH':
                        override = {'scene': scene, 'active_object': object, 'point_cache': modifier.point_cache}
                        bpy.ops.ptcache.bake(override, bake=True)
                        break

        return{'FINISHED'}
    

class DELETE_BAKE_FLAG(bpy.types.Operator):
    """Bake Flag"""
    bl_idname = "delete_bake.flag"
    bl_label = "Delete Bake"

    def execute(self, context):
        
        
        for scene in bpy.data.scenes:
            for object in scene.objects:
                for modifier in object.modifiers:
                    if modifier.type == 'CLOTH':
                        override = {'scene': scene, 'active_object': object, 'point_cache': modifier.point_cache}
                        bpy.ops.ptcache.bake(override, bake=True)
                        break   

class EXPORT_FLAG(bpy.types.Operator):
    """Export Flag to Pointcache"""
    bl_idname = "export.flag"
    bl_label = "Export Flag"

#        bpy.context.area.ui_type = 'FILE_BROWSER'
#        
#        bpy.data.screens['Scripting']['id_keys']
#        bpy.ops.export_shape.pc2(filepath="", check_existing=True, rot_x90=False, world_space=False, apply_modifiers=True, range_start=1, range_end=250, sampling='1')
#        
#        bpy.context.area.ui_type = 'FILE_BROWSER'
#        bpy.context.space_data.recent_folders_active = 0


###        bpy.ops.file.execute()
##        bpy.context.area.ui_type = 'VIEW_3D'

#            return{'FINISHED'}
    
class LOOP_FLAG(bpy.types.Operator):
    """Loop Flag"""
    bl_idname = "loop.flag"
    bl_label = "Loop Flag"

    def execute(self, context):
        
            # Dublicate Flag       
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
#        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
#        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        # Remove Cloth Modifier & add 3 Mesh Cache Modifiers

        bpy.ops.object.modifier_remove(modifier="Cloth")
        bpy.ops.object.modifier_add(type='MESH_CACHE')
        bpy.context.object.modifiers["Mesh Cache"].cache_format = 'PC2'
        
        bpy.context.object.modifiers["Mesh Cache"].frame_start = -251
        start_frame = bpy.ops.screen.frame_jump(end=False)
        bpy.data.objects["Vert.001"].modifiers["Mesh Cache"].factor = 1
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache"].factor')
        
        bpy.context.object.modifiers["Mesh Cache"].flip_axis = {'Z'}
        bpy.context.object.modifiers["Mesh Cache"].forward_axis = 'NEG_Z'
        bpy.context.object.modifiers["Mesh Cache"].up_axis = 'POS_Y'
    
        bpy.data.scenes["Scene"].frame_end = 125
        bpy.ops.screen.frame_jump(end=True)
        bpy.context.object.modifiers["Mesh Cache"].factor = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache"].factor')
        
#        bpy.context.object.modifiers["Mesh Cache.001"].show_viewport = False
#        bpy.data.objects["Plane"].modifiers["Ocean"].time = 10
#        bpy.context.object.keyframe_insert(data_path='modifiers["Ocean"].time')    

        bpy.ops.object.modifier_copy(modifier="Mesh Cache")
        bpy.ops.object.modifier_copy(modifier="Mesh Cache.001")
        bpy.context.object.modifiers["Mesh Cache.001"].factor = 1
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache.001"].factor')
        bpy.ops.screen.frame_jump(end=False)
            
#        start_frame = bpy.ops.screen.frame_jump(end=False)
        bpy.context.object.modifiers["Mesh Cache.001"].factor = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache.001"].factor')
        
        bpy.data.scenes["Scene"].frame_end = 250
        bpy.ops.screen.frame_jump(end=True)
        
        bpy.context.object.modifiers["Mesh Cache.001"].factor = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache.001"].factor')
        
        bpy.context.object.modifiers["Mesh Cache.002"].frame_start = 0
        
        bpy.data.scenes["Scene"].frame_end = 125
        bpy.ops.screen.frame_jump(end=True)
        bpy.context.object.modifiers["Mesh Cache.002"].factor = 0
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache.002"].factor')
        bpy.data.scenes["Scene"].frame_end = 250
        bpy.ops.screen.frame_jump(end=True)
        bpy.context.object.modifiers["Mesh Cache.002"].factor = 1
        bpy.context.object.keyframe_insert(data_path='modifiers["Mesh Cache.002"].factor')

#        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return{'FINISHED'}

#class CAMERA_TURNAROUND_USER_SETTINGS(bpy.types.Operator):
#    """Camera turn around user settings"""
#    bl_idname = "camera.turnaround_user_settings"
#    bl_label = "Turnaround"

#    def execute(self, context):
#        
#        user_props = bpy.context.scene.loop_it_ui
#        
#        if user_props.camera_update_turnaround_frame == False:
#            bpy.ops.camera.turnaround_execute()
#        
#        else:
#            bpy.ops.camera.turnaround_keyframes()
#        
#        return{'FINISHED'}

class CAMERA_TURNAROUND(bpy.types.Operator):
    """Camera turn around an Object"""
    bl_idname = "camera.turnaround_execute"
    bl_label = "Turnaround"

    def execute(self, context):
        
        # User Preferences
        
        user_props = bpy.context.scene.loop_it_ui
        
#         if bpy.data.objects['Cirircle Turn'] in bpy.context.scene.collection.all_objects:
#             print("Yep")
#             
#             pass
         
#        if bpy.data.objects['Cube'] != None:
#            
#            print("Nein")
#            
#            pass
        
        # Saving active object name and renaming
        
        original_object = bpy.context.active_object
        original_object_name = bpy.context.active_object.name
        active_object_turnaround = bpy.context.active_object
        active_object_turnaround.name = "active_object_turnaround"
        location_original_object = active_object_turnaround.location
        
#        print(original_name_object)
#        print(location_original_object)

#        # Adding Empty to use for Constaints (used for UI Settings)
#        
#        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
#        empty_constraint = bpy.context.active_object
#        empty_constraint.name = "Empty Constraint UI"
#        empty_constraint.location = location_original_object
#        bpy.ops.transform.resize(value=(8, 8, 8), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        # Adding Bezier Circle, saving original name,
        # position to original object and scaling up circle
        
        bpy.ops.curve.primitive_bezier_circle_add()
        active_object_bezier_circle = bpy.context.active_object
        active_object_bezier_circle.name = "Circle Turn" # + original_object_name
        active_object_bezier_circle.location = location_original_object
#        bpy.ops.transform.rotate(value=3.14159, orient_axis='Z')
        bpy.ops.transform.resize(value=(9, 9, 9))
        
#        # Adding Constraints for using in UI
#        
#        bpy.ops.object.constraint_add(type='COPY_LOCATION')
#        bpy.context.object.constraints["Copy Location"].name = "Copy Location Loop It"
#        bpy.context.object.constraints["Copy Location Loop It"].target = bpy.data.objects["Empty Constraint UI"]
#        bpy.context.object.constraints["Copy Location Loop It"].show_expanded = False

#        bpy.ops.object.constraint_add(type='COPY_SCALE')
#        bpy.context.object.constraints["Copy Scale"].name = "Copy Scale Loop It"
#        bpy.context.object.constraints["Copy Scale Loop It"].target = bpy.data.objects["Empty Constraint UI"]
#        bpy.context.object.constraints["Copy Scale Loop It"].show_expanded = False
        
        # Drivers
        # from https://blender.stackexchange.com/questions/21474/how-to-add-a-driver-via-python
        # and from https://blender.stackexchange.com/questions/76633/getting-bpy-ops-anim-copy-driver-button-working
        
#        driver_scale_y = bpy.context.object.driver_add("scale", 1)
        
#        # References for adding Drivers
#        
#        circle_turn_drivers = bpy.data.objects['Circle Turn']
#        driver001 = circle_turn_drivers.animation_data.drivers
#        
#
#        dr1[0].data_path
#        # This returns 'scale'

#        dr1[0].expression
#        # This simply returns my expression 'var', because I am using a 1:1 mapping of another object's scale factor

#        dr1[0].driver.variables[0].name
#        # This returns the first (and only in this case) variable that I have named in this driver 'var'

#        dr1[0].driver.variables.items()[0][1].targets.items()[0][1].transform_type
#        # Returns 'SCALE_X'

#        dr1[0].driver.variables.items()[0][1].targets.items()[0][1].transform_space
#        # Returns 'WORLD_SPACE'
        
        
#        bpy.ops.ui.copy_as_driver_button()

        
#        circle_turn_scale_x = bpy.data.objects['Circle Turn'].scale[0]
#        bpy.ops.ui.copy_as_driver_button()

        # Saving Bezier Circle name and renaming
              
        original_name_circle = bpy.context.active_object.name
        circle_turnaround = bpy.context.active_object
        circle_turnaround.name = "circle_turnaround"

        # Adding camera
        
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(0, 0, 0))
        bpy.context.active_object.name = "Camera Turn"
        bpy.data.scenes['Scene'].camera = bpy.context.active_object
        
        # Adding "Follow Path" Constraint and set target to BezierCirlce
        
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        bpy.context.object.constraints["Follow Path"].name = "Follow Path Loop It"
        bpy.context.object.constraints["Follow Path Loop It"].target = bpy.data.objects["circle_turnaround"]
        bpy.context.object.constraints["Follow Path Loop It"].show_expanded = False
              
        # Insert looping keyframes according user pref "Return" checkbox
        
        if user_props.camera_turnaround_return == False:
            bpy.ops.camera.turnaround_keyframes()
            
        else:
            bpy.ops.camera.turnaround_keyframes_return()
        
        # Adding "Track To" Constraint and set target to Active Object
        # and adjusting "To" & "Up" Values
        
        bpy.ops.object.constraint_add(type='TRACK_TO')
        bpy.context.object.constraints["Track To"].name = "Track To Loop It"
        bpy.context.object.constraints["Track To Loop It"].target = bpy.data.objects["active_object_turnaround"]
        bpy.context.object.constraints["Track To Loop It"].up_axis = 'UP_Y'
        bpy.context.object.constraints["Track To Loop It"].track_axis = 'TRACK_NEGATIVE_Z'
        bpy.context.object.constraints["Track To Loop It"].show_expanded = False
        
        # Renaming to original names
        
        active_object_turnaround.name = original_object_name
        circle_turnaround.name = original_name_circle

        # Making Object from beginning active again
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object 
       
        return{'FINISHED'}
 
class CAMERA_TURNAROUND_SUB_KEYFRAMES(bpy.types.Operator):
    """Camera turn insert keyframes to loop"""
    bl_idname = "camera.turnaround_keyframes"
    bl_label = "Turnaround"
    
    def execute(self, context):
        
        # User Preferences Angle & Offset (& Interpolation)
        
        user_props = bpy.context.scene.loop_it_ui        
        user_pref_angle = user_props.camera_turn_angle
        user_pref_offset = user_props.camera_turn_offset
#        user_pref_interpolation = user_props.camera_turn_interpolation
#        user_pref_return = user_props.camera_turn_return
        
        # Saving actual & end frame
        
        actual_frame_user = bpy.context.scene.frame_current
        frame_end_user = bpy.context.scene.frame_end
        
        # Clamping user pref "Offset" to endframe
        
        if user_pref_offset > frame_end_user:
            user_pref_offset = frame_end_user
        
        # Saving original object and making Empty Displacement active object
        
        original_object = bpy.context.active_object
        bpy.ops.object.select_all(False)
        bpy.data.objects['Camera Turn'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Camera Turn']
        
        # Deleting all old keyframes of 
        
        bpy.context.area.ui_type = 'TIMELINE'
        bpy.ops.action.select_all(action='SELECT')
        bpy.ops.action.delete()
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Calculating correct offset of "Follow Path Loop It" constraint
        
        constraint_offset = 100 * user_pref_angle / 360
        first_offset = - constraint_offset / 2
        second_offset = constraint_offset / 2
        
        # Setting end frame one after user settings
        # (for perfect loop if user pref angle = 360 & offset = 0)
        
        if user_pref_offset == 0 or user_pref_offset == frame_end_user:
            bpy.data.scenes['Scene'].frame_end += 1
        
        # Jump to first keyframe position according user pref
        
        first_keyframe = bpy.ops.screen.frame_jump(end=False)
        
        if user_pref_angle == 360 and user_pref_offset == 0:
           first_keyframe = bpy.context.scene.frame_current + user_pref_offset
           
        else:
            first_keyframe = bpy.context.scene.frame_current + user_pref_offset -1        
        bpy.context.scene.frame_set(first_keyframe)
        
        # Adding first keyframe
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.context.object.constraints["Follow Path Loop It"].offset = 0
            
        else:
            bpy.context.object.constraints["Follow Path Loop It"].offset = first_offset
            
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        
        # Jump to second keyframe position according user pref
        
        second_keyframe = bpy.ops.screen.frame_jump(end=True)
        second_keyframe = bpy.context.scene.frame_current - user_pref_offset
        bpy.context.scene.frame_set(second_keyframe)
        
        # Adding second keyframe
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.context.object.constraints["Follow Path Loop It"].offset = 100
            
        else:
            bpy.context.object.constraints["Follow Path Loop It"].offset = second_offset
            
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        
        # Setting end frame back to user settings & jump back to user frame
        
        if user_pref_offset == 0 or user_pref_offset == frame_end_user:
            bpy.data.scenes['Scene'].frame_end -= 1
            
        bpy.context.scene.frame_set(actual_frame_user)   
#        bpy.ops.screen.frame_jump(end=False)
        
        # Change keyframe interpolation mode according user pref
        
        bpy.context.area.ui_type = 'FCURVES'
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.ops.graph.interpolation_type(type='LINEAR')
            
        else:
            bpy.ops.graph.interpolation_type(type='BEZIER')
            
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Making Object from beginning active again
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object
        
        return{'FINISHED'}

class CAMERA_TURNAROUND_SUB_KEYFRAMES_RETURN(bpy.types.Operator):
    """Camera turn insert keyframes to loop return"""
    bl_idname = "camera.turnaround_keyframes_return"
    bl_label = "Turnaround"
    
    def execute(self, context):
        
        # User Preferences Angle & Offset (& Interpolation)
        
        user_props = bpy.context.scene.loop_it_ui        
        user_pref_angle = user_props.camera_turn_angle
        user_pref_offset = user_props.camera_turn_offset
#        user_pref_interpolation = user_props.camera_turn_interpolation
        
        # Saving actual & end frame
        
        actual_frame_user = bpy.context.scene.frame_current
        frame_end_user = bpy.context.scene.frame_end
        
        # Clamping user pref "Offset" to endframe
        
        if user_pref_offset > frame_end_user:
            user_pref_offset = frame_end_user
        
        # Saving original object and making "Camera Turn" active object
        
        original_object = bpy.context.active_object
        bpy.ops.object.select_all(False)
        bpy.data.objects['Camera Turn'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Camera Turn']
        
        # Deleting all old keyframes of 
        
        bpy.context.area.ui_type = 'TIMELINE'
        bpy.ops.action.select_all(action='SELECT')
        bpy.ops.action.delete()
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Calculating correct offset of "Follow Path Loop It" constraint
        
        constraint_offset = 100 * user_pref_angle / 360
        first_offset = - constraint_offset / 2
        second_offset = constraint_offset / 2
        third_offset = first_offset
        
        # Jump to first keyframe position according user pref
        
        first_keyframe = bpy.ops.screen.frame_jump(end=False)
        
        # TODO:
        
        if user_pref_angle == 360 and user_pref_offset == 0:
           first_keyframe = bpy.context.scene.frame_current + user_pref_offset
           
        else:
            first_keyframe = bpy.context.scene.frame_current + user_pref_offset -1        
        
        bpy.context.scene.frame_set(first_keyframe)
        
        # Adding first keyframe
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.context.object.constraints["Follow Path Loop It"].offset = 0
            
        else:
            bpy.context.object.constraints["Follow Path Loop It"].offset = first_offset
            
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        
        # Jump to second keyframe position according user pref
        
        second_keyframe = bpy.context.scene.frame_end / 2
        bpy.context.scene.frame_set(second_keyframe)
        
        # Adding second keyframe
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.context.object.constraints["Follow Path Loop It"].offset = 100
            
        else:
            bpy.context.object.constraints["Follow Path Loop It"].offset = second_offset
            
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        
        # Jump to third keyframe position according user pref
        
        third_keyframe = bpy.ops.screen.frame_jump(end=True)
        third_keyframe = bpy.context.scene.frame_current - user_pref_offset
        bpy.context.scene.frame_set(third_keyframe)
        
        # Adding third keyframe
        
        if user_pref_angle == 360 and user_pref_offset == 0:
            bpy.context.object.constraints["Follow Path Loop It"].offset = 0
            
        else:
            bpy.context.object.constraints["Follow Path Loop It"].offset = third_offset
            
        bpy.context.object.keyframe_insert(data_path='constraints["Follow Path Loop It"].offset')
        
        # Setting end frame back to user settings & jump back to user frame
        
#        if user_pref_offset == 0 or user_pref_offset == frame_end_user:
#            bpy.data.scenes['Scene'].frame_end -= 1
            
        bpy.context.scene.frame_set(actual_frame_user)   
#        bpy.ops.screen.frame_jump(end=False)
        
        # Change keyframe interpolation mode according user pref
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.graph.interpolation_type(type='BEZIER')
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Making Object from beginning active again
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object
        
        return{'FINISHED'}

class CAMERA_TURNAROUND_REFRESH(bpy.types.Operator):
    """Refresh camera turn"""
    bl_idname = "camera.turnaround_refresh"
    bl_label = "Refresh"
    
    def execute(self, context):
        
        # User Preferences Angle & Offset (& Interpolation)
        
        user_props = bpy.context.scene.loop_it_ui
        
        if user_props.camera_turnaround_return == False:
            bpy.ops.camera.turnaround_keyframes()
            
        else:
            bpy.ops.camera.turnaround_keyframes_return()
        
        return{'FINISHED'} 

class CAMERA_TURNAROUND_FLIP(bpy.types.Operator):
    """Flip keyframes"""
    bl_idname = "camera.turnaround_flip"
    bl_label = "Changing direction of camera movement"
    
    def execute(self, context):
        
        # Saving original object & settings and making "Camera Turn" active object
        
        original_object = bpy.context.active_object
        bpy.ops.object.select_all(False)
        bpy.data.objects['Camera Turn'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Camera Turn']
        
        # Flipping F-Curve
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.transform.resize(value=(1, -1, 1))
        bpy.context.area.ui_type = 'VIEW_3D'
        
        # Making Object from beginning active again & jump back to user timeline
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object
        
        return{'FINISHED'} 

class CAMERA_TURNAROUND_DELETE(bpy.types.Operator):
    """Delete camera turn"""
    bl_idname = "camera.turnaround_delete"
    bl_label = "Deleting Camera Turn and Circle Turn"
    
    def execute(self, context):
        
        # Saving original object
        
#        original_object = bpy.context.active_object
        
        if bpy.data.objects.get('Camera Turn') is not None:

            bpy.ops.object.select_all(False)
            bpy.data.objects['Camera Turn'].select_set(True)
            context.view_layer.objects.active = bpy.data.objects['Camera Turn']
#            print(context.view_layer.objects.active)
            bpy.ops.object.delete(use_global=False)
        
#        if bpy.data.objects.get('Circle Turn') is not None:
#            
#            bpy.ops.object.select_all(False)
#            bpy.data.objects['Circle Turn'].select_set(True)
#            context.view_layer.objects.active = bpy.data.objects['Circle Turn']
#            print(context.view_layer.objects.active)
#            bpy.ops.object.delete(use_global=False)
        
#        else:
#            pass
        
#        if original_object != bpy.data.objects['Camera Turn']:

#            # Making Object from beginning active again
#            
#            bpy.ops.object.select_all(False)
#            original_object.select_set(True)
#            context.view_layer.objects.active = original_object
#        
#        if original_object != bpy.data.objects['Circle Turn']:

#            # Making Object from beginning active again
#            
#            bpy.ops.object.select_all(False)
#            original_object.select_set(True)
#            context.view_layer.objects.active = original_object
#        
        return{'FINISHED'}

class CAMERA_ARRAY(bpy.types.Operator):
    """Loop Camera Straight to Array Modifier"""
    bl_idname = "camera.array"
    bl_label = "Array"

    def execute(self, context):
        
        # User Preferences
        
        user_props = bpy.context.scene.loop_it_ui
        
        # Saving original properties
        # and renaming active object for later use
        
        original_object = bpy.context.active_object
        original_name_object = bpy.context.active_object.name
        bpy.context.active_object.name = "object_modifier_add"
        
        # Checking rotation (180° & 360°)
        
        rot_x = bpy.context.object.rotation_euler[0] / math.pi
        rot_y = bpy.context.object.rotation_euler[1] / math.pi
        rot_z = bpy.context.object.rotation_euler[2] / math.pi
        
        rot_x = round(rot_x, 2)
        rot_y = round(rot_y, 2)
        rot_z = round(rot_z, 2)
        
        print("X Axis:", rot_x)
        print("Y Axis:", rot_y)
        print("Z Axis:", rot_z)
         
        if (rot_x % 2) == 0:
            print('X: Even')
        else:
            print('X: Odd')
        if (rot_y % 2) == 0:
            print('Y: Even')
        else:
            print('Y: Odd')   
        if (rot_z % 2) == 0:
            print('Z: Even')
        else:
            print('Z: Odd')
        print(math.pi)
        
        # Dublicating original object
        # Applying scale (ROTATION ???) to get correct dimension index & renaming
        
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={})
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        loop_array_object = bpy.context.active_object
        loop_array_object.name = "array_object"
        
        # Adding Camera & renaming
        
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(0, 0, 0))
        bpy.context.active_object.name = "Camera Array"
        
        # Rotating Camera
        
        if user_props.camera_array_axis == 'X_AXIS':
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X')
            bpy.ops.transform.rotate(value=-1.5708, orient_axis='Z')
            user_pref_dropdown = 0           
        elif user_props.camera_array_axis == 'Y_AXIS':
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X')
            user_pref_dropdown = 1
        else:
            bpy.ops.transform.rotate(value=3.14159, orient_axis='X')
            user_pref_dropdown = 2
        
        # Positioning camera acording user pref
        
        dimensions_index = bpy.data.objects['array_object'].dimensions[user_pref_dropdown]
        dimensions_index = dimensions_index/2
        bpy.data.objects['Camera Array'].location[user_pref_dropdown] = -dimensions_index
        
        # Setting end frame one after user settings (for perfect loop)
        
        bpy.data.scenes['Scene'].frame_end += 1
        
        # Insert looping keyframes
        
        bpy.ops.screen.frame_jump(end=False)
        bpy.context.object.keyframe_insert('location', index=user_pref_dropdown)
        
        bpy.data.objects['Camera Array'].location[user_pref_dropdown] = dimensions_index
        
        bpy.ops.screen.frame_jump(end=True)
        bpy.context.object.keyframe_insert('location', index=user_pref_dropdown)
        
        # Setting End Frame back to User Settings & jump to Start Frame
        
        bpy.data.scenes['Scene'].frame_end -= 1
        bpy.ops.screen.frame_jump(end=False)
        
        # Change keyframe interpolation mode to "Linear"
        
        bpy.context.area.ui_type = 'FCURVES'
        bpy.ops.graph.interpolation_type(type='LINEAR')
        bpy.context.area.ui_type = 'VIEW_3D'
    
        # Deleting dublicated Object
        
        bpy.ops.object.select_all(False)
        loop_array_object.select_set(True)
        context.view_layer.objects.active = loop_array_object
        bpy.ops.object.delete(use_global=False)

        # Making Object from beginning active again
        
        bpy.ops.object.select_all(False)
        original_object.select_set(True)
        context.view_layer.objects.active = original_object 

        # Adding Mirror Modifier with Empty
        
        if user_props.camera_mirror_array == True:
            
            bpy.ops.object.modifier_add(type='MIRROR')
            bpy.context.object.modifiers["Mirror"].use_axis[0] = False
            bpy.context.object.modifiers["Mirror"].use_axis[user_pref_dropdown] = True
            bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
            empty_mirror = bpy.context.active_object
            empty_mirror.name = "Empty Mirror"
            bpy.data.objects['Empty Mirror'].location[user_pref_dropdown] = dimensions_index
            original_object.select_set(True)
            context.view_layer.objects.active = original_object 
            bpy.context.object.modifiers["Mirror"].mirror_object = bpy.data.objects["Empty Mirror"]
            bpy.context.object.modifiers["Mirror"].show_expanded = False

        # Adding Array Modifiers
        
        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.data.objects['object_modifier_add'].modifiers['Array'].relative_offset_displace[0] = 0
        bpy.data.objects['object_modifier_add'].modifiers['Array'].relative_offset_displace[2] = 1
        bpy.ops.object.modifier_copy(modifier="Array")
        bpy.context.object.modifiers["Array"].show_expanded = False
        
        bpy.data.objects['object_modifier_add'].modifiers['Array.001'].relative_offset_displace[2] = 1
        bpy.context.object.modifiers["Array.001"].count = 5
#        bpy.context.object.modifiers["Array.001"].show_expanded = False

        
#        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        
        # Renaming Object to original name

        original_object.name = original_name_object

        return{'FINISHED'}

class CAMERA_TORUS(bpy.types.Operator):
    """Loop Camera through Torus Object"""
    bl_idname = "camera.torus"
    bl_label = "Torus"

    def execute(self, context):
        pass
    
        return{'FINISHED'}

class ADD_PARTICLES(bpy.types.Operator):
    """Add Particle System"""
    bl_idname = "add.particles"
    bl_label = "Add Particle System"

    def execute(self, context):
        
        bpy.ops.object.particle_system_add()
        

        return{'FINISHED'}

class LOOP_PARTICLES(bpy.types.Operator):
    """Loop Particles"""
    bl_idname = "loop.particles"
    bl_label = "Loop Particles"

    def execute(self, context):
        
#        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))

        
        bpy.context.object.particle_systems["ParticleSettings"].name = "start"
        bpy.data.particles["ParticleSettings"].name = 'start'
        
        
        bpy.ops.particle.duplicate_particle_system(use_duplicate_settings=True)
        

        bpy.context.object.particle_systems["start.001"].name = "end"
        
#        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=True, animation=False)
        
        
#        bpy.context.object.active_index = 1
#        bpy.data.particles["end"].name = 'end'
        

#        bpy.data.particles["start"]


        return{'FINISHED'}

# from https://b3d.interplanety.org/en/creating-pop-up-panels-with-user-ui-in-blender-add-on/

class MessageBox(bpy.types.Operator):
    bl_idname = "message.messagebox"
    bl_label = ""
 
    message = bpy.props.StringProperty(
        name = "No Object selected",
        description = "message",
        default = ''
    )
 
    def execute(self, context):
        self.report({'INFO'}, self.message)
        print(self.message)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 100)
 
    def draw(self, context):
        self.layout.label(self.message)
        self.layout.label("No Object selected")

#################################################################
###              UI Panel in Object Mode                      ###
#################################################################

class VIEW3D_PT_timeline(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Timeline"
    bl_context = "objectmode"
#    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        split = layout.split()
#        col = split.column()
        row = layout.row(align=True)
        
        col = split.column()
        col.label(text= "Start Frame:")
        col = split.column()
        col.label(text="End Frame:")
        
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

class VIEW3D_PT_meshes(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Meshes"
    bl_context = "objectmode"
#    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        
        pass
        
class VIEW3D_PT_mesh_displace(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Displacement"
    bl_parent_id = "VIEW3D_PT_meshes"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        loop_props = scene.loop_it_ui # Properties   

        
#        propname = context.texture_user_property.identifier
#        col.prop(ops.texture.new, "texture.new")

#        col.prop(loop_props, "use_displace_texture")
#        if loop_props.displace_texture == False:
#            row.enabled = False
#            sub.enabled = False

        row = layout.row(align=True)
        row.label(text="Texture:")
        sub = row.row()
        sub.scale_x = 1.5
#        col = split.column()
        sub.prop(loop_props, "displace_texture", text="")
        
        row = layout.row(align=True)
        row.label(text="Amount:")
        sub = row.row()
        sub.scale_x = 1.5
#        col = split.column()
        sub.prop(loop_props, "displace_amount", text="")
        

#        row = layout.row(align=True)
#        row.label(text="Object:")
#        sub = row.row()
#        sub.scale_x = 1.5
#        sub.prop_search(scene, "Meshes", bpy.data, "meshes", text='')
        
#        col = layout.column()
#        col.separator()
#        col.prop(loop_props, "update_displacement_timeline") # Checkbox "Update to Timeline"
        
#        col.prop(loop_props, "new_loop") # Checkbox
     
#        if loop_props.update_displacement_frame == False:
        
#        col = layout.column()
        
        split = layout.split()
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
#        col = split.column()
#        sub.prop(loop_props, "displace_amount", text="")
#        col = layout.column()
        sub.operator('loop.displacement_first', 
        icon='MOD_DISPLACE')
#        sub.operator('loop.displacement_user_settings', 
#        icon='MOD_DISPLACE')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('loop.displacement_keyframes', 
        icon='FILE_REFRESH')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('loop.displacement_flip', 
        icon='ARROW_LEFTRIGHT')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('loop.displacement_user_settings', 
#        icon='X')
        
        
#        col = layout.column()
#        col.operator('loop.displacement_user_settings', 
#        icon='MOD_DISPLACE')

class VIEW3D_PT_mesh_tex_coord_node(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Texture Coordinate Node"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_meshes"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        loop_props = scene.loop_it_ui # Properties
#        split = layout.split()
        
#        col_split = split.column()

#        col = layout.column()
        
#        col.prop(loop_props, "texture_coord_node") # Checkbox "Keep Texture"

#        if loop_props.displace_texture == False:
#            row.enabled = False
#            sub.enabled = False
        
        
        row = layout.row(align=True)
        row.label(text="Texture:")
        sub = row.row()
        sub.scale_x = 1.5
#        split = layout.split()
#        col = split.column()
        sub.prop(loop_props, "loop_tex_coord_node", text="")
        
        row = layout.row(align=True)
        row.label(text="Axis:")
        sub = row.row()
        sub.scale_x = 1.5
#        split = layout.split()
#        col = split.column()
        sub.prop(loop_props, "tex_coord_axis", text="")

        row = layout.row(align=True)
        row.label(text="Amount:")
        sub = row.row()
        sub.scale_x = 1.5
#        split = layout.split()
#        col = split.column()
        sub.prop(loop_props, "texture_amount", text="")
        
        
#        row = layout.row(align=True)
#        row.label(text="Object:")
#        sub = row.row()
#        sub.scale_x = 1.5
#        sub.prop_search(scene, "Meshes", bpy.data, "meshes", text='')

#        col = layout.column()
#        col.separator()
#        col.label(text="Rotation Axis:")   
#        col.prop(loop_props, "tex_coord_axis", text="Axis")
        
#        col = layout.column()
#        row = layout.row()
#        col.separator()
#        col.prop(loop_props, "update_texture_coord_settings") # Checkbox "Update Settings"
#        
        split = layout.split()
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
        sub.operator('loop.texture_add_nodes', 
        icon='SHADING_TEXTURE')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('loop.texture_add_nodes', 
        icon='FILE_REFRESH')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('loop.texture_add_nodes', 
        icon='ARROW_LEFTRIGHT')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('loop.texture_add_nodes', 
#        icon='X')
        
#        col = layout.column()        
#        col.operator('loop.texture_add_nodes', 
#        icon='SHADING_TEXTURE')

class VIEW3D_PT_mesh_ocean(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Ocean"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_meshes"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
#        split = layout.split()
        loop_props = scene.loop_it_ui # My Properties

        split = layout.split()
        
        row = layout.row(align=True)
        row.label(text="Time:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "ocean_speed", text="")
        
        row = layout.row(align=True)
        row.label(text="Scale:")
        sub = row.row()
        sub.scale_x = 1.5
        split = layout.split()
        sub.prop(loop_props, "ocean_scale", text="")
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
        sub.operator('loop.ocean', 
        icon='MOD_OCEAN')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('loop.ocean', 
        icon='FILE_REFRESH')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('loop.texture_add_nodes', 
#        icon='X')

class VIEW3D_PT_mesh_ocean_timeline(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Timeline"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_mesh_ocean"
    
    def draw(self, context):

        layout = self.layout
        scene = context.scene
        split = layout.split()
#        col = split.column()
        row = layout.row(align=True)
        
        col = split.column()
        col.label(text= "Start Frame:")
        col = split.column()
        col.label(text="End Frame:")
        
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

#        split = layout.split()

class VIEW3D_PT_mesh_ocean_time_wave(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Wave Time and Wave Scale"
#    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_mesh_ocean"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
#        split = layout.split()
        loop_props = scene.loop_it_ui # My Properties

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Time:")
        col.prop(loop_props, "ocean_speed", text="")
        
        # Second column, aligned
        col = split.column()
        col.label(text="Wave Scale:")
        col.prop(loop_props, "ocean_scale", text="")

        split = layout.split()


class VIEW3D_PT_mesh_ocean_settings(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Settings"
#    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_mesh_ocean"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        split = layout.split()
#        col = layout.column(align=True)
        col = split.column()
        row = layout.row(align=False)
        
#        row = layout.row(align=True)
#        row.label(text="Time:")
#        sub = row.row()
#        sub.scale_x = 1.5
#        sub.prop(loop_props, "ocean_speed", text="")
#        
#        row = layout.row(align=True)
#        row.label(text="Scale:")
#        sub = row.row()
#        sub.scale_x = 1.5
#        split = layout.split()
#        sub.prop(loop_props, "ocean_scale", text="")
        
        # from https://www.youtube.com/watch?v=HAfE1ygZY-E
        
#        col = split.column()
#        col.label(text= "Start Frame:")
#        col = split.column()
#        col.label(text="End Frame:")
        
#        if (bpy.context.actice_object.modifiers.find('Ocean Loop It') != -1):
#        col = layout.column(align=True)
        col.label(text="Active Ocean Modifier:")
#        col.label(text="Settings:")
        
        row.prop(context.object.modifiers['Ocean Loop It'], "repeat_x")
        row.prop(context.object.modifiers['Ocean Loop It'], "repeat_y")
        
        row = layout.row(align=False)
#        row.enabled = False

        row.prop(context.object.modifiers['Ocean Loop It'], "time")
        row.prop(context.object.modifiers['Ocean Loop It'], "resolution")

        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "depth")
        row.prop(context.object.modifiers['Ocean Loop It'], "size")
        
        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "random_seed")
        row.prop(context.object.modifiers['Ocean Loop It'], "spatial_size")

        col = layout.column(align=True)
#        col.separator()
        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "spectrum")      
#        col = layout.column(align=True)
        
        layout.label(text="Waves:")

        split = layout.split()

        col = split.column()
        col.prop(context.object.modifiers['Ocean Loop It'], "choppiness")
        col.prop(context.object.modifiers['Ocean Loop It'], "wave_scale", text="Scale")
        col.prop(context.object.modifiers['Ocean Loop It'], "wave_scale_min")
        col.prop(context.object.modifiers['Ocean Loop It'], "wind_velocity")

        col = split.column()
        col.prop(context.object.modifiers['Ocean Loop It'], "wave_alignment", text="Alignment")
        sub = col.column()
        sub.active = (context.object.modifiers['Ocean Loop It'].wave_alignment > 0.0)
        sub.prop(context.object.modifiers['Ocean Loop It'], "wave_direction", text="Direction")
        sub.prop(context.object.modifiers['Ocean Loop It'], "damping")
        
#        col.label(text="Waves:")
#        
#        row = layout.row(align=False)
#        row.prop(context.object.modifiers['Ocean Loop It'], "choppiness")
#        row.prop(context.object.modifiers['Ocean Loop It'], "wave_alignment")
#        
#        row = layout.row(align=False)
#        row.prop(context.object.modifiers['Ocean Loop It'], "wave_scale")
#        row.prop(context.object.modifiers['Ocean Loop It'], "wave_direction")
#        
#        row = layout.row(align=False)
#        row.prop(context.object.modifiers['Ocean Loop It'], "wave_scale_min")
#        row.prop(context.object.modifiers['Ocean Loop It'], "damping")
#        
#        row = layout.row(align=False)
#        row.prop(context.object.modifiers['Ocean Loop It'], "wind_velocity")
      
        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "use_normals")

        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "use_foam")

        row = layout.row(align=False)
        row.prop(context.object.modifiers['Ocean Loop It'], "foam_coverage")
        row.prop(context.object.modifiers['Ocean Loop It'], "foam_layer_name")

class VIEW3D_PT_mesh_flag(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Flag (in development)"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_meshes"
    
    def draw(self, context):
        
        col = self.layout.column(align=True)
        scene = context.scene
        loop_props = scene.loop_it_ui
        
        col.enabled = False
        
        col.operator('create.flag',
        icon='MOD_CLOTH')
        
        col.operator('bake.flag')
        
        col.operator('delete_bake.flag')
        
        col.operator('export.flag',
        icon='EXPORT') 

class VIEW3D_PT_loop_camera(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Camera"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
#    bl_icon = "OUTLINER_OB_CAMERA"
    
    def draw(self, context):
        
        pass

class VIEW3D_PT_camera_turn(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Turnaround"
    bl_parent_id = "VIEW3D_PT_loop_camera"

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
#        obj = context.object
        loop_props = scene.loop_it_ui
#        col = layout.column(align=True)
#        row = layout.row(align=True)

        split = layout.split()
        
        row = layout.row(align=True)
        row.label(text="Angle:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "camera_turn_angle", text="")
        
        row = layout.row(align=True)
        row.label(text="Offset:")
        sub = row.row()
        sub.scale_x = 1.5
#        split = layout.split()
        sub.prop(loop_props, "camera_turn_offset", text="")
        
#        row = layout.row(align=True)
#        row.label(text="Interpolation Mode:")
#        sub = row.row()
#        sub.scale_x = 1.5
#        split = layout.split()
#        sub.prop(loop_props, "camera_turn_interpolation", text="")
        
        col = layout.column()
#        row = layout.row()
#        col.separator()
        col.prop(loop_props, "camera_turnaround_return") # Checkbox "Update Settings"
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
        sub.operator('camera.turnaround_execute', 
        icon='CURVE_BEZCIRCLE')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_refresh', 
        icon='FILE_REFRESH')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_flip', 
        icon='ARROW_LEFTRIGHT')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('camera.turnaround_delete', 
#        icon='X')

#        col.prop(loop_props, "camera_update_turnaround_fram") # Checkbox "Update Frames"
        
#        col = layout.column(align=False)
#        col.operator('camera.turnaround_user_settings',
#        icon='CURVE_BEZCIRCLE')       

#class VIEW3D_PT_camera_turn_settings(Panel):
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'UI'
#    bl_category = "Loop It"
#    bl_label = "Settings"
#    bl_options = {'DEFAULT_CLOSED'}
#    bl_parent_id = "VIEW3D_PT_camera_turn"
#    
#    def draw(self, context):
#        
#        layout = self.layout
#        scene = context.scene
#        obj = context.object
#        
#        row = layout.row(align=True)
#        row.label(text="Scale:")
#        sub = row.row()
#        sub.scale_x = 1.25
#        sub.prop(obj, "scale", index = 0, text="")
#        
#        row = layout.row(align=True)
#        row.label(text="Position (Z):")
#        sub = row.row()
#        sub.scale_x = 1.25
#        split = layout.split()
#        sub.prop(obj, "location", index = 2, text = "")
        
class VIEW3D_PT_camera_array(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Array"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_loop_camera"


    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        loop_props = scene.loop_it_ui
        
        row = layout.row(align=True)
        row.label(text="Axis:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "camera_array_axis", text="")
        
        row = layout.row(align=True)
        row.label(text="Speed:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "camera_array_speed", text="")
        
        col = layout.column()
#        row = layout.row()
        col.separator()
        col.prop(loop_props, "camera_mirror_array") # Checkbox "Use Mirror Modifier"
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
        sub.operator('camera.array', 
        icon='MOD_ARRAY')
        
        split = layout.split()
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_user_settings', 
        icon='FILE_REFRESH')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_user_settings', 
        icon='ARROW_LEFTRIGHT')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('camera.turnaround_user_settings', 
#        icon='X')


#        self.layout.column(....) # col
#        self.layout.row(....) # row
#        context.scene.loop_it_ui # loop_props
#        self.layout.split(....) # split
#        self.layout.split
        
#        col.prop(loop_props, "camera_mirror_array")
#        col.separator()
#        col.label(text="Camera Direction:")   
#        col.prop(loop_props, "camera_array_axis", text="Axis")

class VIEW3D_PT_camera_object(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "VIEW3D_PT_loop_camera"


    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        loop_props = scene.loop_it_ui
        
        row = layout.row(align=True)
        row.label(text="Axis:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "camera_array_axis", text="")
        
        row = layout.row(align=True)
        row.label(text="Speed:")
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(loop_props, "camera_array_speed", text="")
        
#        col = layout.column()
##        row = layout.row()
#        col.separator()
#        col.prop(loop_props, "camera_mirror_array") # Checkbox "Use Mirror Modifier"
        
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.75
        sub.operator('camera.array', 
        icon='OUTLINER_OB_MESH')
        
        split = layout.split()
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_user_settings', 
        icon='FILE_REFRESH')
        
        sub.scale_x = .3
        col = split.column()
        sub.operator('camera.turnaround_user_settings', 
        icon='ARROW_LEFTRIGHT')
        
#        sub.scale_x = .3
#        col = split.column()
#        sub.operator('camera.turnaround_user_settings', 
#        icon='X')

class VIEW3D_PT_camera_torus(Panel):
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Torus   (in development)"
    bl_parent_id = "VIEW3D_PT_loop_camera"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        loop_props = scene.loop_it_ui
        col = layout.column(align=True)
        
        col.enabled = False
        col.operator('camera.torus',
        icon='MESH_TORUS')

#class VIEW3D_PT_loop_export(View3DPrintPanel, Panel):
class VIEW3D_PT_loop_export(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Export"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

#        print_3d = context.scene.print_3d

#        layout.prop(print_3d, "export_path", text="")

        loop_flag_export = context.scene.loop_flag_export

        layout.prop(loop_flag_export, "export_path", text="")

#        col = layout.column()
#        col.prop(print_3d, "use_apply_scale")
#        col.prop(print_3d, "use_export_texture")

        layout.prop(print_3d, "export_format")
        layout.operator("mesh.print3d_export", text="Export", icon='EXPORT')
       
class VIEW3D_PT_loop_particles(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop It"
    bl_label = "Particles"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        col = self.layout.column(align=True)
        
        col.operator('add.particles',
        icon='ADD')
        
        col.operator('loop.particles',
        icon='CURVE_BEZCIRCLE')

class VIEW3D_PT_CustomPanel_01(bpy.types.Panel):
    bl_label = "My Panel"
#    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Loop It"
    bl_context = "objectmode"   


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        col = layout.column(align=True)
        loop_props = scene.loop_it_ui

#        layout.prop(loop_props, "camera_mirror_array")
#        layout.prop(loop_props, "camera_array_axis", text="Axis")
#        layout.prop(loop_props, "my_int")
#        layout.prop(loop_props, "my_float")
#        layout.prop(loop_props, "my_float_vector", text="")
#        layout.prop(loop_props, "my_string")
#        layout.prop(loop_props, "my_path")
#        layout.operator("wm.hello_world")
#        layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
#        layout.separator()

#        col.prop_search(scene, "Texture", scene, "object")
        layout.prop_search(scene, "Texture", scene, "object")
 
#class VIEW3D_PT_CustomPanel_02(bpy.types.Panel):
#    bl_label = "My Panel"
##    bl_idname = "OBJECT_PT_custom_panel"
#    bl_space_type = "VIEW_3D"   
#    bl_region_type = "UI"
#    bl_category = "Loop It"
#    bl_context = "objectmode"
#    
#    def draw(self, context):
#    
#        layout = self.layout
#        scene = context.scene
#        obj = context.object

#        col=layout.column(align=True)
#        row = col.row()
#        
#        row = layout.row(align=True)
#        row.label(text="Select Object:")
##        row = col.row(align=True)
#        row.prop_search(scene, "Objects", bpy.data, "objects", text='')
        
#################################################################
###                     REGISTRATION                          ###
#################################################################     
            
classes = (
    LOOP_IT_PROPS,
    DISPLACEMENT_USER_SETTINGS,
    DISPLACEMENT_FIRST,
    DISPLACEMENT_SUB_KEYFRAMES,
    DISPLACEMENT_SUB_UPDATE_TIMELINE,
    DISPLACEMENT_FLIP,
    TEXTURE_ADD_NODES,
    TEXTURE_LOOP_NODES,
    OCEAN,
    CAMERA_TURNAROUND,
    CAMERA_TURNAROUND_SUB_KEYFRAMES,
    CAMERA_TURNAROUND_SUB_KEYFRAMES_RETURN,
    CAMERA_TURNAROUND_REFRESH,
    CAMERA_TURNAROUND_FLIP,
    CAMERA_TURNAROUND_DELETE,
    CAMERA_ARRAY,
    CAMERA_TORUS,
    CREATE_FLAG,
    BAKE_FLAG,
    DELETE_BAKE_FLAG,
    EXPORT_FLAG,
    LOOP_FLAG,
    ADD_PARTICLES,
    LOOP_PARTICLES,
    VIEW3D_PT_timeline,
    VIEW3D_PT_meshes,
    VIEW3D_PT_mesh_displace,
    VIEW3D_PT_mesh_tex_coord_node,
    VIEW3D_PT_mesh_ocean,
    VIEW3D_PT_mesh_ocean_timeline,
    VIEW3D_PT_mesh_ocean_time_wave,
    VIEW3D_PT_mesh_ocean_settings,
    VIEW3D_PT_mesh_flag,
    VIEW3D_PT_loop_camera,
    VIEW3D_PT_camera_turn,
    VIEW3D_PT_camera_array,
    VIEW3D_PT_camera_object,
    VIEW3D_PT_camera_torus,
    VIEW3D_PT_loop_particles,
    MessageBox,
) #     VIEW3D_PT_loop_export, VIEW3D_PT_loop_flag, VIEW3D_PT_camera_turn_settings, CAMERA_TURNAROUND_USER_SETTINGS 


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.loop_it_ui = PointerProperty(type=LOOP_IT_PROPS)
    bpy.types.Scene.Meshes = bpy.props.StringProperty()
    bpy.types.Scene.theImage = bpy.props.StringProperty()        
        
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    bpy.types.Scene.loop_it_ui
    bpy.types.Scene.Meshes
    bpy.types.Scene.theImage

      #bpy.context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp


        #object.keyframe_insert(‘location’, frame=1)
        
        #return {"FINISHED"}

if __name__ == '__main__':
    register() 