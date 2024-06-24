# !usr/bin/env/python3
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : main process
# ************************************************************************
# Imports
# ************************************************************************
from flet import(
    Page,
    app
)
from app import Pykins


def main(page: Page):
    page.window_width = 1000
    page.window_height = 650
    page.window_resizable = False
    page.bgcolor = "black"
    page.padding = 0
    page.spacing = 0

    page.add(Pykins(page))


if __name__ == "__main__":
    app(main)
