bl_info = {
	"name": "Blender 2.81 RenderButtons",
	"author": "Mitsuma",
	"version": (0, 0, 3),
	"blender": (2, 81, 0),
	"location": "Render Properties",
	"description": "",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Render"}

import bpy 


class AddRenderPanel(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "Render"
	bl_idname = "OBJECT_PT_Add_Render"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"

	def draw(self, context):
		layout = self.layout

		row = layout.row(align=True)
		row.operator("render.render", text="Render", icon='RENDER_STILL')
		row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
		
		split = layout.split()

		split.label(text="Display:")
		row = split.row(align=True)
		prefs = context.preferences
		row.prop(prefs.view, "render_display_type", text="")
		row.prop(bpy.context.scene.render, "use_lock_interface", icon_only=True)

def register():
	bpy.utils.register_class(AddRenderPanel)

def unregister():
	bpy.utils.unregister_class(AddRenderPanel)

if __name__ == "__main__":
	register()
