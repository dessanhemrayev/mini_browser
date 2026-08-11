import flet as ft
import requests
from requests.exceptions import MissingSchema, RequestException
import time


def check_website(url, timeout=5):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        start = time.time()
        try:
            response = requests.head(url, timeout=timeout, allow_redirects=True)
            code = response.status_code
        except RequestException:
            response = requests.get(url, timeout=timeout, allow_redirects=True)
            code = response.status_code
        elapsed = int((time.time() - start) * 1000)
        if code == 200:
            return code, f"Сайт {url} доступен", elapsed
        else:
            return code, f"Сайт {url} недоступен. Код состояния: {code}", elapsed
    except requests.ConnectionError:
        return 0, f"Не удалось подключиться к сайту {url}", 0
    except MissingSchema as e:
        return 0, f"Неверный формат URL: {e}", 0
    except RequestException as e:
        return 0, f"Ошибка при подключении к {url}: {e}", 0


def main(page: ft.Page):
    page.title = "Mini Browser"
    page.window_height = 600
    page.window_width = 500

    txt_name = ft.TextField(label="Введите URL", expand=True)
    tasks_view = ft.Column()
    progress = ft.ProgressRing(visible=False)
    search_btn = ft.FloatingActionButton(icon=ft.icons.SEARCH_SHARP)

    view = ft.Column(
        width=450,
        controls=[
            ft.Row(
                controls=[txt_name, search_btn, progress],
            ),
            ft.Divider(),
            tasks_view,
            ft.Divider(),
            ft.Container(
                content=ft.Column(controls=[ft.Text("Просмотр сайта:", size=14),]),
            ),
            ft.Container(content=ft.Column(controls=[])),
        ],
    )

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
        # Открыть сайт во встроенном WebView
        try:
            if not url.startswith("http"):
                url = "https://" + url
            webview.src = url
            webview.update()
        except Exception:
            pass
        view.update()

    search_btn.on_click = btn_click
    page.add(view)
    # Добавляем WebView внизу страницы (после добавления view чтобы поддерживать порядок)
    try:
        webview = ft.WebView(src="about:blank", expand=True)
        page.add(webview)
    except Exception:
        # Если WebView недоступен в текущей версии Flet, пропускаем
        pass


ft.app(main)
