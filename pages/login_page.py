from utils.extras import *


class LogInPage(Container):
    def __init__(self, validate_inputs, show_btn_click):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)
        self.validate_inputs = validate_inputs
        self.show_btn_click = show_btn_click

        self.input_leagueid = Container(
            # поле номера лиги
            content=TextField(
                height=start_input_height,
                width=start_input_wigth,
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
                    size=17,
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
            content=TextField(
                height=start_input_height,
                width=start_input_wigth,
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
                value=False,
                label="Save for the next session",
                fill_color={MaterialState.HOVERED: positive_color},
                # on_change=lambda e: print("it`s click, but it`s not clack")
            ),
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

        self.loginpage_elements = Column(
            # колонна основных элемнтов страницы
            controls=[
                Row(
                    # строка с номером и годом лиги
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.input_leagueid,
                        self.input_leagueyr
                    ]
                ),
                Row(
                    # строка с кнопкой шоу
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.show_btn
                    ]
                ),
                Row(
                    # строка с чекбоксом и ссылкой на очистку
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.chk_save_bx,
                        Container(
                            # ссылка на очистку полей ввода
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
                                        url='https://www.google.com/search?q=google'
                                    )
                                ]
                            )
                        )
                    ]
                ),
                Row(
                    # строка сообщений о ошибках
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.error_field
                    ]
                )
            ]
        )

        self.content = Container(
            # контейнер всего содержимого страницы
            height=base_height,
            width=base_wigth,
            bgcolor=base_bg_color,
            content=Stack(
                controls=[
                    Container(
                        # основное лого
                        height=base_height,
                        width=base_wigth,
                        padding=padding.only(top=60),
                        alignment=alignment.top_center,
                        content=Image(
                            src='assets/images/espn_fantasy_basketball_logo-1.jpg',
                        )
                    ),
                    # Container(
                    #     height=base_height,
                    #     width=base_wigth,
                    #     padding=padding.only(top=60),
                    #     alignment=alignment.top_center,
                    #
                    #     content=Image(
                    #         src='assets/images/animated_ball_loading.gif',
                    #     )
                    # ),
                    Container(
                        # основные жлементы страницы
                        padding=padding.only(top=385),
                        content=self.loginpage_elements
                    ),
                ]
            ),
        )
