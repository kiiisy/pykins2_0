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

    def HighLight(self, e):
        if e.data == "true":
            e.control.bgcolor = "white10"
            e.control.update()
            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].color = "white"
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = "white24"
            e.control.content.controls[1].color = "white24"
            e.control.content.update()

    def ContainerdIcon(self, icon_name: str, text: str):
        return Container(
            width=130,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        on_click=partial(self.func2),
                        icon=icon_name,
                        icon_size=25,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=15,
                        opacity=1,
                        animate_opacity=200,
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
            bgcolor="white10",
            border_radius=10,
            margin=10,
            content=Column(
                horizontal_alignment="center",
                controls=[
                    IconButton(
                        icon="menu",
                        icon_color="white",
                        icon_size=25,
                        on_click=partial(self.func1)
                    ),
                    self.ContainerdIcon(icons.BUILD_ROUNDED, "Auto Build"),
                    self.ContainerdIcon(icons.WAVES_ROUNDED, "Auto Sim"),
                    self.ContainerdIcon(icons.EDIT_ROUNDED, "Edit job"),
                    self.ContainerdIcon(icons.DASHBOARD_ROUNDED, "List jobs"),
                    Divider(height=5, color="white24"),
                    self.ContainerdIcon(icons.SETTINGS_ROUNDED, "Setting"),
                ]
            ),
        )
