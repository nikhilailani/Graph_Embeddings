from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Length, DataRequired, NumberRange

# Form for keyword search
class KeywordSearchForm(FlaskForm):
	keyword = StringField("keyword", validators=[InputRequired(), Length(1, 500)], description="Search anything")


# Form for candidate details
class CandidateForm(FlaskForm):
	candidate_id = StringField('Candidate ID', validators=[InputRequired(), DataRequired(), Length(5)], description="Candidate ID")
	country = SelectField('Country', choices=[], validators=[DataRequired()], description="Country")
	city = SelectField('City', choices=[], validators=[DataRequired()], description="City")
	state = SelectField('State', choices=[], validators=[DataRequired()], description="State")
	education = SelectField('Education', choices=[], description="Education")
	experience = IntegerField('Experience (years)', validators=[DataRequired(), NumberRange(min=0)], description="Experience in year(s)")


# Form for job details
class JobForm(FlaskForm):
	job_id = StringField('Job ID', validators=[InputRequired(), DataRequired(), Length(min=5)], description="Job ID")
	country = SelectField('Country', choices=[], validators=[DataRequired()], description="Country")
	city = SelectField('City', choices=[], validators=[DataRequired()], description="City")
	state = SelectField('State', choices=[], validators=[DataRequired()], description="State")
	education = SelectField('Education', choices=[], validators=[DataRequired()], description="Education Level")
	job_title = SelectField('Job Title', choices=[], validators=[DataRequired()], description="Job Title")
	skills = SelectField('Skills', choices=[], validators=[DataRequired()], description="Required Skills", coerce=int)
