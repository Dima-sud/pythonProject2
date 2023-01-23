from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.formula = ""
        b1 = BoxLayout(orientation='vertical', padding=25)
        g1 = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.l1 = Label(text="0", halign='right', size_hint=(1, .25), pos=(0, 450), text_size=(400 - 50, 400 * .4 - 50), valign='center')

        b1.add_widget(self.l1)
        g1.add_widget(Button(text='9', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='8', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='7', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='/', font_size=30, on_press=self.add_operateon))
        g1.add_widget(Button(text='6', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='5', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='4', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='*', font_size=30, on_press=self.add_operateon))
        g1.add_widget(Button(text='1', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='2', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='3', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='-', font_size=30, on_press=self.add_operateon))
        g1.add_widget(Button(text='+', font_size=30, on_press=self.add_operateon))
        g1.add_widget(Button(text='0', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text=',', font_size=30, on_press=self.add_number))
        g1.add_widget(Button(text='=', font_size=30, on_press=self.add_resultate))
        b1.add_widget(g1)
        return b1

    def update_label(self):
        self.l1.text = self.formula

    def add_number(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def add_operateon(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def add_resultate(self, instance):
        self.l1.text = str(eval(self.l1.text))
MyApp().run()