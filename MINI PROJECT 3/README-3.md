# Email Extractor (Task Automation)

A Python script that automates a repetitive task: pulling all email addresses out of a text file and saving them to another file.

**Author:** Pratyush Singh

---

## Features

- Reads `emails.txt` and finds all email addresses using a regular expression
- Removes duplicates (case-insensitive), keeping the original order
- Saves the results to `extracted_emails.txt`
- Prints the found emails on screen
- Shows a clear error message if the input file is missing

## Concepts Used

`os` module, `re` (regular expressions), file handling, lists

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

1. Keep `email_extractor.py` and `emails.txt` in the **same folder**.
2. Open a terminal in that folder.
3. Run:

```
python email_extractor.py
```

If `python` is not recognized, use `py email_extractor.py`.

To use your own data, put any text in `emails.txt` (or change `INPUT_FILE` at the top of the script).

## Sample Output

```
=== EMAIL EXTRACTOR ===
Found 6 email(s), 5 unique.
Saved to 'extracted_emails.txt':

  rahul.sharma@gmail.com
  hr@company.co.in
  careers@company.co.in
  priya_verma99@yahoo.com
  support@mangalmay.edu
```

## How It Works

1. Checks that `emails.txt` exists using `os.path.exists()`.
2. Reads the whole file as text.
3. Uses `re.findall()` with an email pattern to collect all matches.
4. Removes duplicates and writes the unique emails to `extracted_emails.txt`.

## Common Error

```
Error: 'emails.txt' not found in this folder.
```

This means `emails.txt` is not in the same folder as the script. Move it there and run again.

## Files

```
task3_email_extractor/
├── README.md
├── email_extractor.py
└── emails.txt
```

`extracted_emails.txt` is created automatically after running.
