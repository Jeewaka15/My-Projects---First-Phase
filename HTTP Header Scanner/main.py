import httpx
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from urllib.parse import urlparse

console = Console()

# =========================
# BANNER
# =========================
def show_banner():
    console.print(
        Panel(
            "[bold cyan]HTTP SECURITY HEADER SCANNER[/bold cyan]",
            title="Cyber Security Tool",
            subtitle="Final Version"
        )
    )

# =========================
# URL VALIDATION
# =========================
def validate_url(url):
    parsed = urlparse(url)

    if not parsed.scheme:
        url = "https://" + url

    return url

# =========================
# FETCH RESPONSE
# =========================
def fetch_response(url):
    try:
        response = httpx.get(url, timeout=10)
        return response

    except Exception as e:
        console.print(f"[red]Request Error:[/red] {e}")
        return None

# =========================
# SECURITY HEADERS CHECK
# =========================
def check_headers(response):

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    table = Table(title="Security Header Report")

    table.add_column("Header", style="cyan")
    table.add_column("Status", style="white")
    table.add_column("Value", style="green")

    found = 0

    for header in security_headers:
        value = response.headers.get(header)

        if value:
            found += 1
            table.add_row(header, "✓ Found", value)
        else:
            table.add_row(header, "✗ Missing", "-")

    console.print(table)

    return found, len(security_headers)

# =========================
# SCORE CALCULATION
# =========================
def calculate_score(found, total):

    score = (found / total) * 100

    if score >= 80:
        grade = "A (Strong)"
        color = "green"

    elif score >= 50:
        grade = "B (Medium)"
        color = "yellow"

    else:
        grade = "C (Weak)"
        color = "red"

    console.print(f"\n[{color}]Security Score: {score:.1f}/100 - {grade}[/{color}]")

    return score, grade

# =========================
# EXPORT REPORT
# =========================
def export_report(url, score, grade):

    report = {
        "url": url,
        "score": score,
        "grade": grade
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    console.print("\n[green]Report saved to report.json[/green]")

# =========================
# MAIN FUNCTION
# =========================
def main():

    show_banner()

    url = console.input("[bold green]Enter URL: [/bold green]")
    url = validate_url(url)

    response = fetch_response(url)

    if not response:
        return

    console.print("\n[cyan]Status Code:[/cyan]", response.status_code)
    console.print("[cyan]Final URL:[/cyan]", response.url)

    found, total = check_headers(response)

    score, grade = calculate_score(found, total)

    export_report(url, score, grade)


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    main()