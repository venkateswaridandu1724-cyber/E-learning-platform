
from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.security import check_password_hash


import sqlite3
app=Flask(__name__)
app.secret_key="mysecretkey123"
# ---------- DATABASE ----------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT,
quiz_score INTEGER,
progress INTEGER
)
""")

conn.commit()
conn.close()

# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/lesson/<int:id>')
def lesson(id):

    lessons = {

        1: {
            "title": "Data Science Introduction",
            "content": """
            <h1>Data Science ante enti?</h1>
            <p>Data Science ante pedda amount lo unna data ni collect chesi, clean chesi, analyze chesi useful information kanukovadam. Idi companies ki decisions teesukodaniki chala important.</p>

            <h2>Enduku important?</h2>
            <p>Manam daily use chese apps anni data meeda depend avuthayi. Data correct ga use chesthe business growth avuthundi.</p>

            <h2>Real Life Examples</h2>
            <ul>
                <li>Netflix → movies suggest chestundi</li>
                <li>Amazon → products recommend chestundi</li>
                <li>YouTube → videos suggest chestundi</li>
            </ul>

            <h2>Steps</h2>
            <ol>
                <li>Data Collection</li>
                <li>Data Cleaning</li>
                <li>Data Analysis</li>
                <li>Data Visualization</li>
            </ol>
            """
        },

        2: {
            "title": "Python Basics",
            "content": """
            <h1>Python Basics</h1>

            <p>Python oka simple and powerful programming language. Beginners ki chala easy ga ardham avuthundi.</p>

            <h2>Why Python?</h2>
            <p>Python lo syntax easy untundi kabatti beginners fast ga nerchukovachu.</p>

            <h2>Variables</h2>
            <p>Variables ante data store cheyadaniki use chestam.</p>

            <pre>
x = 10
name = "Ravi"
            </pre>

            <h2>Data Types</h2>
            <ul>
                <li>int → numbers</li>
                <li>float → decimals</li>
                <li>string → text</li>
                <li>boolean → True/False</li>
            </ul>

            <h2>Control Statements</h2>
            <p>if-else conditions use chesi decisions tiskuntam.</p>

            <pre>
if x > 5:
    print("Greater")
            </pre>
            """
        },

        3: {
            "title": "Python Libraries",
            "content": """
            <h1>Python Libraries</h1>

            <p>Libraries ante pre-written code. Manaki easy ga work cheyadaniki help chestayi.</p>

            <h2>Important Libraries</h2>
            <ul>
                <li><b>Pandas:</b> Data handling</li>
                <li><b>NumPy:</b> Numerical calculations</li>
                <li><b>Matplotlib:</b> Graphs create cheyadam</li>
            </ul>

            <h2>Example</h2>
            <pre>
import pandas as pd
data = pd.read_csv("file.csv")
            </pre>
            """
        },

        4: {
            "title": "Data Visualization",
            "content": """
            <h1>Data Visualization</h1>

            <p>Data ni visual format lo chupinchadam easy ga ardham avvadanki help chestundi.</p>

            <h2>Types of Charts</h2>
            <ul>
                <li>Bar Chart</li>
                <li>Line Chart</li>
                <li>Pie Chart</li>
            </ul>

            <h2>Example</h2>
            <p>Sales data ni graph lo chupiste trends easy ga kanipistayi.</p>
            """
        },

        5: {
            "title": "Data Cleaning",
            "content": """
            <h1>Data Cleaning</h1>

            <p>Data lo errors, missing values untayi. Avi remove cheyadam Data Cleaning.</p>

            <h2>Methods</h2>
            <ul>
                <li>Null values remove</li>
                <li>Duplicate data remove</li>
                <li>Incorrect values fix</li>
            </ul>

            <h2>Importance</h2>
            <p>Clean data lekunda correct results ravu.</p>
            """
        },

        6: {
            "title": "Data Analysis",
            "content": """
            <h1>Data Analysis</h1>

            <p>Data ni analyze chesi useful insights kanukovadam Data Analysis.</p>

            <h2>Example</h2>
            <p>Company sales data analyze chesi profit increase cheyadam.</p>

            <h2>Tools</h2>
            <ul>
                <li>Python</li>
                <li>Excel</li>
                <li>SQL</li>
            </ul>
            """
        },

        7: {
            "title": "Statistics Basics",
            "content": """
            <h1>Statistics Basics</h1>

            <p>Statistics Data Science ki base.</p>

            <h2>Concepts</h2>
            <ul>
                <li>Mean → average</li>
                <li>Median → middle value</li>
                <li>Mode → most repeated</li>
            </ul>

            <h2>Example</h2>
            <p>Marks average calculate cheyadam.</p>
            """
        },

        8: {
            "title": "SQL Basics",
            "content": """
            <h1>SQL Basics</h1>

            <p>SQL databases manage cheyadaniki use chestaru.</p>

            <h2>Commands</h2>
            <ul>
                <li>SELECT</li>
                <li>INSERT</li>
                <li>UPDATE</li>
            </ul>

            <pre>
