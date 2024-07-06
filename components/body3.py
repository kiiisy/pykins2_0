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
    Row,
    ExpansionPanelList,
    ExpansionPanel,
    ListTile,
    ScrollMode,
    ElevatedButton,
    TextField,
    TextStyle,
    MainAxisAlignment,
)


class DashboardBody(UserControl):
    def __init__(self, page: Page, jenkins):
        super().__init__()
        self.page = page
        self.jenkins = jenkins

        self.panel_list = []
        self.jobs = self.jenkins.get_all_job()
        # 起動時のデータをセット
        self.set_panel_list()

    def build(self):
        return Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.START,
                    spacing=50,
                    controls=[
                        ElevatedButton(text="更新",
                                       color="#f8f8ff",
                                       bgcolor="#1e90ff",
                                       width=100,
                                       on_click=self.handle_click_button),
                        TextField(icon="search",
                                  hint_text="Job検索",
                                  hint_style=TextStyle(color="#fffafa"),
                                  border="underline",
                                  border_color="#ffffff",
                                  color="#f8f8ff",
                                  on_submit=self.handle_submit_text),
                    ]
                ),
                self.create_panels(),
            ]
        )

    def set_panel_list(self, job_name=""):
        # bgcolorの色付けはlambdaで決定する
        # jobが無効であればグレーアウトする
        bgcolor_lambda = lambda build_en: "#add8e6" if build_en else "#778899"
        text_lambda = lambda build_en: "有効Job" if build_en else "無効Job"

        if not job_name:
            jobs = self.jobs
        else:
            for job in self.jobs:
                if job.get("name").casefold() == job_name.casefold():
                    jobs = [job]

        for job in jobs:
            job_info = self.jenkins.get_job_info(job.get("name"))
            self.panel_list.append(ExpansionPanelList(
                expand_icon_color="#ffffff",
                elevation=8,
                controls=[
                    ExpansionPanel(
                        header=ListTile(title=Text(job_info.get("name"))),
                        bgcolor=bgcolor_lambda(job_info.get("buildable")),
                        expand=True,
                        content=ListTile(
                            title=Text(text_lambda(job_info.get("buildable"))),
                        )
                    )
                ]
            ))

    def handle_click_button(self, e):
        self.update_panel(e)

    def handle_submit_text(self, e):
        self.update_panel(e)

    def create_panels(self):
        panels = Column(expand=True, scroll=ScrollMode.ADAPTIVE)

        # 検索した場合は1つのjobしか出てこないため
        if len(self.panel_list) == 1:
            panels.controls.append(self.panel_list[0])
        else:
            list_len = len(self.jobs)
            for i in range(list_len):
                panels.controls.append(self.panel_list[i])

        return panels

    def update_panel(self, e):
        # 関連のあるcontrolsをクリア
        self.panel_list.clear()
        e.control.parent.parent.controls[1].controls.clear()

        # 再度jobを取得
        self.jobs = self.jenkins.get_all_job()

        # 更新がかかるパターン
        # 1.  更新ボタンを押下した場合
        # 2-1.検索窓にてjob指定で検索した場合
        # 2-2.検索窓にてjob指定なし(空欄)で検索した場合
        # 上記パターンの内、e.dataが入っているのはjob指定で検索した場合のみとなる
        self.set_panel_list(e.data)

        e.control.parent.parent.controls[1].controls.append(self.create_panels())
        self.update()
