from utils.extras import *
from espn_api.basketball import League

league = League(league_id=1013716421, year=2025)
# следующая строка превращает сырые данные со списком команд в лиге в список только названий всех команд в лиге
teams_title_list = list((((" ".join(map(str, league.teams))).replace("Team(", "")).replace(")", ".")).split(". "))
# следующая строка превращает список только названий команд в лиге в набор опций для
# dropdown -> одна команда - одна опция
options_list = [ft.dropdown.Option(option) for option in teams_title_list]


team_number = 0
players_names_list = list((",".join(map(str, league.teams[team_number].roster))).replace("Player(", "")
                          .replace(")", "").split(","))


def player_status(name_number):
    player_injury_status = league.teams[team_number].roster[name_number].injuryStatus.lower()
    return player_injury_status


def player_avr(name_number):
    player_avr_number = league.teams[team_number].roster[name_number].avg_points
    return player_avr_number


class MainDataPage(Container):
    def __init__(self, show_btn_click, close_btn_click):
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
                options=options_list,
                # on_change=self.team_dropdown_update
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
                                            Text('Состав'),
                                        ),
                                        DataColumn(
                                            Text('статус'),
                                        ),
                                        DataColumn(
                                            Text('AVR'),
                                        ),
                                        DataColumn(
                                            Text('Количество игр'),
                                        ),
                                        DataColumn(
                                            Text('Week AVR'),
                                        )
                                    ],
                                    rows=[
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[0]}')),
                                                DataCell(Text(f'{player_status(0)}')),
                                                DataCell(Text(f'{player_avr(0)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[1]}')),
                                                DataCell(Text(f'{player_status(1)}')),
                                                DataCell(Text(f'{player_avr(1)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value='2', label="2"),
                                                        Radio(value='3', label="3"),
                                                        Radio(value='4', label="4"),
                                                        Radio(value='5', label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[2]}')),
                                                DataCell(Text(f'{player_status(2)}')),
                                                DataCell(Text(f'{player_avr(2)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[3]}')),
                                                DataCell(Text(f'{player_status(3)}')),
                                                DataCell(Text(f'{player_avr(3)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[4]}')),
                                                DataCell(Text(f'{player_status(4)}')),
                                                DataCell(Text(f'{player_avr(4)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[5]}')),
                                                DataCell(Text(f'{player_status(5)}')),
                                                DataCell(Text(f'{player_avr(5)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[6]}')),
                                                DataCell(Text(f'{player_status(6)}')),
                                                DataCell(Text(f'{player_avr(6)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[7]}')),
                                                DataCell(Text(f'{player_status(7)}')),
                                                DataCell(Text(f'{player_avr(7)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[8]}')),
                                                DataCell(Text(f'{player_status(8)}')),
                                                DataCell(Text(f'{player_avr(8)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[9]}')),
                                                DataCell(Text(f'{player_status(9)}')),
                                                DataCell(Text(f'{player_avr(9)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[10]}')),
                                                DataCell(Text(f'{player_status(10)}')),
                                                DataCell(Text(f'{player_avr(10)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[11]}')),
                                                DataCell(Text(f'{player_status(11)}')),
                                                DataCell(Text(f'{player_avr(11)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[12]}')),
                                                DataCell(Text(f'{player_status(12)}')),
                                                DataCell(Text(f'{player_avr(12)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[13]}')),
                                                DataCell(Text(f'{player_status(13)}')),
                                                DataCell(Text(f'{player_avr(13)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                        DataRow(
                                            # on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                                            cells=[
                                                DataCell(Text(f'{players_names_list[14]}')),
                                                DataCell(Text(f'{player_status(14)}')),
                                                DataCell(Text(f'{player_avr(14)}')),
                                                DataCell(ft.RadioGroup(
                                                    content=Row([
                                                        Radio(value="2", label="2"),
                                                        Radio(value="3", label="3"),
                                                        Radio(value="4", label="4"),
                                                        Radio(value="5", label="5"),
                                                    ])
                                                )),
                                                DataCell(Text('empty')),
                                                DataCell(Text('empty')),
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
