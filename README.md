# Google Form Auto-Filler (Python + Selenium)

A small browser-automation script that opens a Google Form in Chrome, fills its text fields from Python data and submits the form automatically.

## How it works

1. Starts Chrome with Selenium WebDriver (Selenium Manager fetches the matching ChromeDriver).
2. Opens the form URL and waits for the page to load.
3. Finds the text inputs, types each value from `my_details`, and clicks Submit.

## How to run

```bash
pip install -r requirements.txt
python automated_googleform_submition.py
```

To use your own form, change the form URL and the `my_details` list in the script.

## Tech

Python 3, Selenium 4, Google Chrome.
