from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (350, 650)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        title_lbl = Label(text = 'Main Menu', 
                          font_size='40sp', size_hint=(1, 0.4))
        layout.add_widget(title_lbl)
        
        game_btn = Button(text='Game', font_size='20sp', size_hint=(1, 0.2))
        game_btn.bind(on_press=self.go_game)
        layout.add_widget(game_btn)

        settings_btn = Button(text='Settings', font_size='20sp', size_hint=(1, 0.2))
        settings_btn.bind(on_press=self.go_settings)
        layout.add_widget(settings_btn)

        exit_btn = Button(text='exit', font_size='20sp', size_hint=(1, 0.2))
        exit_btn.bind(on_press=self.exit)
        layout.add_widget(exit_btn)

        self.add_widget(layout)

    def go_game(self, *args):
        self.manager.current = 'game'

    def go_settings(self, *args):
        self.manager.current = 'settings'

    def exit(self, *args):
        app.stop()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        title_lbl = Label(text = 'GAME', 
                          font_size='40sp', size_hint=(1, 0.4))
        layout.add_widget(title_lbl)

        exit_btn = Button(text='Menu', font_size='20sp', size_hint=(1, 0.2))
        exit_btn.bind(on_press=self.go_menu)
        layout.add_widget(exit_btn)

        self.add_widget(layout)
    
    def go_menu(self, *args):
        self.manager.current = 'menu'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        title_lbl = Label(text = 'Settings', 
                          font_size='40sp', size_hint=(1, 0.4))
        layout.add_widget(title_lbl)

        exit_btn = Button(text='Menu', font_size='20sp', size_hint=(1, 0.2))
        exit_btn.bind(on_press=self.go_menu)
        layout.add_widget(exit_btn)

        self.add_widget(layout)
    
    def go_menu(self, *args):
        self.manager.current = 'menu'

class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm
    
app = ClickerApp()
app.run()
