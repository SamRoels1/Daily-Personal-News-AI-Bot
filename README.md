# 📰 Daily AI News Curator

An automated, object-oriented Python application that builds a custom daily newspaper. It fetches the top headlines across multiple categories, uses Google's Gemini AI to write a cohesive, engaging summary, and delivers the final briefing directly to Discord and Email.

## ✨ Features
* **Custom Curation:** Automatically pulls the top daily headlines for Global, Technology, Science, and European news using the NewsAPI.
* **AI Summarization:** Utilizes the Google Gemini model to weave raw data into a readable, journalistic morning briefing.
* **Multi-Channel Delivery:** * Delivers a Markdown-formatted message to a private **Discord** server via Webhooks.
  * Converts the AI's Markdown into beautifully styled HTML and sends it via **Email** using SMTP.
* **Fully Automated:** Designed to run headlessly via Windows Task Scheduler (or cron jobs) for hands-free daily delivery.
* **Modular OOP Design:** Built with clean architecture, separating data fetching, AI processing, and delivery mechanisms into distinct classes.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **APIs:** NewsAPI, Google Gen AI SDK (Gemini)
* **Libraries:** `requests`, `google-genai`, `markdown`, `smtplib`, `email`

## 🚀 Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/SamRoels1/Daily-Personal-News-AI-Bot.git](https://github.com/SamRoels1/Daily-Personal-News-AI-Bot.git)
cd Daily-Personal-News-AI-Bot
```

**2. Install dependencies**
```bash
pip install requests google-genai markdown
```

**3. Configure your API Keys**
* Rename the `config_example.py` file to `config.py`.
* Obtain a free API key from NewsAPI.
* Obtain a free API key from Google AI Studio.
* Set up a Discord Webhook in your server settings.
* Generate a 16-character App Password from your Google Account (for email delivery).
* Paste all credentials into your new `config.py` file. *(Note: `config.py` is included in the `.gitignore` to keep your keys safe!)*

## 📂 Project Structure
* `main.py` - The central orchestrator that runs the pipeline.
* `news_fetcher.py` - Handles external requests to NewsAPI.
* `news_summarizer.py` - Manages prompt engineering and Gemini AI generation.
* `discordDelivery.py` - Handles chunking and Webhook transmission to Discord.
* `emailDelivery.py` - Converts Markdown to HTML, applies CSS styling, and sends via SMTP.
* `config.py` - Stores environment variables and API URLs.

## ⚙️ Usage
To run the script manually, execute:
```bash
python main.py
```

**Automation:**
To receive your news daily, set up a trigger in **Windows Task Scheduler** (or a cron job on Linux/macOS) to run `main.py` (or `pythonw.exe` for silent execution) at your preferred time, such as 8:00 AM.