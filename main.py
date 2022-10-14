# import kivy module
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        self.theme_style = "Dark"
        self.primary_palette = "Orange"

        superBox = BoxLayout(orientation='vertical')
        VB = BoxLayout(orientation='vertical')

        Details1 = BoxLayout(orientation='horizontal', size_hint=(1, .1))
        Details2 = BoxLayout(orientation='horizontal', size_hint=(1, .1))

        lbl1 = Label(text="Pwnagotchi.ai", size_hint =(1, .1), halign="left",font_size=22)
        lbl2 = Label(text='(o_o)', size_hint=(1, .3), font_size=50)

        lbl3 = Label(text="CH", size_hint=(.5, 1), font_size=16)
        lbl4 = Label(text="APS", size_hint=(.5, 1), font_size=16)
        lbl5 = Label(text="PWND", size_hint=(.5, 1), font_size=16)
        lbl6 = Label(text="UP", size_hint=(.5, 1), font_size=16)

        lbl7 = Label(text="This is random information.", size_hint=(1, .4),font_size=12)

        Details1.add_widget(lbl3)
        Details1.add_widget(lbl4)
        Details2.add_widget(lbl5)
        Details2.add_widget(lbl6)


        VB.add_widget(lbl1 )
        VB.add_widget(lbl2)
        VB.add_widget(Details1)
        VB.add_widget(Details2)
        VB.add_widget(lbl7)

        superBox.add_widget(VB)

        return superBox

MainApp().run()