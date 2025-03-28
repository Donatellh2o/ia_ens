from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Questions et réponses pour le QCM
questions = [
    {
        "question": "Qu'est-ce que Python ?",
        "choices": ["Un langage de programmation", "Un type de serpent", "Une boisson", "Un film"],
        "answer": "Un langage de programmation"
    },
    {
        "question": "Qui a créé Python ?",
        "choices": ["Guido van Rossum", "Linus Torvalds", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Quelle est l'extension des fichiers Python ?",
        "choices": [".py", ".pyc", ".pyo", ".python"],
        "answer": ".py"
    }
]

# Page d'accueil avec le QCM
home_html = '''
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>QCM Python</title>
</head>
<body>
    <h1>QCM sur Python</h1>
    <form action="/result" method="post">
        {% for q in questions %}
        <div>
            <p>{{ q.question }}</p>
            {% for choice in q.choices %}
            <label><input type="radio" name="{{ loop.index }}" value="{{ choice }}"> {{ choice }}</label><br>
            {% endfor %}
        </div>
        {% endfor %}
        <button type="submit">Soumettre</button>
    </form>
</body>
</html>
'''

# Page de résultat
result_html = '''
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Résultats du QCM</title>
</head>
<body>
    <h1>Résultats du QCM</h1>
    <p>Votre score est : {{ score }} / {{ total }}</p>
    <a href="{{ url_for('home') }}">Recommencer le QCM</a>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(home_html, questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    total = len(questions)
    for i, question in enumerate(questions, start=1):
        user_answer = request.form.get(str(i))
        if user_answer == question["answer"]:
            score += 1
    return render_template_string(result_html, score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
