from flet import(
    UserControl,
    Text,
    Row
)


class AutoSimBody(UserControl):
    def __init__(self):
        super().__init__()
        self.text = Text("page1")
        self.text2 = Text("example")

    def build(self):
        return Row(controls=[
            self.text, self.text2
        ])
