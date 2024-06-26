# !usr/bin/env/python3
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : sidebar process
# ************************************************************************
# Imports
# ************************************************************************
from functools import partial
from flet import(
    UserControl,
    Page,
    Container,
    IconButton,
    Row,
    ButtonStyle,
    RoundedRectangleBorder,
    Text,
    padding,
    alignment,
    Column,
    icons,
    Divider
)


class NavBar(UserControl):
    def __init__(self, page: Page, func1, func2):
        self.page = page
        self.func1 = func1
        self.func2 = func2
        super().__init__()

    def highlight(self, e):
        if e.data == "true":
            e.control.bgcolor = "#404040"
            e.control.update()
            e.control.content.controls[0].icon_color = "#eeeeee"
            e.control.content.controls[1].color = "#eeeeee"
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = "#424242"
            e.control.content.controls[1].color = "#424242"
            e.control.content.update()

    def containerd_icon(self, icon_name: str, text: str):
        return Container(
            width=130,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.highlight(e),
            content=Row(
                controls=[
                    IconButton(
                        on_click=partial(self.func2),
                        icon=icon_name,
                        icon_size=25,
                        icon_color="#424242",
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="#424242",
                        size=15,
                        opacity=1,
                        animate_opacity=200,
                        font_family="Arial",
                    ),
                ]
            ),
        )

    def build(self):
        return Container(
            width=150,
            height=600,
            padding=padding.only(top=5),
            alignment=alignment.center,
            bgcolor="#1d1d1d",
            border_radius=10,
            margin=10,
            content=Column(
                horizontal_alignment="center",
                controls=[
                    IconButton(
                        icon="menu",
                        icon_color="#eeeeee",
                        icon_size=25,
                        on_click=partial(self.func1)
                    ),
                    self.containerd_icon(icons.BUILD_ROUNDED, "Auto Build"),
                    self.containerd_icon(icons.WAVES_ROUNDED, "Auto Sim"),
                    self.containerd_icon(icons.EDIT_ROUNDED, "Edit job"),
                    self.containerd_icon(icons.DASHBOARD_ROUNDED, "List jobs"),
                    Divider(height=5, color="#383838"),
                    self.containerd_icon(icons.SETTINGS_ROUNDED, "Setting"),
                ]
            ),
        )
