"""Transparent, illustrative career matching for a dissertation prototype.

Profiles and weights are authored examples, not validated occupational data.
Scores measure alignment with these profiles, not employment probabilities.
"""
FEATURES = [
    ('programming', 'Programming', 'Technical skills'),
    ('data_analysis', 'Data analysis and spreadsheets', 'Technical skills'),
    ('design', 'Design and digital content', 'Technical skills'),
    ('business', 'Business and financial analysis', 'Technical skills'),
    ('research', 'Research and evidence gathering', 'Technical skills'),
    ('project_tools', 'Project planning tools', 'Technical skills'),
    ('communication', 'Communication', 'Transferable skills'),
    ('teamwork', 'Teamwork', 'Transferable skills'),
    ('problem_solving', 'Problem solving', 'Transferable skills'),
    ('organisation', 'Organisation', 'Transferable skills'),
    ('creativity', 'Creativity', 'Transferable skills'),
    ('leadership', 'Leadership', 'Transferable skills'),
    ('int_technology', 'Technology and software', 'Career interests'),
    ('int_business', 'Business and finance', 'Career interests'),
    ('int_creative', 'Creative work and media', 'Career interests'),
    ('int_people', 'Supporting and developing people', 'Career interests'),
    ('int_research', 'Research and discovery', 'Career interests'),
    ('int_operations', 'Planning and operations', 'Career interests'),
]
KEYS = [key for key, _, _ in FEATURES]
LABELS = {key: label for key, label, _ in FEATURES}
EDUCATION = ['Foundation / pre-university', 'Undergraduate', 'Postgraduate taught', 'Postgraduate research']
SUBJECTS = ['Computing and technology', 'Business and economics', 'Engineering', 'Arts and humanities', 'Social sciences', 'Natural sciences', 'Education', 'Health and life sciences', 'Other / interdisciplinary']


def role(name, industry, description, skills, interests, subjects, activity):
    return dict(career=name, industry=industry, description=description, skills=skills,
                interests=interests, subjects=subjects, activity=activity)


CAREERS = [
    role('Software Developer', 'Technology', 'Build, test and maintain applications with a development team.', {'programming':4,'problem_solving':4,'teamwork':3}, ['int_technology'], ['Computing and technology','Engineering'], 'Build a small application and document its testing.'),
    role('Data Analyst', 'Analytics', 'Explore data and communicate findings to support decisions.', {'data_analysis':4,'research':3,'communication':3,'problem_solving':4}, ['int_research','int_technology'], ['Computing and technology','Business and economics','Natural sciences','Engineering'], 'Analyse a public dataset and present three findings.'),
    role('Business Analyst', 'Business services', 'Understand organisational needs and propose improvements.', {'business':4,'communication':4,'problem_solving':4,'research':3}, ['int_business','int_operations'], ['Business and economics','Computing and technology','Social sciences'], 'Write a process map and improvement proposal for a familiar service.'),
    role('Digital Marketing Assistant', 'Marketing and media', 'Help plan campaigns, create content and review audience engagement.', {'design':3,'creativity':4,'communication':4,'data_analysis':3}, ['int_creative','int_business'], ['Arts and humanities','Business and economics','Social sciences'], 'Create a sample campaign with an audience, content plan and measures.'),
    role('UX Research Assistant', 'Design and research', 'Investigate user needs and help teams improve products and services.', {'research':4,'communication':4,'design':3,'problem_solving':3}, ['int_people','int_creative','int_research'], ['Social sciences','Arts and humanities','Computing and technology'], 'Practise creating a usability task and analysing example observations.'),
    role('Project Coordinator', 'Operations', 'Support schedules, organise resources and communicate project progress.', {'project_tools':4,'organisation':4,'communication':4,'teamwork':3}, ['int_operations','int_business'], ['Business and economics','Engineering'], 'Create a project schedule, risk register and progress report.'),
    role('Human Resources Assistant', 'People and organisations', 'Support recruitment, employee administration and staff development.', {'communication':4,'organisation':4,'teamwork':4,'business':3}, ['int_people','int_business'], ['Business and economics','Social sciences'], 'Draft a sample onboarding plan and recruitment checklist.'),
    role('Research Assistant', 'Research', 'Support literature reviews, evidence collection and research reporting.', {'research':4,'data_analysis':3,'organisation':4,'communication':3}, ['int_research'], ['Natural sciences','Social sciences','Health and life sciences'], 'Prepare a short literature review and evidence summary.'),
    role('Education Programme Assistant', 'Education', 'Help organise learning activities and support learners and programme teams.', {'communication':4,'organisation':4,'teamwork':4,'creativity':3}, ['int_people','int_operations'], ['Education','Arts and humanities','Social sciences'], 'Develop a sample learning activity with clear objectives.'),
    role('Sustainability Project Assistant', 'Environment and sustainability', 'Support environmental projects through research, reporting and coordination.', {'research':4,'project_tools':3,'data_analysis':3,'communication':4}, ['int_research','int_operations'], ['Natural sciences','Engineering','Business and economics'], 'Outline a campus sustainability project and ways to measure progress.'),
    role('Financial Analysis Assistant', 'Finance', 'Help review financial information, prepare spreadsheets and report trends.', {'business':4,'data_analysis':4,'organisation':4,'problem_solving':3}, ['int_business','int_research'], ['Business and economics'], 'Build a sample budget and explain its main variances.'),
    role('Content Designer', 'Creative industries', 'Create clear digital content that helps people understand and use services.', {'design':4,'communication':4,'creativity':4,'research':3}, ['int_creative','int_people'], ['Arts and humanities','Social sciences'], 'Rewrite a complex information page and explain your design choices.'),
]


