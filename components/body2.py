from flet import(
    UserControl,
    Text,
    Row,
)


class EditJobBody(UserControl):
    def __init__(self):
        super().__init__()
        self.text = Text("準備中", size=100, color="#ffffff")

    def build(self):
        return Row(
            controls=[
            self.text,
        ])
