import flet as ft
from structs import RandNum, RandNumArray, PermOfRandRange, UniRandNumArray
from file_writer import FileWriter


def output():
    caseData = []
    writer = FileWriter("input.txt")
    writer.write(caseData)


def main(page: ft.Page):
    """
    変数を追加し、表示するGUIを作成するメイン関数。
    Attributes: page (ft.Page): GUIを表すページオブジェクト。
    Returns   : なし
    """

    # 変数を並べるグリッド
    def drag_will_accept(e):
        e.control.content.border = ft.border.all(2, ft.colors.BLACK45)
        e.control.update()

    def drag_accept(e):
        src = page.get_control(e.src_id)
        e.control.content.content.content.content.value = (
            src.content.content.value.split(" ")[0]
        )
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    def block_on_click(e):
        e.control.content.value = ""
        e.control.update()

    DragTargetArray = ft.Column(
        [
            ft.Row(
                [
                    ft.DragTarget(
                        group="block",
                        content=ft.Container(
                            content=ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text(""),
                                    on_click=block_on_click,
                                ),
                            ),
                            width=50,
                            height=50,
                            bgcolor=ft.colors.BLUE,
                            margin=1,
                        ),
                        on_will_accept=drag_will_accept,
                        on_accept=drag_accept,
                        on_leave=drag_leave,
                    )
                    for _ in range(10)
                ],
                spacing=0,
            )
            for _ in range(10)
        ],
        spacing=0,
    )

    # 変数を追加するプルダウンメニュー
    def on_menu_change(e):
        add_textfield.label = name_arg[addMenu.value]
        add_textfield.update()

    addMenu = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("ランダム数値"),
            ft.dropdown.Option("ランダム数列"),
            ft.dropdown.Option("順列の並べ替え"),
            ft.dropdown.Option("重複なしランダム数列"),
        ],
        on_change=on_menu_change,
    )

    # 対応している引数の情報
    name_arg = {
        "ランダム数値"        : "name min max",
        "ランダム数列"        : "name min max length",
        "順列の並べ替え"      : "name min max",
        "重複なしランダム数列": "name min max length",
    }

    # 変数追加ボタン
    def add_button_click(e):
        sep_list = add_textfield.value.split()
        if len(sep_list) == 0:
            return
        dict_of_variables[sep_list[0]] = " ".join(sep_list[1:])
        Details.controls = [
            ft.Draggable(
                group="block",
                content=ft.Container(
                    content=ft.Text(value=i + " " + j, color=ft.colors.BLACK),
                    bgcolor=ft.colors.CYAN,
                    padding=5,
                    width=100,
                ),
            )
            for i, j in sorted(dict_of_variables.items(), key=lambda x: x[0])
        ]
        print(dict_of_variables, flush=True)
        Details.update()

    add_button = ft.ElevatedButton(text="add", on_click=add_button_click)
    add_textfield = ft.TextField(label="name")
    option = ft.Row([add_textfield, add_button])

    # 変数の詳細を表示する表
    Details = ft.Row(vertical_alignment="START")

    # 変数の一覧
    dict_of_variables = {}

    RandNumRow = ft.Row()
    for i in range(8):
        RandNumRow.controls.append(
            ft.Draggable(
                group="block",
                content=ft.Container(
                    content=ft.Text("RandNum " + str(i)),
                    width=100,
                    height=50,
                    bgcolor=ft.colors.YELLOW,
                ),
            )
        )

    page.add(ft.Row([DragTargetArray, Details], vertical_alignment="START"))
    page.add(addMenu, option)


if __name__ == "__main__":
    ft.app(target=main)
