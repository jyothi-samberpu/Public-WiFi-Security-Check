import subprocess
import tkinter as tk
from tkinter import font


def set_output(message: str) -> None:
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)
    output_text.tag_configure("center", justify="center")
    output_text.tag_add("center", "1.0", tk.END)
    output_text.config(state="disabled")


def set_status(text: str, tone: str) -> None:
    tone_map = {
        "neutral": (palette["muted"], palette["status_neutral_bg"]),
        "safe": (palette["success"], palette["status_safe_bg"]),
        "danger": (palette["danger"], palette["status_danger_bg"]),
    }
    fg, bg = tone_map.get(tone, tone_map["neutral"])
    status_label.config(text=text, fg=fg, bg=bg)


def set_connection_details(ssid: str, security: str) -> None:
    ssid_value_label.config(text=ssid)
    security_value_label.config(text=security)


def check_wifi() -> None:
    try:
        result = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            stderr=subprocess.STDOUT,
        ).decode(errors="ignore")

        ssid = "Not connected"
        security = "Unknown"

        for line in result.splitlines():
            cleaned = line.strip()
            if cleaned.startswith("SSID") and "BSSID" not in cleaned:
                parts = cleaned.split(":", 1)
                if len(parts) > 1 and parts[1].strip():
                    ssid = parts[1].strip()
            if cleaned.startswith("Authentication"):
                parts = cleaned.split(":", 1)
                if len(parts) > 1 and parts[1].strip():
                    security = parts[1].strip()

        if "open" in security.lower():
            set_status("Unsafe network", "danger")
        else:
            set_status("Protected network", "safe")

        set_connection_details(ssid, security)

        message_lines = [
            "Connection Details",
            "-------------------",
            "",
        ]

        if "open" in security.lower():
            message_lines.append(
                "Warning: This Wi-Fi appears open and may expose your data."
            )
        else:
            message_lines.append(
                "Good: This Wi-Fi is encrypted and safer for daily use."
            )

        set_output("\n".join(message_lines))

    except subprocess.CalledProcessError:
        set_status("Unable to read Wi-Fi details", "danger")
        set_connection_details("Not available", "Not available")
        set_output(
            "Could not fetch Wi-Fi information from Windows.\n"
            "Make sure your wireless adapter is enabled and try again."
        )
    except Exception as error:
        set_status("Unexpected error", "danger")
        set_connection_details("Not available", "Not available")
        set_output(f"Error: {error}")


palette = {
    "bg": "#EEF4F8",
    "card": "#FFFFFF",
    "ink": "#1E2A36",
    "muted": "#5A6A79",
    "primary": "#0C6E8F",
    "primary_hover": "#095973",
    "card_border": "#D1DEE8",
    "panel_bg": "#F6FAFD",
    "danger": "#A5372A",
    "success": "#14663A",
    "status_neutral_bg": "#E7EEF4",
    "status_safe_bg": "#DDF2E6",
    "status_danger_bg": "#F8E1DD",
}


def on_button_enter(_event: tk.Event) -> None:
    check_button.config(bg=palette["primary_hover"])


def on_button_leave(_event: tk.Event) -> None:
    check_button.config(bg=palette["primary"])


root = tk.Tk()
root.title("Wi-Fi Security Checker")
root.geometry("820x540")
root.minsize(760, 500)
root.configure(bg=palette["bg"])

title_font = font.Font(family="Segoe UI", size=21, weight="bold")
subtitle_font = font.Font(family="Segoe UI", size=10)
button_font = font.Font(family="Segoe UI", size=10, weight="bold")
status_font = font.Font(family="Segoe UI", size=11, weight="bold")

header_frame = tk.Frame(root, bg=palette["bg"])
header_frame.pack(fill="x", padx=24, pady=(20, 8))

title_label = tk.Label(
    header_frame,
    text="Public Wi-Fi Security Checker",
    font=title_font,
    bg=palette["bg"],
    fg=palette["ink"],
)
title_label.pack(anchor="center")

subtitle_label = tk.Label(
    header_frame,
    text="Check if your current wireless connection is open or encrypted.",
    font=subtitle_font,
    bg=palette["bg"],
    fg=palette["muted"],
)
subtitle_label.pack(anchor="center", pady=(2, 0))

card = tk.Frame(
    root,
    bg=palette["card"],
    highlightthickness=1,
    highlightbackground=palette["card_border"],
)
card.pack(fill="both", expand=True, padx=24, pady=(6, 20))

action_frame = tk.Frame(card, bg=palette["card"])
action_frame.pack(pady=(16, 10))

check_button = tk.Button(
    action_frame,
    text="Check Wi-Fi Security",
    command=check_wifi,
    font=button_font,
    bg=palette["primary"],
    fg="#FFFFFF",
    activebackground=palette["primary_hover"],
    activeforeground="#FFFFFF",
    relief="flat",
    padx=14,
    pady=8,
    cursor="hand2",
)
check_button.pack(side="left")
check_button.bind("<Enter>", on_button_enter)
check_button.bind("<Leave>", on_button_leave)

status_label = tk.Label(
    action_frame,
    text="Ready to scan",
    font=status_font,
    bg=palette["status_neutral_bg"],
    fg=palette["muted"],
    padx=10,
    pady=4,
)
status_label.pack(side="left", padx=14)

details_frame = tk.Frame(
    card,
    bg=palette["panel_bg"],
    highlightthickness=1,
    highlightbackground=palette["card_border"],
)
details_frame.pack(fill="x", padx=18, pady=(0, 10))

details_title = tk.Label(
    details_frame,
    text="Connection Details",
    font=("Segoe UI", 11, "bold"),
    bg=palette["panel_bg"],
    fg=palette["ink"],
)
details_title.pack(anchor="center", pady=(12, 8))

ssid_row = tk.Frame(details_frame, bg=palette["panel_bg"])
ssid_row.pack(anchor="center", pady=2)

ssid_label = tk.Label(
    ssid_row,
    text="Network Name:",
    font=("Segoe UI", 10, "bold"),
    bg=palette["panel_bg"],
    fg=palette["muted"],
)
ssid_label.pack(side="left", padx=(0, 8))

ssid_value_label = tk.Label(
    ssid_row,
    text="-",
    font=("Segoe UI", 10),
    bg=palette["panel_bg"],
    fg=palette["ink"],
)
ssid_value_label.pack(side="left")

security_row = tk.Frame(details_frame, bg=palette["panel_bg"])
security_row.pack(anchor="center", pady=(0, 12))

security_label = tk.Label(
    security_row,
    text="Authentication:",
    font=("Segoe UI", 10, "bold"),
    bg=palette["panel_bg"],
    fg=palette["muted"],
)
security_label.pack(side="left", padx=(0, 8))

security_value_label = tk.Label(
    security_row,
    text="-",
    font=("Segoe UI", 10),
    bg=palette["panel_bg"],
    fg=palette["ink"],
)
security_value_label.pack(side="left")

output_text = tk.Text(
    card,
    height=10,
    wrap="word",
    bd=0,
    highlightthickness=0,
    font=("Consolas", 11),
    bg=palette["panel_bg"],
    fg=palette["ink"],
    padx=12,
    pady=12,
)
output_text.pack(fill="both", expand=True, padx=18, pady=(4, 18))
output_text.config(state="disabled")

set_connection_details("Not scanned", "Not scanned")

set_output(
    "Press 'Check Wi-Fi Security' to see your current network status and safety message."
)

root.mainloop()