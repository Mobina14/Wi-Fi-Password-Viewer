import subprocess
import tkinter as tk
from tkinter import messagebox, ttk

# تابع برای بازیابی اطلاعات وای‌فای‌ها
def get_wifi_passwords():
    wifi_list = []
    try:
        data = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8")
        profiles = [line.split(":")[1][1:] for line in data.splitlines() if "All User Profile" in line]
        for profile in profiles:
            try:
                result = subprocess.check_output(f"netsh wlan show profile \"{profile}\" key=clear", shell=True).decode("utf-8")
                password_line = [line for line in result.splitlines() if "Key Content" in line]
                password = password_line[0].split(":")[1][1:] if password_line else "N/A"
                wifi_list.append((profile, password))
            except subprocess.CalledProcessError:
                wifi_list.append((profile, "N/A"))
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to retrieve Wi-Fi profiles.")
    return wifi_list

# ساخت رابط گرافیکی
def create_gui():
    root = tk.Tk()
    root.title("Wi-Fi Password Viewer")
    root.geometry("500x400")
    root.config(bg="#2c3e50")

    # تیتر
    title_label = tk.Label(root, text="Wi-Fi Password Viewer", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white")
    title_label.pack(pady=10)

    # لیست ویو برای نمایش وای‌فای‌ها
    tree = ttk.Treeview(root, columns=("WiFi Name", "Password"), show="headings")
    tree.heading("WiFi Name", text="WiFi Name")
    tree.heading("Password", text="Password")
    tree.column("WiFi Name", anchor="center")
    tree.column("Password", anchor="center")
    tree.pack(pady=20, fill=tk.BOTH, expand=True)

    # دکمه برای بازیابی رمزها
    def show_passwords():
        wifi_data = get_wifi_passwords()
        for wifi in wifi_data:
            tree.insert("", "end", values=wifi)

    retrieve_button = tk.Button(root, text="Show Wi-Fi Passwords", font=("Helvetica", 12), command=show_passwords, bg="#2980b9", fg="white")
    retrieve_button.pack(pady=10)

    root.mainloop()

# اجرای برنامه
if __name__ == "__main__":
    create_gui()
