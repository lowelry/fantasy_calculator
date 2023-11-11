from utils.extras import *

class MainDataPage(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.offset = transform.Offset(0, 0)

        self.startpage_elements = Column(
        )

        self.content = Container(
            # контейнер всего содержимого
            height=base_window_height,
            width=base_window_wigth,
            bgcolor=base_bg_color,
            content=Stack(
                controls=[
                    # Container(
                    #     height=base_height,
                    #     width=base_window_wigth,
                    #     padding=padding.only(top=60),
                    #     alignment=alignment.top_center,
                    #     content=Image(
                    #         src='assets/images/espn_fantasy_basketball_logo-1.jpg',
                    #     )
                    # ),
                    Container(
                        offset=(0.5, 0),
                        height=base_window_height,
                        width=base_window_wigth / 2,
                        padding=padding.only(top=60),
                        alignment=alignment.center,
                        content=Image(
                            src='assets/images/animated_ball_loading.gif',
                        )
                    ),
                    Container(
                        padding=padding.only(top=365),
                        content=self.startpage_elements
                    ),
                    Container(
                        bgcolor="GREY",
                        content=TextField(
                            height=70,
                            max_length=4,
                            counter_style=TextStyle(size=0)
                        )
                    )
                ]
            ),


        )
