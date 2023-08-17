import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class CounterApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0

    def build(self):
        root = BoxLayout(orientation='vertical')

        label = Label(text=str(self.counter))
        root.add_widget(label)

        button_increment = Button(text='Increment')
        button_increment.bind(on_press=self.increment_counter)
        root.add_widget(button_increment)

        button_decrement = Button(text='Decrement')
        button_decrement.bind(on_press=self.decrement_counter)
        root.add_widget(button_decrement)

        return root

    def increment_counter(self):
        self.counter += 1
        label.text = str(self.counter)

    def decrement_counter(self):
        self.counter -= 1
        label.text = str(self.counter)


if __name__ == '__main__':
    CounterApp().run()
