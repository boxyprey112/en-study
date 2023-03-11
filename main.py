from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Грамматика'
      

            MDLabel:
                text: 'Mail'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Словарь'
         

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Переводчик'
            
            MDRoundFlatIconButton:
                
                text: "Перевести   "
                text_color: "black"
                line_color: "black"
                md_bg_color: "orange"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDTextFieldRect:
                hint_text: "Введите текст"
                hint_text_color: 'black'
                set_fill_color: 'black'
                size_hint: 0.5, 0.20
                height: "30dp"
                pos_hint: {"center_x": .5, "center_y": .66}
                background_color: 'orange'

            MDTextFieldRect:
                size_hint: 0.5, 0.20
                height: "30dp"
                background_color: 'orange'
                pos_hint: {"center_x": .5, "center_y": .34}
'''
        )
        


Test().run()
