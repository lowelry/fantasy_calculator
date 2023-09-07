import flet as ft


def main(page: ft.page):
    textField = ft.TextField()
    addBtn = ft.ElevatedButton(text="Add")

    page.bgcolor = "#FF9B82"
    addBtn.bgcolor = "#57375D"

    page.add(textField, addBtn)


ft.app(target = main)
