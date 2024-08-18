from app import app,render_template,request
import explore
from connections import connection
from models import get_yoga_data


@app.route('/Description<username>&<part>')
def description(username,part):
    data = get_details(part)
    if username != 'None':
        return render_template('Description.html',data=data,username=username)
    return render_template('Description.html',data=data)

def get_details(part):
    data = get_yoga_data(part.upper())
    return data