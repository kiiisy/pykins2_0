# !usr/bin/env/python3
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : app process
# ************************************************************************
# Imports
# ************************************************************************
import time
from flet import(
    UserControl,
    Page,
    Container,
    transform,
    animation,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
    LinearGradient,
    alignment
)

from components.body0 import AutoBuildBody
from components.body1 import AutoSimBody
from components.body2 import EditJobBody
from components.body3 import DashboardBody
from components.sidebar import NavBar
import jenkins_module.my_jenkins as jmodule


class Pykins(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.jenkins = jmodule.MyJenkins()
        self.body_list = [AutoBuildBody(self.page, self.jenkins), AutoSimBody(), EditJobBody(), DashboardBody()]

        # ボディ作成
        self.mycontents = Container(
            width=780,
            height=600,
            padding=10,
            margin=10,
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=["0xff1f005c","0x00000000"],
            ),
            border_radius=10,
            content=self.body_list[0],
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(250, "easeOut")
        )

        # サイドバー作成
        self.navrail = NavBar(self.page, self.toggle_icon, self.change_route)

    def build(self):
        return Container(
            Row(
                expand=True,
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[self.navrail, self.mycontents]
            )
        )

    def change_route(self, e):
        self.mycontents.offset = transform.Offset(0, 1.5)
        self.update()
        time.sleep(0.2)
        self.mycontents.offset = transform.Offset(0, 0)
        if e.control.icon == "build_rounded" :
            self.mycontents.content = self.body_list[0]
        elif e.control.icon == "waves_rounded" :
            self.mycontents.content = self.body_list[1]
        elif e.control.icon == "edit_rounded" :
            self.mycontents.content = self.body_list[2]
        elif e.control.icon == "dashboard_rounded" :
            self.mycontents.content = self.body_list[3]
        elif e.control.icon == "settings_rounded" :
            self.mycontents.content = self.body_list[3]
        self.update()

    def toggle_icon(self, e):
        navbar = self.page.controls[0].controls[0].content.controls[0].controls[0]
        body = self.page.controls[0].controls[0].content.controls[1]
        # サイドバーの大きさ変更による画面サイズの調整
        if navbar.width != 42:
            navbar.width = 42
            body.width = 890
            if isinstance(body.content, AutoBuildBody):
                self.format_body0(body.content, 1)
            body.update()
            navbar.update()
        else:
            navbar.width = 150
            body.width = 780
            if isinstance(body.content, AutoBuildBody):
                self.format_body0(body.content, 0)
            body.update()
            navbar.update()
            time.sleep(0.2)
            for item in navbar.content.controls[:]:
                item.opacity = 1
                item.update()

    def format_body0(self, body, is_expanded):
        # ウィジェットの場所を示す
        # !!レイアウトを変更した場合は注意!!
        # 00:Text
        # 01:Row.controls[0].TextField
        #   :Row.controls[1].TextField
        # 02:Divider
        # 03:Text
        # 04:TextField
        # 05:Row.controls[0].TextField
        #   :Row.controls[1].TextField
        # 06:Divider
        # 07:Text
        # 08:TextField
        # 09:Divier
        # 10:Text
        # 11:Row.controls[0].Text
        #   :Row.controls[1].Checkbox
        #   :Row.controls[2].Checkbox
        #   :Row.controls[3].Checkbox
        #   :Row.controls[4].Checkbox
        #   :Row.controls[5].Checkbox
        #   :Row.controls[6].Checkbox
        #   :Row.controls[7].Checkbox
        # 12:Row.controls[0].Text
        #   :Row.controls[1].TextButton
        # 13:Row.controls[0].ElevatedButton
        if is_expanded:
            body.controls[0].controls[1].controls[0].width = 430
            body.controls[0].controls[1].controls[1].width = 430
            body.controls[0].controls[5].controls[0].width = 430
            body.controls[0].controls[5].controls[1].width = 430
            body.controls[0].controls[11].spacing = 50
            body.controls[0].controls[12].spacing = 40
        else :
            body.controls[0].controls[1].controls[0].width = 376
            body.controls[0].controls[1].controls[1].width = 376
            body.controls[0].controls[5].controls[0].width = 376
            body.controls[0].controls[5].controls[1].width = 376
            body.controls[0].controls[11].spacing = 35
            body.controls[0].controls[12].spacing = 25

        body.controls[0].controls[1].update()
        body.controls[0].controls[5].update()
        body.controls[0].controls[11].update()
        body.controls[0].controls[12].update()

    def format_body1(self, body, is_expanded):
        pass

    def format_body2(self, body, is_expanded):
        pass

    def format_body3(self, body, is_expanded):
        pass
