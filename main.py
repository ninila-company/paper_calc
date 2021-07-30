import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

kivy.require('1.0.6')  # replace with your current kivy version !


class MainApp(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.solution1 = TextInput(multiline=False, readonly=False, halign='left', font_size=55,
                                   hint_text='Введите начальный диаметр роля', write_tab=False,
                                   input_filter='float')
        self.solution2 = TextInput(multiline=False, readonly=False, halign='left', font_size=55,
                                   hint_text='Введите начальную массу роля', write_tab=False,
                                   input_filter='float')
        self.solution3 = TextInput(multiline=False, readonly=False, halign='left', font_size=55,
                                   hint_text='Введите диаметр остатка', write_tab=False,
                                   input_filter='float')
        self.print_result = Label()
        main_layout.add_widget(self.solution1)
        main_layout.add_widget(self.solution2)
        main_layout.add_widget(self.solution3)
        main_layout.add_widget(self.print_result)

        # КЛАВИАТУРА ДЛЯ ПРИЛОЖЕНИЯ (ПОКА УБРАЛ)
        # buttons = [
        #     ['7', '8', '9'],
        #     ['4', '5', '6'],
        #     ['1', '2', '3'],
        #     ['.', '0', 'C']
        # ]
        #
        # for row in buttons:
        #     h_layout = BoxLayout()
        #     for label in row:
        #         button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #         button.bind(on_press=self.on_button_press)
        #         h_layout.add_widget(button)
        #     main_layout.add_widget(h_layout)

        equals_button = Button(text='РЕЗУЛЬТАТ', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        if instance.text == 'C':
            self.solution1.text, self.solution2.text, self.solution3.text = '', '', ''
        else:
            if self.solution1.focus:
                self.solution1.text += instance.text
            elif self.solution2.focus:
                self.solution2.text += instance.text
            else:
                self.solution3.text += instance.text

    def on_solution(self, instance):
        if self.solution1.text and self.solution2.text and self.solution3.text:
            try:
                t = str((float(self.solution1.text) - float(self.solution3.text)) / float(2))
                y = str((float(4) * float(t) * (float(self.solution1.text) - float(t)) /
                         (float(self.solution1.text) * float(self.solution1.text) - 0.1 * 0.1) *
                         float(self.solution2.text)))
                z = str(float(self.solution2.text) - float(y))
                self.print_result.text = f'Масса остатка {round(float(z), 2)} кг'
            except AttributeError:
                self.print_result.text = 'Error'
        else:
            self.print_result.text = 'Заполните все поля'


if __name__ == '__main__':
    MainApp().run()
