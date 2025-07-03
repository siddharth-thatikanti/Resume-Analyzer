from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Example company requirements (simplified)
company_requirements = {
    "TCS": ["Python", "Communication", "Teamwork"],
    "Infosys": 
    ["Java", "Problem Solving", "DSA"],
    "Wipro": ["C++", "Projects", "Leadership"],
    "Cognizant": ["HTML", "CSS", "Teamwork"],
    "Accenture": ["Python", "AI/ML", "Innovation"],
    "Capgemini": ["JavaScript", "React", "Communication"],
    "HCL": ["SQL", "Projects", "Soft Skills"],
    "Tech Mahindra": ["Java", "Spring", "Problem Solving"],
    "IBM": ["Cloud", "Python", "Git"],
    "L&T Infotech": ["Networking", "Security", "Teamwork"]
}

@app.route("/upload", methods=["POST"])
def analyze_resume():
    file = request.files.get("resume")
    company = request.form.get("company")

    if not file or not company:
        return jsonify({"error": "Missing resume or company"}), 400

    text = file.read().decode("utf-8")

    # Analyze the resume text for company requirements
    requirements = company_requirements.get(company, [])
    faults = []

    for req in requirements:
        if req.lower() not in text.lower():
            faults.append({
                "fault": f"Missing required skill: {req}",
                "suggestion": f"Consider adding details about your experience with {req}"
            })

    return jsonify({"faults": faults})

if __name__ == "__main__":
    app.run(debug=True)
