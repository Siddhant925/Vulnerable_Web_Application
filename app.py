from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            content TEXT
        )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "Database Initialized"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        conn.close()

        if user:
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    return f"""
        <h2>Welcome {session['username']}</h2>
        <a href="/create_post">Create Post</a><br><br>
        <a href="/view_posts">View Posts</a><br><br>
        <a href="/logout">Logout</a>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        content = request.form["content"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)",
                       (session["user_id"], content))

        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("create_post.html")

@app.route("/view_posts")
def view_posts():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT posts.id, users.username, posts.content
        FROM posts
        JOIN users ON posts.user_id = users.id
    """)

    posts = cursor.fetchall()
    conn.close()

    return render_template("view_posts.html", posts=posts)

@app.route("/profile/<int:user_id>")
def profile(user_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    if user:
        return f"""
            <h2>Profile Page</h2>
            <p>User ID: {user[0]}</p>
            <p>Username: {user[1]}</p>
            <a href="/dashboard">Back</a>
        """
    else:
        return "User not found"


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
