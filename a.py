from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def details():

    if request.method == "GET":
        return render_template("index.html")

    location = request.form.get("location", "").strip()

    if not location:
        return render_template(
            "index.html",
            error="Give the correct location"
        )

    try:

        url = "https://nominatim.openstreetmap.org/search"

        params = {
            "q": location,
            "format": "json",
            "limit": 1
        }

        headers = {
            "User-Agent": "MyFlaskApp/1.0"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        data_json = response.json()

        if not data_json:
            return render_template(
                "index.html",
                error="Location not found"
            )

        data = {
            "latitude": data_json[0]["lat"],
            "longitude": data_json[0]["lon"]
        }

        return render_template(
            "index.html",
            data=data
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )

if __name__ == "__main__":
    app.run(debug=True)