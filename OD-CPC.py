#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
OD-CPC

@Author: Otkupman D.G.
@Description: Compound Parabolic Concentrator Modeling Tool with GUI
@License: MIT
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import threading
import time
import math

class CPC_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("OD-CPC — Compound Parabolic Concentrator Modeling Tool © Otkupman D.G.")
        self.root.minsize(width=860, height=768)
        # Set icon
        icon = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAxnpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjabVBBEsMgCLz7ij4BWTT4HNPYmf6gzy9G7MS2m3GzgLMCob2ej3Dr4ChB0qa55EwGKVK4mlAaqCdHkpM9oCmWfPgU2FKwP0ao2e/PfKTFKVZT6WKkdy/sa6GI++uXkT+E3hGbONyouBF4FKIb1DEW5aLbdYS90QodJ3Ta3fXsiH5j2Wx7R7J3wNwQQcaAjgbQTwqoJooxI9vFaF+FWFSRMEeyhfzb00R4AzhqWdEvgiPTAAABhWlDQ1BJQ0MgcHJvZmlsZQAAeJx9kT1Iw0AcxV9bpVUqDnaQ4hChOohdVMSxVLEIFkpboVUHk0u/oElDkuLiKLgWHPxYrDq4OOvq4CoIgh8g7oKToouU+L+k0CLGg+N+vLv3uHsHeJtVphg9MUBRTT2diAu5/Krgf0UfwghgAqMiM7RkZjEL1/F1Dw9f76I8y/3cn2NALhgM8AjEMabpJvEG8eymqXHeJw6xsigTnxNP6nRB4keuSw6/cS7Z7OWZIT2bnicOEQulLpa6mJV1hXiGOCIrKuV7cw7LnLc4K9U6a9+TvzBYUFcyXKc5ggSWkEQKAiTUUUEVJqK0qqQYSNN+3MUftv0pcknkqoCRYwE1KBBtP/gf/O7WKE5POUnBOND7YlkfY4B/F2g1LOv72LJaJ4DvGbhSO/5aE5j7JL3R0SJHwOA2cHHd0aQ94HIHGH7SRF20JR9Nb7EIvJ/RN+WBoVugf83prb2P0wcgS10t3wAHh8B4ibLXXd4d6O7t3zPt/n4A5zly1awNjdEAAA12aVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA0LjQuMC1FeGl2MiI+CiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpHSU1QPSJodHRwOi8vd3d3LmdpbXAub3JnL3htcC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgeG1wTU06RG9jdW1lbnRJRD0iZ2ltcDpkb2NpZDpnaW1wOmYyMWI4NWUzLTdiYjUtNDVjZC05YmU2LWE1Mzk2MTFhOTE2ZCIKICAgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpmZWVhOTE2Yi1kNTBmLTRiYzgtYjM2MC0xMjM3YTVlMjhhMmYiCiAgIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpjZDU4OWFhNi02MDBmLTQ0N2YtOTMxOC0xNmViN2JlZDI1NWMiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICBHSU1QOkFQST0iMi4wIgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTc1ODg3NjE3MzY4NjY5NCIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjM4IgogICB0aWZmOk9yaWVudGF0aW9uPSIxIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyNTowOToyNlQxMTo0Mjo1MyswMzowMCIKICAgeG1wOk1vZGlmeURhdGU9IjIwMjU6MDk6MjZUMTE6NDI6NTMrMDM6MDAiPgogICA8eG1wTU06SGlzdG9yeT4KICAgIDxyZGY6U2VxPgogICAgIDxyZGY6bGkKICAgICAgc3RFdnQ6YWN0aW9uPSJzYXZlZCIKICAgICAgc3RFdnQ6Y2hhbmdlZD0iLyIKICAgICAgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo2MGM4NjA2ZS01MDRmLTQyZGMtYWRhYS0yYTM3YmFkNWM3M2UiCiAgICAgIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkdpbXAgMi4xMCAoV2luZG93cykiCiAgICAgIHN0RXZ0OndoZW49IjIwMjUtMDktMjZUMTE6NDI6NTMiLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+paAlzAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAAd0SU1FB+kJGggqNfjgbNMAAAD5SURBVDjLpZO/SgQxEIe/OWy2uaexmsYrLGxs70UsFbIBLe99LJWTgGBzr7LNlWNxzpLNn1VwIGThN5n95ZuJ2ITxjxDAbILxECpxfIiXvaPJFjae4Ml5wngIqxoAqmqAhRDMpuWer1IDTFVNfopaCKGu3rDtWowRQDZN24XlNW12UILM/1a6coCAiHNIKdEqUnbBD6sqKaXLFVJK0utGj4GfuaqSsiL5FXrzMENUVSe7GjFGVLWCSAtmy4nDqxy4C9nSbaPD+y2qacyn7y8PbDG2+XerwKILN3df9vx4ZrcfAPg43QLw9jmw299zPJ55ehns/fV6ZvANLLDCy1QHI3IAAAAASUVORK5CYII="
        img = tk.PhotoImage(data=icon)
        self.root.tk.call("wm", "iconphoto", root._w, img)
        
        # Main parameter variables
        self.theta_var = tk.DoubleVar(value=30.0)
        self.d1_var = tk.DoubleVar(value=50.0)
        self.step_var = tk.IntVar(value=100)
        self.n_var = tk.DoubleVar(value=1.0)
        self.d2_var = tk.DoubleVar()
        self.r2_var = tk.DoubleVar()
        self.s2_var = tk.DoubleVar()
        self.r1_var = tk.DoubleVar()
        self.s1_var = tk.DoubleVar()
        self.ratio_var = tk.DoubleVar()
        self.f_var = tk.DoubleVar()
        self.L_var = tk.DoubleVar()
        self.C_max_var = tk.DoubleVar()
        
        # Variables for STL export
        self.decimal_places_var = tk.IntVar(value=6)
        self.radial_segments_var = tk.IntVar(value=36)
        self.export_half_only_var = tk.BooleanVar(value=False)
        
        # Variables for ray tracing
        self.ray_pos_var = tk.DoubleVar(value=0.0)
        self.ray_angle_var = tk.DoubleVar(value=0.0)
        self.show_ray_labels_var = tk.BooleanVar(value=False)
        self.accumulate_rays_var = tk.BooleanVar(value=False)
        
        # Variables for the progress bar
        self.progress_var = tk.DoubleVar(value=0.0)
        self.progress_label_var = tk.StringVar(value="Ready")
        
        # Cached parameters
        self.current_theta = None
        self.current_d1 = None
        self.cpc_params = None
        self.profile_points = None
        
        # Trace data
        self.ray_paths = []  # list of all traced rays
        self.current_ray_path = []  # current ray
        self.current_ray_segments_info = []  # current ray metadata
        
        # Interpolation step for finding intersections
        self.intersection_eps = 1e-8
        
        self.create_widgets()
        self.calculate_all()
        
        self.root.bind('<Return>', lambda event: self.calculate_all()) # pressing Enter
    
    def create_widgets(self):
        # Main frames
        input_frame = ttk.LabelFrame(self.root, text="Input Parameters", padding=8)
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        
        result_frame = ttk.Frame(self.root, padding=7)
        result_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        ray_frame = ttk.Frame(self.root, padding=4)
        ray_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
        
        stl_frame = ttk.Frame(self.root, padding=4)
        stl_frame.grid(row=3, column=0, padx=5, pady=5, sticky="sw")
        
        # Creating tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=1, rowspan=4, padx=5, pady=5, sticky="nsew")
        
        # First tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Geometry")
        
        # Second tab
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Parameter Dependencies")
        
        # Setting up charts for tabs
        self.setup_tab1_geometry()
        self.setup_tab2_dependencies()
        
        # Input parameters
        ttk.Label(input_frame, text="Acceptance half-angle θ (°):").grid(row=0, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.theta_var, width=10).grid(row=0, column=1, sticky="w")
        
        ttk.Label(input_frame, text="Receiver Ø (mm):").grid(row=1, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.d1_var, width=10).grid(row=1, column=1, sticky="w")
        
        ttk.Label(input_frame, text="Step (points + 1):").grid(row=2, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.step_var, width=10).grid(row=2, column=1, sticky="w")
        ttk.Label(input_frame, text="1 — cone", font=("", "8", "italic")).grid(row=3, column=1, sticky="w")
        
        ttk.Label(input_frame, text="Refractive index:").grid(row=4, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.n_var, width=10).grid(row=4, column=1, sticky="w")
        ttk.Label(input_frame, text="1 — mirror", font=("", "8", "italic")).grid(row=5, column=1, sticky="w")
        
        style = ttk.Style()
        style.configure("TButton", background="yellow")
        ttk.Button(input_frame, text="Calculate & Redraw", command=self.calculate_all).grid(row=6, column=0, columnspan=2, pady=7)
        
        # Ray tracing controls
        ttk.Label(ray_frame, text="🗦 Ray Tracing 🗧", foreground="dark red").grid(row=0, column=0, sticky="w")
        ttk.Label(ray_frame, text="Position on aperture (mm):").grid(row=1, column=0, sticky="w")
        ttk.Entry(ray_frame, textvariable=self.ray_pos_var, width=10).grid(row=1, column=1, sticky="w")
        ttk.Label(ray_frame, text="±R").grid(row=1, column=2, sticky="w")
        ttk.Label(ray_frame, text="Angle (°):").grid(row=2, column=0, sticky="w") # relative to optical axis
        ttk.Entry(ray_frame, textvariable=self.ray_angle_var, width=10).grid(row=2, column=1, sticky="w")
        ttk.Label(ray_frame, text="±θ").grid(row=2, column=2, sticky="w")
        
        ttk.Checkbutton(ray_frame, text="Show labels", variable=self.show_ray_labels_var,
                        command=self.on_toggle_show_labels).grid(row=3, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(ray_frame, text="Accumulate rays", variable=self.accumulate_rays_var).grid(row=4, column=0, columnspan=2, sticky="w")
        
        ttk.Button(ray_frame, text="Trace", command=self.trace_ray_button).grid(row=5, column=0, pady=7)
        ttk.Button(ray_frame, text="Clear", command=self.clear_ray).grid(row=5, column=1, pady=7)
        
        # Results
        ttk.Label(result_frame, text="Calculation Results", font=("", "12", "bold")).grid(row=0, column=0, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Aperture Ø (mm):").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.d2_var).grid(row=1, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Aperture R (mm):").grid(row=2, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.r2_var).grid(row=2, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Aperture area (mm²):").grid(row=3, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.s2_var).grid(row=3, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Receiver R (mm):").grid(row=4, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.r1_var).grid(row=4, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Receiver area (mm²):").grid(row=5, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.s1_var).grid(row=5, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Area ratio:").grid(row=6, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.ratio_var).grid(row=6, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Focal length (mm):").grid(row=7, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.f_var).grid(row=7, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Length (mm):").grid(row=8, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.L_var).grid(row=8, column=1, sticky="w", pady=2)
        
        ttk.Label(result_frame, text="Maximum concentration:").grid(row=9, column=0, sticky="w", pady=2)
        ttk.Label(result_frame, textvariable=self.C_max_var).grid(row=9, column=1, sticky="w", pady=2)
        
        # STL Export Settings
        ttk.Label(stl_frame, text="Export", font=("", "10", "underline")).grid(row=0, column=0, sticky="w")
        
        ttk.Label(stl_frame, text="Decimal places:").grid(row=1, column=0, sticky="w")
        ttk.Entry(stl_frame, textvariable=self.decimal_places_var, width=10).grid(row=1, column=1)
        
        ttk.Label(stl_frame, text="Radial segments:").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Entry(stl_frame, textvariable=self.radial_segments_var, width=10).grid(row=2, column=1)
        ttk.Label(stl_frame, text="4 — square", font=("", "8", "italic")).grid(row=3, column=1, sticky="w")
        
        ttk.Checkbutton(stl_frame, text="Half only", variable=self.export_half_only_var).grid(row=4, column=1, sticky="w")
        
        ttk.Button(stl_frame, text="Save to STL", command=self.start_stl_export).grid(row=5, column=1, pady=(6,0))
        
        # Progress bar
        self.progress_frame = ttk.Frame(self.root)
        self.progress_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        
        self.progress_label = ttk.Label(self.progress_frame, textvariable=self.progress_label_var)
        self.progress_label.pack(side=tk.TOP, fill=tk.X, pady=(0, 5))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, variable=self.progress_var, maximum=100, mode='determinate')
        self.progress_bar.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        self.progress_frame.grid_remove()  # hide the progress bar initially
        
        # Grid settings
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_rowconfigure(3, weight=0)
    
    def setup_tab1_geometry(self):
        self.fig1, self.ax1 = plt.subplots(figsize=(8, 5))
        self.canvas1 = FigureCanvasTkAgg(self.fig1, self.tab1)
        self.canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.toolbar1 = NavigationToolbar2Tk(self.canvas1, self.tab1)
        self.toolbar1.update()
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def setup_tab2_dependencies(self):
        self.fig2, self.ax2_primary = plt.subplots(figsize=(8, 5))
        self.ax2_secondary = self.ax2_primary.twinx()
        
        self.canvas2 = FigureCanvasTkAgg(self.fig2, self.tab2)
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.toolbar2 = NavigationToolbar2Tk(self.canvas2, self.tab2)
        self.toolbar2.update()
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Initializing an empty graph
        self.plot_dependencies()
    
    def plot_dependencies(self): # nomogram
        self.ax2_primary.clear()
        self.ax2_secondary.clear()
        
        # Range of angles for analysis (from 1 to 89 degrees)
        theta_range = np.linspace(1, 89, 100)
        theta_rad = np.radians(theta_range)
        
        # Current parameters
        current_d1 = self.d1_var.get()
        current_n = self.n_var.get()
        
        # Calculating dependencies
        #d2_range = current_d1 / np.sin(theta_rad)  # aperture diameter
        L_range = (current_d1/2 * (1 + np.sin(theta_rad)) * np.cos(theta_rad)) / (np.sin(theta_rad) ** 2)  # length
        C_max_range = current_n ** 2 / (np.sin(theta_rad) ** 2)  # maximum concentration
        
        # The graph on the main axis (left) is Concentration
        color_red = 'tab:red'
        self.ax2_primary.plot(theta_range, C_max_range, color=color_red, linewidth=2, label='Max Concentration')
        self.ax2_primary.set_xlabel('Acceptance Half-Angle θ (°)')
        self.ax2_primary.locator_params(axis='x', nbins=20)
        self.ax2_primary.set_xlim(0, 90)
        self.ax2_primary.set_ylabel('Maximum Concentration', color=color_red)
        self.ax2_primary.tick_params(axis='y', direction='inout', length=10, width=2, color=color_red, labelcolor=color_red)
        self.ax2_primary.tick_params(axis='y', which='minor', direction='in', length=5, color=color_red, labelcolor=color_red)
        self.ax2_primary.grid(axis='y', color='r', alpha=0.3)
        self.ax2_primary.grid(visible=True, which='minor', color='r', alpha=0.1)
        self.ax2_primary.set_yscale('log')  # log scale
        
        # Graph on the second axis (right) is Length
        color_blue = 'tab:blue'
        self.ax2_secondary.plot(theta_range, L_range, color=color_blue, linewidth=2, linestyle='--', label='Length')
        self.ax2_secondary.set_ylabel('Length (mm)', color=color_blue)
        self.ax2_secondary.tick_params(axis='y', direction='inout', length=10, width=2, color=color_blue, labelcolor=color_blue)
        self.ax2_secondary.tick_params(axis='y', which='minor', direction='in', length=5, color=color_blue, labelcolor=color_blue)
        self.ax2_secondary.yaxis.set_label_position("right")  # signature on the right
        self.ax2_secondary.yaxis.tick_right()  # divisions on the right
        self.ax2_secondary.grid(color='b', alpha=0.3, linestyle='--')
        self.ax2_secondary.grid(visible=True, which='minor', color='b', alpha=0.1, linestyle='--')
        self.ax2_secondary.set_yscale('log')  # log scale
        
        # Mark the current angle value if there is a calculation
        if self.current_theta is not None:
            current_theta = self.current_theta
            current_C_max = self.cpc_params['C_max'] if self.cpc_params else current_n ** 2 / (np.sin(np.radians(current_theta)) ** 2)
            current_L = self.cpc_params['L'] if self.cpc_params else (current_d1/2 * (1 + np.sin(np.radians(current_theta))) * np.cos(np.radians(current_theta))) / (np.sin(np.radians(current_theta)) ** 2)
            
            # Vertical line at the current angle
            self.ax2_primary.axvline(x=current_theta, color='green', linestyle=':', alpha=0.7, label=f'Current θ = {current_theta}°')
            
            # Points on curves
            self.ax2_primary.plot(current_theta, current_C_max, 'ro', markersize=7)
            self.ax2_secondary.plot(current_theta, current_L, 'bo', markersize=7)
        
        # Setting up a schedule
        self.ax2_primary.grid(True, alpha=0.4)
        self.ax2_primary.set_title('Maximum Concentration vs Acceptance Half-Angle vs Lenght')
        
        # Combining legends from two axes
        lines1, labels1 = self.ax2_primary.get_legend_handles_labels()
        lines2, labels2 = self.ax2_secondary.get_legend_handles_labels()
        self.ax2_primary.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
        
        self.fig2.tight_layout()
        self.canvas2.draw()
    
    def calculate_cpc_parameters(self, theta_deg, d1, n):
        """Calculates all CPC parameters once and caches them"""
        # z = (f/2)(1 + cosφ)  ⇒  cosφ = 2z/f - 1; r = f·sinφ/(1 + cosφ) + d/2 = f·tan(φ/2) + d/2
        theta = np.radians(theta_deg)
        
        # Basic constants
        C = np.cos(theta)
        S = np.sin(theta)
        P = 1 + S
        Q = 1 + P
        T = 1 + Q
        
        # Basic calculations
        d2 = d1 / S
        focus = (d1 / 2) * (1 + S)
        L = (focus * C) / (S ** 2)
        C_max = n ** 2 / (S ** 2)
        
        # Pre-calculated constants for the profile equation
        A_const = C ** 2
        B_const_part1 = 2 * C * S
        B_const_part2 = 2 * (d1 / 2) * P ** 2
        D_const_part1 = S ** 2
        D_const_part2 = 2 * (d1 / 2) * C * Q
        D_const_part3 = (d1 / 2) ** 2 * P * T
        
        return {
            'theta': theta,
            'theta_deg': theta_deg,
            'd1': d1,
            'd2': d2,
            'focus': focus,
            'L': L,
            'C_max': C_max,
            'C': C,
            'S': S,
            'P': P,
            'Q': Q,
            'T': T,
            'A_const': A_const,
            'B_const_part1': B_const_part1,
            'B_const_part2': B_const_part2,
            'D_const_part1': D_const_part1,
            'D_const_part2': D_const_part2,
            'D_const_part3': D_const_part3
        }
    
    def calculate_profile_points(self, params, num_points):
        if num_points == 1:
            z_values = np.array([0, params['L']])
        else:
            z_values = np.linspace(0, params['L'], num_points + 1)
            
        profile_points = []
        
        for z in z_values:
            B = params['B_const_part1'] * z + params['B_const_part2']
            D = (params['D_const_part1'] * z ** 2 - 
                 params['D_const_part2'] * z - 
                 params['D_const_part3'])
            
            discriminant = B ** 2 - 4 * params['A_const'] * D
            if discriminant >= 0:
                r = (-B + np.sqrt(discriminant)) / (2 * params['A_const'])
                profile_points.append((z, r))
            else:
                profile_points.append((z, 0.0))
        
        return profile_points
    
    def calculate_all(self):
        try:
            theta_deg = self.theta_var.get()
            d1 = self.d1_var.get()
            num_points = self.step_var.get()
            n = self.n_var.get()
            
            if theta_deg <= 0 or theta_deg >= 90:
                messagebox.showerror("Error", "Angle θ must be between 0 and 90 degrees")
                return
            
            # Calculate all parameters once
            self.cpc_params = self.calculate_cpc_parameters(theta_deg, d1, n)
            self.profile_points = self.calculate_profile_points(self.cpc_params, max(1, int(num_points)))
            
            # Updating variables
            self.d2_var.set(f"{self.cpc_params['d2']:.7G}")
            self.r2_var.set(f"{self.cpc_params['d2']/2:.7G}")
            self.s2_var.set(f"{np.pi*(self.cpc_params['d2']/2)**2:.7G}")
            self.r1_var.set(f"{self.cpc_params['d1']/2:.7G}")
            self.s1_var.set(f"{np.pi*(self.cpc_params['d1']/2)**2:.7G}")
            self.ratio_var.set(f"1:{self.cpc_params['d2']/self.cpc_params['d1']:.7G}")
            self.f_var.set(f"{self.cpc_params['focus']:.7G}")
            self.L_var.set(f"{self.cpc_params['L']:.7G}")
            self.C_max_var.set(f"{self.cpc_params['C_max']:.7G}")
            
            # Caching current parameters
            self.current_theta = theta_deg
            self.current_d1 = d1
            
            # Redraw the graphs on both tabs
            self.plot_cpc_profile()
            self.plot_dependencies()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def plot_cpc_profile(self):
        """Builds a CPC profile graph using cached data and draws ray traces"""
        if not self.cpc_params or not self.profile_points:
            return
            
        self.ax1.clear()
        params = self.cpc_params
        
        # Extracting data from a profile
        z_values = [p[0] for p in self.profile_points]
        r_values = [p[1] for p in self.profile_points]
        
        # Filling the area between the top and bottom of the profile
        if self.n_var.get() == 1:
            cpc_color = 'silver'
        else:
            cpc_color = 'lightblue'
        self.ax1.fill_between(z_values, r_values, [-r for r in r_values], color=cpc_color, alpha=0.35)
        # Building a profile
        self.ax1.plot(z_values, r_values, 'b-', linewidth=2, label='Profile')
        self.ax1.plot(z_values, [-r for r in r_values], 'b-', linewidth=2)
        
        # Lower and upper canonical ray
        self.ax1.plot([params['L'], 0], 
                    [-params['d2']/2, params['d1']/2], 
                    color='orange', linewidth=1, label='Canonical ray')
        self.ax1.plot([params['L'], 0], 
                    [params['d2']/2, -params['d1']/2], 
                    color='orange', linewidth=1)
        # Aperture
        self.ax1.plot([params['L'], params['L']], 
                    [-params['d2']/2, params['d2']/2], 
                    color='orangered', linewidth=3, label='Aperture')
        # Receiver
        self.ax1.plot([0, 0], 
                    [-params['d1']/2, params['d1']/2], 
                    'r-', linewidth=3, label='Receiver')
        
        # Optical axis and point of intersection of rays
        self.ax1.axhline(y=0, color='k', linestyle='-.', alpha=0.5, label='Optical axis')
        self.ax1.plot(params['d1']/(2*np.tan(params["theta"])), 0, 'mo', markersize=2) #label='Intersection of rays'
        
        # Draw all accumulated rays
        colors = ['green', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        for idx, (ray_path, segments_info) in enumerate(self.ray_paths):
            color = colors[idx % len(colors)]
            zs = [p[0] for p in ray_path]
            rs = [p[1] for p in ray_path]
            
            # Draw ray segments
            for i in range(len(zs)-1):
                z0, z1 = zs[i], zs[i+1]
                r0, r1 = rs[i], rs[i+1]
                self.ax1.plot([z0, z1], [r0, r1], color=color, linewidth=1, marker='o', markersize=3)
                
                if self.show_ray_labels_var.get() and i < len(segments_info):
                    angle_deg = segments_info[i].get("angle_deg", None)
                    mz = 0.5*(z0+z1)
                    mr = 0.5*(r0+r1)
                    if angle_deg is not None:
                        self.ax1.text(mz, mr, f"{i+1}: {angle_deg:.1f}°", fontsize=8, 
                                   color='darkred', bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7))
                    else:
                        self.ax1.text(mz, mr, f"{i+1}", fontsize=8, 
                                   color='darkred', bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7))
            
            # Show end point on collector for last beam only when labels are enabled
            if self.show_ray_labels_var.get() and idx == len(self.ray_paths) - 1 and len(ray_path) > 1:
                final_z, final_r = ray_path[-1]
                if abs(final_z) < 1e-6:  # if the beam reached the collector (z=0)
                    self.ax1.plot(final_z, final_r, 's', markersize=8, color=color, 
                               label=f'Ray position: {final_r:.3f} mm')
                    self.ax1.text(final_z + params['L']*0.02, final_r, 
                               f'{final_r:.3f} mm', fontsize=9, color=color,
                               bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.8))
        
        # Setting up a schedule
        self.ax1.set_xlabel('Axial coordinate (mm)')
        self.ax1.set_ylabel('Radial coordinate (mm)')
        
        # Determining the name depending on the parameters
        if self.radial_segments_var.get() == 4 and self.step_var.get() == 1:
            name = 'Truncated Pyramid'
        elif self.radial_segments_var.get() == 4:
            name = 'Square CPC'
        elif self.step_var.get() == 1:
            name = 'Cone'
        else:
            name = 'CPC'
            
        self.ax1.set_title(f'{name} Drawing (2θ = {2*params["theta_deg"]:.4G}°)')
        self.ax1.grid(True, alpha=0.5)
        self.ax1.minorticks_on()
        self.ax1.grid(which="minor", linestyle='dotted', alpha=0.2)
        self.ax1.set_aspect('equal')
        #self.ax1.set_xlim(-params['L']*0.05, params['L']*1.05)
        #self.ax1.set_ylim(-params['d2']/2*1.5, params['d2']/2*1.5)
        
        # Legend only if there are elements and labels are enabled
        if self.show_ray_labels_var.get() and len(self.ax1.get_legend_handles_labels()[0]) > 0:
            self.ax1.legend(fontsize=8)
            
        self.fig1.patch.set_facecolor('#f0f0f0')
        plt.tight_layout()
        
        self.canvas1.draw()
    
    def trace_ray_button(self):
        if not self.cpc_params or not self.profile_points:
            messagebox.showwarning("Warning", "Please calculate the CPC profile first")
            return
        
        try:
            pos = float(self.ray_pos_var.get())
            angle_deg = float(self.ray_angle_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for ray position and angle")
            return
        
        # Aperture half radius
        half_r = self.cpc_params['d2']/2.0
        if pos < -half_r - 1e-9 or pos > half_r + 1e-9:
            messagebox.showwarning("Warning", f"Position {pos:.4g} mm is outside aperture range [-{half_r:.4g}, +{half_r:.4g}]")
        
        # Perform ray trace
        ray_path, segments_info = self.trace_ray_from_aperture(pos, angle_deg)
        
        # Saving the current beam
        self.current_ray_path = ray_path
        self.current_ray_segments_info = segments_info
        
        # Add to the list of rays if accumulation is enabled
        if self.accumulate_rays_var.get():
            self.ray_paths.append((ray_path, segments_info))
        else:
            self.ray_paths = [(ray_path, segments_info)]  # replacing all rays with the current one
        
        self.plot_cpc_profile()
    
    def clear_ray(self):
        self.ray_paths = []
        self.current_ray_path = []
        self.current_ray_segments_info = []
        self.plot_cpc_profile()
    
    def on_toggle_show_labels(self):
        self.plot_cpc_profile()
    
    def trace_ray_from_aperture(self, r0_aperture, angle_deg, max_bounces=50):
        params = self.cpc_params
        profile = self.profile_points
        
        # Convert angle to radians
        alpha = math.radians(angle_deg)
        
        # Beam direction: inside CPC (towards collector)
        dz = -1.0  # moving towards z=0
        dr = math.tan(alpha)  # radial component
        
        # Normalize the direction
        v = np.array([dz, dr], dtype=float)
        v_len = np.linalg.norm(v)
        if v_len > 0:
            v = v / v_len
        
        # Starting point on the aperture
        z0 = params['L']
        r0 = float(r0_aperture)
        path = [(z0, r0)]
        segments = []
        
        bounce_count = 0
        current_point = np.array([z0, r0], dtype=float)
        current_direction = v.copy()
        
        # Pre-calculate profile segments
        seg_z = np.array([p[0] for p in profile])
        seg_r_upper = np.array([p[1] for p in profile])  # upper surface
        seg_r_lower = np.array([-p[1] for p in profile])  # bottom surface (mirror)
        
        # We first check whether the beam comes back out through the aperture (simplified check)
        # If the angle is too large (greater than the concentrator angle), the beam will not hit the collector
        if abs(angle_deg) > params['theta_deg'] + 5:  # adding a small margin of error
            # The beam will not enter the collector, but will exit through the aperture.
            # Find the exit point through the aperture
            if abs(current_direction[0]) > 1e-12:
                t_to_aperture = (z0 - current_point[0]) / current_direction[0]
                if t_to_aperture > 1e-9:
                    exit_pt = current_point + current_direction * t_to_aperture
                    path.append((float(exit_pt[0]), float(exit_pt[1])))
                    segments.append({"angle_deg": angle_deg, "type": "escape_direct"})
                    return path, segments
        
        while bounce_count <= max_bounces:
            # 1. Check the intersection with the collector (z=0)
            if abs(current_direction[0]) > 1e-12:
                t_to_receiver = (0.0 - current_point[0]) / current_direction[0]
                if t_to_receiver > 1e-9:
                    receiver_intersect = current_point + current_direction * t_to_receiver
                    receiver_r = receiver_intersect[1]
                    # Check if it gets to the manifold
                    if abs(receiver_r) <= params['d1']/2 + 1e-9:
                        path.append((0.0, receiver_r))
                        segments.append({"angle_deg": angle_deg, "type": "receiver", "final_r": receiver_r})
                        break
            
            # 2. Check intersection with aperture (z = L)
            aperture_z = params['L']
            if current_direction[0] > 0 and current_point[0] < aperture_z:  # moves towards the aperture
                t_to_aperture = (aperture_z - current_point[0]) / current_direction[0]
                if t_to_aperture > 1e-9:
                    aperture_intersect = current_point + current_direction * t_to_aperture
                    aperture_r = aperture_intersect[1]
                    
                    # Check if it fits into the aperture and does not go inside the hub
                    if abs(aperture_r) <= params['d2']/2 + 1e-9:
                        # Check if the beam enters the concentrator along the way
                        # Find intersections with the profile that may occur earlier
                        t_min = t_to_aperture
                        profile_intersection_earlier = False
                        
                        # Find any intersections with the profile that occur earlier
                        for profile_r, surface_type in [(seg_r_upper, "upper"), (seg_r_lower, "lower")]:
                            for i in range(len(seg_z)-1):
                                # Profile segment points
                                z1, r1 = seg_z[i], profile_r[i]
                                z2, r2 = seg_z[i+1], profile_r[i+1]
                                
                                # Segment vector
                                seg_vec = np.array([z2 - z1, r2 - r1])
                                
                                # Solve the system: current_point + t*current_direction = [z1, r1] + u*seg_vec
                                A = np.column_stack((current_direction, -seg_vec))
                                b = np.array([z1 - current_point[0], r1 - current_point[1]])
                                
                                try:
                                    t, u = np.linalg.solve(A, b)
                                    
                                    # Check the validity of the intersection
                                    if t > 1e-9 and t < t_min - 1e-9 and 0 <= u <= 1.0:
                                        profile_intersection_earlier = True
                                        break
                                except np.linalg.LinAlgError:
                                    continue
                            
                            if profile_intersection_earlier:
                                break
                        
                        if not profile_intersection_earlier:
                            # The beam actually comes out through the aperture
                            path.append((float(aperture_intersect[0]), float(aperture_intersect[1])))
                            segments.append({"angle_deg": math.degrees(math.atan2(current_direction[1], -current_direction[0])), 
                                           "type": "escape_aperture", "final_r": aperture_r})
                            break
            
            # 3. Find the intersections with the upper and lower surfaces
            t_candidates = []
            intersection_info = []
            
            # Check both profiles (upper and lower)
            for profile_r, surface_type in [(seg_r_upper, "upper"), (seg_r_lower, "lower")]:
                for i in range(len(seg_z)-1):
                    # Profile segment points
                    z1, r1 = seg_z[i], profile_r[i]
                    z2, r2 = seg_z[i+1], profile_r[i+1]
                    
                    # Segment vector
                    seg_vec = np.array([z2 - z1, r2 - r1])
                    
                    # Solve the system: current_point + t*current_direction = [z1, r1] + u*seg_vec
                    A = np.column_stack((current_direction, -seg_vec))
                    b = np.array([z1 - current_point[0], r1 - current_point[1]])
                    
                    try:
                        t, u = np.linalg.solve(A, b)
                        
                        # Checking the validity of the intersection
                        if t > 1e-9 and 0 <= u <= 1.0:
                            intersection_pt = current_point + t * current_direction
                            t_candidates.append(t)
                            intersection_info.append({
                                "t": t, 
                                "point": intersection_pt,
                                "segment_index": i,
                                "u": u,
                                "surface_type": surface_type,
                                "segment_points": ((z1, r1), (z2, r2))
                            })
                    except np.linalg.LinAlgError:
                        continue
            
            # Selecting the nearest intersection
            if t_candidates:
                min_t_idx = np.argmin(t_candidates)
                nearest = intersection_info[min_t_idx]
                
                # Add an intersection point to a path
                intersect_pt = nearest["point"]
                path.append((float(intersect_pt[0]), float(intersect_pt[1])))
                
                # Calculate the normal at the intersection point
                z1, r1 = nearest["segment_points"][0]
                z2, r2 = nearest["segment_points"][1]
                seg_tangent = np.array([z2 - z1, r2 - r1])
                seg_tangent = seg_tangent / (np.linalg.norm(seg_tangent) + 1e-12)
                
                # Normal to the segment (perpendicular to the tangent)
                if nearest["surface_type"] == "upper":
                    normal = np.array([seg_tangent[1], -seg_tangent[0]])  # for the top surface
                else:
                    normal = np.array([-seg_tangent[1], seg_tangent[0]])  # for the bottom surface (mirror)
                
                normal = normal / (np.linalg.norm(normal) + 1e-12)
                
                # Reflection
                incident = current_direction
                dot = np.dot(incident, normal)
                reflected = incident - 2 * dot * normal
                reflected = reflected / (np.linalg.norm(reflected) + 1e-12)
                
                # Save segment information
                current_angle = math.degrees(math.atan2(current_direction[1], -current_direction[0]))
                segments.append({
                    "angle_deg": current_angle, 
                    "type": "reflect", 
                    "surface": nearest["surface_type"],
                    "segment_index": nearest["segment_index"]
                })
                
                # Update point and direction for next step
                current_point = intersect_pt + reflected * 1e-6  # a slight shift to avoid self-intersection
                current_direction = reflected
                bounce_count += 1
                
            else:
                # There are no intersections - the beam goes to infinity
                far_point = current_point + current_direction * params['L']
                path.append((float(far_point[0]), float(far_point[1])))
                segments.append({"angle_deg": angle_deg, "type": "no_intersection"})
                break
        
        return path, segments

    # STL
    def start_stl_export(self):
        if not self.cpc_params or not self.profile_points:
            messagebox.showwarning("Warning", "Please calculate the CPC profile first")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".stl",
            filetypes=[("STL files", "*.stl"), ("All files", "*.*")],
            title="Save STL file"
        )
        
        if not file_path:
            return
        
        self.progress_frame.grid()
        self.progress_var.set(0)
        self.progress_label_var.set("Starting STL export...")
        self.root.update()
        
        thread = threading.Thread(target=self.save_to_stl_thread, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def save_to_stl_thread(self, file_path):
        """Stream for generating STL file with progress update"""
        try:
            decimal_places = self.decimal_places_var.get()
            radial_segments = self.radial_segments_var.get()
            export_half = self.export_half_only_var.get()
            
            total_triangles = (len(self.profile_points) - 1) * (radial_segments if not export_half else radial_segments // 2) * 2
            triangles_generated = 0
            
            fmt = f".{decimal_places}f"
            azimuth_step = 2 * np.pi / radial_segments
            
            if export_half:
                azimuth_range = np.linspace(0, np.pi, radial_segments // 2 + 1)
            else:
                azimuth_range = np.linspace(0, 2 * np.pi, radial_segments + 1)
            
            cos_phi = np.cos(azimuth_range)
            sin_phi = np.sin(azimuth_range)
            
            # Writing to a file
            with open(file_path, 'w', encoding='ascii') as f:
                f.write("solid OD-CPC_3D_Model\n")
                
                for i in range(len(self.profile_points) - 1):
                    z1, r1 = self.profile_points[i]
                    z2, r2 = self.profile_points[i + 1]
                    
                    for j in range(len(azimuth_range) - 1):
                        cos_phi1 = cos_phi[j]
                        sin_phi1 = sin_phi[j]
                        cos_phi2 = cos_phi[j + 1]
                        sin_phi2 = sin_phi[j + 1]
                        
                        x11 = r1 * cos_phi1
                        y11 = r1 * sin_phi1
                        x12 = r1 * cos_phi2
                        y12 = r1 * sin_phi2
                        x21 = r2 * cos_phi1
                        y21 = r2 * sin_phi1
                        x22 = r2 * cos_phi2
                        y22 = r2 * sin_phi2
                        
                        self.write_triangle(f, (x11, y11, z1), (x21, y21, z2), (x12, y12, z1), fmt)
                        self.write_triangle(f, (x21, y21, z2), (x22, y22, z2), (x12, y12, z1), fmt)
                        
                        triangles_generated += 2
                        
                        if triangles_generated % 200 == 0:
                            progress = min(100.0, (triangles_generated / total_triangles) * 100 if total_triangles>0 else 100.0)
                            self.progress_var.set(progress)
                            self.progress_label_var.set(f"Generating STL: {triangles_generated}/{total_triangles} triangles ({progress:.1f}%)")
                            self.root.update()
                
                f.write("endsolid OD-CPC_3D_Model\n")
            
            self.progress_var.set(100)
            self.progress_label_var.set("STL export completed successfully!")
            time.sleep(0.5)
            self.root.after(0, self.hide_progress)
            self.root.after(0, lambda: messagebox.showinfo("Success", f"STL file saved successfully:\n{file_path}"))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to save STL file:\n{str(e)}"))
            self.root.after(0, self.hide_progress)
    
    def hide_progress(self):
        self.progress_frame.grid_remove()
    
    def write_triangle(self, file, v1, v2, v3, fmt):
        """Write one triangle to an STL file"""
        v1_arr = np.array(v1)
        v2_arr = np.array(v2)
        v3_arr = np.array(v3)
        
        normal = np.cross(v2_arr - v1_arr, v3_arr - v1_arr)
        norm = np.linalg.norm(normal)
        if norm > 0:
            normal = normal / norm
        
        file.write(f"  facet normal {normal[0]:{fmt}} {normal[1]:{fmt}} {normal[2]:{fmt}}\n")
        file.write("    outer loop\n")
        
        for vertex in [v1, v2, v3]:
            file.write(f"      vertex {vertex[0]:{fmt}} {vertex[1]:{fmt}} {vertex[2]:{fmt}}\n")
        
        file.write("    endloop\n")
        file.write("  endfacet\n")

def main():
    root = tk.Tk()
    app = CPC_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()