import tkinter as tk
from tkinter import ttk

# Define the main application window
root = tk.Tk()
root.title("Brain Tumor Symptom Checker")
root.geometry("500x600")
root.configure(bg="#e8f5e9")  # Light green background color

# Define the symptoms and related questions
questions = [
    "Do you experience frequent headaches?",
    "Do you have nausea or vomiting?",
    "Do you have blurred or double vision?",
    "Do you have difficulty in balancing?",
    "Do you have seizures?",
    "Do you have changes in hearing or speech?",
    "Do you feel weakness in one part of your body?",
    "Do you have memory problems?",
    "Do you experience personality changes?",
    "Do you have trouble concentrating?",
    "Do you experience dizziness?",
    "Do you have hearing loss?"
]

# Create a list to store user responses
responses = []

# Define a function to handle the survey submission
def submit_responses():
    global responses
    responses = [var.get() for var in vars]

    # Count the number of symptoms
    num_symptoms = sum(responses)

    # Assess the risk level and customize message box color
    if num_symptoms == 0:
        message = "You seem to be safe. If you have any concerns, please consult a doctor."
        bg_color = "green"
        text_color = "white"
    elif num_symptoms <= 3:
        message = "You have some symptoms, but they are not very concerning. If symptoms persist, consult a doctor."
        bg_color = "orange"
        text_color = "black"
    else:
        message = "You have multiple symptoms. It is recommended to consult a doctor for a detailed evaluation."
        bg_color = "red"
        text_color = "white"

    # Create a custom message box centered on the screen
    msg_box = tk.Toplevel(bg=bg_color)
    msg_box.geometry("400x200+{}+{}".format(int(root.winfo_screenwidth()/2 - 200), int(root.winfo_screenheight()/2 - 100)))
    msg_label = tk.Label(msg_box, text=message, bg=bg_color, fg=text_color, font=("Arial", 14), wraplength=380, justify="center")
    msg_label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
    msg_button = tk.Button(msg_box, text="OK", command=msg_box.destroy, bg="white",width=10,padx=7,pady=5)
    msg_button.pack(pady=10)

# Set the style for the GUI
style = ttk.Style()
style.configure("TFrame", background="#e8f5e9")
style.configure("TLabel", background="#e8f5e9", font=("Helvetica", 12))
style.configure("TCheckbutton", background="#e8f5e9", font=("Helvetica", 12))
style.configure("TButton", font=("Arial", 12), padding=10)

# Create a title label
title_frame = tk.Frame(root, bg="#4CAF50", pady=10)  # Change the background color to match the button
title_frame.pack(fill=tk.X)
title_label = tk.Label(
    title_frame, 
    text="Brain Tumor Symptom Checker", 
    font=("Times New Roman", 20, "bold"), 
    bg="#4CAF50",  # Match the background color
    fg="white"
)
title_label.pack()

# Create the survey form
vars = []
for question in questions:
    frame = ttk.Frame(root)
    frame.pack(fill=tk.X, padx=20, pady=2)  # Adjusted padding for closer spacing

    label = ttk.Label(frame, text=question, anchor="w", font=("Helvetica", 12))
    label.pack(side=tk.LEFT)

    var = tk.BooleanVar()
    vars.append(var)

    checkbutton = ttk.Checkbutton(frame, variable=var)
    checkbutton.pack(side=tk.RIGHT)

# Add a submit button
submit_button = ttk.Button(root, text="Submit", command=submit_responses)
submit_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
