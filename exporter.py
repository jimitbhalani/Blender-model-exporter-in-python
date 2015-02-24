# Required Blender information.
bl_info = {
           "name": "My Exporter",
           "author": "",
           "version": (1, 0),
           "blender": (2, 65, 0),
           "location": "File > Export > Test (.tst)",
           "description": "",
           "warning": "",
           "wiki_url": "",
           "tracker_url": "",
           "category": "Import-Export"
          }

# Import the Blender required namespaces.
import sys, getopt

import bpy
from bpy_extras.io_utils import ExportHelper

# The main exporter class.
class MyExporter(bpy.types.Operator, ExportHelper):
   bl_idname       = "export_scene.my_exporter";
   bl_label        = "My Exporter";
   bl_options      = {'PRESET'};

   obj_name        = "";

   def __init__(self):
      pass

   def execute(self, context):
      print("Execute was called.");

      self.parse_command_line_options();

      if (self.obj_name == ""):
         print("No suitable object name was provided .");
         return {'FINISHED'};
      print("Executing......");
      # Now start exporting the target object.
      self.export_object(self.obj_name);
      # Parse all the objects in the scene.
      print("Finished");
      return {'FINISHED'};


   def export_object(self, obj_name):
       for item in bpy.data.objects:
           if item.name == obj_name and item.type == 'MESH' :
              for face in item.data.polygons:
                  verts_in_face = face.vertices[:]
                  print("face index ", face.index)
                  print("normal ", face.normal)
                  for vert in verts_in_face:
                      print("vertex coords", item.data.vertices[vert].co)
                  

   def parse_command_line_options(self):
      obj_name = "";
      myArgs = [];
      argsStartPos = 0;

      if (("--" in sys.argv) == False):
         return;

      argsStartPos = sys.argv.index("--");
      argsStartPos += 1;
      myArgs = sys.argv[argsStartPos:];

      try:
         opts, args = getopt.getopt(myArgs, 'hm:', ["help", "model-file="]);
      except getOpt.GetoptError:
         print("Opt Error.");
         return;

      for opt, arg in opts:
         if (opt in ("-h", "--help")):
            print("Run this as the following blender command.");
            print("\tblender <blend file> --background --python <script file> -- -m <Object name>");
         elif (opt == "-m"):
            obj_name = arg;

      if (obj_name != ""):
         self.obj_name = obj_name;
         print(obj_name);


# Define the Blender required registration functions.
def register():
   """
   Handles the registration of the Blender Addon.
   """
   bpy.utils.register_module(__name__);

def unregister():
   """
   Handles the unregistering of this Blender Addon.
   """
   bpy.utils.unregister_module(__name__);

# Handle running the script from Blender's text editor.
if (__name__ == "__main__"):
   print("Registering.");
   register();

   print("Executing.");
   bpy.ops.export_scene.my_exporter();