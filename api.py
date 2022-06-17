import flask
from flask import request, jsonify
import db_conn

app = flask.Flask(__name__)
app.config["DEBUG"] = False

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

job_list = [
    {'id': 0,
     'title': 'System Support Engineer',
     'company': 'Sourcetoad',
     'start_date': 'Sept 2021',
     'end_date': 'June 2022',
     'description': 'Devops engineering, working with Jira tickets to build and improve the software infrastructure, as well as the CI/CD pipeline.'
     },
    {'id': 1,
     'title': 'Redhat System Administrator',
     'company': 'Jacobs Technology',
     'start_date': 'June 2019',
     'end_date': 'Sept 2021',
     'description': 'System administrator for multiple Linux servers both physical and virtual to maintain the DNS, and Mail Architecture for USTRANSCOM'
     },
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Chavez Ellis Resume</h1>
<p>A prototype API for the career of Chavez Ellis.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/jobs/all', methods=['GET'])
def api_jobs():
    return jsonify(job_list)

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_skills():
    return jsonify(books)

@app.route('/api/v1/resources/jobs', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for job in job_list:
        if job['id'] == id:
            results.append(job)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()