SKILL_GUIDES = {
    'programming': ('Write a small script with guidance.', 'Build and debug a small application independently.', 'Design a larger application and explain its testing.', 'Build a small tool and record how you tested it.'),
    'data_analysis': ('Enter data and use simple spreadsheet formulas.', 'Clean a dataset and explain patterns with charts.', 'Choose analysis methods and evaluate their limitations.', 'Clean a public dataset and present a chart with an explanation.'),
    'design': ('Adapt a template with guidance.', 'Create clear content or layouts for a defined audience.', 'Develop and evaluate a consistent design approach.', 'Create a sample page and ask someone to review its clarity.'),
    'business': ('Read a simple budget or business summary.', 'Analyse costs or a process and explain a recommendation.', 'Evaluate business alternatives and their assumptions.', 'Prepare a small budget and explain the main costs.'),
    'research': ('Find sources with guidance.', 'Compare credible sources and summarise evidence.', 'Design an investigation and critically evaluate evidence.', 'Compare three sources and write a short evidence summary.'),
    'project_tools': ('Update a task list with guidance.', 'Maintain a project schedule and track dependencies.', 'Coordinate plans, risks and progress across a team.', 'Create a task board with milestones and dependencies.'),
    'communication': ('Explain a familiar task with support.', 'Present ideas clearly and adapt them to an audience.', 'Communicate complex ideas and handle difficult questions.', 'Give a short presentation and request specific feedback.'),
    'teamwork': ('Complete an assigned group task with support.', 'Coordinate contributions and resolve routine disagreements.', 'Help a team work through complex collaboration problems.', 'Join a group task and reflect on how you supported others.'),
    'problem_solving': ('Follow a worked example to resolve a problem.', 'Compare possible solutions and test a chosen approach.', 'Solve unfamiliar problems and evaluate trade-offs.', 'Document a problem, two solutions and the result of a small test.'),
    'organisation': ('Follow a checklist with reminders.', 'Prioritise tasks and meet competing deadlines.', 'Manage complex workloads and adapt plans when priorities change.', 'Plan a week of tasks and review what helped you meet deadlines.'),
    'creativity': ('Adapt an existing idea with support.', 'Generate and develop several ideas for a task.', 'Create and evaluate original approaches under constraints.', 'Sketch three approaches to a familiar problem and develop one.'),
    'leadership': ('Take responsibility for a small task with support.', 'Coordinate a small group and support shared decisions.', 'Guide a team through uncertainty and reflect on outcomes.', 'Facilitate a short group task and ask for feedback.'),
}


class CareerModel:
    def recommend(self, values, education, subject, top_k=5):
        results = []
        for career in CAREERS:
            skills = [dict(key=k, label=LABELS[k], activity=SKILL_GUIDES[k][3], value=values[k], target=target,
                           alignment=round(min(values[k]/target, 1)*100))
                      for k, target in career['skills'].items()]
            interests = [dict(label=LABELS[k], value=values[k]) for k in career['interests']]
            skill_score = 100 * sum(min(values[k]/t, 1) for k,t in career['skills'].items()) / len(skills)
            interest_score = 100 * sum(i['value'] for i in interests) / (5*len(interests))
            subject_score = 100 if subject in career['subjects'] else 50
            # Education describes study stage; it is not a proxy for capability.
            score = .65*skill_score + .30*interest_score + .05*subject_score
            results.append(dict(**{k: v for k, v in career.items() if k != 'skills'}, score=round(score, 1), skill_score=round(skill_score, 1),
                                interest_score=round(interest_score, 1), subject_score=subject_score,
                                skills=skills, interest_analysis=interests,
                                strengths=[s for s in skills if s['value'] >= s['target']],
                                gaps=sorted([s for s in skills if s['value'] < s['target']],
                                            key=lambda s:s['target']-s['value'], reverse=True),
                                education_note=f'At your {education.lower()} stage, discuss suitable entry routes, placements and further training with your university careers team.'))
        return sorted(results, key=lambda r:r['score'], reverse=True)[:top_k]


model = CareerModel()
