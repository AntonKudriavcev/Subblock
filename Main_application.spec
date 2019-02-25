# -*- mode: python ; coding: utf-8 -*-
from kivy.deps import sdl2, glew, gstreamer
from kivy.app import App
from kivy.clock             import Clock
from kivy.core.window       import Window
from kivy.config            import ConfigParser
from kivy.garden.graph      import Graph, MeshLinePlot, MeshStemPlot, LinePlot, SmoothLinePlot, ContourPlot
from kivy.uix.button        import Button
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.checkbox      import CheckBox
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider        import Slider
from kivy.uix.widget        import Widget
from kivy.uix.textinput     import TextInput
from kivy.uix.label         import Label
from kivy.uix.popup         import Popup
from kivy.lang              import Builder
from kivy.properties        import ObjectProperty
import struct
import socket 
import time
from threading              import Thread 
import os
import pysrt
block_cipher = None

a = Analysis(['src\\Main_application.py'],
             pathex=['C:\\Users\\Kudriavcev\\Desktop\\Main_application\\src\\', 
                      'C:\\Users\\Kudriavcev\\Desktop\\Main_application\\src\\src\\graph'],
             binaries=[],
             datas= [],
             hiddenimports=['kivy.garden', 'kivy.garden.graph', 'win32timezone', 'backend_kivy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,Tree('C:\\Users\\Kudriavcev\\Desktop\\Main_application\\src\\src\\'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
          name='Subblock',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True, 
          icon  = 'C:\\Users\\Kudriavcev\\Desktop\\subblock.ico')
