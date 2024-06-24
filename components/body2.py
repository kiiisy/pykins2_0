from flet import(
    UserControl,
    Text,
    Row
)


class EditJobBody(UserControl):
    def __init__(self):
        super().__init__()
        self.text = Text("page2")
        self.text2 = Text("example")

    def build(self):
        return Row(controls=[
            self.text, self.text2
        ])
