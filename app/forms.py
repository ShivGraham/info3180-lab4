from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields import FileField 

class UploadForm(FlaskForm):
	image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])