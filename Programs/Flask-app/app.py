from flask import Flask, render_template, flash, request
from flask_restful import reqparse
from forms import CandidateForm, JobForm
from neo4j_models import Neo4jTool

app = Flask(__name__)
app.secret_key = 'ym1c9izrh8H216Z61dY_VXvOK0zBnubquGFZQspoRn4'
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False)) 

global entity_json
neo_con = Neo4jTool()
neo_con.connect2neo4j()


@app.route('/', methods=['GET', 'POST'])
def main():
    print('Neo4J has connected...')
    candidate_form = CandidateForm(request.form)
    candidate_form.country.choices = neo_con.get_countries()
    candidate_form.state.choices = neo_con.get_states()
    candidate_form.city.choices = neo_con.get_cities()
    candidate_form.education.choices = neo_con.get_education_choices()
    try:
        if candidate_form.validate_on_submit():
            candidate_form_data = {
                'candidate_id': candidate_form.candidate_id.data.strip(),
                'country': candidate_form.country.data,
                'state': candidate_form.state.data,
                'city': candidate_form.city.data,
                'education': candidate_form.education.data,
                'experience': candidate_form.experience.data,
            }
            print(candidate_form_data)
            candidate_creation(candidate_form_data)
            print("Submitted successfully...")
        else:
            flash("Valid Form")
    except:
        print("[log-neo4j] empty form")

    return render_template('candidate_profile.html', form=candidate_form)

@app.route('/job', methods=['GET', 'POST'])
def job_page():
    job_form = JobForm(request.form)
    job_form.country.choices = neo_con.get_countries()
    job_form.state.choices = neo_con.get_states()
    job_form.city.choices = neo_con.get_cities()
    job_form.education.choices = neo_con.get_education_choices()
    try:
        if job_form.validate_on_submit():
            form_data = {
                'job_id': job_form.job_id.data.strip(),
                'country': job_form.country.data,
                'state': job_form.state.data,
                'city': job_form.city.data,
                'education': job_form.education.data,
            }
            job_creation(form_data)
            print("Submitted successfully...")
        else:
            flash("Valid Form")
    except:
        print("[log-neo4j] empty form")

    return render_template('job_creation.html', form=job_form)


def candidate_creation(form_data):
    db = neo_con
    try:
        data = db.create_candidate(form_data)
    except Exception as e:
        print("Error:", e)
    return data

def job_creation(form_data):
    db = neo_con
    try:
        data = db.create_job(form_data)
    except Exception as e:
        print("Error:", e)
    return data

parser = reqparse.RequestParser()
parser.add_argument('string', type=str)


if __name__ == '__main__':
    app.run()
