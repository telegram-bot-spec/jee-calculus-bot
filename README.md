# 🧮 JEE Calculus Bot

Ultimate **JEE Advanced Calculus solver** with triple-strategy analysis, SymPy verification, and publication-quality PDF reports.

## ✨ Features

### 🎯 Triple-Strategy Solving
- **Strategy 1: Cengage Method** - Systematic, step-by-step textbook approach
- **Strategy 2: Black Book Shortcuts** - Pattern recognition & quick tricks (3-10 seconds)
- **Strategy 3: Olympiad/Exceptional** - Elegant insights (Feynman tricks, substitutions)

### ✅ SymPy Verification
- Verifies every algebraic step symbolically
- Catches calculation errors automatically
- Confirms all three strategies agree

### 📊 Beautiful Graphs
- Matplotlib-generated function plots
- Shows original function, derivative, and integral
- Embedded directly in PDF

### 📄 Publication-Quality PDFs
- PyLaTeX + pdflatex (Springer/Nature standard)
- Perfect mathematical character rendering
- Zero subscript/superscript issues
- Professional LaTeX typesetting

### 💯 JEE-Specific Intelligence
- Detects common JEE traps (missing +C, domain restrictions)
- Integration technique decision trees
- Standard shortcuts (King's Property, symmetry)
- Olympiad-level tricks database

### 🆓 100% FREE
- Gemini 2.0 Flash (FREE tier)
- SymPy (FREE Python library)
- Matplotlib (FREE)
- PyLaTeX (FREE)
- Total cost: **$0**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- LaTeX distribution (TeX Live/MiKTeX)
- Telegram Bot Token
- Google Gemini API Keys (5 recommended)

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/jee-calculus-bot.git
cd jee-calculus-bot

# Install dependencies
pip install -r requirements.txt

# Install LaTeX (if not already installed)
# Ubuntu/Debian:
sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-latex-extra

# macOS:
brew install --cask mactex

# Windows:
# Download and install MiKTeX from https://miktex.org/download
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

Add your API keys:
```
TELEGRAM_BOT_TOKEN=your_telegram_token
GEMINI_API_KEY_1=your_gemini_key_1
GEMINI_API_KEY_2=your_gemini_key_2
...
```

### Run Locally

```bash
python bot.py
```

---

## 🐳 Deployment (Railway)

### Method 1: Direct GitHub Connection

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/jee-calculus-bot.git
git push -u origin main
```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `jee-calculus-bot` repository
   - Railway will auto-detect Dockerfile and deploy

3. **Set Environment Variables**
   - In Railway dashboard, go to Variables
   - Add all variables from `.env.example`
   - Save and redeploy

### Method 2: Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

---

## 📁 Project Structure

```
jee-calculus-bot/
├── bot.py                    # Main Telegram bot
├── calculus_solver.py        # Triple-strategy solving logic
├── knowledge_base.py         # JEE calculus logic database
├── sympy_verifier.py         # SymPy verification pipeline
├── pdf_generator.py          # PyLaTeX + Matplotlib PDF generation
├── image_enhancer.py         # Image preprocessing (OCR optimization)
├── requirements.txt          # Python dependencies
├── Dockerfile               # Railway deployment config
├── railway.toml             # Railway settings
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                #
