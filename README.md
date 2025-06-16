# Project-1-Web-App-Scanner

# 🛡️ Web Application Vulnerability Scanner – Project Guide

## 🎯 Objective

Build a Python-based scanner with a Flask UI to detect common web application vulnerabilities like:

- XSS (Cross-Site Scripting)
- SQL Injection (SQLi)
- CSRF (Cross-Site Request Forgery)

---

## 🧰 Tools & Technologies

- **Python 3**
- `requests`, `BeautifulSoup` – for crawling and form detection
- `re` – for pattern matching
- **Flask** – for web interface
- **OWASP Top 10** – reference for common vulnerabilities

---

## 🗂️ Project Structure

Web-Vuln-Scanner/

├── app/

│ ├── app.py # Flask web interface

│ └── templates/

│ └── index.html # UI form

├── scanner/

│ ├── init.py

│ ├── scanner.py # XSS scanning logic

│ ├── crawler.py # Extract links/forms

│ ├── payloads.py # XSS/SQLi payloads

│ └── reporter.py # Save and show reports

├── reports/

│ └── report_<timestamp>.json

└── README.md



---

## ✅ Step-by-Step Workflow

### 1. **Crawl the Web Page**
- Use `requests` to fetch the page.
- Use `BeautifulSoup` to find all forms and input fields.

 python
soup = BeautifulSoup(response.text, 'html.parser')
forms = soup.find_all("form") 


### 2. Inject Payloads
- Use predefined XSS/SQLi payloads from payloads.py.

- Send payloads in each input field using POST/GET.payload = "<script>alert(1)</script>"

### 3. Analyze the Response
- Look for payload reflection in the HTML.

- Use regex or direct string search to detect vulnerability.

- if payload in response.text:
    # Vulnerable


### 4. Log and Save Reports
 Save results to reports/report_<timestamp>.json.
 Log:
- Target URL
- Input field name
- Vulnerability type
- Evidence
- Severity level

### 5. Flask Web Interface
- Input: User enters a target URL.
- Output: Results are displayed in the browser and saved.

@app.route("/", methods=["GET", "POST"])
def index():
    # Call scan_xss() and render results

### 🚀 How to Run

## 1. Install dependencies:
- pip install flask requests beautifulsoup4

## 2. Navigate to the project root:
- cd Web-Vuln-Scanner

## 3. Run the Flask app:
- python app/app.py

## 4. Open in your browser:
- http://127.0.0.1:5000

### 📁 View Saved Reports
## Check the reports/ folder for detailed logs:
- cat reports/report_*.json

### 🔧 Next Steps / Improvements
- Add SQL Injection detection
- Handle CSRF token validation
- Export reports to PDF or CSV
- Dockerize the app for deployment
- Add authentication and scan history in UI

