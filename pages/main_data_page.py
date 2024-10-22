from utils.extras import *
from espn_api.basketball import League


class MainDataPage(Container):
    def __init__(self, close_btn_click, on_radio_change_0, on_radio_change_1, on_radio_change_2,
                 on_radio_change_3, on_radio_change_4, on_radio_change_5, on_radio_change_6, on_radio_change_7,
                 on_radio_change_8, on_radio_change_9, on_radio_change_10, on_radio_change_11, on_radio_change_12,
                 on_radio_change_13, on_radio_change_14, on_radio_change_15, on_dropdown_change):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)
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

        # создаем пустышку наполнения таблицы
        self.playes_data = [
             {"name": "", "position": "", "avg_points": 0.0, "injury": ""}
             for _ in range(16)  # Генератор для создания 16 элементов
        ]

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
                on_change=on_dropdown_change
            )
        )

        self.DataRow0 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[0]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_0
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow1 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[1]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_1
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow2 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[2]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_2
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow3 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[3]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_3
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow4 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[4]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_4
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow5 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[5]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_5
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow6 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[6]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_6
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow7 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[7]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_7
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow8 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[8]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_8
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow9 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[9]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_9
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow10 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[10]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_10
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow11 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[11]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_11
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow12 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[12]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_12
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow13 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[13]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_13
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow14 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[14]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_14
                )),
                DataCell(content=Text('')),
            ]
        )

        self.DataRow15 = DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text(f'{self.playes_data[15]["avg_points"]:.2f}')),
                DataCell(ft.RadioGroup(
                    content=Row([
                        Radio(value="2", label="2"),
                        Radio(value="3", label="3"),
                        Radio(value="4", label="4"),
                        Radio(value="5", label="5"),
                    ]),
                    on_change=on_radio_change_15
                )),
                DataCell(content=Text('')),
            ]
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
                        content=Column(
                            height=450,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                DataTable(
                                    heading_text_style=TextStyle(
                                        size=13,
                                        color=input_hint_color,
                                        weight=FontWeight.NORMAL,
                                        font_family="Sansation",
                                    ),
                                    data_text_style=TextStyle(
                                        size=13,
                                        color=input_hint_color,
                                        weight=FontWeight.NORMAL,
                                        font_family="Sansation",
                                    ),
                                    show_checkbox_column=True,
                                    columns=[
                                        DataColumn(
                                            Text('Slot'),
                                        ),
                                        DataColumn(
                                            Text('Player'),
                                        ),
                                        DataColumn(
                                            Text('Status'),
                                        ),
                                        DataColumn(
                                            Text('AVR'),
                                        ),
                                        DataColumn(
                                            Text('Games Number'),
                                        ),
                                        DataColumn(
                                            Text('Week AVR'),
                                        )
                                    ],
                                    rows=[
                                        self.DataRow0,
                                        self.DataRow1,
                                        self.DataRow2,
                                        self.DataRow3,
                                        self.DataRow4,
                                        self.DataRow5,
                                        self.DataRow6,
                                        self.DataRow7,
                                        self.DataRow8,
                                        self.DataRow9,
                                        self.DataRow10,
                                        self.DataRow11,
                                        self.DataRow12,
                                        self.DataRow13,
                                        self.DataRow14,
                                        self.DataRow15
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
