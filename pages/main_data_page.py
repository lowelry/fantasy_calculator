from utils.extras import *
from espn_api.basketball import League

league = League(league_id=1013716421, year=2024)
# следующая строка превращает сырые данные со списком команд в лиге в список только названий всех команд в лиге
teams_title_list = list((((" ".join(map(str, league.teams))).replace("Team(", "")).replace(")", ".")).split(". "))
# следующая строка превращает список только названий команд в лиге в набор опций для
# dropdown -> одна команда - одна опция
options_list = [ft.dropdown.Option(option) for option in teams_title_list]


class MainDataPage(Container):
    def __init__(self, show_btn_click, close_btn_click):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)

        print(show_btn_click)
        self.close_btn = Container(
            # кнопка закрытия приложения
            content=IconButton(
                icon=icons.CLOSE,
                icon_color=positive_color,
                icon_size=icons_size,
                tooltip="close app",
                on_click=close_btn_click
            )
        )

        self.teams_dropdown = Container(
            # выпадющий список с командами
            content=Dropdown(
                height=btn_height,
                width=btn_wigth,
                bgcolor=base_bg_color,
                alignment=alignment.center,
                border_radius=10,
                border_width=0.5,
                focused_border_color=positive_color,
                focused_border_width=2.5,
                focused_bgcolor=base_bg_color,
                autofocus=True,
                hint_style=TextStyle(
                    size=13,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                ),
                text_style=TextStyle(
                    size=13,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                    font_family="Sansation"
                ),
                # в данный момент список названий команд берется из запроса с предустановленными данными перед
                # формированием страницы, в дальнейшем, когда будет сделан переход между страницами, этот список будет
                # браться из show_btn_click
                options=options_list
            )
        )

        self.content = Container(
            # базовый контейнер страницы
            height=base_window_height,
            width=base_window_wigth,
            bgcolor=base_bg_color,
            alignment=alignment.center,
            content=Column(
                controls=[
                    Container(
                        self.close_btn,
                        padding=padding.only(right=30),
                        alignment=alignment.top_right
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.teams_dropdown
                        ]
                    ),
                    Container(
                        alignment=alignment.center,
                        content=
                        # ft.DataTable(
                        #     width=700,
                        #     bgcolor="yellow",
                        #     border=ft.border.all(2, "red"),
                        #     border_radius=10,
                        #     vertical_lines=ft.border.BorderSide(3, "blue"),
                        #     horizontal_lines=ft.border.BorderSide(1, "green"),
                        #     sort_column_index=0,
                        #     sort_ascending=True,
                        #     heading_row_color=ft.colors.BLACK12,
                        #     heading_row_height=100,
                        #
                        #     show_checkbox_column=True,
                        #     divider_thickness=0,
                        #     column_spacing=200,
                        #     columns=[
                        #         ft.DataColumn(
                        #             ft.Text("Column 1"),
                        #             on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                        #         ),
                        #         ft.DataColumn(
                        #             ft.Text("Column 2"),
                        #             tooltip="This is a second column",
                        #             # numeric=True,
                        #             on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                        #         ),
                        #     ],
                        #     rows=[
                        #         ft.DataRow(
                        #             [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                        #             # selected=True,
                        #             on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                        #         ),
                        #         ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
                        #     ],
                        # ),
                        ft.DataTable(
                            show_checkbox_column=True,
                            columns=[
                                ft.DataColumn(
                                    Text('Состав'),
                                ),
                                ft.DataColumn(
                                    Text('статус'),
                                ),
                                ft.DataColumn(
                                    Text('AVR'),
                                ),
                                ft.DataColumn(
                                    Text('Количество игр'),
                                ),
                                ft.DataColumn(
                                    Text('Week AVR'),
                                )
                            ],
                            rows=[
                                DataRow(
                                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                    cells=[
                                        DataCell(Text('Trae Young')),
                                        DataCell(Text('active')),
                                        DataCell(Text(7.29)),
                                        DataCell(ft.RadioGroup(
                                            content=Row([
                                                ft.Radio(value="red", label="2"),
                                                ft.Radio(value="green", label="3"),
                                                ft.Radio(value="grey", label="4"),
                                                ft.Radio(value="black", label="5"),
                                            ])
                                        )),
                                        DataCell(Text('empty')),
                                        DataCell(Text('empty')),
                                    ]
                                ),
                                DataRow(
                                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                    cells=[
                                        DataCell(Text('LaMelo Ball')),
                                        DataCell(Text('active')),
                                        DataCell(Text(7.76)),
                                        DataCell(ft.RadioGroup(
                                            content=Row([
                                                ft.Radio(value="red", label="2"),
                                                ft.Radio(value="green", label="3"),
                                                ft.Radio(value="grey", label="4"),
                                                ft.Radio(value="black", label="5"),
                                            ])
                                        )),
                                        DataCell(Text('empty')),
                                        DataCell(Text('empty')),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )