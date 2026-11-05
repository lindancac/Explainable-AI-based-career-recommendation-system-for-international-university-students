# Career Explorer — dissertation prototype v0.2

Flask prototype for international university students exploring careers across multiple industries.

## Run

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open http://127.0.0.1:5001. Debug mode is off by default.

## Scope

Inputs: technical and transferable skill proficiency (0–5), career interests (0–5), education level and subject of study. Outputs: five ranked careers, matching scores, personalised explanations, separate skill and interest analyses, example skill gaps and career information. Twelve illustrative roles span technology, analytics, business, finance, marketing, design, operations, HR, research, education and sustainability.

The transparent scoring method uses 65% skill alignment, 30% interest alignment and 5% subject relevance. Education informs entry-route guidance rather than ranking. The interface explains the formula, targets and limitations. Scores are independent alignment measures, not probabilities. Ties follow catalogue order.

Role profiles, skill targets, related subjects and weights are manually authored design assumptions. They have not been validated against occupational data or employers. The earlier classifier trained on simulated data has been removed; this version makes no machine-learning performance claim. If the dissertation requires an ML model or SHAP, this version is an interface and explainable baseline, not completion of that requirement. Select and document an occupational dataset, validate its mapping and assess the final method before efficacy claims.

No database, analytics, participant identifiers or application-level profile logging are implemented. Browser history and hosting/access logs require separate consideration before research deployment. Do not collect participant data until institutional ethical approval and consent procedures are in place.

## Files

- `app.py`: routes, request validation and form rendering.
- `model.py`: catalogue, matching formula and explanation data.
- `templates/`, `static/style.css`: responsive interface.
- `docs/dissertation-plan.md`: implementation schedule and draft usability protocol to adapt for the supervisor and ethics application.

## Usability features

Skill-specific examples support proficiency ratings. Results carry answers into an edit form without database storage. Students can compare two or three recommended careers side by side and explore changes by editing ratings. Each career includes up to three prioritised skill-development activities, feedback prompts and a next step for careers support. These plans use illustrative targets.

## Manual checks

Complete the form, confirm five careers, expand each analysis and inspect a skill gap. Try an all-zero profile, different subjects and a narrow screen. Verify keyboard navigation and printing in your target browsers. Automated route and scoring checks can be run using the Flask test client; passing these does not establish usability or efficacy.
