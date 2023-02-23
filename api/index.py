import os, openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        keywords = request.form["keywords"]
        response = openai.Completion.create (
            model="text-davinci-003",
            prompt=generate_prompt(keywords),
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))
    
    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(keywords):
    return """websites that offer or contain {} including the link""".format(keywords.capitalize())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)

