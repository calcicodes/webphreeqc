from flask import Flask, render_template, request, session
import os
import uuid
from utils.code_runner import run_code, database_options
from utils.phreeqc_inputs import PHREEQC_INPUT_TEMPLATES

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    # return render_template('index.html', input_placeholder='')
    return render_template(
        'index.html', 
        initial_input=PHREEQC_INPUT_TEMPLATES['Blank'],
        database_options=database_options,
        input_options=PHREEQC_INPUT_TEMPLATES
    )

@app.route('/get_template/<template_name>', methods=['GET'])
def get_template(template_name):
    return {'template': PHREEQC_INPUT_TEMPLATES[template_name]}

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    user_code = data['user_code']
    UID = str(uuid.uuid4())
    
    output = run_code(UID, code=user_code)
    
    return {'output': output}

if __name__ == '__main__':
    app.run(debug=True)