from collections import OrderedDict
from pathlib import Path
from typing import Dict, List, Optional
from utils.extras import *
from pages.new_login_page import LogInPage
from pages.main_data_page import MainDataPage
from services.validation import *
import logging


class WindowDrag(UserControl):
    def __init__(self):
        super().__init__()
        # self.color = color

    def build(self):
        return Container(content=WindowDragArea(height=30, content=Container(bgcolor=base_bg_color, border=border.only(
            bottom=ft.border.BorderSide(0.5, "#DCDCDC")))))


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class App(UserControl):
    def __init__(self, pg: Page):
        super().__init__()
        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT
        pg.window_resizable = False
        pg.window_width = base_window_wigth
        pg.window_height = base_window_height
        pg.theme_mode = "Light"
        pg.fonts = {
            "Sansation": "https://github.com/google/fonts/raw/990be3ed8f77e31c26bf07b148d6a74b8e6241cf/ofl/sansation/"
                         "Sansation-Regular.ttf",
        }
        pg.theme = Theme(font_family="Sansation")
        pg.window_center()

        self.pg = pg
        self.pg.spacing = 0
        self.login_page = LogInPage(self.validate_inputs, self.show_btn_click, self.close_btn_click)
        self.error_handlers: Dict[str, Optional[TextField]] = {
            "Please enter correct year": self.login_page.input_leagueyr.content,
            "Please enter correct league ID": self.login_page.input_leagueid.content,
            "It seems that access to viewing this league is limited": None,
            ("I can't find a league with that ID for this year\nPlease check your data "
             "and try again"): None,
            "Something went wrong\nPlease contact me https://t.me/lowbylow": None,
        }
        self.league = None
        self.teams_titles_list: List[str] = []
        radio_handlers = [self._make_radio_handler(i) for i in range(16)]
        self.main_data_page = MainDataPage(
            self.close_btn_click,
            *radio_handlers,
            on_dropdown_change=self.on_dropdown_change,
        )
        self.screen_views = Stack(
            controls=[
                self.login_page,
            ]
        )
        self.init_helper()

    # region helpers
    def _set_error(self, message: str, field: Optional[TextField] = None):
        self.login_page.error_field.content.value = message
        if field is not None:
            field.focused_border_color = negative_color
            field.focus()
        self.login_page.update()

    def _handle_successful_validation(self, inputid: str, inputyr: str, validation_result):
        if self.login_page.trasfer_from_login_to_animation.content == self.login_page.login_elements:
            self.login_page.trasfer_from_login_to_animation.content = self.login_page.loading_animation

        self.league = validation_result[2]
        teams = self.league.teams

        self.teams_titles_list = [
            entry.replace("Team(", "").replace(")", "")
            for entry in " ".join(map(str, teams)).split(") ")
            if entry
        ]

        options_list = [ft.dropdown.Option(option) for option in self.teams_titles_list]
        self.main_data_page.teams_dropdown.content.options = options_list

        self.login_page.error_field.content.value = validation_result[0]
        self.login_page.update()

        with open("assets/data_files/league_login_data_save.txt", "w") as file:
            if self.login_page.chk_save_bx.content.value:
                file.write(inputid + inputyr)
            else:
                file.write("")

        time.sleep(0.5)
        self.switch_page()

    def _update_expected_points(self, row_index: int, control_value: str):
        selected_value = int(control_value)
        data_row = getattr(self.main_data_page, f"DataRow{row_index}")
        result = float(data_row.cells[3].content.value) * selected_value
        data_row.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def _make_radio_handler(self, row_index: int):
        def handler(e):
            self._update_expected_points(row_index, e.control.value)

        return handler

    # endregion

    def switch_page(self):
        # функция смены страниц: очищаем текущий вид, заполняем текущий вид другой страницей, обновляем страницу
        self.screen_views.controls.clear()
        self.screen_views.controls.append(self.main_data_page)
        self.screen_views.update()

    def validate_inputs(self, e):
        # проверяем валидацию полей ввода при каждом новом символе функцией is_valid_input_str, после изменения
        # устанавливаем бордер под фокусом в синий, обновляем страницу
        self.login_page.input_leagueid.content.value = is_valid_input_str(self.login_page.input_leagueid.content.value)
        self.login_page.input_leagueyr.content.value = is_valid_input_str(self.login_page.input_leagueyr.content.value)
        self.login_page.input_leagueyr.content.focused_border_color = self.login_page.input_leagueid.content.\
            focused_border_color = positive_color
        self.login_page.update()

    def close_btn_click(self, e):
        self.pg.window_destroy()

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
            validation_result = print_data_from_inputs(inputid, inputyr)

            message = validation_result[0]
            if message in self.error_handlers:
                self._set_error(message, self.error_handlers[message])
                return

            self._handle_successful_validation(inputid, inputyr, validation_result)

    def on_dropdown_change(self, e):
        # запрашиваем состояние дропдауна, обращаемся к глобальной переменной списка команд, определяем индекс выбранной
        # команды в общем списке команд из глобальной переменной куда мы занесли список в кнопке show_btn_click,
        # устанавливаем в поле дропдауна выбранную команду
        selected_team = e.control.value
        team_index = self.teams_titles_list.index(selected_team)
        self.main_data_page.teams_dropdown.content.value = selected_team
        # определяем порядок ортировки данных об игроках согласно позициям
        position_order = ["PG", "SG", "SF", "PF", "C", "BE", "IR"]
        order_map = {position: idx for idx, position in enumerate(position_order)}

        def get_position_order(player):
            # задаем функцию сортировки
            return order_map.get(player["position"], len(order_map))

        def colleсt_and_sort_players_info():
            # задаем функцию сбора всех информации по игрокам для таблицы данных в единый объект
            players_info = []
            for name_number, player in enumerate(self.league.teams[team_index].roster):
                name = player.name
                position = self.league.teams[team_index].roster[name_number].lineupSlot
                avg_points = self.league.teams[team_index].roster[name_number].avg_points
                injury = self.league.teams[team_index].roster[name_number].injuryStatus.lower()
                players_info.append({"name": name, "position": position, "avg_points": avg_points, "injury": injury})
            players_sorted = sorted(players_info, key=get_position_order)
            # добивка листа еще одним игроком, если IR пустой
            if len(players_sorted) < 16:
                empty_player = {
                    "name": "",
                    "position": "",
                    "avg_points": 0.00,
                    "injury": ""
                }
                players_sorted.append(empty_player)
            return players_sorted
        players_data = colleсt_and_sort_players_info()
        # передаем данные в ячейки, а также обновляем состояние радиобаттонов и рассчитанный результат Week AVR
        for i in range(16):
            row = getattr(self.main_data_page, f"DataRow{i}")
            row.cells[0].content.value = players_data[i]["position"]
            row.cells[1].content.value = players_data[i]["name"]
            row.cells[2].content.value = players_data[i]["injury"]
            row.cells[3].content.value = f'{players_data[i]["avg_points"]:.2f}'
            row.cells[4].content.value = None
            row.cells[4].content.disabled = False
            row.cells[5].content.value = ''
        self.main_data_page.update()

    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            self.screen_views
        )


app(target=App, assets_dir='assets')
