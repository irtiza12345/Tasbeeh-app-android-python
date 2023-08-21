import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CounterApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = self.load_count()  # Load previous count

    def build(self):
        root = BoxLayout(orientation='vertical')

        self.label = Label(text=str(self.counter))
        root.add_widget(self.label)

        button_increment = Button(text='Increment')
        button_increment.bind(on_press=self.increment_counter)
        root.add_widget(button_increment)

        button_decrement = Button(text='Decrement')
        button_decrement.bind(on_press=self.decrement_counter)
        root.add_widget(button_decrement)

        button_reset = Button(text='Reset')
        button_reset.bind(on_press=self.reset_counter)
        root.add_widget(button_reset)

        return root

    def increment_counter(self, instance):
        self.counter += 1
        self.update_label()

    def decrement_counter(self, instance):
        self.counter -= 1
        self.update_label()

    def reset_counter(self, instance):
        self.counter = 0
        self.update_label()

    def update_label(self):
        self.label.text = str(self.counter)
        self.save_count()  # Save current count

    def load_count(self):
        try:
            with open("count.txt", "r") as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_count(self):
        with open("count.txt", "w") as f:
            f.write(str(self.counter))

if __name__ == '__main__':
    CounterApp().run()
