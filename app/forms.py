
#  Create a form called UploadForm that has
# two fields. A TextArea field called 'description' that requires a user to
# fill in some data and a FileField called 'photo' that only allows images to
# be uploaded. 

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

from wtforms import PasswordField
from wtforms.validators import InputRequired
class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])
