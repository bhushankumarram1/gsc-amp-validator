## Project Structure

- This project is a sample project. <br />
- For validating via command line. <br />
- JSON files in <b>data/</b> directory <br />

---

## Create Environment for Project

Follow only for the first time setup

1. Create virtual environment: python3 -m venv env
2. Activate virtual environment: source env/bin/activate
3. Install AMP HTML Validator on command: npm install -g amphtml-validator


---

# Validate GSC exported AMP URLs

Quickly Validate AMP URLs exported as csv from GSC, just follow following steps mannually
 
Steps:
1. Export AMP URLs from Google Search Console as CSV file
2. Copy the Table.csv file in the imports folder
4. Run the code : python validate-gsc.py
