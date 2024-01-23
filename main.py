import tkinter as tk

class BulletJournalApp:
    def __init__(self, root):
        self._root = root
        self._root.geometry("+100+100")
        self.title("Bullet Journal")
        self._tasks = []

    def create_gui(self):
        self.create_frame()
        self.create_note_entry()
        self.create_add_button()
        self.create_task_listbox()
        self.create_yscrollbar()
        self.create_clear_button()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_frame(self):
        self.frame = tk.Frame(self._root)
        self.frame.pack()
    def create_note_entry(self):
        self.note_entry = tk.Entry(self.frame, width=40)
        self.note_entry.grid(row=0, column=0, padx=10, pady=10)

    def create_add_button(self):
        self.add_button = tk.Button(self.frame, text="Agregar", command=self.add_note)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

    def create_task_listbox(self):
        self.task_listbox = tk.Listbox(self.frame, height=15, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.config(yscrollcommand=self.task_listbox.yview)

    def create_yscrollbar(self):
        self.yscrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.task_listbox.yview)
        self.yscrollbar.grid(row=1, column=2, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.yscrollbar.set)

    def create_clear_button(self):
        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def create_note(self, note_text):
        if note_text:
            new_note = f"• {note_text}"
            self._tasks.append(new_note)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self._tasks:
            self.task_listbox.insert(tk.END, task)

    def add_note(self):
        note_text = self.note_entry.get().strip()
        self.create_note(note_text)
        self.clear_note_entry()

    def clear_tasks(self):
        self._tasks = []
        self.task_listbox.delete(0, tk.END)

    def clear_note_entry(self):
        self.note_entry.delete(0, tk.END)

    def title(self, text):
        self._root.title(text)

    def destroy(self):
        self._root.destroy()

    def run(self):
        self._root.mainloop()
        self.create_gui()

    def quit(self):
        self._root.quit()

    def on_closing(self):
        title= "Salir"
        message= "¿Confirmas que quieres salir?"
        if tk.messagebox.askokcancel(title, message):
            self.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = BulletJournalApp(root)
    app.run()