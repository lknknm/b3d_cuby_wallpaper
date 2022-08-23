import bpy
import random

# Initially based on the David Mignot Tutorial

# defines UV value for materials
def setUV():
    bpy.ops.object.editmode_toggle()
    bpy.ops.uv.cube_project(cube_size=10)
    bpy.ops.object.editmode_toggle()
    
# Adds Bevel Modifier with 0.01m amount and 2 segments per cube    
def addBevel():
    mod_bevel = bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = 0.01
    bpy.context.object.modifiers["Bevel"].segments = 2

# Cubes array function is defined
# But the next step is find out how to mirror the cubes array up without the need of manual process in Blender
def make_cubes_array():
    spacing = 2.2
    for x in range(20):
        for y in range(20): 
            location = (x * spacing, y * spacing, random.random() *2)
            scale=(1, 1, x)
            cube = bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=scale)
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            setUV()

            #bpy context for further need
            ob = bpy.context.object
            
            # Adds Bevel Modifier with 0.01m amount and 2 segments per cube
            addBevel()
            
            # Assign material
            item = bpy.context.object
            if random.random() < 0.6:
               item.data.materials.append(bpy.data.materials["Metal Preto"])
            else:
                item.data.materials.append(bpy.data.materials["CARRARA GIOIA"])


# make 'em
make_cubes_array()