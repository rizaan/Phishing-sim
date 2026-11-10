# Phish_test

A minimal **phishing-awareness demonstration** built with Flask. It serves a fake "Login" page styled to look like a social-media sign-in, captures whatever credentials are typed into it, prints them to the server terminal, and redirects the visitor to a harmless placeholder feed.

The purpose is to **show how credential-harvesting pages work** so that students, trainees, and users can recognise and defend against them.

> ⚠️ **For education and authorised security-awareness training only — in a lab or on machines you own.**
> This code impersonates a login page to capture passwords. Using it to deceive real people, or hosting it where real users can reach it, is **illegal** in most jurisdictions and a serious ethical breach. See [Legal & Ethical Use](#legal--ethical-use). Do not deploy it publicly, do not point it at a real brand's users, and do not use real logos/trademarks if you share or extend it.

---

## Table of Contents

- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Running](#installation--running)
- [What You'll See](#what-youll-see)
- [What This Teaches (Defensive Takeaways)](#what-this-teaches-defensive-takeaways)
- [Notes & Known Issues](#notes--known-issues)
- [Legal & Ethical Use](#legal--ethical-use)

---

## How It Works

```
Browser ──GET /──► Flask serves login.html (fake login form)
   │
   └─ user submits form ──POST /submit──► app.py reads username + password
                                              │
                                              ├─ prints them to the server terminal
                                              │     [+] Captured Credentials -> Username: ..., Password: ...
                                              │
                                              └─ redirect ──► /home (harmless placeholder feed)
```

The whole app is three routes in `app.py`:

| Route | Method | What it does |
|---|---|---|
| `/` | GET | Renders `login.html` — the fake login page. |
| `/submit` | POST | Reads the `username` and `password` fields, prints them to the terminal, redirects to `/home`. |
| `/home` | GET | Renders `home.html` — a decoy feed so the visitor sees something "normal" after logging in. |

There is **no database and no storage** — captured input is only echoed to stdout. This is deliberate: it keeps the demo simple and leaves no credential store behind.

---

## Project Structure

| Path | Description |
|---|---|
| `app.py` | The Flask application (3 routes). |
| `templates/login.html` | The fake login form. |
| `templates/home.html` | The decoy feed shown after "login". |
| `static/style.css` | Styling for the login page. |
| `static/images/instalogo.png` | Logo image used on the pages. |
| `readme.txt` | Original quick-run notes. |

---

## Requirements

- Python 3
- Flask

---

## Installation & Running

Run it **locally, in an isolated environment** (the original notes use Kali, but any OS with Python works).

```bash
# 1. Install Python 3 (if needed)
sudo apt-get install python3

# 2. Install Flask
pip3 install flask

# 3. Run the app
python3 app.py

# 4. Open it in your browser
#    http://localhost:5000
```

---

## What You'll See

1. Open `http://localhost:5000` — the fake login page loads.
2. Type any test values, e.g. `hacker123` / `testpass`, and click **Login**.
3. In the terminal running the app, you'll see:

   ```
   [+] Captured Credentials -> Username: hacker123, Password: testpass
   ```

4. The browser redirects to `/home`, the placeholder feed.

That round-trip — a convincing-looking form that quietly ships what you type to someone else — is the entire point of the demonstration.

---

## What This Teaches (Defensive Takeaways)

Use this demo to make the following lessons concrete:

- **Looks mean nothing.** A page can perfectly copy a brand's logo and styling and still be hostile. Never judge a login by appearance.
- **Check the address bar.** The real defence is the **URL and the certificate** — `localhost:5000` is obviously not the real site. Teach people to read the domain, not the logo.
- **Forms can post anywhere.** The form's `action` sent data to an attacker's route, not the real service. Credentials typed into the wrong place are instantly exposed.
- **Use a password manager + MFA.** Managers won't autofill on a look-alike domain, and MFA blunts a stolen password.
- **Report, don't reuse.** If you ever type a password into a suspicious page, change it everywhere it was reused.

---

## Notes & Known Issues

- **`debug=True` and `host='0.0.0.0'`** in `app.py` make the app reachable from other machines on the LAN and expose the Flask debugger. For a contained demo, prefer `app.run(host='127.0.0.1', port=5000)` and keep debug off so it stays on your own machine only.
- **Broken `<img>` tags.** In both `login.html` and `home.html` the logo tag is malformed:
  ```html
  <img src=""{{ url_for('static', filename='images/instalogo.png') }} alt="...">
  ```
  There's a stray `""` and the `src` attribute is never properly closed. It should be:
  ```html
  <img src="{{ url_for('static', filename='images/instalogo.png') }}" alt="...">
  ```
- **Trademarked logo.** `instalogo.png` is a real brand's mark. If you share or extend this project, replace it with a clearly fictional brand so the material can't be mistaken for, or used as, a real phishing page.
- **No storage by design** — credentials are only printed, never saved.

---

## Legal & Ethical Use

This project exists to **teach people to recognise phishing**, not to commit it.

- Run it **only** on your own machine or in a closed lab, with **test data only**.
- **Never** deploy it on a public server, send its link to anyone, or use it to collect credentials from real people.
- **Never** impersonate a real organisation to real users — that is fraud and unauthorised access, and it is a crime in most countries.
- You are solely responsible for complying with the laws in your jurisdiction.

The author provides this for educational purposes and accepts no liability for misuse.
