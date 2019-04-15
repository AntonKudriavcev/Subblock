from kivy.app               import App
from kivy.core.window       import Window
from kivy.garden.graph      import Graph, LinePlot
from kivy.uix.button        import Button
from kivy.uix.togglebutton  import ToggleButton
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.checkbox      import CheckBox
from kivy.uix.dropdown      import DropDown
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider        import Slider
from kivy.uix.widget        import Widget
from kivy.uix.textinput     import TextInput
from kivy.uix.label         import Label
from kivy.uix.popup         import Popup
from kivy.uix.spinner       import Spinner
from kivy.uix.filechooser   import FileChooserIconView

import os
import pysrt

##=====================================================================================
##==================================IMPORT CLASSES=====================================
##=====================================================================================

from READ_AND_WRITE         import READ_AND_WRITE
from TEMPERATURE            import TEMPERATURE
from CONTROL                import CONTROL
from BOOTLOADER_SETTINGS    import BOOTLOADER_SETTINGS
from SETTING                import SETTING

##=====================================================================================
##==================================IMPORT SCREENS=====================================
##=====================================================================================

import SCREEN_TEMPERATURE
import SCREEN_READ_AND_WRITE
import SCREEN_CONTROL
import SCREEN_BOOTLOADER_SETTINGS
import SCREEN_SETTING

##=====================================================================================
##
##=====================================================================================

sm = ScreenManager()
sm.add_widget(TEMPERATURE(name         = 'TEMPERATURE'))
sm.add_widget(READ_AND_WRITE(name      = 'READ_AND_WRITE'))
sm.add_widget(CONTROL(name             = 'CONTROL'))
sm.add_widget(BOOTLOADER_SETTINGS(name = 'BOOTLOADER_SETTINGS'))
sm.add_widget(SETTING(name             = 'SETTING'))

class MainApplication(App):    
    def build(self):
        return sm
    
if __name__ == '__main__':

    Window.size           = (1024,768)
    Window.minimum_width  = (800)
    Window.minimum_height = (600)  
    Window.clearcolor     = (.33,.34,.38,1)
    Window.show()
    MainApplication().run()
