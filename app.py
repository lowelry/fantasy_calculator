from utils.extras import *
from pages.login_page import LogInPage
from pages.main_data_page import MainDataPage
from services.validation import *


class WindowDrag(UserControl):
    def __init__(self):
        super().__init__()
        # self.color = color

    def build(self):
        return Container(content=WindowDragArea(height=10, content=Container(bgcolor=colors.TRANSPARENT)))


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
        self.login_page = LogInPage(self.validate_inputs, self.show_btn_click)
        self.main_data_page = MainDataPage()
        self.screen_views = Stack(
            controls=[
                self.login_page,
                # self.main_data_page
            ]
        )
        self.init_helper()

    # def switch_to_main_data_page(self):
    #     # Измените размер окна
    #     self.pg.window_width = self.pg.window_width * 2  # Увеличьте ширину вдвое
    #     self.pg.window_height = new_height  # Здесь укажите новую высоту окна
    #
    #     # Замените текущее содержимое на main_data_page
    #     self.screen_views.controls = [self.main_data_page]

    def validate_inputs(self, e):
        # валидация ввода ID
        self.login_page.input_leagueid.content.value = is_valid_input_str(self.login_page.input_leagueid.content.value)
        self.login_page.input_leagueyr.content.focused_border_color = positive_color
        self.login_page.input_leagueid.content.focused_border_color = positive_color
        self.login_page.update()

        # валидация ввода года
        self.login_page.input_leagueyr.content.value = is_valid_input_str(self.login_page.input_leagueyr.content.value)
        self.login_page.update()

    def show_btn_click(self, e):
        inputid = self.login_page.input_leagueid.content.value
        inputyr = self.login_page.input_leagueyr.content.value
        self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
        if print_data_from_inputs(inputid, inputyr)[0] == "Please enter correct year":
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueyr.content.focused_border_color = negative_color
            self.login_page.update()
            self.login_page.input_leagueyr.content.focus()
        elif print_data_from_inputs(inputid, inputyr)[0] == "Please enter correct league ID":
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueid.content.focused_border_color = negative_color
            self.login_page.update()
            self.login_page.input_leagueid.content.focus()
        elif print_data_from_inputs(inputid, inputyr)[0] == "It seems that access to viewing this league is limited":
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
                focused_border_color = positive_color
            self.login_page.update()
        elif print_data_from_inputs(inputid, inputyr)[0] == ("I can't find a league with that ID for this year\nPlease "
                                                             "check your data and try again"):
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
                focused_border_color = positive_color
            self.login_page.update()
        elif print_data_from_inputs(inputid, inputyr)[0] == ("Something went wrong\nPlease contact me "
                                                             "https://t.me/lowbylow"):
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
                focused_border_color = positive_color
            self.login_page.update()
        else:
            self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
            self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
                focused_border_color = positive_color
            self.login_page.update()

    def init_helper(self):
        self.pg.add(
          WindowDrag(),
          self.screen_views
        )


app(target=App, assets_dir='assets')
