from utils.extras import *


def chk_previous_session_login_data():
    pre_log_data = ["", "", False]
    with open("assets/data_files/league_login_data_save.txt", "r") as file:
        previous_login_data = file.read()
    if previous_login_data != "":
        pre_log_data = [previous_login_data[:10], previous_login_data[10:14], True]
        return pre_log_data
    else:
        return pre_log_data


class LogInPage(Container):
    def __init__(self, validate_inputs, show_btn_click):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)
        self.validate_inputs = validate_inputs
        self.show_btn_click = show_btn_click

        self.espn_logo = Container(
            # основное лого
            width=espn_logo_wigth,
            padding=padding.only(top=espn_logo_top_offset),
            alignment=alignment.center,
            content=Image(
                src='assets/images/espn_fantasy_basketball_logo-1.jpg',
            )
        )

        self.input_leagueid = Container(
            # поле номера лиги
            padding=padding.only(top=inputs_top_offset),
            content=TextField(
                value=chk_previous_session_login_data()[0],
                height=inputs_height,
                width=inputs_wigth,
                max_length=10,
                counter_text="",
                counter_style=TextStyle(size=0),
                hint_text='LEAGUE ID',
                bgcolor=base_bg_color,
                border=InputBorder.OUTLINE,
                border_radius=10,
                border_width=0.5,
                focused_border_color=positive_color,
                focused_border_width=2.5,
                focused_bgcolor=base_bg_color,
                text_align=TextAlign.CENTER,
                hint_style=TextStyle(
                    size=18,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                ),
                text_style=TextStyle(
                    size=18,
                    color=input_hint_color
                ),
                tooltip="espn basketball\nfantasy 10-digits\nleagues number",
                on_change=self.validate_inputs
            )
        )

        self.input_leagueyr = Container(
            # поле года лиги
            padding=padding.only(top=inputs_top_offset),
            content=TextField(
                value=chk_previous_session_login_data()[1],
                height=inputs_height,
                width=inputs_wigth,
                max_length=4,
                counter_text="",
                counter_style=TextStyle(size=0),
                hint_text='LEAGUE YR',
                bgcolor=base_bg_color,
                border=InputBorder.OUTLINE,
                border_radius=10,
                border_width=0.5,
                focused_border_color=positive_color,
                focused_border_width=2.5,
                focused_bgcolor=base_bg_color,
                text_align=TextAlign.CENTER,
                hint_style=TextStyle(
                    size=18,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                ),
                text_style=TextStyle(
                    size=18,
                    color=input_hint_color
                ),
                tooltip='league year: 20xx',
                on_change=self.validate_inputs
            )
        )

        self.show_btn = Container(
            # кнопка шоу
            content=Text(
                value='SHOW',
                size=18,
                color=input_hint_color,
                weight=FontWeight.NORMAL
            ),
            height=btn_height,
            width=btn_wigth,
            bgcolor=positive_color,
            border_radius=10,

            alignment=alignment.center,
            on_click=self.show_btn_click
        )

        self.chk_save_bx = Container(
            # чекбокс запонимания лиги на следующую сессию
            height=30,
            width=230,
            alignment=alignment.top_left,
            padding=padding.only(left=-37, top=-2),
            # bgcolor="GREY",
            content=Checkbox(
                scale=0.8,
                value=chk_previous_session_login_data()[2],
                label="Save for the next session",
                fill_color={MaterialState.HOVERED: positive_color},
            ),
        )

        self.anothe_league_link = Container(
            # ссылка на очистку полей
            height=30,
            width=130,
            # bgcolor="GREY",
            alignment=alignment.top_right,
            padding=padding.only(top=6),
            content=Text(
                size=14.5,
                weight=FontWeight.NORMAL,
                font_family="Sansation",
                spans=[
                    TextSpan(
                        style=TextStyle(decoration=TextDecoration.UNDERLINE),
                        text="Another League",
                        on_click=lambda e: self.show_btn_click(self, 1)
                    )
                ]
            )
        )

        self.error_field = Container(
            # строка с сообщением об ошибке входа
            content=Text(
                value='',
                size=12,
                color="#ff9600",
                weight=FontWeight.NORMAL,
                text_align=TextAlign.CENTER,
                selectable=True
            ),
            height=60,
            width=btn_wigth,
            alignment=alignment.center
        )

        self.loading_animation = Container(
            # анимация загрузки
            height=base_window_height,
            width=btn_wigth,
            padding=padding.only(top=60),
            content=Image(
                src='assets/images/animated_ball_loading.gif',
            )
        )

        self.loginpage_elements = Container(
            # контейнер содержимого страницы
            content=Column(
                controls=[
                    self.espn_logo,
                    Row(
                        # строка с номером и годом лиги
                        width=espn_logo_wigth,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.input_leagueid,
                            self.input_leagueyr
                        ]
                    ),
                    self.show_btn,
                    Row(
                        # строка с чекбоксом и ссылкой
                        width=espn_logo_wigth,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.chk_save_bx,
                            self.anothe_league_link
                        ]
                    ),
                    self.error_field
                ]
            )
        )

        self.content = Container(
            # базовый контейнер страницы
            height=base_window_height,
            width=base_window_wigth,
            bgcolor=base_bg_color,
            alignment=alignment.center,
            content=self.loginpage_elements
        )