SELECT * FROM students;
            </pre>
            """
        },

        9: {
            "title": "Machine Learning Intro",
            "content": """
            <h1>Machine Learning</h1>

            <p>Machine Learning data ni use chesi predictions chestundi.</p>

            <h2>Types</h2>
            <ul>
                <li>Supervised Learning</li>
                <li>Unsupervised Learning</li>
            </ul>

            <h2>Example</h2>
            <p>Email spam detection.</p>
            """
        },

        10: {
            "title": "Mini Project",
            "content": """
            <h1>Mini Project</h1>

            <p>Student marks analyze chesi report create cheyadam.</p>

            <h2>Steps</h2>
            <ol>
                <li>Data collect</li>
                <li>Clean</li>
                <li>Analyze</li>
            </ol>
            """
        },

        11: {
            "title": "Real Applications",
            "content": """
            <h1>Real Applications</h1>

            <ul>
                <li>Healthcare → disease prediction</li>
                <li>Finance → fraud detection</li>
                <li>Marketing → customer targeting</li>
            </ul>
            """
        },

        12: {
            "title": "Career Path",
            "content": """
            <h1>Career Path</h1>

            <p>Data Science lo chala jobs untayi.</p>

            <ul>
                <li>Data Scientist</li>
                <li>Data Analyst</li>
                <li>ML Engineer</li>
            </ul>

            <h2>Skills</h2>
            <ul>
                <li>Python</li>
                <li>SQL</li>
                <li>Statistics</li>
            </ul>
            """
        }

    }

    lesson = lessons.get(id)

    return render_template("lesson.html", lesson=lesson)
@app.route('/course/datascience')
def datascience():
    return render_template("datascience.html")
@app.route('/ml_lesson/<int:id>')
def ml_lesson(id):
    lesson = ml_lessons.get(id)
    return render_template("lesson.html", lesson=lesson)
ml_lessons = {

    1: {
        "title": "Introduction to Machine Learning",
        "content": """
        <h1>Machine Learning ante enti?</h1>
        <p>Machine Learning ante computer systems data ni use chesi automatic ga nerchukoni predictions cheyadam.</p>

        <h2>Real Life Examples</h2>
        <ul>
            <li>Netflix → movie recommendations</li>
            <li>Email → spam detection</li>
            <li>Amazon → product suggestions</li>
        </ul>
        """
    },

    2: {
        "title": "Types of Machine Learning",
        "content": """
        <h1>Types of ML</h1>

        <h2>1. Supervised Learning</h2>
        <p>Labelled data use chestaru.</p>

        <h2>2. Unsupervised Learning</h2>
        <p>Data lo patterns kanukuntundi.</p>

        <h2>3. Reinforcement Learning</h2>
        <p>Rewards & punishments tho nerchukuntundi.</p>
        """
    },

    3: {
        "title": "Supervised Learning Deep Dive",
        "content": """
        <h1>Supervised Learning</h1>

        <p>Input + Output data ivvadam dwara model train chestam.</p>

        <h2>Examples</h2>
        <ul>
            <li>House price prediction</li>
            <li>Student marks prediction</li>
        </ul>
        """
    },

    4: {
        "title": "Unsupervised Learning",
        "content": """
        <h1>Unsupervised Learning</h1>

        <p>Output labels lekunda data ni group chestundi.</p>

        <h2>Example</h2>
        <ul>
            <li>Customer segmentation</li>
        </ul>
        """
    },

    5: {
        "title": "Regression",
        "content": """
        <h1>Regression</h1>

        <p>Continuous values predict cheyadaniki use chestaru.</p>

        <h2>Example</h2>
        <p>House price prediction</p>
        """
    },

    6: {
        "title": "Classification",
        "content": """
        <h1>Classification</h1>

        <p>Categories predict cheyadam.</p>

        <h2>Examples</h2>
        <ul>
            <li>Spam / Not Spam</li>
            <li>Pass / Fail</li>
        </ul>
        """
    },

    7: {
        "title": "Model Training",
        "content": """
        <h1>Model Training</h1>

        <p>Model ni data tho train chestam.</p>

        <h2>Steps</h2>
        <ol>
            <li>Data collect</li>
            <li>Train model</li>
            <li>Test model</li>
        </ol>
        """
    },

    8: {
        "title": "Overfitting & Underfitting",
        "content": """
        <h1>Overfitting vs Underfitting</h1>

        <p>Overfitting → model data ni too much memorize chestundi.</p>
        <p>Underfitting → model sarigga nerchukodu.</p>
        """
    },

    9: {
        "title": "Model Evaluation",
        "content": """
        <h1>Model Evaluation</h1>

        <p>Model performance check chestam.</p>

        <h2>Metrics</h2>
        <ul>
            <li>Accuracy</li>
            <li>Precision</li>
            <li>Recall</li>
        </ul>
        """
    },

    10: {
        "title": "ML Project",
        "content": """
        <h1>Mini ML Project</h1>

        <p>Student marks prediction system create cheyadam.</p>

        <h2>Steps</h2>
        <ol>
            <li>Data collect</li>
            <li>Train model</li>
            <li>Predict output</li>
        </ol>
        """
    }
}
@app.route('/course/ml')
def ml():
    return render_template("machinelearning.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        score = 0

        for i in range(1, 11):
            if request.form.get(f"q{i}") == "1":
                score += 1

        if score >= 7:
            recommendation = "Machine Learning"
        else:
            recommendation = "Data Science Basics"

        return render_template(
            'dashboard.html',
            user="Student",
            score=score,
            recommendation=recommendation
        )

    return render_template('quiz.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students (name, email, password, quiz_score, progress) VALUES (?, ?, ?, ?, ?)",
                (name, email, password, 0, 0))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("signup.html")
# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']

        # ✅ session lo save
        session['user'] = username

        return redirect('/dashboard')

    return render_template('signin.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    user = session.get('user')

    if not user:
        return redirect('/login')

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, quiz_score, progress FROM students WHERE name=?", (user,))
    data = cursor.fetchone()

    conn.close()

    return render_template("dashboard.html", student=data)
@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

if __name__ == "__main__":
    app.run(debug=True)

