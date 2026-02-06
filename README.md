# 🏗️ Archinamer

**[English](README.md)** | **[简体中文](README.zh.md)**

**Archinamer** is an AI-powered "Architect Consultant" for your terminal. It solves the developer paradox of knowing exactly _what_ you want to build but spending too much time deciding on the _perfect_ repository name.

Instead of just generating random names, it uses an LLM to clarify your intent (Personal vs. Enterprise, CLI vs. Web) before suggesting an industry-standard, context-aware name.

---

## ✨ Features | 功能特性

- **Consultative Approach**: Asks targeted architectural questions before naming.
- **Context-Aware**: Recognizes tech stacks (Spring Boot, Python, etc.) and adjusts suffixes like `-service`, `-api`, or `-cli`.
- **Terminal Integrated**: Initializes your folder, git repository, and a bilingual base README in one go.
- **Professional Logic**: Enforces `kebab-case` and excludes redundant words like "project" or "repo".

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Qwen (DashScope) API Key** (or any OpenAI-compatible SDK key)

### Installation

1. **Clone the repository** to your local machine.
2. **Run the automated setup script** to create your virtual environment and install the tool:

```bash
chmod +x setup.sh
./setup.sh

```

3. **Configure your API key** in the generated `.env` file:

```text
DASHSCOPE_API_KEY=your_actual_key_here

```

---

## 🛠️ Usage

Simply run the `archinamer` command followed by your project idea:

```bash
archinamer "a backend system for tracking cat health via spring boot"

```

1. **Consultation**: The AI asks follow-up questions to understand your architecture.
2. **Input**: Provide context (e.g., "Enterprise microservice, Spring Boot, K8s").
3. **Confirmation**: Review and confirm the suggested name (e.g., `feline-vitals-service`).
4. **Result**: A new folder is created with `git init` and a generated README.

---

## 📂 Project Structure

This project uses a **Flat Layout** for clean packaging and easy distribution:

```text
archinamer/
├── archinamer/        # Source code package (源代码包)
│   ├── config.py      # Environment & Profile settings
│   ├── consultant.py  # AI Logic & Professional Prompts
│   └── main.py        # CLI Entry point
├── pyproject.toml     # Modern Python build config
└── setup.sh           # Automated bootstrap script

```

---

## 🧠 Tech Stack

- **Language**: Python 3.13
- **AI Engine**: Qwen (via OpenAI SDK)
- **Environment**: `python-dotenv`
