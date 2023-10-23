import flet as ft
from utils.extras import *


class LogInPage(Container):
    def __init__(self, validate_inputs):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)
        self.validate_inputs = validate_inputs

        self.input_leagueyr = Container(
            # поле года лиги
            height=start_input_height,
            width=start_input_wigth,
            border_radius=10,
            border=border.all(0.1),
            bgcolor='white',
            shadow=BoxShadow(
                offset=Offset(2, 2),
                blur_style=ShadowBlurStyle.INNER,
                blur_radius=50
            ),
            content=ft.TextField(
                max_length=4,
                counter_text=' ',
                hint_text='LEAGUE YR',
                text_align=TextAlign.CENTER,
                hint_style=TextStyle(
                    size=12,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                ),
                text_style=TextStyle(
                    size=12,
                    color=input_hint_color
                ),
                border=InputBorder.NONE,
                content_padding=padding.only(top=26),
                on_change=self.validate_inputs
            )
        )

        self.input_leagueid = Container(
            # поле номера лиги
            height=start_input_height,
            width=start_input_wigth,
            border_radius=10,
            border=border.all(0.1),
            bgcolor='white',
            shadow=BoxShadow(
                offset=Offset(2, 2),
                blur_style=ShadowBlurStyle.INNER,
                blur_radius=50
            ),
            content=ft.TextField(
                max_length=10,
                counter_text=' ',
                hint_text='LEAGUE ID',
                text_align=TextAlign.CENTER,
                hint_style=TextStyle(
                    size=12,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                ),
                text_style=TextStyle(
                    size=12,
                    color=input_hint_color
                ),
                border=InputBorder.NONE,
                content_padding=padding.only(top=26),
                on_change=self.validate_inputs
            )
        )

        self.startpage_elements = Column(
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
                        Container(
                            height=btn_height,
                            width=btn_wigth,
                            bgcolor=start_btn_color,
                            border=border.all(0.1),
                            border_radius=10,
                            alignment=alignment.center,
                            content=Text(
                                value='SHOW',
                                size=12,
                                color=input_hint_color,
                                weight=FontWeight.NORMAL
                            ),
                            shadow=BoxShadow(
                                offset=Offset(2, 2),
                                blur_style=ShadowBlurStyle.INNER,
                                blur_radius=50
                            ),
                        )
                    ]
                ),
                Row(
                    # строка с чекбоксом и ссылкой на очистку
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        Container(
                            # чекбокс запонимания лиги на следующую сессию
                            height=btn_height,
                            width=220,
                            alignment=alignment.top_left,
                            padding=padding.only(left=-34, top=-12),
                            # bgcolor="GREY",
                            content=Checkbox(
                                scale=0.8,
                                value=False,
                                label="Save for the next session",
                            ),
                        ),
                        Container(
                            # ссылка на очистку полей ввода
                            height=btn_height,
                            width=120,
                            alignment=alignment.top_right,
                            # bgcolor="GREY",
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
                )
             ]
        )

        self.content = Container(
            # контейнер всего содержимого
            height=base_height,
            width=base_wigth,
            bgcolor=base_color,
            content=Stack(
                controls=[
                    Container(
                        height=base_height,
                        width=base_wigth,
                        padding=padding.only(top=60),
                        alignment=alignment.top_center,

                        content=Image(
                            src='assets/images/espn_fantasy_basketball_logo.jpg',
                        )
                    ),
                    Container(
                        padding=padding.only(top=365),
                        content=self.startpage_elements
                    ),
                ]
            )
        )
