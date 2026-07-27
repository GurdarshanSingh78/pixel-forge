---
title: Pixel Forge
emoji: 🎨
colorFrom: blue
colorTo: indigo
sdk: gradio
app_file: app.py
pinned: false
---

<div align="center">

# PixelForge

**Query in. Curated images out.**

An automated pipeline that fetches, deduplicates, and AI-filters images from natural-language queries — then delivers a ready-to-use zip straight to your inbox.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-CLIP-ee4c2c?logo=pytorch&logoColor=white)
![APScheduler](https://img.shields.io/badge/Jobs-APScheduler-informational)
![SQLite](https://img.shields.io/badge/DB-SQLite-003b57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## 🎬 What is PixelForge?

Type a query — *"cyberpunk city street at night"* — and walk away. PixelForge fetches a large batch of candidate images, runs them through OpenAI's **CLIP** model to score semantic relevance, strips out near-duplicates, and packages only the best matches into a downloadable zip — emailed to you the moment it's ready. No manual sifting through hundreds of stock photos required.

```
   query → fetch → embed → filter → dedupe → zip → email
```

## ✨ Features

| | |
|---|---|
| 🌐 **Automated Fetching** | Pulls high-resolution images at scale via the Pexels API |
| 🧠 **AI-Powered Filtering** | Uses CLIP (PyTorch/Transformers) to semantically rank images against your query and discard weak matches |
| 🪞 **Smart Deduplication** | Detects and removes near-identical images before delivery |
| ⏱️ **Background Processing** | Jobs are queued and run asynchronously via APScheduler, backed by SQLite for persistence |
| 📦 **Automated Delivery** | Zips the final curated set and emails a download link — no dashboard babysitting required |
| ⚡ **FastAPI-Powered** | A lightweight FastAPI + Uvicorn server exposes a clean web interface to kick off and track jobs |

## 🏗️ How It Works

1. **Submit** a text query through the web interface.
2. **Fetch** — PixelForge pulls a large candidate pool from the Pexels API.
3. **Embed & Score** — Each image and the query are embedded via CLIP; images are ranked by cosine similarity.
4. **Filter & Dedupe** — Low-relevance and near-duplicate images are dropped.
5. **Package** — The surviving images are zipped.
6. **Deliver** — An email with the download link is sent automatically via SMTP.

All of this runs as a background job — APScheduler and SQLite handle queuing, retries, and job state, so a query can be submitted and left to finish on its own.

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **API/Server:** FastAPI + Uvicorn
- **AI/ML:** OpenAI CLIP via PyTorch & Hugging Face Transformers
- **Image Source:** Pexels API
- **Scheduling/Jobs:** APScheduler
- **Persistence:** SQLite
- **Delivery:** SMTP (Gmail App Password)

## 📋 Prerequisites

- Python 3.10+
- A [Pexels API Key](https://www.pexels.com/api/)
- A Gmail App Password (for SMTP delivery)

## 🚀 Local Setup

**1. Clone and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Configure environment variables**

Create a `.env` file in the project root:

```env
PEXELS_API_KEY=your_pexels_key
MAIL_USERNAME=your_gmail_address
MAIL_PASSWORD=your_16_character_app_password
MAIL_FROM=your_gmail_address
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
```

**3. Initialize the database**

```bash
python initial_setup.py
```

**4. Start the server**

```bash
uvicorn app.main:app
```

> **macOS (Apple Silicon) users:** set these first to avoid C++ multithreading crashes:
> ```bash
> export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
> export TOKENIZERS_PARALLELISM=false
> export OMP_NUM_THREADS=1
> ```

**5. Open the app**

Visit **http://127.0.0.1:8000** to submit queries and track jobs from the web interface.

## 📄 License

Released under the [MIT License](LICENSE).

---

<div align="center">
<sub>Built with ⚡ by Gurdarshan</sub>
</div>