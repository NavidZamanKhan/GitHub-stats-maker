from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_stats", methods=["POST"])
def generate_stats():
    username = request.form.get("username")
    stat_type = request.form.get("stat_type")
    theme = request.form.get("theme")

    base_url = "https://github-readme-stats.vercel.app/api"
    urls = []

    if stat_type == "general":
        # Automatically include all general stats without displaying checkboxes
        general_stats = [
            f'<img id="profile-details" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme={theme}" alt="Profile Details" style="width: 100%;">'
        ]
        urls.extend(general_stats)

    elif stat_type == "top_langs":
        # For Top Languages
        layout = "compact" if "compact" in request.form else "default"
        url = f"{base_url}/top-langs/?username={username}&theme={theme}&layout={layout}"
        urls.append(url)

    elif stat_type == "profile_details":
        # For Profile Details
        details_options = request.form.getlist("details")
        show_icons = "true" if "show_icons" in details_options else "false"
        hide_border = "true" if "hide_border" in details_options else "false"
        url = f"https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme={theme}&show_icons={show_icons}&hide_border={hide_border}"
        urls.append(url)

    return render_template("result.html", stat_urls=urls)


if __name__ == "__main__":
    app.run(debug=True)
