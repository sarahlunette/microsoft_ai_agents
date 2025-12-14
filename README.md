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

Recommended Python versions: 3.10+

---

### 🧪 Running the Notebook

* Open Jupyter or Colab.
* Navigate into the `notebooks/` directory.
* Use `LLM_app.py` (uncleaned version):

  * Skip the sections marked "skip"
  * Stop after the `snapshot_downloads` section to run the cells

---

### 🌐 Creating the Colab API

1. Open `with_cloudflared.ipynb` on Colab.
2. Run the notebook to expose the model via Cloudflare.
3. Copy the external Cloudflare URL.
4. Paste the URL in `llm_app_generate_on_colab.py` under `COLAB_URL`.

---

### 🖥️ Running the API Backend Locally

Launch the API locally:

```bash
uvicorn llm_app_generated_on_colab:app --port 9000
```

> ⚠️ Make sure the port is changed to avoid conflicts with Colab connections.

---

### 📱 Running the Streamlit Demo

Start the interactive demo:

```bash
streamlit run demo.py
```

This opens a UI where you can interact with the AI agent in your browser.

---

### 📲 Building the Android Demo

The `complete_app/` folder contains a Buildozer configuration for packaging a demo Android app.

```bash
cd complete_app
buildozer init
buildozer android debug
```

* Use OpenMTP to copy the generated `.apk` to your device (Downloads folder on a Google phone).
* Install the APK to test the mobile experience.
* **Important:** Modify the Cloudflare link in the app if the Colab API changes, then repackage and reinstall the APK.

---

## 🔄 How It Works (High‑Level)

This project combines:

* **LLM inference** — via accessible models like Zephyr, BioMistral, or HuggingFace models.
* **Agent logic** — Python notebooks demonstrating task delegation to models.
* **Interactive UI** — Streamlit for quick UX iteration.
* **Mobile integration** — Buildozer + Python backend for Android prototyping.

---

## 📦 Dependencies

Listed in `requirements.txt`. Typical entries include:

* fastapi
* uvicorn
* streamlit
* openai / huggingface client
* ...

> Adjust dependencies based on your runtime and chosen model provider.

---

## 📚 Resources & Inspiration

Inspired by modern AI agent frameworks that let LLMs act as autonomous helpers:

* Microsoft Agent Framework — multi-language agent ecosystem for Python and .NET ([GitHub](https://github.com/microsoft/AI-Agents))
* AI agent learning materials and courses — such as Microsoft’s AI Agents for Beginners series ([GitHub](https://github.com/microsoft/AI-Agents))

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add new agent demos
* Improve notebooks with clearer explanations
* Add CI workflows
* Refine mobile build setup

Please open issues or pull requests.

---

## ❓ Questions

If you need help getting started, drop a GitHub issue — happy to help!
