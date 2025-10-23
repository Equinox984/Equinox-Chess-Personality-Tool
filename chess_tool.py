"""Equinox Chess Personality Tool"""

# Username & Welcome


def name(user):  # Creo la función "name" con el parámetro de "user"
    print(f"Hello {user}!, Welcome to Equinox Chess Personality Tool! \n")
# La línea 7 pertenece a la función que creamos (name) con def debido a el ":"


username = (input("Hello, please write your name: \n"))
# Lo que el usuario escriba aquí, será "username"
name(username)  # La variable "username" es ahora el parámetro "user"

#####################################################################################################################################

# Chess Style Questions
print("Answer the following questions to find out your chess personality type.\n")


def user_questions(question):
    while True:
        answer = input(question + " (1 = Low, 2 = Mid, 3 = High) ").strip()
        if answer in {"1", "2", "3"}:
            return int(answer)
        print("Invalid response. We only accept 1, 2, or 3 as an answer.")


chess_questions = {
    "Tactician": [
        "1. I enjoy looking for sacrifices and sharp combinations to break my opponent.",
        "2. I feel confident calculating long tactical lines under time pressure.",
        "3. I often create complications on purpose to provoke mistakes.",
        "4. I prioritize winning material or delivering mating attacks over long-term structure.",
        "5. I spot tactical motifs (pins, forks, skewers) quickly in most positions.",
        "6. I get frustrated by dry, closed positions with no tactical chances."
    ],
    "Positional": [
        "7. I prefer improving piece placement and slowly outplaying my opponent.",
        "8. I focus on pawn structure, weak squares, and long-term plans rather than immediate tactics.",
        "9. I willingly trade active pieces if it improves my structure or reduces opponent counterplay.",
        "10. I am comfortable playing slow maneuvering games where progress is small but steady.",
        "11. I study endgames and often convert small advantages into wins.",
        "12. I avoid risky sacrifices unless they have a clear justification."
    ],
    "Dynamic": [
        "13. I feel comfortable in imbalanced positions with opposite-side attacks or material differences.",
        "14. I look for the initiative and prefer forcing play even if it’s risky.",
        "15. I willingly accept weakened pawns or structural defects for active piece play.",
        "16. I thrive when the position becomes unclear and chaotic.",
        "17. I often choose sharp, less-traveled lines to take opponents out of comfort zones.",
        "18. I sometimes overpress or overcomplicate hoping the opponent blunders."
    ],
    "Theorist": [
        "19. I memorize opening lines and feel most confident when the game follows theory.",
        "20. I prepare specific lines to gain an advantage in the first 15–20 moves.",
        "21. I frequently study master games, opening novelties, and database lines.",
        "22. I prefer positions where my preparation gives practical advantages.",
        "23. I feel annoyed when opponents play weird sidelines that force me to think from scratch.",
        "24. I value known theoretical knowledge more than relying purely on over-the-board intuition."
    ],
    "Intuitive": [
        "25. I play moves that “feel right” even if I can’t fully calculate every variation.",
        "26. I trust my positional sense to find plans without heavy memorization.",
        "27. I often make moves based on whole-position understanding rather than concrete tactics alone.",
        "28. I adapt quickly to the flow of the game and rely on pattern recognition.",
        "29. I sometimes can’t explain my best moves verbally but they work on the board.",
        "30. I prefer flexible systems and moves that keep many plans alive."
    ]
}

styles_value = {chess_style: 0 for chess_style in chess_questions.keys()}

for chess_style, questions in chess_questions.items():
    for q in questions:
        points = user_questions(q)
        styles_value[chess_style] += points

####################################################################################################################################

# Finding the Highest Value
max_points = max(styles_value.values())
best_styles = [chess_style for chess_style, pts in styles_value.items()
               if pts == max_points]
primary_style = best_styles[0]

# Openings for every Playstyle
openings = {
    "Tactician": "King's Gambit (White) / Sicilian Dragon (Black)",
    "Positional": "Queen's Gambit (White) / Caro-Kann (Black)",
    "Dynamic": "London System (White) / King's Indian Defense (Black)",
    "Theorist": "Ruy López (White), Sicilian Najdorf (Black)",
    "Intuitive": "English Opening (White), Dutch Defense (Black)"
}

# Final Message
print("\n### Results ###")
print(f"Hello {username}!, your primary chess style is: {primary_style}!")
print(f"Recommended openings: {openings[primary_style]}")
print(f"Total points by style: {styles_value}")
