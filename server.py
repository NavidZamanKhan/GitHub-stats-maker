from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_stats", methods=["POST"])
def generate_stats():
    username = request.form.get("username")
    theme = request.form.get("theme")

    urls = {
        "general": f"https://github-readme-stats.vercel.app/api?username={username}&theme={theme}&show_icons=true&hide_border=true&count_private=true",  # General Stats
        "languages": f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&theme={theme}&show_icons=true&hide_border=true&layout=compact",  # Top Languages
        "profile": f"https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme={theme}&hide_border=true",  # Profile Details
    }

    return jsonify(urls)


if __name__ == "__main__":
    app.run(debug=True)
