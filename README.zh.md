# 🏗️ Archinamer

**[English](README.md)** | **[简体中文](README.zh.md)**

**Archinamer** 是一款专为终端设计的 AI 驱动型“架构顾问”。它旨在解决开发者常遇到的“命名悖论”：深知要构建什么功能，却在决定一个“完美”的仓库名称上耗费过多时间。

与随机名称生成器不同，它通过 LLM（大语言模型）理清你的设计意图（如：个人项目 vs. 企业级服务、CLI vs. Web），并据此建议符合行业标准、具备上下文感知能力的命名。

---

## ✨ 功能特性

- **顾问式沟通 (Consultative Approach)**：在给出建议前，会像资深架构师一样提出针对性的架构问题。
- **上下文感知 (Context-Aware)**：能够识别技术栈（如 Spring Boot, Python 等），并智能调整 `-service`、`-api` 或 `-cli` 等后缀。
- **终端深度集成 (Terminal Integrated)**：一键完成文件夹创建、Git 仓库初始化及中英双语 README 生成。
- **专业命名逻辑 (Professional Logic)**：强制执行 `kebab-case` 规范，并自动剔除 "project" 或 "repo" 等冗余词汇。

---

## 🚀 快速上手

### 前提条件

- **Python 3.8+**
- **通义千问 (DashScope) API Key** (或任何兼容 OpenAI SDK 的 API 密钥)

### 安装步骤

1. **克隆仓库**到本地。
2. **运行自动化安装脚本**来创建虚拟环境并安装工具：

```bash
chmod +x setup.sh
./setup.sh

```

3. **配置 API 密钥**。在自动生成的 `.env` 文件中填入你的密钥：

```text
DASHSCOPE_API_KEY=your_actual_key_here

```

---

## 🛠️ 使用说明

在终端中输入 `archinamer` 命令并紧跟你的项目想法即可：

```bash
archinamer "一个基于 Spring Boot 的猫咪健康数据采集后端系统"

```

1. **架构咨询**：AI 会提出后续问题以理解你的系统架构。
2. **提供背景**：输入你的需求细节（例如：“企业级微服务，使用 Spring Boot 和 K8s”）。
3. **确认名称**：预览并确认 AI 建议的名称（例如：`feline-vitals-service`）。
4. **即刻开始**：工具将自动创建文件夹、初始化 Git 并生成初始 README。

---

## 📂 项目结构

本项目采用 **Flat Layout** 结构，确保打包简洁且易于分发：

```text
archinamer/
├── archinamer/        # 源代码包
│   ├── config.py      # 环境配置与用户画像设置
│   ├── consultant.py  # AI 逻辑与专业提示词 (Prompts)
│   └── main.py        # CLI 命令行入口
├── pyproject.toml     # 现代 Python 构建配置
└── setup.sh           # 自动化引导脚本

```

---

## 🧠 技术栈

- **编程语言**：Python 3.13
- **AI 引擎**：Qwen 通义千问 (基于 OpenAI SDK)
- **环境管理**：`python-dotenv`
