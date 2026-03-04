import random 

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

import unicodedata

def remove_diacritics(text):
    return "".join(char for char in unicodedata.normalize("NFD", text)
                   if unicodedata.category(char) != "Mn")

def normalize(text):
    return remove_diacritics(text.lower().strip())

def game():
    question_list = list(questions.keys())
    score = 0

    select_question = random.sample(question_list, len(question_list))

    for idx, question in enumerate(select_question):
        print(f"{idx + 1}. {question}")
        user_answer = input("Tvoja odpoveď: ")

        correct_answer = questions[question]

        if normalize(user_answer) == normalize(correct_answer):
            print("Správne! ✔️\n")
            score +=1
        else:
            print(f"Nesprávne. ❌ Správna odpoveď je: {correct_answer}. \n")
    print(f"Koniec hry! tvoje skóre je: {score}/{len(question_list)}")

def menu():
    while True:
        game()
        again = input("chces hrat znovu? (1)\n"
                    "chces hru ukoncit? (2) ")
        if again == "1": 
            continue
        if again == "2":
            print("dakujem za hru.")
            break
        else:
            print("vyber len z uvedenych moznosti. ")
        
menu()  
