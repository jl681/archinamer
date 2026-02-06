# 🏗️ Archinamer

**Archinamer** is an AI-powered "Architect Consultant" for your terminal. It solves the developer paradox of knowing exactly _what_ you want to build but spending too much time deciding on the _perfect_ repository name.

Instead of just generating random names, it uses an LLM to clarify your intent (Personal vs. Enterprise, CLI vs. Web) before suggesting an industry-standard, context-aware name.

## ✨ Features

- **Consultative Approach:** Asks targeted architectural questions before naming.
- **Context-Aware:** Recognizes tech stacks (Spring Boot, Python, etc.) and adjusts suffixes like `-service`, `-api`, or `-cli`.
- **Terminal Integrated:** Initializes your folder, git repository, and a base README in one go.
- **Professional Logic:** Enforces kebab-case and excludes redundant words like "project" or "repo."

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- A QWEN API Key

### Installation

1.  **Clone the repository** to your local machine.
2.  **Run the setup script** to create your environment and install the tool:
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
3.  **Configure your API key** in the generated `.env` file:
    ```text
    DASHSCOPE_API_KEY=your_actual_key_here
    ```

## 🛠️ Usage

Simply run the `archinamer` command followed by your project idea:

```bash
archinamer "a system to extract and summarize youtube transcripts"

```

1. **Consultation:** The AI will ask a few follow-up questions.
2. **Input:** Provide your context (e.g., "Personal CLI tool in Python").
3. **Confirmation:** Confirm the suggested name (e.g., `yt-summary-cli`).
4. **Result:** A new folder is created, `git init` is run, and you're ready to code.

## 📂 Project Structure

This project uses a **Flat Layout** for clean packaging and easy distribution:

```text
archinamer/
├── archinamer/        # Source code package
│   ├── config.py      # Environment & Profile settings
│   ├── consultant.py  # AI Logic & Prompts
│   └── main.py        # CLI Entry point
├── pyproject.toml     # Modern Python build config
└── setup.sh           # Automated bootstrap script

```

## 🧠 Tech Stack

- **Language:** Python
- **AI Engine:** QEWn (Openai SDK)
- **Environment:** `python-dotenv`
