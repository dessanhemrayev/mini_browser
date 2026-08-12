import time

import requests
from requests.exceptions import MissingSchema, RequestException


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
        return code, f"Сайт {url} недоступен. Код состояния: {code}", elapsed
    except requests.ConnectionError:
        return 0, f"Не удалось подключиться к сайту {url}", 0
    except MissingSchema as e:
        return 0, f"Неверный формат URL: {e}", 0
    except RequestException as e:
        return 0, f"Ошибка при подключении к {url}: {e}", 0
