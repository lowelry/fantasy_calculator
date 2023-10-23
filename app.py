# from flet import *
from utils.extras import *
from pages.login_page import LogInPage
from service.validation import *


class WindowDrag(UserControl):
    def __init__(self):
        super().__init__()
        # self.color = color

    def build(self):
        return Container(content=WindowDragArea(height=10, content=Container(bgcolor='grey')))


class App(UserControl):
    def __init__(self, pg: Page):
        super().__init__()
        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT
        pg.window_width = base_wigth
        pg.window_height = base_height
        pg.theme_mode = "Light"
        pg.fonts = {
            "Sansation": "https://github.com/google/fonts/raw/990be3ed8f77e31c26bf07b148d6a74b8e6241cf/ofl/sansation/"
                         "Sansation-Regular.ttf",
        }
        pg.theme = Theme(font_family="Sansation")
        pg.window_center()

        self.pg = pg
        self.pg.spacing = 0
        self.start_page = LogInPage(self.validate_inputs)
        self.screen_views = Stack(
            controls=[
                self.start_page
            ]
        )
        self.init_helper()

    def validate_inputs(self, e):
        # валидация ввода ID
        self.start_page.input_leagueid.content.value = is_valid_input_str(self.start_page.input_leagueid.content.value)
        self.start_page.update()

        # валидация ввода года
        self.start_page.input_leagueyr.content.value = is_valid_input_str(self.start_page.input_leagueyr.content.value)
        self.start_page.update()

    def init_helper(self):
        self.pg.add(
          WindowDrag(),
          self.screen_views
        )


app(target=App, assets_dir='assets')
