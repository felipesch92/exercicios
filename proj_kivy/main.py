from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botão 1',
                        font_size=30,
                        on_release=self.incrementar)
        self.label = Label(text='1', font_size=20)
        box.add_widget(self.label)
        box.add_widget(button)
        return box

    def incrementar(self, button):
        self.label.text = str(int(self.label.text) + 1)


Teste().run()
