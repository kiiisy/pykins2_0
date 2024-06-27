# !usr/bin/env/python3 
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : Dash Board body
# ************************************************************************
# Imports
# ************************************************************************
from flet import(
    Page,
    UserControl,
    Text,
    Column,
    ExpansionPanelList,
    ExpansionPanel,
    ListTile,
    IconButton,
    icons,
    ScrollMode,
    ElevatedButton,
)


class DashboardBody(UserControl):
    def __init__(self, page: Page, jenkins):
        super().__init__()
        self.page = page
        self.jenkins = jenkins

        self.panel_list = []
        # 起動時のデータをセット
        self.set_panel_list("1回目")


    def build(self):
        return Column(
            controls=[
                ElevatedButton(text="test", on_click=self.handle_click_button),
                self.create_col_panel(),
            ]
        )

    def set_panel_list(self, txt: str):
        #  TODO : 動作確認のためパネルの作りが雑
        #         色々作り込む必要あり
        appned_ = self.panel_list.append
        for i in range(20):
            appned_(ExpansionPanelList(
                expand_icon_color="",
                elevation=8,
                divider_color="",
                controls=[
                    ExpansionPanel(
                        bgcolor="",
                        expand=True,
                        content=ListTile(
                            title=Text(f"This is in Panel {i}"),
                            subtitle=Text(txt),
                            trailing=IconButton(icon=icons.DELETE),
                        )
                    )
                ]
            ))

    def handle_click_button(self, e):
        self.panel_list.clear()
        e.control.parent.controls[1].controls.clear()
        self.set_panel_list("2回目")
        e.control.parent.controls[1].controls.append(self.create_col_panel())
        self.update()

    def create_col_panel(self):
        # TODO : 動作確認のため回数が固定になっている
        #        job数で回したのでその引数を追加する必要あり
        tmp = Column(expand=True, scroll=ScrollMode.AUTO)
        for i in range(20):
            tmp.controls.append(self.panel_list[i])

        return tmp
