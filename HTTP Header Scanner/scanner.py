from urllib.parse import urlparse
import httpx

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def normalize_url(url):

    # if user types google.com → convert to https://google.com
    parsed = urlparse(url)

    if not parsed.scheme:
        url = "https://" + url

    return url


def scan_url(url):

    url = normalize_url(url)

    try:
        response = httpx.get(url, timeout=10)

    except Exception as e:
        return {"error": str(e)}

    found = 0
    results = []

    for header in security_headers:
        value = response.headers.get(header)

        if value:
            found += 1
            results.append({
                "header": header,
                "status": "FOUND",
                "value": value
            })
        else:
            results.append({
                "header": header,
                "status": "MISSING",
                "value": "-"
            })

    score = (found / len(security_headers)) * 100

    return {
        "url": str(response.url),
        "status_code": response.status_code,
        "score": round(score, 2),
        "headers": results
    }