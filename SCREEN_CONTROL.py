from kivy.lang              import Builder

Builder.load_string("""
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
            on_press: root.manager.current = 'READ_AND_WRITE'
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
                                text:' 4A: Регистр коррекции коэффициента САМ'
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
                                text:'4B: Регистр коррекции коэффициента САМ'
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
""")