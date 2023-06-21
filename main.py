import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MenuApp(App):
    def build(self):
        # Crear el layout principal
        layout = BoxLayout(orientation='vertical')

        # Crear los botones del menú
        button1 = Button(text='Opción 1')
        button1.bind(on_release=self.option1_selected)
        layout.add_widget(button1)

        button2 = Button(text='Opción 2')
        button2.bind(on_release=self.option2_selected)
        layout.add_widget(button2)

        button3 = Button(text='Opción 3')
        button3.bind(on_release=self.option3_selected)
        layout.add_widget(button3)

        return layout

    def option1_selected(self, instance):
        print('Opción 1 seleccionada')

    def option2_selected(self, instance):
        print('Opción 2 seleccionada')

    def option3_selected(self, instance):
        print('Opción 3 seleccionada')

if __name__ == '__main__':
    MenuApp().run()
