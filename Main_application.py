from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.garden.graph import Graph, MeshLinePlot, MeshStemPlot, LinePlot, SmoothLinePlot, ContourPlot
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.filechooser import FileChooserIconView
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import struct
import socket 
import time
from threading import Thread 
import os
import pysrt
Builder.load_string("""
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
<RAW>:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'center'
        padding: 3
        Widget:
            size_hint: (.8,1)
            canvas:
                Color:
                    rgba: .22,.22,.26,1
                Rectangle:
                    size: self.size
                    pos: self.pos                
    BoxLayout:
        orientation : 'vertical'
        size_hint : (.2, 1)
        padding: 3
        Button:
            text: 'Чтение/Запись'
            bold : 'True'
            color: [0,0,0,1]
            background_color : [.62,.93,.25,1]
            background_normal : ''
        Button:
            text : 'Температура ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.manager.current = 'TEMPERATURE'
            on_press:root.cont_drawing()
        Button:
            text : 'Регистры ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'CONTROL'
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'BOOTLOADER_SETTINGS'
        Button:
            text : 'Сетевые настройки'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'SETTING'
            on_press:root.cont_drawing()
        Button:
            size_hint: (1,6.5)
            background_color : [.22,.22,.26,1]
            background_normal : ''
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'center'
        size_hint : [1.2, 1.3]
        GridLayout: 
            cols: 2
            size_hint: [.45, .3]
            spacing: 3
            Label:
                text: 'Адрес'
                text_size:self.size
                halign:'left'
                valign:'middle'
            TextInput:
                id: address
                text:
                multiline: False
            Label:
                text: 'Данные на запись'
                text_size:self.size
                halign:'left'
                valign:'middle'
            TextInput:
                id: data
                text:
                multiline: False
            Widget:
            Widget:
            Label:
                text: 'Прочитанные данные'
                text_size:self.size
                halign:'left'
                valign:'top'
            TextInput:
                id: income_data
                size_hint: (1,2)
                text:
            Widget:
            Widget:
            Button:
                text: 'ЗАПИСЬ'
                bold : 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_press: root.write()
            Button:
                text: 'ЧТЕНИЕ'
                bold : 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_press: root.read() 
<TEMPERATURE>: 
    BoxLayout:
        orientation : 'vertical'
        size_hint : (.2, 1)
        padding: 3
        Button:
            text: 'Чтение/Запись'
            bold : 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.stop_drawing()
            on_press: root.manager.current = 'RAW'           
        Button:
            text: 'Температура ПЛИС'
            bold : 'True'
            color: [0,0,0,1]
            background_color : [.62,.93,.25,1]
            background_normal : ''     
        Button:
            text : 'Регистры ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.stop_drawing()
            on_press: root.manager.current = 'CONTROL'
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.stop_drawing()
            on_press: root.manager.current = 'BOOTLOADER_SETTINGS'
        Button:
            text : 'Сетевые настройки'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'SETTING'
        Button:
            size_hint: (1,6.5)
            background_color : [.22,.22,.26,1]
            background_normal : ''
    AnchorLayout:
        padding: 3
        anchor_x : 'right'
        anchor_y : 'top'
        GridLayout:
            cols: 1
            size_hint: .8, 1
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                size_hint: (1, .2)
                Widget:
                    canvas:
                        Color:
                            rgba: .22,.22,.26,1
                        Rectangle:
                            size: self.size
                            pos: self.pos
                BoxLayout:   
                    Label:
                        text:'Т е м п е р а т у р н ы й  р е ж и м  я д е р  П Л И С'
                        font_size: 20
                        bold: True
            Graph:
                id: graph
                size_hint : [1, 4]
                background_color : [.22,.22,.26,1]
                plot: MeshLinePlot
                xlabel: "Time"
                ylabel: "Temperature"
                ylabel_pos: 'right'
                x_ticks_major:10
                y_ticks_major:5             
                y_grid_label : True
                padding:5
                x_grid:True
                y_grid:True
                xmin:int(300) - int("%d" % display_time.value)
                xmax:300
                ymin:20
                ymax:60
            AnchorLayout:
                anchor_x : 'left'
                anchor_y : 'center'
                padding : (0,2)
                size_hint: (1, .4)
                Widget:
                    canvas:
                        Color:
                            rgba: .22,.22,.26,1
                        Rectangle:
                            size: self.size
                            pos: self.pos
                AsyncImage
                    size_hint: (1, 1)
                    source: 'image.PNG'                  
            AnchorLayout:
                anchor_x : 'right'
                anchor_y : 'bottom'
                Widget:
                    size_hint: (1, 1)
                    canvas:
                        Color:
                            rgba: .22,.22,.26,1
                        Rectangle:
                            size: self.size
                            pos: self.pos 
                GridLayout:
                    cols: 3
                    spacing: 3
                    padding:5
                    BoxLayout:
                        orientation: 'horizontal'
                        Slider:
                            size_hint: [3,1]
                            id: time_updating
                            value_track : True
                            value_track_color :[.62,.93,.25,1]
                            range: (100, 5000)
                            step: 50
                            value:500
                            on_touch_move: root.move()
                        Label:
                            id: updating_time
                            text: "%d" % time_updating.value
                            font_size:16
                            multiline: False
                    Label:
                        text: 'мсек, интервал обновления данных'
                        text_size:self.size
                        halign:'left'
                        valign:'middle'
                        font_size: 12
                    BoxLayout:
                        padding: 3
                        orientation: 'horizontal'    
                        Switch :
                            id: switch
                            active: False
                        Label:
                            text: 'записывать лог'
                            font_size: 12
                            
                    BoxLayout:
                        orientation: 'horizontal'
                        Slider:
                            id: display_time
                            size_hint: [3,1]
                            value_track : True
                            value_track_color :[.62,.93,.25,1]
                            range: (10,300)
                            step: 10
                            value: 300
                            on_touch_move: root.display_time_changes()
                        Label:
                            id: time_of_display
                            text: '150'
                            font_size:16
                            multiline: False
                    Label:
                        text: 'сек, окно отображения при данном  интервале обновления данных'
                        font_size: 12
                        text_size:self.size
                        halign:'left'
                        valign:'middle'

                    Button:
                        id: start_control
                        text: "СТАРТ"
                        font_size: 20
                        bold: True
                        color: [0,0,0,1]
                        background_color : [.62,.93,.25,1]
                        background_normal : ''
                        on_press: root.start_stop()   
<CONTROL>:
    BoxLayout:
        orientation : 'vertical'
        size_hint : (.2, 1)
        padding: 3
        Button:
            text: 'Чтение/Запись'
            bold : 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'RAW'
        Button:
            text : 'Температура ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.cont_drawing()
            on_press: root.manager.current = 'TEMPERATURE'
        Button:
            text: 'Регистры ПЛИС'
            bold : 'True'
            color: [0,0,0,1]
            background_color : [.62,.93,.25,1]
            background_normal : ''
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'BOOTLOADER_SETTINGS'
        Button:
            text : 'Сетевые настройки'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press:root.cont_drawing()
            on_press: root.manager.current = 'SETTING'
        Button:
            size_hint: (1,6.5)
            background_color : [.22,.22,.26,1]
            background_normal : ''       
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'center'
        padding: 3
        AnchorLayout:
            anchor_x:'right'
            anchor_y:'top'
            ScrollView:
                size_hint: .8,.9
                GridLayout:
                    size_hint_y: 1.13
                    cols: 3
                    spacing: 2
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos                       
                        BoxLayout:
                            padding: 5
                            orientation: 'vertical'
                            Label:
                                text:'01: Разрешеие дублирования потока'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: duplication_off_01
                                    group: 'duplication resolution'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: duplication_on_01
                                    group:'duplication resolution'
                                    
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos            
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:' 04A: Регистр коррекции коэффициента САМ'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: correction_register_04A
                                size_hint:(1,.6)
                                text:''
                                multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos            
                        BoxLayout:
                            padding: 5
                            orientation: 'vertical'
                            Label:
                                text:'04B: Регистр коррекции коэффициента САМ'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: correction_register_04B
                                size_hint:(1,.6)
                                text:''
                                multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'44: Запрет адаптации к скорости ПП ПЛИС_3'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: prohibition_of_adaptation_off_44
                                    group: 'prohibition of adaptation'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: prohibition_of_adaptation_on_44
                                    group:'prohibition of adaptation'
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'45: Размер окна усреднения'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: averaging_window_45
                                size_hint:(1,.6)
                                text:''
                                multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'46: Граница полосы подавления'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: suppression_band_46
                                size_hint:(1,.6)
                                text:''
                                multiline: False                        
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos    
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'47: Регистр управления погогом ПЛИС_3'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: threshold_control_register_47
                                size_hint:(1,.6)
                                text:''
                                multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos            
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'48: Регистр управления МДФ, ЧПК ПЛИС_3'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: MDF_control_register_off_48
                                    group: 'MDF control register'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: MDF_control_register_on_48
                                    group:'MDF control register'
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos    
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text:'49: Порог числа периодов для переключения на ЧПК РВ1'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            TextInput:
                                id: period_threshold_49
                                size_hint:(1,.6)
                                text:''
                                multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos            
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '50: Компенсация настабильности амплитуды'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: amplitude_unstability_off_50
                                    group: 'amplitude unstability'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: amplitude_unstability_on_50
                                    group:'amplitude unstability'
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '51: Компенсация настабильности фазы'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: phase_unstability_off_51
                                    group: 'phase unstability'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: phase_unstability_on_51
                                    group:'phase unstability'
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '52: Контрольный регистр уровня шума'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Уровень шума'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: noise_level_52
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '53: Контрольный регистр превышения уровня шума'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Уровень шума'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: noise_level_excess_53
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '54: Включить внешний порог фазы'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: phase_threshold_off_54
                                    group: 'phase threshold'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: phase_threshold_on_54
                                    group:'phase threshold'
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '55: Контрольный регистр порога фазы'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Порог фазы для КНА'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: phase_threshold_register_55
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '56: Контрольный регистр порога фазы'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Порог фазы для КНФ'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: phase_threshold_register_56
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '57: Порог суммы дельт для однозн. опр. скорости'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'bottom'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Значение порога'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: sum_delta_threshold_57
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '58: Размер усреднения оценки скорости'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                Label:
                                    text: 'Размер окна уср.'
                                    font_size: 12
                                    text_size:self.size
                                    halign:'left'
                                    valign:'middle'
                                TextInput:
                                    id: velocity_evaluation_58
                                    size_hint:(1,.8)
                                    text:''
                                    multiline: False
                    AnchorLayout:
                        Widget:
                            canvas:
                                Color:
                                    rgba: .22,.22,.26,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                        BoxLayout:
                            orientation: 'vertical'
                            padding: 5
                            Label:
                                text: '59: Разрешение БНП М для ПП3'
                                font_size: 12
                                text_size:self.size
                                halign:'left'
                                valign:'middle'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'OFF'
                                    font_size: 12
                                CheckBox:
                                    id: BNP_resolution_off_59
                                    group: 'BNP resolution'
                                    active: 'True'
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint:(1,.6)
                                Label:
                                    text:'ON'
                                    font_size: 12
                                CheckBox:
                                    id: BNP_resolution_on_59
                                    group:'BNP resolution'
                    Widget:
                        canvas:
                            Color:
                                rgba: .22,.22,.26,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                    Widget:
                        canvas:
                            Color:
                                rgba: .22,.22,.26,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                    Widget:
                    Widget:
                    Widget:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        padding: 3
        GridLayout:
            size_hint:(.8, .1)
            cols: 4
            spacing: 3
            Button:
                text:'Сохранить'
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.show_save()
            Button:
                text:'Загрузить'
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.show_load()
            Button:
                text:'Применить'
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.apply()
            Button:
                text:'Запросить'
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.request()
<LoadDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser
        BoxLayout:
            size_hint_y: None
            height: 40
            spacing: 5
            Button:
                text: "Cancel"
                on_release: root.cancel()
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
            Button:
                text: "Load"
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.load(filechooser.path, filechooser.selection)
<SaveDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser
        TextInput:
            id: text_input
            text: '.txt'
            size_hint_y: None
            height: 40
            multiline: False
        BoxLayout:
            size_hint_y: None
            height: 40
            spacing: 5
            Button:
                text: "Cancel"
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.cancel()
            Button:
                text: "Save"
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_release: root.save(filechooser.path, text_input.text)
            
<BOOTLOADER_SETTINGS>:
    BoxLayout:
        orientation : 'vertical'
        size_hint : (.2, 1)
        padding: 3
        Button:
            text: 'Чтение/Запись'
            bold : 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'RAW'
            on_press: root.reconf_all()
        Button:
            text : 'Температура ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'TEMPERATURE'
            on_press: root.cont_drawing()
            on_press: root.reconf_all()
        Button:
            text : 'Регистры ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'CONTROL'
            on_press: root.reconf_all()
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            color: [0,0,0,1]
            background_color : [.62,.93,.25,1]
            background_normal : ''
        Button:
            text : 'Сетевые настройки'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'SETTING'
            on_press: root.reconf_all()
            on_press: root.cont_drawing()
        Button:
            size_hint: (1,6.5)
            background_color : [.22,.22,.26,1]
            background_normal : ''
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'center'
        padding: 3
        Widget:
            size_hint: (.8,1)
            canvas:
                Color:
                    rgba: .22,.22,.26,1
                Rectangle:
                    size: self.size
                    pos: self.pos
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        size_hint: (1.2,.9)
        GridLayout:
            cols: 1
            spacing: 3
            size_hint:(.4,.45)
            Label:
                text: '00: Контрольный регистр адреса ПЛИС_1'
                text_size:self.size
                halign:'left'
                valign:'middle'
            BoxLayout:
                orientation: 'horizontal'
                Widget:
                Button:
                    id: reset
                    text: 'СБРОС'
                    bold: 'True'
                    size_hint:(.5,2)
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.reset()
            Label:
                text: '04: Настройка загрузчика ПЛИС_1'
                text_size:self.size
                halign:'left'
                valign:'middle'
            BoxLayout:
                spacing: 3   
                TextInput:
                    id: reconfiguration_04
                    multiline: False
                Button:
                    size_hint:(.5,2)
                    text:'Реконфигурция'
                    bold: 'True'
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.reconf_FPGA_1()
            Label:
                text:'24: Настройка загрузчика ПЛИС_2'
                text_size:self.size
                halign:'left'
                valign:'middle'
            BoxLayout:
                spacing: 3
                TextInput:
                    id: reconfiguration_24
                    multiline: False
                Button:
                    text:'Реконфигурция'
                    bold: 'True'
                    size_hint:(.5,2)
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.reconf_FPGA_2()
            Label:
                text:'04C: Настройка загрузчика ПЛИС_3'
                text_size:self.size
                halign:'left'
                valign:'middle'
            BoxLayout:
                spacing: 3
                TextInput:
                    id: reconfiguration_04C
                    multiline: False
                Button:
                    text:'Реконфигурция'
                    bold: 'True'
                    size_hint:(.5,2)
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.reconf_FPGA_3()
            
            BoxLayout:
                orientation: 'horizontal'
                spacing: 3
                size_hint:(1,2)
                Button:
                	id: request
                    text: ''
                    bold: 'True'
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.request()
                Button:
                    text: 'Применить все'
                    bold: 'True'
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.apply()
            
<SETTING>:
    BoxLayout:
        orientation : 'vertical'
        size_hint : (.2, 1)
        padding: 3
        Button:
            text: 'Чтение/Запись'
            bold : 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'RAW'
            on_press:root.stop_drawing()
        Button:
            text : 'Температура ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'TEMPERATURE'
        Button:
            text : 'Регистры ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'CONTROL'
            on_press: root.stop_drawing()
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.manager.current = 'BOOTLOADER_SETTINGS'
            on_press: root.stop_drawing()
        Button:
            text: 'Сетевые настройки'
            bold : 'True'
            color: [0,0,0,1]
            background_color : [.62,.93,.25,1]
            background_normal : ''       
        Button:
            size_hint: (1,6.5)
            background_color : [.22,.22,.26,1]
            background_normal : ''
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'center'
        padding: 3
        Widget:
            size_hint: (.8,1)
            canvas:
                Color:
                    rgba: .22,.22,.26,1
                Rectangle:
                    size: self.size
                    pos: self.pos
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        size_hint: (1.2,1.5)
        GridLayout:
            cols: 2
            size_hint: (.45,.25)
            spacing: 3
            padding: 2
            Label:
            	text: 'IP КОМП'
            	text_size: self.size
            	halign: 'left'
            	valign: 'middle'
            Spinner:
                id: COMP_IP
                text_size: self.size
            	halign: 'left'
            	valign: 'middle'
            	color: [0,0,0,1]
            	background_color : [.9,.9,.9,1]
            	background_normal : ''

            Label:
                text: 'IP МЦОС'
                text_size:self.size
                halign:'left'
                valign:'middle'
            TextInput:
                id: IP_DSPM
                text:'172.16.0.13'
                multiline: False
            Label:
                text:'PORT МЦОС'
                text_size:self.size
                halign:'left'
                valign:'middle'
            TextInput:
                id: PORT_DSPM
                text: '65261'
                multiline: False
            Widget:
            Widget:
            Label:
                id: reconf
                text:
                font_size: 14
                text_size:self.size
                halign:'left'
                valign:'middle'
            Button:
                text:'ПРИМЕНИТЬ'
                bold: 'True'
                color: [0,0,0,1]
                background_color : [.62,.93,.25,1]
                background_normal : ''
                on_press: root.reconfig()
            Widget:
            Widget:
""")
def get_temperature_level():
    global FPGA_TEMPER_1
    global FPGA_TEMPER_2
    global FPGA_TEMPER_3
    global max_temp
    global min_temp
    counter = 0
    pack_for_FPGA_1 = bytes ([0x00, 0x03,
                                0x88, 0xA6,
                                0x1F, 0x11,
                                0x80, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x03,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00])
    pack_for_FPGA_2 = bytes ([0x00, 0x03,
                                0x88, 0xA6,
                                0x1F, 0x11,
                                0x80, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x23,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00])
    
    pack_for_FPGA_3 = bytes ([0x00, 0x03,
                                0x88, 0xA6,
                                0x1F, 0x11,
                                0x80, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x43,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00])  
    while True:
        if waiting == 1:##-----when press START------
            clientSock.sendto(pack_for_FPGA_1,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
            try:
                income_pack, addr = clientSock.recvfrom(1024)
            except:
                pass
            else:
                if ((bytes([income_pack[2]])  == bytes([0x88])) and
                    (bytes([income_pack[3]])  == bytes([0xA6])) and
                    (bytes([income_pack[4]])  == bytes([0xF1])) and
                    (bytes([income_pack[5]])  == bytes([0xA5])) and
                    (bytes([income_pack[15]]) == bytes([0x03]))):   
                    temper_1 = int.from_bytes(bytes([income_pack[23]]),
                                              byteorder = 'big', signed=True)
                    FPGA_TEMPER_1.append(temper_1)
                else:
                    FPGA_TEMPER_1.append(temper_1)##########################
                ##print (temper_1)
            clientSock.sendto(pack_for_FPGA_2,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
            try:
                income_pack, addr = clientSock.recvfrom(1024)
            except:
                pass
            else:
                if ((bytes([income_pack[2]])  == bytes([0x88])) and
                    (bytes([income_pack[3]])  == bytes([0xA6])) and
                    (bytes([income_pack[4]])  == bytes([0xF1])) and
                    (bytes([income_pack[5]])  == bytes([0xA5])) and
                    (bytes([income_pack[15]]) == bytes([0x23]))):
                    temper_2 = int.from_bytes(bytes([income_pack[23]]),
                                              byteorder = 'big', signed=True)
                    FPGA_TEMPER_2.append(temper_2)
                else:
                    FPGA_TEMPER_2.append(temper_2)##############################
                ##print (temper_2)
            clientSock.sendto(pack_for_FPGA_3,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
            try:
                income_pack, addr = clientSock.recvfrom(1024)
            except:
                pass
            else:
                if ((bytes([income_pack[2]])  == bytes([0x88])) and
                    (bytes([income_pack[3]])  == bytes([0xA6])) and
                   ((bytes([income_pack[4]])  == bytes([0xF1])) or
                    (bytes([income_pack[4]])  == bytes([0x21])))and
                    (bytes([income_pack[5]])  == bytes([0xA5])) and
                    (bytes([income_pack[15]]) == bytes([0x43]))):
                    temper_3 = int.from_bytes(bytes([income_pack[23]]),
                                              byteorder = 'big',signed=True)
                    FPGA_TEMPER_3.append(temper_3)                   
                else:
                    FPGA_TEMPER_3.append(temper_3)############################
                ##print (temper_3)              
            if len(FPGA_TEMPER_1) >= 302:
                del FPGA_TEMPER_1[0]
                del FPGA_TEMPER_2[0]
                del FPGA_TEMPER_3[0]
            try:    
                max_temp = max(max(FPGA_TEMPER_1),max(FPGA_TEMPER_2),max(FPGA_TEMPER_3))
                min_temp = min(min(FPGA_TEMPER_1),min(FPGA_TEMPER_2),min(FPGA_TEMPER_3))               
            except ValueError:
                pass           
            print('max = ', max_temp)##
            print('min = ', min_temp)##
            if write_to_file == True:                
                with open(file_name,'a', encoding = 'utf-8') as txt_file:
                    try:
                        txt_file.write('{0}\t{1}\t{2}\t{3}\n'
                                            .format(round((time.perf_counter() - time_of_start),3),
                                            FPGA_TEMPER_1[counter],
                                            FPGA_TEMPER_2[counter],
                                            FPGA_TEMPER_3[counter]))
                        if counter == 300:
                            counter = 300
                        else:
                            counter += 1
                    except IndexError:
                        pass
            time.sleep(update/1000.0000-0.0018)
            
        elif waiting == 0:##----when press STOP----------------
            counter = 0
            time.sleep(.01)
        elif waiting == 2:##----when moving to RAW window------
            time.sleep(.01)
##---------------------------------------------------            
def txt_creator():
    global time_of_start  
    with open(file_name,'w', encoding = 'utf-8') as txt_file:
        txt_file.write(time_of_creation + '\n' + '\n')
        txt_file.write('TIME\tFPGA_1\tFPGA_2\tFPGA_3\n')
    time_of_start = time.perf_counter()
##---------------------------------------------------
def write_to_reg(address, data):
	if (data != '') and (address != '') :
	    headline = bytes ([0x00, 0x03,
	                       0x88, 0xA6,
	                       0x1F, 0x01,
	                       0x80, 0x00,
	                       0x00, 0x00,
	                       0x00, 0x00,
	                       0x00, 0x00,
	                       0x00])
##------check parity of input address and data-------        
	    if (len(address)%2) != 0:
	        address = '0' + address           
	    if (len(data)%2) != 0:
	        data = '0' + data
##------------------------------------------------
	    try:
	        address = bytes.fromhex(address)
	    except ValueError:
	        pass
	    else:
	        try:
	            data = bytes.fromhex(data)
	        except ValueError:
	            pass
	        else:
	            if len(data) < 8:
	                data = (8 - len(data))*bytes([0x00]) + data
	            packadge = headline + address + data
	            clientSock.sendto(packadge,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
	            print(packadge.hex())##
	            print('IP назначения', DSPM_IP_ADDRESS)##
	            print('PORT назначения', DSPM_PORT_NO)##
	            print('IP оправки', IP_ADDRESS)##
	            print('все IP', socket.gethostbyname_ex(socket.getfqdn()))##
##------------------------------------------------------
def read_from_reg(address):
    headline = bytes ([0x00, 0x03,
                    0x88, 0xA6,
                    0x1F, 0x11,
                    0x80, 0x00,
                    0x00, 0x00,
                    0x00, 0x00,
                    0x00, 0x00,
                    0x00])    
    if (len(address)%2) != 0:
        address = '0' + address
    try:
        address = bytes.fromhex(address)
    except ValueError:
        return 'Проверьте правильность адреса'           
    else:    
        empty_data = bytes([0x00, 0x00,
                            0x00, 0x00,
                            0x00, 0x00,
                            0x00, 0x00])
        packadge = headline + address + empty_data
        clientSock.sendto(packadge,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
        try:
            income_pack, addr = clientSock.recvfrom(1024)
        except:
            return 'Ответ не получен\nПроверьте соединение\nили правильность запроса'
        else:
            if ((bytes([income_pack[2]]) == bytes([0x88])) and
                (bytes([income_pack[3]]) == bytes([0xA6])) and
               ((bytes([income_pack[4]]) == bytes([0xF1])) or
                (bytes([income_pack[4]]) == bytes([0x21])))and
                (bytes([income_pack[5]]) == bytes([0xA5]))):
                return income_pack
            else:#################################
            	return income_pack################
    
class RAW(Screen):
    def __init__(self, **kw):
        super(RAW, self).__init__(**kw)       
    def read(self):      
        address = self.ids.address.text
        inf = read_from_reg(address)
        try:
            self.ids.income_data.text = str(inf.hex())
        except AttributeError:
            self.ids.income_data.text = inf
    def write(self):     
        address = self.ids.address.text
        data  = self.ids.data.text
        write_to_reg(address,data)
##------when moving to TEMP or SETT window----
    def cont_drawing(self):
        global waiting
        global local_waiting
        waiting = local_waiting
##---------------------------------------        
class TEMPERATURE(Screen):
    def __init__(self, **kw):
        super(TEMPERATURE, self).__init__(**kw)       
        self.graph_1 = LinePlot(line_width = 1.2, color = [.62,.93,.25,1])
        self.graph_2 = LinePlot(line_width = 1.2, color = [.31,.42,.96,1])
        self.graph_3 = LinePlot(line_width = 1.2, color = [.96,.46,.21,1])
    def start_stop(self):
        global start_stop
        global waiting
        global update
        global write_to_file
        global time_of_creation
        global file_name
        global time_of_start
        start_stop += 1
        if start_stop == 1:                   
            waiting = 1
            file_name = []
            self.ids.switch.touch_control = False
            if self.ids.switch.active == True:
                write_to_file = True              
                time_of_creation = str(time.strftime('%d.%m.%Y_h%Hm%Ms%S'))
                for symbol in time_of_creation:
                    file_name.append(symbol)
                file_name = ("".join(file_name) + '.txt')               
                txt_creator()                
            else:
                write_to_file = False
            self.ids.start_control.text = 'СТОП'           
            self.ids.graph.add_plot(self.graph_1)
            self.ids.graph.add_plot(self.graph_2)
            self.ids.graph.add_plot(self.graph_3)
            Clock.schedule_interval(self.get_value_1, 0.001)
            Clock.schedule_interval(self.get_value_2, 0.001)
            Clock.schedule_interval(self.get_value_3, 0.001)         
        else:
            start_stop = 0
            waiting = 0
            FPGA_TEMPER_1.clear()
            FPGA_TEMPER_2.clear()
            FPGA_TEMPER_3.clear()
            self.ids.start_control.text = 'СТАРТ'
            self.ids.switch.touch_control = None
            Clock.unschedule(self.get_value_1)
            Clock.unschedule(self.get_value_2)
            Clock.unschedule(self.get_value_3)
                   
    def get_value_1(self, dt):
        self.graph_1.points = [(i,j) for i, j in enumerate(FPGA_TEMPER_1)] 
    def get_value_2(self, dt):
        self.graph_2.points = [(i,j) for i, j in enumerate(FPGA_TEMPER_2)]
    def get_value_3(self, dt):
        self.graph_3.points = [(i,j) for i, j in enumerate(FPGA_TEMPER_3)]
##------autoscale---------------------
        self.ids.graph.ymax = max_temp + 5
        self.ids.graph.ymin = min_temp - 5       
##------for control speed of updating gpaph------     
    def move(self):
        global update
        update = int(self.ids.updating_time.text)
        number_of_dots = self.ids.display_time.value/100 
        self.ids.time_of_display.text = str(int(number_of_dots*update/10))
##------updating values of label--------------------
    def display_time_changes(self):
        global update
        number_of_dots = self.ids.display_time.value/100 
        self.ids.time_of_display.text = str(int(number_of_dots*update/10))
##------when moving to RAW or CONTROL or BOOTL window-----    
    def stop_drawing(self):
        global waiting
        global local_waiting
        local_waiting = waiting
        waiting = 2
##-----------------------------------        
class CONTROL(Screen):
    def __init__(self, **kw):
        super(CONTROL, self).__init__(**kw)
##------when moving to TEMP or SETT window----
    def cont_drawing(self):
        global waiting
        global local_waiting
        waiting = local_waiting
##--------------------------------------- 
    def dismiss_popup(self):
        self._popup.dismiss()
        
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    
    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        
    def load(self, path, filename):
        global BOOTLOADER_SETTINGS_FPGA_1
        global BOOTLOADER_SETTINGS_FPGA_2
        global BOOTLOADER_SETTINGS_FPGA_3
        try:
            with open(os.path.join(path, filename[0]),'r') as stream:
                file = stream.read().split('\n')
        except:
            pass
        else:
##----------radio buttons-------------
            try:
                if (file[3] == '0'):
                    self.ids.duplication_off_01.active = True
                    self.ids.duplication_on_01.active  = False
                else:
                    self.ids.duplication_on_01.active  = True
                    self.ids.duplication_off_01.active = False                
                if (file[15] == '0'):
                    self.ids.prohibition_of_adaptation_off_44.active = True
                    self.ids.prohibition_of_adaptation_on_44.active  = False
                else:
                    self.ids.prohibition_of_adaptation_on_44.active  = True
                    self.ids.prohibition_of_adaptation_off_44.active = False               
                if (file[23] == '0'):
                    self.ids.MDF_control_register_off_48.active = True
                    self.ids.MDF_control_register_on_48.active  = False 
                else:
                    self.ids.MDF_control_register_on_48.active  = True
                    self.ids.MDF_control_register_off_48.active = False                
                if (file[37] == '0'):
                    self.ids.amplitude_unstability_on_50.active  = True
                    self.ids.amplitude_unstability_off_50.active = False
                else:
                    self.ids.amplitude_unstability_off_50.active = True
                    self.ids.amplitude_unstability_on_50.active  = False                
                if (file[39] == '0'):
                    self.ids.phase_unstability_on_51.active  = True
                    self.ids.phase_unstability_off_51.active = False 
                else:
                    self.ids.phase_unstability_off_51.active = True
                    self.ids.phase_unstability_on_51.active  = False                
                if (file[45] == '0'):
                    self.ids.phase_threshold_on_54.active  = True
                    self.ids.phase_threshold_off_54.active = False 
                else:
                    self.ids.phase_threshold_off_54.active = True
                    self.ids.phase_threshold_on_54.active  = False                
                if (file[55] == '0'):
                    self.ids.BNP_resolution_off_59.active = True
                    self.ids.BNP_resolution_on_59.active  = False
                else:
                    self.ids.BNP_resolution_on_59.active  = True
                    self.ids.BNP_resolution_off_59.active = False 
            except IndexError:
                pass
##----------bootloader----------------------                
            try:
                BOOTLOADER_SETTINGS_FPGA_1 = file[5]
                BOOTLOADER_SETTINGS_FPGA_2 = file[13]
                BOOTLOADER_SETTINGS_FPGA_3 = file[11]
            except IndexError:
                pass   
##----------text input------------------------
            try:
                self.ids.correction_register_04A.text       = file[7]
            except IndexError:
                pass
            try:
                self.ids.correction_register_04B.text       = file[9]
            except IndexError:
                pass
            try:
                self.ids.averaging_window_45.text           = file[17]
            except IndexError:
                pass
            try:
                self.ids.suppression_band_46.text           = file[19]
            except IndexError:
                pass
            try:
                self.ids.threshold_control_register_47.text = file[21]
            except IndexError:
                pass
            try:
                self.ids.period_threshold_49.text           = file[25]
            except IndexError:
                pass
            try:
                self.ids.noise_level_52.text                = file[41]
            except IndexError:
                pass
            try:
                self.ids.noise_level_excess_53.text         = file[43]
            except IndexError:
                pass
            try:
                self.ids.phase_threshold_register_55.text   = file[47]
            except IndexError:
                pass
            try:
                self.ids.phase_threshold_register_56.text   = file[49]
            except IndexError:
                pass
            try:
                self.ids.sum_delta_threshold_57.text        = file[51]
            except IndexError:
                pass
            try:
                self.ids.velocity_evaluation_58.text        = file[53]
            except IndexError:
                pass

            self.dismiss_popup()
    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write('REGISTERS\n')
            stream.write('\n')
            stream.write('Register 0x01:\n')
            if (self.ids.duplication_off_01.active == True):
                stream.write('0\n')
            else:
                stream.write('1\n')
            stream.write('Register 0x4:\n')
            stream.write(str(BOOTLOADER_SETTINGS_FPGA_1) + '\n')
            stream.write('Register 0x4A:\n')
            stream.write(str(self.ids.correction_register_04A.text) + '\n')
            stream.write('Register 0x4B:\n')
            stream.write(str(self.ids.correction_register_04B.text) + '\n')
            stream.write('Register 0x4C:\n')
            stream.write(str(BOOTLOADER_SETTINGS_FPGA_3) + '\n')
            stream.write('Register 0x24:\n')
            stream.write(str(BOOTLOADER_SETTINGS_FPGA_2) + '\n')
            stream.write('Register 0x44:\n')
            if (self.ids.prohibition_of_adaptation_off_44.active == True):
                stream.write('0\n')
            else:
                stream.write('1\n')
            stream.write('Register 0x45:\n')
            stream.write(str(self.ids.averaging_window_45.text) + '\n')
            stream.write('Register 0x46:\n')
            stream.write(str(self.ids.suppression_band_46.text) + '\n')
            stream.write('Register 0x47:\n')
            stream.write(str(self.ids.threshold_control_register_47.text) + '\n')
            stream.write('Register 0x48:\n')
            if (self.ids.MDF_control_register_off_48.active == True):
                stream.write('0\n')
            else:
                stream.write('1\n')
            stream.write('Register 0x49:\n')
            stream.write(str(self.ids.period_threshold_49.text) + '\n')
            
            stream.write('Temperature 1:\n')
            tempr_1 = read_from_reg('03')
            try: 
                tempr_1 = int.from_bytes(bytes([tempr_1[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_1) + '\n')
                
            stream.write('Temperature 2:\n')
            tempr_2 = read_from_reg('23')
            try: 
                tempr_2 = int.from_bytes(bytes([tempr_2[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_2) + '\n')
                
            stream.write('Temperature 3:\n')
            tempr_3 = read_from_reg('43')
            try: 
                tempr_3 = int.from_bytes(bytes([tempr_3[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_3) + '\n')
                
            stream.write('IP:\n')
            stream.write(str(DSPM_IP_ADDRESS) + '\n')
            stream.write('PORT:\n')
            stream.write(str(DSPM_PORT_NO) + '\n')

            stream.write('Register 0x50:\n') 
            if (self.ids.amplitude_unstability_off_50.active == True):
                stream.write('1\n')
            else:
                stream.write('0\n')
                
            stream.write('Register 0x51:\n')
            if (self.ids.phase_unstability_off_51.active == True):
                stream.write('1\n')
            else:
                stream.write('0\n')                
            stream.write('Register 0x52:\n')
            stream.write(str(self.ids.noise_level_52.text) + '\n')
            stream.write('Register 0x53:\n')
            stream.write(str(self.ids.noise_level_excess_53.text) + '\n')
            stream.write('Register 0x54:\n')
            if (self.ids.phase_threshold_off_54.active == True):
                stream.write('1\n')
            else:
                stream.write('0\n')
            stream.write('Register 0x55:\n')
            stream.write(str(self.ids.phase_threshold_register_55.text) + '\n')
            stream.write('Register 0x56:\n')
            stream.write(str(self.ids.phase_threshold_register_56.text) + '\n')
            stream.write('Register 0x57:\n')
            stream.write(str(self.ids.sum_delta_threshold_57.text) + '\n')
            stream.write('Register 0x58:\n')
            stream.write(str(self.ids.velocity_evaluation_58.text) + '\n')
            stream.write('Register 0x59:\n')
            if (self.ids.BNP_resolution_off_59.active == True):
                stream.write('0\n')
            else:
                stream.write('1\n')          
        self.dismiss_popup()
    def apply(self):
##------radio buttons------------
        if (self.ids.duplication_off_01.active == True) and (self.ids.duplication_on_01.active == False):
             write_to_reg('01', 'AC10002C00')
        elif (self.ids.duplication_off_01.active == False) and (self.ids.duplication_on_01.active == False):
            write_to_reg('01', '')
        else:
            write_to_reg('01', 'AC10002C01')

        if (self.ids.prohibition_of_adaptation_off_44.active == True) and (self.ids.prohibition_of_adaptation_on_44.active == False):
             write_to_reg('44', '00')
        elif (self.ids.prohibition_of_adaptation_off_44.active == False) and (self.ids.prohibition_of_adaptation_on_44.active == False):
            write_to_reg('44', '')
        else:
            write_to_reg('44', '01')

        if (self.ids.MDF_control_register_off_48.active == True) and (self.ids.MDF_control_register_on_48.active == False):
             write_to_reg('48', '00')
        elif (self.ids.MDF_control_register_off_48.active == False) and (self.ids.MDF_control_register_on_48.active == False):
            write_to_reg('48', '')
        else:
            write_to_reg('48', '01')

        if (self.ids.amplitude_unstability_on_50.active == True) and (self.ids.amplitude_unstability_off_50.active == False):
             write_to_reg('50', '00')
        elif (self.ids.amplitude_unstability_on_50.active == False) and (self.ids.amplitude_unstability_off_50.active == False):
            write_to_reg('50', '')
        else:
            write_to_reg('50', '01')

        if (self.ids.phase_unstability_on_51.active == True) and (self.ids.phase_unstability_off_51.active == False):
             write_to_reg('51', '00')
        elif (self.ids.phase_unstability_on_51.active == False) and (self.ids.phase_unstability_off_51.active == False):
            write_to_reg('51', '')
        else:
            write_to_reg('51', '01')

        if (self.ids.phase_threshold_on_54.active == True) and (self.ids.phase_threshold_off_54.active == False):
             write_to_reg('54', '00')
        elif (self.ids.phase_threshold_on_54.active == False) and (self.ids.phase_threshold_off_54.active == False):
            write_to_reg('54', '')
        else:
            write_to_reg('54', '01')

        if (self.ids.BNP_resolution_off_59.active  == True) and (self.ids.BNP_resolution_on_59.active  == False):
             write_to_reg('59', '00')
        elif (self.ids.BNP_resolution_off_59.active  == False) and (self.ids.BNP_resolution_on_59.active  == False):
            write_to_reg('59', '')
        else:
            write_to_reg('59', '01')
##------text input--------------
        try:
        	packadge = hex(int(self.ids.averaging_window_45.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('45', packadge[2:])

        try:
        	packadge = hex(int(self.ids.suppression_band_46.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('46', packadge[2:])

        try:
        	packadge = hex(int(self.ids.threshold_control_register_47.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('47', packadge[2:])

        try:
        	packadge = hex(int(self.ids.period_threshold_49.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('49', packadge[2:])

        try:
        	packadge = hex(int(self.ids.correction_register_04A.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('4A', packadge[2:])

        try:
        	packadge = hex(int(self.ids.correction_register_04B.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('4B', packadge[2:])

        try:
        	packadge = hex(int(self.ids.sum_delta_threshold_57.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('57', packadge[2:])

        try:
        	packadge = hex(int(self.ids.velocity_evaluation_58.text))
        except ValueError:
        	pass
        else:
        	write_to_reg('58', packadge[2:])
##------single float------------------------
        try:
        	packadge = float(self.ids.noise_level_52.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	write_to_reg('52', packadge[2:])

        try:
        	packadge = float(self.ids.noise_level_excess_53.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	write_to_reg('53', packadge[2:])

        try:
        	packadge = float(self.ids.phase_threshold_register_55.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	write_to_reg('55', packadge[2:])

        try:
        	packadge = float(self.ids.phase_threshold_register_56.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	write_to_reg('56', packadge[2:])

    def request(self):
##----------radio buttons-------------
        packadge = read_from_reg('01')
        if type(packadge) == str:
            self.ids.duplication_on_01.active  = False
            self.ids.duplication_off_01.active = False
        else:
            if (packadge[23] == 0):
                self.ids.duplication_off_01.active = True
                self.ids.duplication_on_01.active  = False
            elif (packadge[23] == 1):
                self.ids.duplication_on_01.active  = True
                self.ids.duplication_off_01.active = False

        packadge = read_from_reg('44')
        if type(packadge) == str:
            self.ids.prohibition_of_adaptation_on_44.active  = False
            self.ids.prohibition_of_adaptation_off_44.active = False
        else:
            if (packadge[23] == 0):
                self.ids.prohibition_of_adaptation_off_44.active = True
                self.ids.prohibition_of_adaptation_on_44.active  = False
            elif (packadge[23] == 1):
                self.ids.prohibition_of_adaptation_on_44.active  = True
                self.ids.prohibition_of_adaptation_off_44.active = False
                
        packadge = read_from_reg('48')
        if type(packadge) == str:
            self.ids.MDF_control_register_on_48.active  = False
            self.ids.MDF_control_register_off_48.active = False
        else:
            if (packadge[23] == 0):
                self.ids.MDF_control_register_off_48.active = True
                self.ids.MDF_control_register_on_48.active  = False
            elif (packadge[23] == 1):
                self.ids.MDF_control_register_on_48.active  = True
                self.ids.MDF_control_register_off_48.active = False
                
        packadge = read_from_reg('50')
        if type(packadge) == str:
            self.ids.amplitude_unstability_on_50.active  = False
            self.ids.amplitude_unstability_off_50.active = False
        else:
            if (packadge[23] == 0):
                self.ids.amplitude_unstability_on_50.active = True
                self.ids.amplitude_unstability_off_50.active  = False
            elif (packadge[23] == 1):
                self.ids.amplitude_unstability_off_50.active  = True
                self.ids.amplitude_unstability_on_50.active = False
                
        packadge = read_from_reg('51')
        if type(packadge) == str:           
            self.ids.phase_unstability_on_51.active  = False
            self.ids.phase_unstability_off_51.active = False
        else:
            if (packadge[23] == 0):
                self.ids.phase_unstability_on_51.active = True
                self.ids.phase_unstability_off_51.active  = False
            elif (packadge[23] == 1):
                self.ids.phase_unstability_off_51.active  = True
                self.ids.phase_unstability_on_51.active = False
                
        packadge = read_from_reg('54')
        if type(packadge) == str:
            self.ids.phase_threshold_on_54.active  = False
            self.ids.phase_threshold_off_54.active = False
        else:
            if (packadge[23] == 0):
                self.ids.phase_threshold_on_54.active = True
                self.ids.phase_threshold_off_54.active  = False
            elif (packadge[23] == 1):
                self.ids.phase_threshold_off_54.active  = True
                self.ids.phase_threshold_on_54.active = False
                
        packadge = read_from_reg('59')
        if type(packadge) == str:
            self.ids.duplication_on_01.active  = False
            self.ids.BNP_resolution_off_59.active = False
        else:
            if (packadge[23] == 0):
                self.ids.BNP_resolution_off_59.active = True
                self.ids.BNP_resolution_on_59.active  = False
            elif (packadge[23] == 1):
                self.ids.BNP_resolution_on_59.active  = True
                self.ids.BNP_resolution_off_59.active = False
##------text input--------------------
        packadge = read_from_reg('45')
        try:
            self.ids.averaging_window_45.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('46')
        try:
            self.ids.suppression_band_46.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('47')
        try:
            self.ids.threshold_control_register_47.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('49')
        try:
            self.ids.period_threshold_49.text = str(int.from_bytes(packadge[23:24], byteorder='big') )
        except TypeError:
            pass
        packadge = read_from_reg('4A')
        try:
            self.ids.correction_register_04A.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('4B')
        try:
            self.ids.correction_register_04B.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('57')
        try:
            self.ids.sum_delta_threshold_57.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = read_from_reg('58')
        try:
            self.ids.velocity_evaluation_58.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
##------float------------------------
        packadge = read_from_reg('52')
        try:
        	self.ids.noise_level_52.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = read_from_reg('53')
        try:
        	self.ids.noise_level_excess_53.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = read_from_reg('55')
        try:
        	self.ids.phase_threshold_register_55.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = read_from_reg('56')
        try:
        	self.ids.phase_threshold_register_56.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        
##----sorry I dont know how it works C:
class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
class SaveDialog(BoxLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
##-----------------------------
class BOOTLOADER_SETTINGS(Screen):
    def __init__(self,**kw):
        super(BOOTLOADER_SETTINGS,self).__init__(**kw)
        self.ids.request.text = '    Запросить данные'+'\n'+'из прочитанного файла'
##------when moving to TEMP or SETT window----
    def cont_drawing(self):
        global waiting
        global local_waiting
        waiting = local_waiting
##--------------------------------------- 
    def reconf_FPGA_1(self):
        write_to_reg('04', self.ids.reconfiguration_04.text)
    def reconf_FPGA_2(self):
        write_to_reg('24', self.ids.reconfiguration_24.text)        
    def reconf_FPGA_3(self):
        write_to_reg('4C', self.ids.reconfiguration_04C.text)

    def apply(self):
        self.reconf_FPGA_1()
        self.reconf_FPGA_2()
        self.reconf_FPGA_3()        
    def request(self):
        self.ids.reconfiguration_04.text  = BOOTLOADER_SETTINGS_FPGA_1
        self.ids.reconfiguration_24.text  = BOOTLOADER_SETTINGS_FPGA_2
        self.ids.reconfiguration_04C.text = BOOTLOADER_SETTINGS_FPGA_3
    def reset(self):
        write_to_reg('00', '00')
##------when move to another window-------
    def reconf_all(self):
        global BOOTLOADER_SETTINGS_FPGA_1
        global BOOTLOADER_SETTINGS_FPGA_2
        global BOOTLOADER_SETTINGS_FPGA_3
        BOOTLOADER_SETTINGS_FPGA_1 = self.ids.reconfiguration_04.text  
        BOOTLOADER_SETTINGS_FPGA_2 = self.ids.reconfiguration_24.text
        BOOTLOADER_SETTINGS_FPGA_3 = self.ids.reconfiguration_04C.text
##----------------------------------------
class SETTING(Screen):
    def __init__(self, **kw):
        super(SETTING, self).__init__(**kw)
        self.ids.reconf.text  = 'Применить новый IP-адрес и порт'
        ip_list = []
        for i in socket.gethostbyname_ex(socket.getfqdn())[2]:
        	ip_list.append( ' ' + i)
        self.ids.COMP_IP.values = ip_list
        self.ids.COMP_IP.text   = ip_list[0]
    def reconfig(self):
        global clientSock
        global DSPM_IP_ADDRESS
        global DSPM_PORT_NO
        global IP_ADDRESS
        clientSock.close()
        IP_ADDRESS = str(self.ids.COMP_IP.text)[1:]
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.setsockopt(socket.SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
        ##clientSock.setsockopt()
        try:
        	clientSock.bind((IP_ADDRESS, COMP_PORT_NO))
        except:
        	pass
        clientSock.settimeout(0.3)
##------try send something to check correct IP and PORT----- 
        try:
        	clientSock.sendto(bytes("", 'utf-8'),(str(self.ids.IP_DSPM.text), int(self.ids.PORT_DSPM.text)))
        except:
        	print('alarm')
        else:
        	DSPM_IP_ADDRESS = str(self.ids.IP_DSPM.text)
        	DSPM_PORT_NO    = int(self.ids.PORT_DSPM.text)
##------when moving to RAW or CONTROL or BOOTL window-----
    def stop_drawing(self):
        global waiting
        global local_waiting
        local_waiting = waiting
        waiting = 2
##--------------------------------        
sm = ScreenManager()
sm.add_widget(TEMPERATURE(name='TEMPERATURE'))
sm.add_widget(RAW(name = 'RAW'))
sm.add_widget(CONTROL(name='CONTROL'))
sm.add_widget(BOOTLOADER_SETTINGS(name='BOOTLOADER_SETTINGS'))
sm.add_widget(SETTING(name='SETTING'))

class MainApplication(App):    
    def build(self):
        return sm
    
if __name__ == '__main__':
##-----for test only-----
##IP_ADDRESS = "127.0.0.1"
##------------------------
    IP_ADDRESS = str(socket.gethostbyname(socket.getfqdn()))
    COMP_PORT_NO = 44203
    DSPM_IP_ADDRESS = "172.16.0.13"
    ##DSPM_IP_ADDRESS = "192.168.111.63 192.168.111.12"
    DSPM_PORT_NO = 65261  
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IP_MTU_DISCOVER   = 10
    IP_PMTUDISC_DONT  =  0
    clientSock.setsockopt(socket.SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
    ##clientSock.setsockopt()
    clientSock.bind((IP_ADDRESS, COMP_PORT_NO))
    clientSock.settimeout(0.3)
    
    start_stop = 0 ## for start/stop control of plotting graph  
    update = 500   ## first value of updating graph
    write_to_file = False
    FPGA_TEMPER_1 = []  
    FPGA_TEMPER_2 = []
    FPGA_TEMPER_3 = []
    max_temp = 50
    min_temp = 30
    waiting = 0 ## first state of threading (get_temperature_lev-'''el)
    
    BOOTLOADER_SETTINGS_FPGA_1 = ''
    BOOTLOADER_SETTINGS_FPGA_2 = ''
    BOOTLOADER_SETTINGS_FPGA_3 = ''
    
    get_level_thread = Thread(target = get_temperature_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    
    Window.size = (1024,768)
    Window.minimum_width = (800)
    Window.minimum_height = (600)
    
    Window.clearcolor = (.33,.34,.38,1)
    Window.show()
    MainApplication().run()
