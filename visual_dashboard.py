import time
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

LOG_FILE = "server_logs.txt"
console = Console()

def generate_stats():
    stats = {"SUCCESS": 0, "ATTACK": 0, "TOTAL": 0}
    recent_alerts = []

    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            stats["TOTAL"] = len(lines)
            for line in lines:
                if "Accepted" in line:
                    stats["SUCCESS"] += 1
                elif "Failed" in line:
                    stats["ATTACK"] += 1
                    # Keep only the last 5 alerts for the display
                    recent_alerts.append(line.strip())
            
        return stats, recent_alerts[-5:] # Return stats and last 5 logs
    except FileNotFoundError:
        return stats, []

def draw_dashboard():
    stats, alerts = generate_stats()
    
    # Create the Layout Table
    table = Table(title="🛡️ AI SOC COMMAND CENTER", expand=True)
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Total Events Processed", str(stats["TOTAL"]))
    table.add_row("Authorized Logins ✅", f"[green]{stats['SUCCESS']}[/green]")
    table.add_row("Intrusion Attempts 🚨", f"[red]{stats['ATTACK']}[/red]")

    # Create an Alert Panel for the bottom
    alert_text = "\n".join(alerts) if alerts else "Waiting for traffic..."
    alert_panel = Panel(alert_text, title="⚠️ RECENT INCIDENTS", border_style="red")
    
    return table, alert_panel

if __name__ == "__main__":
    with Live(console=console, refresh_per_second=2) as live:
        while True:
            table, panel = draw_dashboard()
            # We display the table and the alert panel together
            live.update(Panel.fit(table, title="Live Stats"))
            time.sleep(1)