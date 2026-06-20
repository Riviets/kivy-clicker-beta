from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image

from kivy import platform
from kivy.properties import NumericProperty
from kivy.clock import Clock


class MenuScreen(Screen):

    def go_game(self, *args):
        self.manager.current = 'game'

    def go_settings(self, *args):
        self.manager.current = 'settings'

    def exit(self, *args):
        app.stop()


class SettingsScreen(Screen):

    def go_menu(self, *args):
        self.manager.current = 'menu'


class Fish(Image):
    fish_current = None
    fish_index = 0
    hp_current = None

    def new_fish(self, *args):
        self.fish_current = app.LEVELS[app.LEVEL][self.fish_index]
        self.source = app.FISHES[self.fish_current]['source']
        self.hp_current = app.FISHES[self.fish_current]['hp']
        self.opacity = 1

    def defeated(self):
        self.opacity = 0

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) or not self.opacity:
            return

        game_screen = app.root.get_screen('game')

        self.hp_current -= 1
        game_screen.score += 1

        if self.hp_current <= 0:
            self.defeated()
            if len(app.LEVELS[app.LEVEL]) > self.fish_index + 1:
                self.fish_index += 1
                Clock.schedule_once(self.new_fish, 1.2)
            else:
                Clock.schedule_once(game_screen.level_complete, 1.2)
                self.fish_index = 0

        return super().on_touch_down(touch)


class GameScreen(Screen):
    score = NumericProperty(0)

    def on_pre_enter(self, *args):
        self.score = 0
        app.LEVEL = 0
        self.ids.level_complete.opacity = 0
        self.ids.fish.fish_index = 0
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        self.start_game()
        return super().on_enter(*args)

    def start_game(self):
        self.ids.fish.new_fish()

    def level_complete(self, *args):
        self.ids.level_complete.opacity = 1

    def go_menu(self, *args):
        self.manager.current = 'menu'

class ClickerApp(App):

    LEVEL = 0

    FISHES = {
        'fish1': {'source': 'assets/images/fish_01.png', 'hp': 10},
        'fish2': {'source': 'assets/images/fish_02.png', 'hp': 20},
    }
    
    LEVELS = [
        ['fish1', 'fish1', 'fish2']
    ]

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if platform != 'android':
    Window.size = (350, 650)

app = ClickerApp()
app.run()
