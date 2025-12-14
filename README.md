# Microsoft AI Agents

A collection of AI agent experiments, notebooks, and demo applications that explore building autonomous agents using modern open‑source large language models (LLMs) and orchestration tools.

This repository provides runnable examples, demo apps, and workflows to help you prototype and experiment with AI agent ideas — from basic LLM prompting to full API + mobile integrations.

---

## 🧠 What’s Inside

```

├── complete_app/           # Standalone applications and demos
├── notebooks/              # Jupyter notebooks for exploration and prototyping
├── prior_work/             # Reference, research, or legacy experiments
├── requirements.txt        # Python dependencies
├── README.md               # This file

````

The core demos include:

- Notebook workflows for interacting with LLMs
- A prototype backend API (`llm_app_generated_on_colab.py`)
- A Streamlit frontend demo
- Mobile build configuration via Buildozer (Android)

---

## 🚀 Quick Start

### 🛠️ Prerequisites

Install dependencies:

```bash
pip install -r requirements.txt
````

> Recommended Python versions: **3.10+**

---

### 🧪 Running the Notebook

1. Open Jupyter or Colab.
2. Navigate into the `notebooks/` directory.
3. Run the notebook(s) to experiment with LLM prompts and agent logic.

---

### 🖥️ Running the API Backend Locally

This project includes a simple API you can launch locally:

```bash
uvicorn llm_app_generated_on_colab:app --reload --port 9000
```

You can then send requests from any client to the running server.

---

### 📱 Running the Demo (Streamlit)

Start the interactive demo:

```bash
streamlit run demo.py
```

This opens a UI where you can interact with the AI agent in your browser.

---

## 📲 Building the Android Demo

The `complete_app/` folder contains a Buildozer configuration for packaging a demo Android app.

To build (Linux/macOS):

```bash
cd complete_app
buildozer init
buildozer android debug
```

Install the generated `.apk` on a device to test the mobile experience.

---

## 🔄 How It Works (High‑Level)

This project combines:

* **LLM inference** — via accessible models like Zephyr, BioMistral, or HuggingFace models.
* **Agent logic** — Py notebooks and Python functions that demonstrate task delegation to models.
* **Interactive UI** — Streamlit for quick UX iteration.
* **Mobile integration** — Buildozer + Python backend for Android prototyping.

This is ideal for experimentation and learning how to build more capable autonomous systems.

---

## 📦 Dependencies

Listed in `requirements.txt`. Typical entries include:

```text
fastapi
uvicorn
streamlit
openai / huggingface client
...
```

(Be sure to adjust based on your runtime / chosen model provider.)

---

## 📚 Resources & Inspiration

This project is inspired by modern **AI agent frameworks** that let LLMs act as autonomous helpers — coordinating tasks and tools to solve problems. Examples include:

* **Microsoft Agent Framework** — a comprehensive multi‑language agent ecosystem for Python and .NET. ([GitHub][1])
* **AI agent learning materials and courses** — such as Microsoft’s AI Agents for Beginners series. ([GitHub][2])

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add new agent demos
* Improve notebooks with clearer explanations
* Add CI workflows
* Refine mobile build setup

Please open issues or pull requests.

---

## 📄 License

Distributed under the terms of the MIT License.

---

## ❓ Questions

If you need help getting started, drop a GitHub issue — happy to help!

```

---

If you want, I can also generate **badges** (CI, license, PyPI), a **template issue/PR**, or a **detailed architecture diagram** to include in the README.
::contentReference[oaicite:2]{index=2}
```

[1]: https://github.com/microsoft/agent-framework?utm_source=chatgpt.com "GitHub - microsoft/agent-framework: A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET."
[2]: https://github.com/microsoft/ai-agents-for-beginners?utm_source=chatgpt.com "GitHub - microsoft/ai-agents-for-beginners: 12 Lessons to Get Started Building AI Agents"
