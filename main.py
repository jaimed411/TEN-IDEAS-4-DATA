import os
import openai #pip install openai
import customtkinter as ctk #pip install customtkinter

def generate():
    prompt = "Por favor, crea 10 ideas para crear proyectos de data science. "
    language = language_dropdown.get()
    prompt += "El lenguaje de programación es " + language + ". "
    difficulty = difficulty_value.get()
    prompt += "La dificultad es  " + difficulty + ". "

    if checkbox1.get():
        prompt += "El proyecto debería incluir una database. "
    if checkbox2.get():
        prompt += "El proyecto debería incluir una API. "

    print(prompt)

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert(0.0, answer)

root = ctk.CTk()
root.geometry("750x550")
root.title("Data Science Idea Generator by ToekiousBIG")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="Data Science Idea Generator",
                           font=ctk.CTkFont(size=30, weight="bold"), text_color="#27EA80")
title_label.pack(padx=10, pady=(40,20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")
language_label = ctk.CTkLabel(
    language_frame, text="Lenguaje Programación", font=ctk.CTkFont(weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Python", "R", "Java", "MATLAB", "SQL"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Dificultad de Proyecto", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Fácil")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Fácil", variable=difficulty_value, value="Fácil")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medio", variable=difficulty_value, value="Medio")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Díficil", variable=difficulty_value, value="Díficil")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Características", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(frame, text="Genera Ideas", text_color="#ECECEC", command=generate, fg_color="#27EA80")
button.pack(padx=100, fill="x", pady=(5, 20))

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=14), text_color="#ECECEC")
result.pack(pady=10, fill="x", padx=100)


root.mainloop()