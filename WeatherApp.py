import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle",
    53: "Moderate drizzle", 55: "Dense drizzle", 56: "Freezing drizzle",
    57: "Freezing drizzle (dense)", 61: "Rain (slight)", 63: "Rain (moderate)",
    65: "Rain (heavy)", 66: "Freezing rain (light)", 67: "Freezing rain (heavy)",
    71: "Snow fall (slight)", 73: "Snow fall (moderate)", 75: "Snow fall (heavy)",
    77: "Snow grains", 80: "Rain showers (slight)", 81: "Rain showers (moderate)",
    82: "Rain showers (violent)", 85: "Snow showers (slight)", 86: "Snow showers (heavy)",
    95: "Thunderstorm (slight/moderate)", 96: "Thunderstorm with hail (slight)",
    99: "Thunderstorm with hail (heavy)"
}

def fetch_city(city, callback):
    try:
        geo = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
        r = requests.get(geo, timeout=5).json().get("results", [])
        callback(r[0] if r else None, None if r else "City not found")
    except Exception as e:
        callback(None, f"Network Error: {e}")

def fetch_weather(lat, lon, callback):
    try:
        url = (f"https://api.open-meteo.com/v1/forecast?"
               f"latitude={lat}&longitude={lon}"
               f"&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m"
               f"&temperature_unit=celsius&wind_speed_unit=kmh&timezone=auto")
        data = requests.get(url, timeout=5).json()["current"]
        callback(data, None)
    except Exception as e:
        callback(None, f"Weather fetch failed: {e}")

class WeatherApp:
    def __init__(self, root):
        self.root = root
        root.title("Weather App")
        root.geometry("480x420")
        root.configure(bg="#1E1E1E")
        root.resizable(False, False)

        self.apply_styles()
        self.build_ui()

    def apply_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TEntry", padding=6)
        style.configure("TButton",
                        background="#2B2B2B",
                        foreground="#E8E8E8",
                        padding=6,
                        relief="flat")
        style.map("TButton",
                  background=[("active", "#363636")],
                  foreground=[("active", "#FFFFFF")])

    def build_ui(self):
        title = tk.Label(self.root, text="🌤 Let's Weather!",
                         font=("Segoe UI", 20, "bold"),
                         fg="#E8E8E8", bg="#1E1E1E")
        title.pack(pady=12)

        frame = tk.Frame(self.root, bg="#1E1E1E")
        frame.pack()

        self.entry = ttk.Entry(frame, width=28)
        self.entry.grid(row=0, column=0, padx=6)

        btn = ttk.Button(frame, text="Search", command=self.search_city)
        btn.grid(row=0, column=1, padx=6)

        self.card = tk.Frame(self.root, bg="#2B2B2B",
                             highlightbackground="#8A8A8A", highlightthickness=1)
        self.card.pack(pady=25, ipadx=10, ipady=10)
        self.card.pack_propagate(False)
        self.card.config(width=420, height=220)

        self.result = tk.Label(self.card, text="",
                               fg="#E8E8E8", bg="#2B2B2B",
                               justify="left", font=("Segoe UI", 11))
        self.result.pack(anchor="w", padx=18, pady=10)

    def search_city(self):
        city = self.entry.get().strip()
        if not city:
            messagebox.showinfo("Input", "Type a city name first.")
            return
        threading.Thread(target=fetch_city, args=(city, self.handle_city), daemon=True).start()

    def handle_city(self, loc, error):
        if error:
            messagebox.showerror("Error", error)
            return
        threading.Thread(target=fetch_weather,
                         args=(loc["latitude"], loc["longitude"], self.show_weather),
                         daemon=True).start()

    def show_weather(self, data, error):
        if error:
            messagebox.showerror("Error", error)
            return

        text = (f"Temperature : {data['temperature_2m']}°C\n"
                f"Feels Like  : {data['apparent_temperature']}°C\n"
                f"Condition   : {WEATHER_CODES.get(data['weather_code'], 'Unknown')}\n"
                f"Humidity    : {data['relative_humidity_2m']}%\n"
                f"Wind Speed  : {data['wind_speed_10m']} km/h")

        self.result.config(text=text)

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
