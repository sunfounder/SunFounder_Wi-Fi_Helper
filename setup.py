from distutils.core import setup
import py2exe
import sys,os
import wifi_helper
#includes = ["tkinter", "string", "os", "_thread", "socket", "platform"]
options = {"py2exe":
     { "compressed": 1,
      "optimize": 0,
      #"includes": includes,
      "dll_excludes": ["tcl85.dll", "tk85.dll"],
      "bundle_files": 2,
     }
   }
setup(
  version = wifi_helper.WiFiHelper().VERSION,
  description = "SunFounder WiFi Helper for Raspberry Pi",
  options = options,
  zipfile=None,
  windows=[{"script": "wifi_helper.py", "icon_resources": [(1, "./SunFounder_LOGO_small.ico")] }],
)
