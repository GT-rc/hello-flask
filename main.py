from flask import Flask, request, render_template
import cgi
import os 
import jinja2

# Don't need these with render_template
#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    #template = jinja_env.get_template("hello_form.html")
    return render_template("hello_form.html")

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form["first_name"]
    #template = jinja_env.get_template("hello_greeting.html")
    return render_template("hello_greeting.html", name=first_name)




# Copied code to catch up


@app.route('/validate-time')
def display_time_form():
    #template = jinja_env.get_template("time_form.html")
    return render_template("time_form.html")

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
        

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return '/valid-time?time={0}'.format(time)
    else:
        template = jinja_env.get_template("time_form.html")
        return render_template("time_form.html", hours_error=hours_error,
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)

tasks = []

@app.route("/todos", methods=["POST", "GET"])
def todos():

    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)

    template = jinja_env.get_template("todos.html")
    return render_template("todos.html", tasks=tasks, title="This is a test")


app.run()
