import requests

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers or {}

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]

        missing = []
        present = {k.lower(): v for k, v in headers.items()}
        for header in security_headers:
            if header.lower() not in present:
                missing.append(header)

        return missing
    except requests.RequestException:
        return ["Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options", "X-XSS-Protection"]
