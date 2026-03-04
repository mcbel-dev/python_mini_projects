import unicodedata
import random 
import tkinter as tk

def remove_diacritics(text):
    return "".join(char for char in unicodedata.normalize("NFD", text)
                   if unicodedata.category(char) != "Mn")

def normalize(text):
    return remove_diacritics(text.lower().strip())

def enter_handler(event):
    if check_button["state"] == "normal":
        check_answer()
    elif next_button["state"] == "normal":
        next_question()

questions = {
    "Ktorá rieka na svete je najdlšia?": "Níl",
    "Kto namaľoval Monu Lisu?": "Leonardo DaVinci",
    "Ktorý orgán ľudského tela je najväčší?": "koža",
    "Aká je chemická značka striebra?": "Ag",
    "Ktorý herec získal Oscara za najlepší mužský herecký výkon za film Forrest Gump (1994)?": "Tom Hanks",
    "Ako sa volá vlk Jona Snowa?": "Duch",
    "Koľko základných farieb má dúha?": "7",
    "Aký džús je potrebný na výrobu Bloody Marry?": "paradajkový"
}
question_list = list(questions.keys())
random.shuffle(question_list)
score = 0
current_index = 0
current_question = question_list[current_index]

# printovanie otazok
def check_answer():
    if check_button["state"] == "disabled":
        return
    
    global score, current_question
    user_answer = answer_entry.get()
    if normalize(user_answer) == "":
        feedback_label.config(text="Prosím zadaj odpoveď.")
        return
    
    corect_answer = questions[current_question]
    
    #kontrola odpovedi
    if normalize(user_answer) == normalize(corect_answer):
        feedback_label.config(text="Správne! ✔️")
        score += 1
        score_label.config(text=f"Skóre: {score}")
    else:
        feedback_label.config(text=f"Nesprávne! ❌ Správna odpoveď: {corect_answer}")
    
    # "stabilizovanie" tlacitok
    check_button.config(state="disabled")
    next_button.config(state="normal")


# vyber dalsej otazky
def next_question():
    global current_index, current_question
    
    current_index +=1
    #zistenie ci uz je posledna otazka + zablokovanie tlacidiel
    if current_index >= len(question_list):
        question_label.config(text="Koniec hry. 🎉")
        feedback_label.config(text="")
        score_label.config(text=f"Tvoje skóre: {score} / {len(question_list)}")
        answer_entry.delete(0, tk.END)
        answer_entry.config(state="disabled")
        check_button.config(state="disabled")
        next_button.config(state="disabled")
        restart_button.config(state="normal")
        return 
    # dalsia otazka + povolenie tlacidiel
    current_question = question_list[current_index]
    question_label.config(text=current_question)
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")
    check_button.config(state="normal")
    next_button.config(state="disabled")

def restart_game():
    global score, current_index, current_question

    score = 0
    current_index = 0

    random.shuffle(question_list)
    current_question = question_list[current_index]
    
    question_label.config(text=current_question)
    feedback_label.config(text="")
    score_label.config(text="Skóre: 0")
    answer_entry.config(state="normal")
    answer_entry.delete(0, tk.END)
    check_button.config(state="normal")
    next_button.config(state="disabled")
    restart_button.config(state="disabled")

root = tk.Tk()
root.title("🌟 ---Kvíz--- 🌟")
root.geometry("600x400")

question_label = tk.Label(root, text=current_question)
question_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()
answer_entry.bind("<Return>", enter_handler)

check_button = tk.Button(root,text="Skontrolovať", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Ďalej", command=next_question)
next_button.pack()
next_button.config(state="disabled")

restart_button = tk.Button(root, text="Hrať znovu", command=restart_game)
restart_button.pack()
restart_button.config(state="disabled")

feedback_label = tk.Label(root, text="")
feedback_label.pack()

score_label = tk.Label(root, text=f"Skóre: {score}")
score_label.pack()



root.mainloop()





# questions = {
#     "Ktorá rieka na svete je najdlšia?": "Níl",
#     "Kto namaľoval Monu Lisu?": "Leonardo DaVinci",
#     "Ktorý orgán ľudského tela je najväčší?": "koža",
#     "Aká je chemická značka striebra?": "Ag",
#     "Ktorý herec získal Oscara za najlepší mužský herecký výkon za film Forrest Gump (1994)?": "Tom Hanks",
#     "Ako sa volá vlk Jona Snowa?": "Duch",
#     "Koľko základných farieb má dúha?": "7",
#     "Aký džús je potrebný na výrobu Bloody Marry?": "paradajkový"
# }


# def remove_diacritics(text):
#     return "".join(char for char in unicodedata.normalize("NFD", text)
#                    if unicodedata.category(char) != "Mn")

# def normalize(text):
#     return remove_diacritics(text.lower().strip())

# def game():
#     question_list = list(questions.keys())
#     score = 0

#     select_question = random.sample(question_list, len(question_list))

#     for idx, question in enumerate(select_question):
#         print(f"{idx + 1}. {question}")
#         user_answer = input("Tvoja odpoveď: ")

#         correct_answer = questions[question]

#         if normalize(user_answer) == normalize(correct_answer):
#             print("Správne! ✔️\n")
#             score +=1
#         else:
#             print(f"Nesprávne. ❌ Správna odpoveď je: {correct_answer}. \n")
#     print(f"Koniec hry! tvoje skóre je: {score}/{len(question_list)}")

# def menu():
#     while True:
#         game()
#         again = input("chces hrat znovu? (1)\n"
#                     "chces hru ukoncit? (2) ")
#         if again == "1": 
#             continue
#         if again == "2":
#             print("dakujem za hru.")
#             break
#         else:
#             print("vyber len z uvedenych moznosti. ")
        
# menu()  