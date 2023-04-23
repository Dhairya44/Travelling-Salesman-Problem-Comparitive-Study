import tkinter as tk
from tkinter import font as tkfont
import os
import sys

city_sizes = ['8', '16', '32', '64', '128', '256', '512', 'Comparision']
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Choose One")
        self.master.geometry("500x500")
        self.master.eval('tk::PlaceWindow . center')
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(fill='both', expand=True)
        self.choice = tk.StringVar()
        self.choice.set("")
        self.choices = ["Anneal", "DP", "Genetic", "DivCon", "PSO", "Greedy", "Time Comparison", "Cost Comparison", "Exit"]
        self.city_choices = {
            "Anneal": city_sizes,
            "DP": city_sizes,
            "Genetic": city_sizes,
            "DivCon": city_sizes,
            "PSO": city_sizes,
            "Greedy": city_sizes,
        }
        title_font = tkfont.Font(family='Helvetica', size=14, weight="bold")
        button_font = tkfont.Font(family='Helvetica', size=12)
        title_label = tk.Label(self.frame, text="Select a choice:", font=title_font)
        title_label.pack(pady=10)
        title_label.grid(row=0, column=0, padx=10, pady=10)
        row = 1
        col = 0
        for choice in self.choices:
            button = tk.Button(self.frame, text=choice, font=button_font,
                                command=lambda x=choice: self.show_city_choices(x), padx=10, pady=5, width=20)
            button.grid(row=row, column=col, padx=10, pady=5, sticky='we')
            col += 1
            if col == 2:
                row += 1
                col = 0


    def show_city_choices(self, choice):
        if(choice == "Exit"):
            sys.exit()
        if(choice == "Time Comparison"):
            os.system(f'python pvis_algos_vs_cost.py time_results')
            root.destroy()
            return
        if(choice == "Cost Comparison"):
            os.system(f'python pvis_algos_vs_cost.py cost_results')
            root.destroy()
            return
        city_choices = self.city_choices.get(choice, [])
        self.frame.destroy()
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(fill='both', expand=True)
        title_font = tkfont.Font(family='Helvetica', size=14, weight="bold")
        button_font = tkfont.Font(family='Helvetica', size=12)
        title_label = tk.Label(self.frame, text=f"Select a city for {choice}:", font=title_font)
        title_label.grid(row=0, column=0, padx=10, pady=10)
        row = 1
        col = 0
        for city in city_choices:
            wi = 20
            button = tk.Button(self.frame, text=city, font=button_font,
                                command=lambda x=city: self.set_choice(f"{choice}, {x}"), padx=10, pady=5, width=wi)
            button.grid(row=row, column=col, padx=10, pady=5, sticky='we')
            col += 1
            if col == 2:
                row += 1
                col = 0
    
    def set_choice(self, choice):
        self.choice.set(f"You selected: {choice}")
        [algo, choice] = choice.split(", ")
        file_name = ""
        if algo == "Anneal":
            file_name = "anneal.py"
        elif algo == "DP":
            file_name = "dynamic_programming.py"
        elif algo == "Genetic":
            file_name = "genetic.py"
        elif algo == "DivCon":
            file_name = "divide_and_conquer.py"
        elif algo == "PSO":
            file_name = "pso.py"
        elif algo == "Greedy":
            file_name = "greedy_tsp.py"
        # execute another python file with the chosen file path
        # subprocess.run(["python", "path/to/other/file.py", file_path])
        if(choice == "Comparision"):
            os.system(f'python pyvis_points_vs_time.py {file_name[0:-3]}_results')
        else:
            os.system(f'python algorithm/{file_name} {choice}')
        root.destroy()

while(1):
    root = tk.Tk()
    root.minsize(400, 200)
    app = App(root)
    root.mainloop()