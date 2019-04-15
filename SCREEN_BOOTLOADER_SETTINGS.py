from kivy.lang              import Builder

Builder.load_string("""
           
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
            on_press: root.manager.current = 'READ_AND_WRITE'
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
            size_hint:(.4,.45)
            spacing: 3
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
                    on_press: root.reconf_FPGA('04', reconfiguration_04.text)
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
                    on_press: root.reconf_FPGA('24', reconfiguration_24.text)
            Label:
                text:'4C: Настройка загрузчика ПЛИС_3'
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
                    on_press: root.reconf_FPGA('4C', reconfiguration_04C.text)
            
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
                	id: request_from_reg
                	text:''
                	bold: 'True'
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.request_from_reg()

                Button:
                    text: 'Применить все'
                    bold: 'True'
                    background_color : [.62,.93,.25,1]
                    background_normal : ''
                    color: [0,0,0,1]
                    on_press: root.apply(reconfiguration_04.text, reconfiguration_24.text, reconfiguration_04C.text)
""")