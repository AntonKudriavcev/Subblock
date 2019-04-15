from kivy.lang              import Builder

Builder.load_string("""
            
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
            on_press: root.manager.current = 'READ_AND_WRITE'
        Button:
            text : 'Температура ПЛИС'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.cont_drawing()
            on_press: root.manager.current = 'TEMPERATURE'
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
            on_press: root.socket_close()
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