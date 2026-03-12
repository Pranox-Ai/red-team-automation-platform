import requests

def check_headers(domain):

    if not domain.startswith("http"):
        url = "http://" + domain
    else:
        url = domain

    try:
        r = requests.get(url, timeout=5)
        headers = r.headers

        security_headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "X-XSS-Protection"
        ]

        result = {}

        for header in security_headers:
            result[header] = "Present" if header in headers else "Missing"

        return result

    except Exception as e:
        return {"error": str(e)}