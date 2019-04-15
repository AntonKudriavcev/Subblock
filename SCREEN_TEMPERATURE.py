from kivy.lang              import Builder

Builder.load_string("""
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
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
            on_press: root.stop_drawing()
            on_press: root.refresh_socket()
            on_press: root.manager.current = 'READ_AND_WRITE'           
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
            on_press: root.refresh_socket()
            on_press: root.manager.current = 'CONTROL'
        Button:
            text : 'Настройки загрузчика'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.stop_drawing()
            on_press: root.socket_close()
            on_press: root.manager.current = 'BOOTLOADER_SETTINGS'
        Button:
            text : 'Сетевые настройки'
            bold: 'True'
            background_color : [.22,.22,.26,1]
            background_normal : ''
            on_press: root.stop_drawing()
            on_press: root.refresh_socket()
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

                    ToggleButton:
                        id: start_control
                        text: "СТАРТ"
                        font_size: 20
                        bold: True
                        color: [0,0,0,1]
                        background_color : [.62,.93,.25,1]
                        background_normal : ''
                        on_press: root.start_stop(start_control)   
""")