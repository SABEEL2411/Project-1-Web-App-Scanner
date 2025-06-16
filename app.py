import sys
import pathlib

# Adds the parent of "app" (i.e., the project root) to sys.path
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))


from flask import Flask, render_template, request
from Scanner.scanner import scan_xss
from Scanner.reporter import save_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    report_path = None
    if request.method == "POST":
        url = request.form["url"].strip()
        results = scan_xss(url)
        if results:
            report_path = save_report(results)
    return render_template("index.html", results=results, report=report_path)

if __name__ == "__main__":
    # Always start from project root:  python app/app.py
    app.run(debug=True, port=5000)

