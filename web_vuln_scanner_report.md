# 🛡️ Web Application Vulnerability Scanner – Final Project Report

## 📌 Project Title
**Web Application Vulnerability Scanner Using Python and Flask**

---

## 📄 Abstract

This project involves developing a lightweight, Python-based web application vulnerability scanner that can detect common vulnerabilities like XSS (Cross-Site Scripting), SQL Injection, and CSRF. It includes both a command-line scanner and a user-friendly Flask web interface. The scanner uses static and dynamic analysis techniques to crawl target websites, inject payloads, and report any discovered security flaws.

---

## 🎯 Objectives

- Detect common vulnerabilities in web applications based on the OWASP Top 10.
- Automate the process of finding input fields and forms in websites.
- Inject payloads and analyze server responses for vulnerability indicators.
- Provide a web-based UI for initiating scans and reviewing reports.

---

## 🧰 Technologies Used

| Component         | Technology              |
|------------------|-------------------------|
| Programming Lang | Python 3                |
| HTTP Requests     | `requests`              |
| HTML Parsing      | `BeautifulSoup`         |
| Pattern Matching  | `re`                    |
| Web Framework     | Flask                   |
| Reporting         | JSON File Logging       |

---

## 🧱 System Architecture

```
+------------------------+
|      Flask UI          |
| (app/app.py + HTML)    |
+------------------------+
          ↓
+------------------------+
|    Scanner Engine      |
|  (scanner/scanner.py)  |
| - Injects Payloads     |
| - Detects Vulns        |
+------------------------+
          ↓
+------------------------+
|     Crawler Module     |
| (scanner/crawler.py)   |
| - Parses Forms & URLs  |
+------------------------+
          ↓
+------------------------+
|   Reporting System     |
| (scanner/reporter.py)  |
| - Logs Results to JSON |
| - Displays in Web UI   |
+------------------------+
```

---

## ⚙️ Implementation Details

### 🔹 Crawling
- Fetches and parses HTML using `requests` and `BeautifulSoup`.
- Extracts all forms and input fields from the page.

### 🔹 Payload Injection
- Loads test payloads for XSS from `payloads.py`.
- Submits payloads into each form input.

### 🔹 Vulnerability Detection
- Analyzes server responses for reflected payloads.
- Uses simple pattern matching and regex to identify vulnerabilities.

### 🔹 Reporting
- Logs vulnerabilities with:
  - Target URL
  - Vulnerable parameter
  - Payload used
  - Evidence
  - Severity level
- Saves report as timestamped `.json` file in `reports/` folder.
- Displays results in browser after scan.

---

## 🌐 Web Interface

- Built using Flask.
- Provides a form to input the target URL.
- Displays results dynamically on the same page.
- Allows for easy scan management via browser.

---

## 🧪 Sample Scan Result (Example)

```json
{
  "url": "http://testphp.vulnweb.com",
  "vulnerabilities": [
    {
      "type": "XSS",
      "parameter": "search",
      "payload": "<script>alert(1)</script>",
      "evidence": "alert(1) script reflected in response",
      "severity": "High"
    }
  ],
  "timestamp": "2025-06-16T14:22:01"
}
```

---

## 📁 Folder Structure

```
Web-Vuln-Scanner/
├── app/
│   └── app.py, templates/
├── scanner/
│   └── scanner.py, crawler.py, reporter.py, payloads.py
├── reports/
│   └── report_<timestamp>.json
```

---

## 📊 Results & Achievements

- Successfully detects reflected XSS in GET/POST forms.
- Scans and analyzes multiple forms on a page.
- Clean and simple UI to perform scans.
- Stores and displays detailed scan reports.

---

## 🚀 Future Enhancements

- Add detection for:
  - SQL Injection
  - CSRF token issues
  - Authentication bypass
- Implement login/session handling
- Add recursive crawler for multi-page sites
- Export report to CSV or PDF
- Add CVSS-based severity scoring
- Dockerize the application for portability

---

## 📚 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Flask Documentation](https://flask.palletsprojects.com/)