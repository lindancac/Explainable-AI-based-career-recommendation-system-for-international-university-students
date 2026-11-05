from flask import Flask, render_template, request
from model import FEATURES, KEYS, EDUCATION, SUBJECTS, SKILL_GUIDES, model

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024


def profile_form(error=None, status=200):
    groups = {}
    for key, label, group in FEATURES:
        groups.setdefault(group, []).append((key, label))
    return render_template('index.html', groups=groups, education=EDUCATION,
                           subjects=SUBJECTS, values=request.form, guides=SKILL_GUIDES, error=error), status


@app.get('/')
def index():
    return profile_form()


@app.post('/edit')
def edit():
    return profile_form()


@app.post('/compare')
@app.post('/recommend')
def recommend():
    try:
        values = {k: int(request.form[k]) for k in KEYS}
        education = request.form['education']
        subject = request.form['subject']
        if any(v < 0 or v > 5 for v in values.values()) or education not in EDUCATION or subject not in SUBJECTS:
            raise ValueError
    except (KeyError, ValueError):
        return profile_form('Please choose your education and subject, and give every rating a whole number from 0 to 5.', 400)
    results = model.recommend(values, education, subject)
    selected = request.form.getlist('career')
    comparison = []
    comparison_error = None
    status = 200
    if request.path == '/compare':
        names = {r['career'] for r in results}
        if not 2 <= len(selected) <= 3 or len(set(selected)) != len(selected) or any(name not in names for name in selected):
            comparison_error = 'Choose two or three different careers from your results to compare.'
            status = 400
        else:
            comparison = [r for r in results if r['career'] in selected]
    return render_template('results.html', results=results, profile={**values, 'education': education, 'subject': subject},
                           comparison=comparison, comparison_error=comparison_error, selected=selected,
                           education=education, subject=subject,
                           empty_profile=not any(values.values())), status


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)
