# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "AutoFitCam",
    "author" : "Tobias Ladzenski",
    "description" : "Automatically fits the camera view to the selected objects.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class AutoFitCam(bpy.types.Operator):
    bl_idname = "autofitcam"
    bl_label = "Fit Camera to Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.camera_to_view_selected()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(AutoFitCam)

def unregister():
    bpy.utils.unregister_class(AutoFitCam)