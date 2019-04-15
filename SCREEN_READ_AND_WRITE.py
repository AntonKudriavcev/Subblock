from kivy.lang              import Builder

Builder.load_string("""
<READ_AND_WRITE>:
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
            on_press: root.socket_close()
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
""")