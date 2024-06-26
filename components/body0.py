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
    TextButton,
    ButtonStyle,
    Ref,
    Divider,
    AlertDialog,
    TextStyle,
    ButtonStyle,
    TimePicker,
    TimePickerEntryMode,
)


class AutoBuildBody(UserControl):
    def __init__(self, page: Page, jenkins):
        super().__init__()
        self.page = page
        self.jenkins = jenkins

        # Job関連のウィジェット作成
        self.text_job = Text("Job設定", size=19, color="#dcdcdc", font_family="YuGothic")
        self.text_job_name = TextField(label="Job名(必須)",
                                       label_style=TextStyle(color="#87ceeb"),
                                       text_size=15,
                                       text_style=TextStyle(font_family="YuGothic"),
                                       width=376,
                                       border_width=3,
                                       border_radius=10,
                                       border_color="#add8e6",
                                       hint_text="プロジェクト名と同じであること",
                                       hint_style=TextStyle(color="#fffafa"),
                                       focused_border_color="#e0ffff",
                                       color="#fffafa",
                                       )
        self.text_job_desc = TextField(label="Job概要",
                                       label_style=TextStyle(color="#87ceeb"),
                                       text_size=15,
                                       text_style=TextStyle(font_family="YuGothic"),
                                       width=376,
                                       border_width=3,
                                       border_radius=10,
                                       border_color="#add8e6",
                                       hint_text="例) <Job名>のAutoビルド用",
                                       hint_style=TextStyle(color="#fffafa"),
                                       focused_border_color="#e0ffff",
                                       color="#fffafa",
                                       )

        # Git関連のウィジェット作成
        self.text_git = Text("Git設定", size=19, color="#dcdcdc", font_family="YuGothic")
        self.text_git_url = TextField(label="Git URL(必須)",
                                      label_style=TextStyle(color="#87ceeb"),
                                      text_size=15,
                                      text_style=TextStyle(font_family="YuGothic"),
                                      border_width=3,
                                      border_radius=10,
                                      border_color="#add8e6",
                                      focused_border_color="#e0ffff",
                                      color="#fffafa",
                                      )
        self.text_git_branch = TextField(label="ブランチ名",
                                         label_style=TextStyle(color="#87ceeb"),
                                         text_size=15,
                                         text_style=TextStyle(font_family="YuGothic"),
                                         width=376,
                                         border_width=3,
                                         border_radius=10,
                                         border_color="#add8e6",
                                         focused_border_color="#e0ffff",
                                         color="#fffafa",
                                         )
        self.text_build_folder = TextField(label="ビルド対象フォルダ",
                                           label_style=TextStyle(color="#87ceeb"),
                                           text_size=15,
                                           text_style=TextStyle(font_family="YuGothic"),
                                           width=376,
                                           border_width=3,
                                           border_radius=10,
                                           border_color="#add8e6",
                                           focused_border_color="#e0ffff",
                                           color="#fffafa",
                                           )

        # Teams関連のウィジェット作成
        self.text_teams = Text("Teams設定", size=19, color="#dcdcdc", font_family="YuGothic")
        self.text_teams_url = TextField(label="Teams URL(必須)",
                                        label_style=TextStyle(color="#87ceeb"),
                                        text_size=15,
                                        border_width=3,
                                        border_radius=10,
                                        border_color="#add8e6",
                                        focused_border_color="#e0ffff",
                                        color="#fffafa",
                                        password=True,
                                        can_reveal_password=True,
                                        )

        # Build関連のウィジェット作成
        self.text_buid_setting = Text("Build設定", size=19, color="#dcdcdc", font_family="YuGothic")
        self.text_buid_data = Text("ビルド実行曜日", size=17, color="#dcdcdc", font_family="YuGothic")
        self.chkbox_sun = Checkbox(label="Sun",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=False,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_mon = Checkbox(label="Mon",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=True,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_tue = Checkbox(label="Tue",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=True,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_wed = Checkbox(label="Wed",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=True,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_thu = Checkbox(label="Thu",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=True,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_fri = Checkbox(label="Fri",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=True,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )
        self.chkbox_sat = Checkbox(label="Sat",
                                   label_style=TextStyle(color="#fffafa", font_family="Arial"),
                                   shape=RoundedRectangleBorder(radius=5),
                                   value=False,
                                   scale=1.2,
                                   check_color="#ffffff",
                                   active_color="#4169e1",
                                   )

        # 実行ボタンのウィジェット作成
        self.button = ElevatedButton(
            text="実行",
            color="#f8f8ff",
            bgcolor="#0054FF",
            width=150,
            style=ButtonStyle(overlay_color="#0000cd"),
            on_click=self.handle_open_dlg,
        )
        self.dlg = AlertDialog(
            # ダイアログの外側をクリックして閉じれないようにする
            modal=True,
            title=Text("Alert Dialog", size=25, font_family="Arial"),
            content=Text("必須項目を入力してください", size=15, font_family="YuGothic"),
            actions=[
                TextButton("閉じる", on_click=self.handle_close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        # タイムピッカーのウィジェット作成
        self.timer_picker = TimePicker(
            error_invalid_text="有効な時間を入力してください",
            help_text="時間を入力してください",
            time_picker_entry_mode=TimePickerEntryMode.INPUT_ONLY,
            on_change=self.handle_change_timer_picker,
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
                        self.text_job_desc,
                    ]
                ),
                Divider(height=5, color="#292929", thickness=2),
                self.text_git,
                self.text_git_url,
                Row(
                    controls=[
                        self.text_git_branch,
                        self.text_build_folder,
                    ]
                ),
                Divider(height=5, color="#292929", thickness=2),
                self.text_teams,
                self.text_teams_url,
                Divider(height=5, color="#292929", thickness=2),
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
                        self.chkbox_sat,
                    ]
                ),
                Row(
                    tight=True,
                    spacing=25,
                    controls=[
                        Text("ビルド開始時間", size=17, color="#dcdcdc", font_family="YuGothic"),
                        TextButton(
                            content=Text("22:00",
                                        size=20,
                                        color="#f8f8ff",
                                        font_family="Arial",
                                        ref=self.timer_picker_value_ref,
                                    ),
                            on_click=self.handle_open_time_picker,
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

    async def handle_open_time_picker(self, e):
        await self.timer_picker.pick_time_async()

    async def handle_change_timer_picker(self, e):
        time_ = time.strptime(e.data, "%H:%M")
        self.timer_picker_value_ref.current.value = str(time_[3]) + ":" + str(time_[4])
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

    def did_mount(self):
        # タイムピッカーを現在のページにマウント
        self.page.overlay.append(self.timer_picker)
        self.page.update()

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
