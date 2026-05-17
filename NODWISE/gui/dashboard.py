import customtkinter as ctk
import subprocess

from core.detector import PostureDetector

ctk.set_appearance_mode("dark")

def start_detection():
    detector = PostureDetector()
    detector.run()

def show_graphs():
    subprocess.run(["python", "graphs/generate_graphs.py"])

def launch_dashboard():

    root = ctk.CTk()

    root.title("NODWISE Dashboard")
    root.geometry("900x600")

    title = ctk.CTkLabel(
        root,
        text="NODWISE",
        font=("Arial", 40, "bold")
    )

    title.pack(pady=30)

    subtitle = ctk.CTkLabel(
        root,
        text="Smart ML Framework for Head Movement Awareness",
        font=("Arial", 18)
    )

    subtitle.pack(pady=10)

    start_btn = ctk.CTkButton(
        root,
        text="Start Monitoring",
        width=250,
        height=50,
        command=start_detection
    )

    start_btn.pack(pady=20)

    graph_btn = ctk.CTkButton(
        root,
        text="Show Research Graphs",
        width=250,
        height=50,
        command=show_graphs
    )

    graph_btn.pack(pady=20)

    exit_btn = ctk.CTkButton(
        root,
        text="Exit",
        width=250,
        height=50,
        command=root.destroy
    )

    exit_btn.pack(pady=20)

    root.mainloop()
