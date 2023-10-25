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
        self.login_page.input_leagueyr.content.value = is_valid_input_str(self.login_page.input_leagueyr.content.value)
        self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
            focused_border_color = positive_color
        self.login_page.update()

    def show_btn_click(self, e, another_league_flag=0):

        # проверяем есть ли флаг нажатия на ссылку очистки полей

        if another_league_flag == 1:

            # если да, устанавливаем значение полей и сообщения об ошибке в ноль и обновляем страницу

            self.login_page.input_leagueid.content.value = self.login_page.input_leagueyr.content.\
                value = self.login_page.error_field.content.value = ""
            self.login_page.update()

        else:

            # если нет, то передаем значения полей в переменную и вызываем функцию конечной валидации этих полей

            inputid = self.login_page.input_leagueid.content.value
            inputyr = self.login_page.input_leagueyr.content.value

            # проверяем итоговую валидацию полей "print_data_from_inputs"

            if print_data_from_inputs(inputid, inputyr)[0] == "Please enter correct year":

                # если текстовый результат - ошибка количества символов в поле года, то выводим кастомное сообщение об
                # ошибке, устанавливаем цвет бордера поля под фокусом в красный, обновляем страницу, наводим фокус на
                # поле

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.input_leagueyr.content.focused_border_color = negative_color
                self.login_page.update()
                self.login_page.input_leagueyr.content.focus()

            elif print_data_from_inputs(inputid, inputyr)[0] == "Please enter correct league ID":

                # если текстовый результат - ошибка количества символов в поле id, то выводим кастомное сообщение об
                # ошибке, устанавливаем цвет бордера поля под фокусом в красный, обновляем страницу, наводим фокус на
                # поле

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.input_leagueid.content.focused_border_color = negative_color
                self.login_page.update()
                self.login_page.input_leagueid.content.focus()

            elif print_data_from_inputs(inputid, inputyr)[0] == ("It seems that access to viewing this league is "
                                                                 "limited"):

                # если текстовый результат - ошибка прав на получение данных (ошибка запроса 401), то выводим
                # кастомное сообщение об ошибке, обновляем страницу

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.update()

            elif print_data_from_inputs(inputid, inputyr)[0] == ("I can't find a league with that ID for this "
                                                                 "year\nPlease check your data and try again"):

                # если текстовый результат - ошибка лига с такими данными не существует (ошибка запроса 404), то
                # выводим кастомное сообщение об ошибке, обновляем страницу

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.update()

            elif print_data_from_inputs(inputid, inputyr)[0] == ("Something went wrong\nPlease contact me "
                                                                 "https://t.me/lowbylow"):

                # если текстовый результат - неизвестная ошибка (ошибка запроса не равная 200, 401, 404), то
                # выводим кастомное сообщение об ошибке, обновляем страницу

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.update()

            else:

                # в остальных случаях запрос на получение данных будет успешным, выводим в стоку сообщений об ошибках
                # название перовой команды из списка полученного в запросе, обновляем страницу, проверяем был ли
                # установлен чекбокс на сохранение введенных данных для следующей сессии:
                # *если value чекбокса == True - перезаписываем данные полей в файл
                # *если value чекбокса == False - перезаписываем в файл пустую строку

                self.login_page.error_field.content.value = print_data_from_inputs(inputid, inputyr)[0]
                self.login_page.update()
                if self.login_page.chk_save_bx.content.value:
                    with open("assets/data_files/league_login_data_save.txt", "w") as file:
                        file.write(inputid+inputyr)
                else:
                    with open("assets/data_files/league_login_data_save.txt", "w") as file:
                        file.write("")

    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            self.screen_views
        )


app(target=App, assets_dir='assets')
