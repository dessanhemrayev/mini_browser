import flet as ft

import requests
from requests.exceptions import MissingSchema


def check_website(url):
    if not url.startswith("http"):
        url = "https://" + url  # Добавляем схему https://, если ее нет
    code = 400
    try:
        response = requests.head(url)
        code = response.status_code
        if code == 200:
            return code, f"Сайт {url} доступен"
        else:
            return code, f"Сайт {url} недоступен. Код состояния: {code}"
    except requests.ConnectionError:
        return code, f"Не удалось подключиться к сайту {url}"
    except MissingSchema as e:
        return code, f"Неверный формат URL: {e}"


def main(page: ft.Page):
    page.title = "Mini Browser"
    page.window_height = 600
    page.window_width = 500

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your url"
            view.update()
        else:
            code, result = check_website(txt_name.value)
            txt_name.error_text = ""
            page.add(
                ft.Text(
                    result,
                    size=20,
                    color="pink600" if code != 200 else "green",
                    italic=True,
                )
            )

    txt_name = ft.TextField(label="Your url", expand=True)
    tasks_view = ft.Column()
    view = ft.Column(
        width=450,
        controls=[
            ft.Row(
                controls=[
                    txt_name,
                    ft.FloatingActionButton(
                        icon=ft.icons.SEARCH_SHARP, on_click=btn_click
                    ),
                ],
            ),
            tasks_view,
        ],
    )
    page.add(view)


ft.app(main)
