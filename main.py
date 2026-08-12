import flet as ft

from browser_ui import create_browser_ui
from check_website import check_website


def main(page: ft.Page):
    page.title = "Mini Browser"
    page.window_height = 600
    page.window_width = 500

    ui = create_browser_ui(page)
    view = ui["view"]
    txt_name = ui["txt_name"]
    tasks_view = ui["tasks_view"]
    progress = ui["progress"]
    search_btn = ui["search_btn"]
    set_browser_url = ui["set_browser_url"]

    def btn_click(e):
        url = txt_name.value.strip()
        if not url:
            txt_name.error_text = "Введите URL"
            view.update()
            return

        txt_name.error_text = ""
        progress.visible = True
        search_btn.disabled = True
        view.update()

        code, result, elapsed = check_website(url)

        progress.visible = False
        search_btn.disabled = False
        color = "green" if code == 200 else "red"
        tasks_view.controls.insert(
            0,
            ft.Row(
                controls=[
                    ft.Text(result, size=16, color=color, italic=True),
                    ft.Text(f"{elapsed} ms", size=12, color="grey600"),
                ],
                alignment="spaceBetween",
            ),
        )

        if not url.startswith("http"):
            url = "https://" + url
        set_browser_url(url)
        view.update()

    search_btn.on_click = btn_click
    page.add(view)


ft.app(main)
