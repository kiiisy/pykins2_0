# !usr/bin/env/python3 
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : Auto build body
# ************************************************************************
# Imports
# ************************************************************************
import time
from flet import(
    Page,
    UserControl,
    Column,
    Row,
    TextField,
    MainAxisAlignment,
    Checkbox,
    RoundedRectangleBorder,
    Text,
    CrossAxisAlignment,
    ElevatedButton,
    CupertinoTimerPicker,
    TextButton,
    CupertinoBottomSheet,
    colors,
    ButtonStyle,
    padding,
    CupertinoTimerPickerMode,
    Ref,
    Divider,
    AlertDialog
)


class AutoBuildBody(UserControl):
    def __init__(self, page: Page, jenkins):
        super().__init__()
        self.page = page
        self.jenkins = jenkins

        # Job関連のウィジェット作成
        self.text_job = Text("Job設定", size=17, color="#f8f8ff")
        self.text_job_name = TextField(label="Job名(必須)",
                                       text_size=15,
                                       border_width=3,
                                       width=384,
                                       border_radius=10,
                                       hint_text="プロジェクト名と同じであること")
        self.text_job_desc = TextField(label="Job概要",
                                       text_size=15,
                                       border_width=3,
                                       width=384,
                                       border_radius=10,
                                       hint_text="例) M222のAutoビルド用")

        # Git関連のウィジェット作成
        self.text_git = Text("Git設定", size=17, color="#f8f8ff")
        self.text_git_url = TextField(label="Git URL(必須)",
                                      text_size=15,
                                      border_width=3,
                                      border_radius=10)
        self.text_git_branch = TextField(label="ブランチ名",
                                         text_size=15,
                                         border_width=3,
                                         width=384,
                                         border_radius=10)
        self.text_build_folder = TextField(label="ビルド対象フォルダ",
                                           text_size=15,
                                           border_width=3,
                                           width=384,
                                           border_radius=10)

        # Teams関連のウィジェット作成
        self.text_teams = Text("Teams設定", size=17, color="#f8f8ff")
        self.text_teams_url = TextField(label="Teams URL(必須)",
                                        text_size=15,
                                        border_width=3,
                                        border_radius=10,
                                        password=True,
                                        can_reveal_password=True)

        # Build関連のウィジェット作成
        self.text_buid_setting = Text("Build設定", size=17, color="#f8f8ff")
        self.text_buid_data = Text("ビルド実行曜日", size=15, color="#f8f8ff", opacity=1)
        self.chkbox_sun = Checkbox(label="Sun", shape=RoundedRectangleBorder(radius=5), value=False, scale=1.3)
        self.chkbox_mon = Checkbox(label="Mon", shape=RoundedRectangleBorder(radius=5), value=True, scale=1.3)
        self.chkbox_tue = Checkbox(label="Tue", shape=RoundedRectangleBorder(radius=5), value=True, scale=1.3)
        self.chkbox_wed = Checkbox(label="Wed", shape=RoundedRectangleBorder(radius=5), value=True, scale=1.3)
        self.chkbox_thu = Checkbox(label="Thu", shape=RoundedRectangleBorder(radius=5), value=True, scale=1.3)
        self.chkbox_fri = Checkbox(label="Fri", shape=RoundedRectangleBorder(radius=5), value=True, scale=1.3)
        self.chkbox_sat = Checkbox(label="Sat", shape=RoundedRectangleBorder(radius=5), value=False, scale=1.3)

        # 実行ボタンのウィジェット作成
        self.dlg = AlertDialog(
            # ダイアログの外側をクリックして閉じれないようにする
            modal=True,
            title=Text("Please confilm"),
            content=Text("必須項目をしてください"),
            actions=[
                TextButton("閉じる", on_click=self.handle_close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )
        self.button = ElevatedButton(
            text="実行",
            bgcolor="#0054FF",
            width=150,
            on_click=self.handle_open_dlg
        )

        # タイムピッカーのウィジェット作成
        self.timer_picker = CupertinoTimerPicker(
            value=3600,
            second_interval=10,
            minute_interval=1,
            mode=CupertinoTimerPickerMode.HOUR_MINUTE,
            on_change=self.handle_timer_picker_change,
        )
        # タイムピッカーの値はRefで参照する
        self.timer_picker_value_ref = Ref[Text]()

    def build(self):
        return Column(
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.START,
            controls=[
                self.text_job,
                Row(
                    controls=[
                        self.text_job_name,
                        self.text_job_desc
                    ]
                ),
                Divider(height=5, color="white12", thickness=2),
                self.text_git,
                self.text_git_url,
                Row(
                    controls=[
                        self.text_git_branch,
                        self.text_build_folder
                    ]
                ),
                Divider(height=5, color="white12", thickness=2),
                self.text_teams,
                self.text_teams_url,
                Divider(height=5, color="white12", thickness=2),
                self.text_buid_setting,
                Row(
                    spacing=35,
                    controls=[
                        self.text_buid_data,
                        self.chkbox_sun,
                        self.chkbox_mon,
                        self.chkbox_tue,
                        self.chkbox_wed,
                        self.chkbox_thu,
                        self.chkbox_fri,
                        self.chkbox_sat
                    ]
                ),
                Row(
                    tight=True,
                    spacing=25,
                    controls=[
                        Text("ビルド開始時間", size=15, color="f8f8ff"),
                        TextButton(
                            content=Text("22:00",
                                        size=20,
                                        color="white",
                                        ref=self.timer_picker_value_ref
                                    ),
                            style=ButtonStyle(color=colors.RED),
                            on_click=lambda _: self.page.show_bottom_sheet(
                                CupertinoBottomSheet(
                                    self.timer_picker,
                                    height=216,
                                    padding=padding.only(top=6),
                                )
                            ),
                        ),
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        self.button
                    ]
                ),
            ]
        )

    def handle_timer_picker_change(self, e):
        val = int(e.data)
        self.timer_picker_value_ref.current.value = time.strftime("%H : %M", time.gmtime(val))
        self.page.controls[0].controls[0].content.controls[1].content.update()

    def handle_close_dlg(self, e):
        self.dlg.open = False
        e.control.page.update()

    def handle_open_dlg(self, e):
        result = self.check_input(e)

        # インプット確認で問題があればダイアログを表示し、
        # 問題がなければJenkinsへデータを送信する
        if result != 0:
            e.control.page.dialog = self.dlg
            self.dlg.open = True
            e.control.page.update()
        else:
            self.send_input(e)

    def send_input(self, e):
        # テキストのデータ取得
        job_name = e.page.controls[0].controls[0].content.controls[1].content.text_job_name.value
        job_desc = e.page.controls[0].controls[0].content.controls[1].content.text_job_desc.value
        git_url = e.page.controls[0].controls[0].content.controls[1].content.text_git_url.value
        git_branch = e.page.controls[0].controls[0].content.controls[1].content.text_git_branch.value
        teams_url = e.page.controls[0].controls[0].content.controls[1].content.text_teams_url.value
        build_folder = e.page.controls[0].controls[0].content.controls[1].content.text_build_folder.value

        # チェックボックスのデータ取得
        is_sun = e.page.controls[0].controls[0].content.controls[1].content.chkbox_sun.value
        is_mon = e.page.controls[0].controls[0].content.controls[1].content.chkbox_mon.value
        is_tue = e.page.controls[0].controls[0].content.controls[1].content.chkbox_tue.value
        is_wed = e.page.controls[0].controls[0].content.controls[1].content.chkbox_wed.value
        is_thu = e.page.controls[0].controls[0].content.controls[1].content.chkbox_thu.value
        is_fri = e.page.controls[0].controls[0].content.controls[1].content.chkbox_fri.value
        is_sat = e.page.controls[0].controls[0].content.controls[1].content.chkbox_sat.value
        weekday = (is_sun, is_mon, is_tue, is_wed, is_thu, is_fri, is_sat)

        # タイムピッカーのデータ取得
        build_time = self.timer_picker_value_ref

        #result = self.jenkins.create(job_name, job_desc, git_url, git_branch, teams_url, build_folder, weekday, build_time)

    def check_input(self, e):
        result = 0

        # テキストのデータ取得(jobのビルド動作に必ず必要なもののみチェックする)
        job_name = e.page.controls[0].controls[0].content.controls[1].content.text_job_name.value
        git_url = e.page.controls[0].controls[0].content.controls[1].content.text_git_url.value
        teams_url = e.page.controls[0].controls[0].content.controls[1].content.text_teams_url.value

        if not job_name or not git_url or not teams_url:
            return (result := -1)

        # チェックボックスのデータ取得
        is_sun = e.page.controls[0].controls[0].content.controls[1].content.chkbox_sun.value
        is_mon = e.page.controls[0].controls[0].content.controls[1].content.chkbox_mon.value
        is_tue = e.page.controls[0].controls[0].content.controls[1].content.chkbox_tue.value
        is_wed = e.page.controls[0].controls[0].content.controls[1].content.chkbox_wed.value
        is_thu = e.page.controls[0].controls[0].content.controls[1].content.chkbox_thu.value
        is_fri = e.page.controls[0].controls[0].content.controls[1].content.chkbox_fri.value
        is_sat = e.page.controls[0].controls[0].content.controls[1].content.chkbox_sat.value
        weekday = (is_sun, is_mon, is_tue, is_wed, is_thu, is_fri, is_sat)

        # 全て選択されなかった場合のみエラーとする
        if not any(weekday):
            return (result := -1)

        return result
