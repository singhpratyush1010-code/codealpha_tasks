import os
import re

INPUT_FILE = "emails.txt"            # file to read from
OUTPUT_FILE = "extracted_emails.txt"  # file to save results in

# Regex pattern for matching email addresses
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def main():
    print("=== EMAIL EXTRACTOR ===")

    # Check that the input file exists
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found in this folder.")
        return

    # Read the whole file
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Find all emails and remove duplicates (keeping original order)
    found = re.findall(EMAIL_PATTERN, text)
    unique_emails = list(dict.fromkeys(email.lower() for email in found))

    if not unique_emails:
        print("No email addresses found.")
        return

    # Save to output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_emails))

    print(f"Found {len(found)} email(s), {len(unique_emails)} unique.")
    print(f"Saved to '{OUTPUT_FILE}':\n")
    for email in unique_emails:
        print(f"  {email}")


if __name__ == "__main__":
    main()
