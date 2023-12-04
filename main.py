from question import Question
from questionnaire import Questionnaire

# --- Création d'un tuple questions contenant toutes nos questions et leurs réponse
questions = (Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
             Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
             Question("Quelle est la capitale de la France ?", ("Bafoussam", "Yaounde", "Douala", "Buea"), "Yaounde"),
             Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"))

# --- Création d'un objet Questionnaire ---
questionnaire = Questionnaire(questions)

# --- Appelle de la méthode lancer questionnaire ---
questionnaire.lancer()

"""
# --- Création des objets Question ---
q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q2 = Question("Quelle est la capitale de la France ?", ("Bafoussam", "Yaounde", "Douala", "Buea"), "Yaounde")
q3 = Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
q4 = Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")

# --- Appelle de la méthode poser question ---
q1.poser()
q2.poser()
q3.poser()
q4.poser()
"""