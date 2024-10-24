from utils.extras import *
from pages.new_login_page import LogInPage
from pages.main_data_page import MainDataPage
from services.validation import *

league = None
teams_titles_list = None


class WindowDrag(UserControl):
    def __init__(self):
        super().__init__()
        # self.color = color

    def build(self):
        return Container(content=WindowDragArea(height=30, content=Container(bgcolor=base_bg_color, border=border.only(
            bottom=ft.border.BorderSide(0.5, "#DCDCDC")))))


class App(UserControl):
    def __init__(self, pg: Page):
        super().__init__()
        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT
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
        self.main_data_page = MainDataPage(self.close_btn_click, self.on_radio_change_0,
                                           self.on_radio_change_1, self.on_radio_change_2, self.on_radio_change_3,
                                           self.on_radio_change_4, self.on_radio_change_5, self.on_radio_change_6,
                                           self.on_radio_change_7, self.on_radio_change_8, self.on_radio_change_9,
                                           self.on_radio_change_10, self.on_radio_change_11, self.on_radio_change_12,
                                           self.on_radio_change_13, self.on_radio_change_14, self.on_radio_change_15,
                                           self.on_dropdown_change)
        self.screen_views = Stack(
            controls=[
                self.login_page,
            ]
        )
        self.init_helper()

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
            # проверяем итоговую валидацию полей "print_data_from_inputs"
            if validation_result[0] == "Please enter correct year":
                # если текстовый результат - ошибка количества символов в поле года, то выводим кастомное сообщение об
                # ошибке, устанавливаем цвет бордера поля под фокусом в красный, обновляем страницу, наводим фокус на
                # поле
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.input_leagueyr.content.focused_border_color = negative_color
                self.login_page.update()
                self.login_page.input_leagueyr.content.focus()
            elif validation_result[0] == "Please enter correct league ID":
                # если текстовый результат - ошибка количества символов в поле id, то выводим кастомное сообщение об
                # ошибке, устанавливаем цвет бордера поля под фокусом в красный, обновляем страницу, наводим фокус на
                # поле
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.input_leagueid.content.focused_border_color = negative_color
                self.login_page.update()
                self.login_page.input_leagueid.content.focus()
            elif validation_result[0] == "It seems that access to viewing this league is limited":
                # если текстовый результат - ошибка прав на получение данных (ошибка запроса 401), то выводим
                # кастомное сообщение об ошибке, обновляем страницу
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.update()
            elif validation_result[0] == ("I can't find a league with that ID for this year\nPlease check your data "
                                          "and try again"):
                # если текстовый результат - ошибка лига с такими данными не существует (ошибка запроса 404), то
                # выводим кастомное сообщение об ошибке, обновляем страницу
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.update()
            elif validation_result[0] == "Something went wrong\nPlease contact me https://t.me/lowbylow":
                # если текстовый результат - неизвестная ошибка (ошибка запроса не равная 200, 401, 404), то
                # выводим кастомное сообщение об ошибке, обновляем страницу
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.update()
            else:
                # в остальных случаях воспроизводим анимацию
                if self.login_page.trasfer_from_login_to_animation.content == self.login_page.login_elements:
                    self.login_page.trasfer_from_login_to_animation.content = self.login_page.loading_animation
                # обращаемся к глобальной переменной лиги, передаем в нее данные из полей логина, запрашиваем список
                # команд, обращаемся к глобальной переменной списка команд и передаем в нее преобразованный в набор
                # опций список и передаем список опций в дпордаун
                global league
                league = validation_result[2]
                teams = league.teams
                global teams_titles_list
                teams_titles_list = list(
                    (((" ".join(map(str, teams))).replace("Team(", "")).replace(")", ".")).split(". "))
                options_list = [ft.dropdown.Option(option) for option in teams_titles_list]
                self.main_data_page.teams_dropdown.content.options = options_list
                # записываем в строку ошибок информационное сообщение с успешным собержанием, обновляем страницу
                self.login_page.error_field.content.value = validation_result[0]
                self.login_page.update()
                # если чек-бокс на созранение стоял, то перезаписываем строку в файле, если не слоял, то не
                # перезаписываем, делаем задержку в 7.5 секунд для анимации и переключаемся на страницу данных
                if self.login_page.chk_save_bx.content.value:
                    with open("assets/data_files/league_login_data_save.txt", "w") as file:
                        file.write(inputid+inputyr)
                else:
                    with open("assets/data_files/league_login_data_save.txt", "w") as file:
                        file.write("")
                time.sleep(0.5)
                self.switch_page()

    def on_radio_change_0(self, e):
        # опрашиваем состояние радиокнопок, после чего делаем перемножение, чтобы вычислить ожидаемое количество очков,
        # устанавливаем ожидаемое количество очков в ячейку и перезагружаем страницу
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow0.cells[3].content.value) * selected_value
        self.main_data_page.DataRow0.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_1(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow1.cells[3].content.value) * selected_value
        self.main_data_page.DataRow1.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_2(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow2.cells[3].content.value) * selected_value
        self.main_data_page.DataRow2.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_3(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow3.cells[3].content.value) * selected_value
        self.main_data_page.DataRow3.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_4(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow4.cells[3].content.value) * selected_value
        self.main_data_page.DataRow4.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_5(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow5.cells[3].content.value) * selected_value
        self.main_data_page.DataRow5.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_6(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow6.cells[3].content.value) * selected_value
        self.main_data_page.DataRow6.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_7(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow7.cells[3].content.value) * selected_value
        self.main_data_page.DataRow7.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_8(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow8.cells[3].content.value) * selected_value
        self.main_data_page.DataRow8.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_9(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow9.cells[3].content.value) * selected_value
        self.main_data_page.DataRow9.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_10(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow10.cells[3].content.value) * selected_value
        self.main_data_page.DataRow10.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_11(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow11.cells[3].content.value) * selected_value
        self.main_data_page.DataRow11.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_12(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow12.cells[3].content.value) * selected_value
        self.main_data_page.DataRow12.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_13(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow13.cells[3].content.value) * selected_value
        self.main_data_page.DataRow13.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_14(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow14.cells[3].content.value) * selected_value
        self.main_data_page.DataRow14.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_radio_change_15(self, e):
        selected_value = int(e.control.value)
        result = float(self.main_data_page.DataRow15.cells[3].content.value) * selected_value
        self.main_data_page.DataRow15.cells[5].content.value = f"{result:.2f}"
        self.main_data_page.update()

    def on_dropdown_change(self, e):
        # запрашиваем состояние дропдауна, обращаемся к глобальной переменной списка команд, определяем индекс выбранной
        # команды в общем списке команд из глобальной переменной куда мы занесли список в кнопке show_btn_click,
        # устанавливаем в поле дропдауна выбранную команду
        selected_team = e.control.value
        global teams_titles_list
        team_index = teams_titles_list.index(selected_team)
        self.main_data_page.teams_dropdown.content.value = selected_team
        # определяем порядок ортировки данных об игроках согласно позициям
        position_order = ["PG", "SG", "SF", "PF", "C", "BE", "IR"]

        def get_position_order(player):
            # задаем функцию сортировки
            return position_order.index(player["position"])

        def colleсt_and_sort_players_info():
            # задаем функцию сбора всех информации по игрокам для таблицы данных в единый объект
            players_info = []
            for name_number, player in enumerate(league.teams[team_index].roster):
                name = player.name
                position = league.teams[team_index].roster[name_number].lineupSlot
                avg_points = league.teams[team_index].roster[name_number].avg_points
                injury = league.teams[team_index].roster[name_number].injuryStatus.lower()
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
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[0].content.value = players_data[i]["position"]
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[1].content.value = players_data[i]["name"]
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[2].content.value = players_data[i]["injury"]
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[3].content.value = \
                f'{players_data[i]["avg_points"]:.2f}'
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[4].content.value = None
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[4].content.disabled = False
            self.main_data_page.__getattribute__(f'DataRow{i}').cells[5].content.value = ''
        self.main_data_page.update()

    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            self.screen_views
        )


app(target=App, assets_dir='assets')
