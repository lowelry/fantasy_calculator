import flet as ft


def main(page: ft.page):
    textField = ft.TextField()
    addBtn = ft.ElevatedButton(text="Add")

    page.bg_color = "#FF0000"

    page.add(textField, addBtn)


ft.app(target = main)
