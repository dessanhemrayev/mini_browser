import flet as ft


def create_browser_ui(page: ft.Page):
    txt_name = ft.TextField(label="Введите URL", expand=True)
    tasks_view = ft.Column()
    progress = ft.ProgressRing(visible=False)
    search_btn = ft.FloatingActionButton(icon=ft.icons.SEARCH_SHARP)
    browser_placeholder = ft.Text("Просмотр сайта:", size=14)
    webview = None

    def set_browser_url(url):
        nonlocal webview
        if not url.startswith("http"):
            url = "https://" + url
        try:
            if webview is None:
                webview = ft.WebView(src=url, expand=True)
                page.add(webview)
            else:
                webview.src = url
                webview.update()
        except Exception:
            browser_placeholder.value = "Встроенный просмотр недоступен в этой сборке. Открываю ссылку в браузере."
            browser_placeholder.update()
            page.launch_url(url)

    view = ft.Column(
        width=450,
        controls=[
            ft.Row(
                controls=[txt_name, search_btn, progress],
            ),
            ft.Divider(),
            tasks_view,
            ft.Divider(),
            ft.Container(content=ft.Column(controls=[browser_placeholder])),
            ft.Container(content=ft.Column(controls=[])),
        ],
    )

    return {
        "view": view,
        "txt_name": txt_name,
        "tasks_view": tasks_view,
        "progress": progress,
        "search_btn": search_btn,
        "set_browser_url": set_browser_url,
    }
