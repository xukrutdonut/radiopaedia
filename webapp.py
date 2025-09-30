#!/usr/bin/env python3
"""
Pediatric Radiology Web Application
Display scraped Radiopaedia cases in a simple web interface
"""

from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)


def load_cases():
    """Load cases from JSON file"""
    cases_file = os.path.join('data', 'cases.json')
    
    if not os.path.exists(cases_file):
        return []
    
    try:
        with open(cases_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading cases: {e}")
        return []


@app.route('/')
def index():
    """Home page - list all cases"""
    cases = load_cases()
    return render_template('index.html', cases=cases, total=len(cases))


@app.route('/case/<int:case_id>')
def case_detail(case_id):
    """Case detail page"""
    cases = load_cases()
    
    if 0 <= case_id < len(cases):
        return render_template('case.html', case=cases[case_id], case_id=case_id)
    else:
        return "Case not found", 404


@app.route('/api/cases')
def api_cases():
    """API endpoint to get all cases"""
    cases = load_cases()
    return jsonify(cases)


@app.route('/api/case/<int:case_id>')
def api_case(case_id):
    """API endpoint to get a single case"""
    cases = load_cases()
    
    if 0 <= case_id < len(cases):
        return jsonify(cases[case_id])
    else:
        return jsonify({'error': 'Case not found'}), 404


if __name__ == '__main__':
    print("=" * 60)
    print("Pediatric Radiology Web Application")
    print("=" * 60)
    print("\nStarting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
