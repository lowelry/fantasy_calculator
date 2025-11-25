from utils.extras import *


class MainDataPage(Container):
    _RADIO_VALUES = ("2", "3", "4", "5")

    def __init__(self, close_btn_click, *radio_change_handlers, on_dropdown_change):
        super().__init__()
        # вызываем растяжение на весь объем страницы
        self.expand = True
        # задаем нулевое базовое смещение страницы
        self.offset = transform.Offset(0, 0)

        if len(radio_change_handlers) != 16:
            raise ValueError("Expected 16 radio handlers for data rows")

        self.close_btn = Container(
            # кнопка закрытия приложения
            content=IconButton(
                # задаем вид иконки, цвет, размер, тест тултипа, реакцию на клик, и через задание стиля задаем
                # окрашивание при наведении курсора
                icon=icons.CLOSE,
                icon_color=input_hint_color,
                icon_size=icons_size,
                tooltip="close app",
                on_click=close_btn_click,
                style=ft.ButtonStyle(
                    overlay_color=positive_color
                )
            ),
        )
        self.change_theme_btn = Container(
            # кнопка изменения темы приложения
            content=IconButton(
                # задаем вид иконки, цвет, размер, тест тултипа и через задание стиля задаем
                # окрашивание при наведении курсора
                icon=icons.WB_SUNNY_OUTLINED,
                icon_color=input_hint_color,
                icon_size=icons_size,
                tooltip="change theme",
                # реакция на клик не прописана потому что еще не существует обработчика реакции кнопки
                # on_click=close_btn_click,
                style=ft.ButtonStyle(
                    overlay_color=positive_color
                )
            ),
        )
        self.teams_dropdown = Container(
            # выпадющий список со списком командам
            content=Dropdown(
                # задаем высоту, ширину, цвет фона, выравнивание, радиус скругления контура, ширину линии контура, цвет
                # контура при фокусе, ширину линии контура при фокусе, автоматическую установку фокуса при открытии
                # страницы
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
                # задаем стиль текста внутри выпадающего списка и внутри поля: размер шрифта, цвет текста, толщину
                # шрифта, а также указываем какой конкретно шрифт мы используем
                text_style=TextStyle(
                    size=13,
                    color=input_hint_color,
                    weight=FontWeight.NORMAL,
                    font_family="Sansation"
                ),
                # задаем реакцию на выбор элемента из выпадающего списка через обработчик из файла app.py
                on_change=on_dropdown_change
            )
        )
        self.data_rows = [
            self._build_data_row(handler)
            for handler in radio_change_handlers
        ]
        for index, row in enumerate(self.data_rows):
            setattr(self, f"DataRow{index}", row)
        self.ghost_container = Container(
            # теневой контейнер справа от таблицы данных и дропдауна, предназначенный для вывода рассчетного
            # результата, равный левому контейнеру выбора подвкладок
            width=200,
            height=200,
            bgcolor=base_bg_color,
        )
        tab_button_style = ft.ButtonStyle(
            bgcolor=base_bg_color,
            shape=ft.RoundedRectangleBorder(radius=5),
            overlay_color=positive_color
        )

        def make_tab_button(label: str, padding_top: int, on_click):
            return Container(
                padding=padding.only(top=padding_top),
                content=TextButton(
                    content=ft.Text(
                        value=label,
                        size=13,
                        color=input_hint_color,
                        weight=ft.FontWeight.NORMAL
                    ),
                    style=tab_button_style,
                    height=50,
                    width=200,
                    on_click=on_click
                )
            )

        self.custom_tabs_menu = Container(
            # контейнер содержащий меню выбора подвкладок данных, содержащий три кнопки
            # задаем общую высоту и ширину контейнера
            height=535,
            width=200,
            content=Column(
                # общая колонна для трех кнопок
                controls=[
                    make_tab_button('Machup calculations', 89, lambda e: print("First clicked")),
                    make_tab_button('Player statistic', -10, lambda e: print("Second clicked")),
                    make_tab_button('Player comparison', -10, lambda e: print("Third clicked")),
                ]
            )
        )

        self.dropdown_and_data = Column(
            # колонна с дропдауном и таблицей данных
            controls=[
                Row(
                    # строка с дропдауном
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.teams_dropdown
                    ]
                ),
                Container(
                    # контейнер таблицы данных
                    alignment=alignment.center,
                    expand=False,
                    content=Column(
                        height=535,
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
                                        Text('Slot')
                                    ),
                                    DataColumn(
                                        Text('Player')
                                    ),
                                    DataColumn(
                                        Text('Status')
                                    ),
                                    DataColumn(
                                        Text('AVR')
                                    ),
                                    DataColumn(
                                        Text('Number of Games')
                                    ),
                                    DataColumn(
                                        Text('Week AVR')
                                    )
                                ],
                                rows=[
                                    *self.data_rows
                                ]
                            )
                        ]
                    )
                )
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.content = Container(
            # базовый контейнер страницы
            height=base_window_height,
            width=base_window_wigth,
            bgcolor=base_bg_color,
            alignment=alignment.center,
            content=Column(
                controls=[
                    Row(
                        # верхня строка с базовыми кнопками
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                                self.change_theme_btn,
                                padding=padding.only(left=30),
                                alignment=alignment.top_left
                            ),
                            Container(
                                self.close_btn,
                                padding=padding.only(right=30),
                                alignment=alignment.top_right
                            )
                        ]
                    ),
                    Row(
                        # строка с тремя основными контейнерами (левым, центральным и правым)
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(
                                # левый контейнер для переключения подвкладок
                                self.custom_tabs_menu,
                                padding=padding.only(left=30),
                                alignment=alignment.top_left,
                                expand=False
                            ),
                            Container(
                                self.dropdown_and_data
                            ),
                            Container(
                                # теневой контейнер справа
                                self.ghost_container,
                                padding=padding.only(right=30),
                                alignment=alignment.top_right,
                                expand=False
                            )
                        ]
                    )
                ]
            )
        )

    def _create_radio_group(self, on_change):
        return ft.RadioGroup(
            content=Row([
                Radio(value=value, label=value)
                for value in self._RADIO_VALUES
            ]),
            on_change=on_change,
            disabled=True
        )

    def _build_data_row(self, handler):
        return DataRow(
            cells=[
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(content=Text('')),
                DataCell(self._create_radio_group(handler)),
                DataCell(content=Text('')),
            ]
        )
