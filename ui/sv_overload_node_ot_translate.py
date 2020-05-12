# This file is part of project Sverchok. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/nortikin/sverchok/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE


import bpy
from bpy.types import Operator, Macro


class SvNodeTransformFinalize(Operator):
    bl_idname = "node.sv_transform_translate_finalize"
    bl_label = "Finalize transform"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        if not space.type == "NODE_EDITOR":
            return
        return space.tree_type in sv_tree_types

    def execute(self, context):
        if context.active_node and context.active_node.bl_idname == "SvStethoscopeNodeMK2":
            context.active_node.process_node(context)
            print("did something!?")

        print("DONE!")
        return {'FINISHED'}

class SvTransformTranslateMacro(Macro):
    bl_idname = "node.sv_transform_translate"
    bl_label = "Overloaded G function"


classes = [SvNodeTransformFinalize, SvTransformTranslateMacro]


def register():
    _ = [bpy.utils.register_class(cls) for cls in classes]
    SvTransformTranslateMacro.define("TRANSFORM_OT_translate")
    SvTransformTranslateMacro.define("node.sv_transform_translate_finalize")

def unregister(): 
    _ = [bpy.utils.unregister_class(cls) for cls in reversed(classes)]
