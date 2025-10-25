# 🚀 Render Deployment Guide - JEE Calculus Bot

## ✅ What Was Fixed

### 1. **LaTeX Compilation** 
- Changed from `texlive-full` (5GB) to minimal packages
- Switched from `xelatex` to `pdflatex` (more reliable)
- Increased timeout to 120 seconds
- Better error logging

### 2. **Gemini API Quota**
- Added automatic API key rotation
- Handles 429 errors gracefully
- Supports up to 5 API keys = 250 requests/day

### 3. **Telegram Markdown Errors**
- Escaped all special characters in error messages
- Uses MarkdownV2 format properly

### 4. **Render Port Issue**
- Added `render.yaml` configured as **Background Worker**
- No port binding required

---

## 📝 Step-by-Step Deployment

### **Step 1: Get Your API Keys**

#### A. Telegram Bot Token
1. Open Telegram, search for `@BotFather`
2. Send `/newbot`
3. Follow prompts to create bot
4. **Copy the token** (format: `1234567890:ABCdef...`)

#### B. Google Gemini API Keys (Get 5 keys!)
1. Go to https://aistudio.google.com/app/apikey
2. Click "Get API Key" → "Create API key"
3. Repeat **5 times** to get 5 keys
4. Each key = 50 requests/day = **250 total/day**

---

### **Step 2: Prepare Your Files**

Replace these files in your project:

1. ✅ `Dockerfile` - Fixed LaTeX installation
2. ✅ `bot.py` - Fixed error message escaping
3. ✅ `calculus_solver.py` - Fixed API rotation
4. ✅ `pdf_generator.py` - Fixed pdflatex compilation
5. ✅ `render.yaml` - NEW file for Render config
6. ✅ `.env.example` - Template for environment variables
7. ✅ `.gitignore` - Git ignore rules

---

### **Step 3: Test Locally (Optional but Recommended)**

```bash
# Install dependencies
pip install -r requirements.txt

# Install LaTeX (if testing locally)
# Ubuntu/Debian:
sudo apt-get install texlive-latex-base texlive-latex-extra

# macOS:
brew install --cask basictex

# Create .env file
cp .env.example .env
nano .env  # Add your API keys

# Run bot
python bot.py
```

Test with a simple calculus problem image.

---

### **Step 4: Push to GitHub**

```bash
git init
git add .
git commit -m "Fixed: LaTeX, API rotation, Render deployment"
git branch -M main
git remote add origin https://github.com/yourusername/jee-calculus-bot.git
git push -u origin main
```

---

### **Step 5: Deploy on Render**

#### Option A: Using render.yaml (Recommended)

1. Go to https://render.com/
2. Sign in with GitHub
3. Click **"New" → "Blueprint"**
4. Connect your `jee-calculus-bot` repository
5. Render will detect `render.yaml` automatically
6. Click **"Apply"**

#### Option B: Manual Setup

1. Go to https://render.com/
2. Click **"New" → "Background Worker"** (NOT Web Service!)
3. Connect your repository
4. Settings:
   - **Name**: `jee-calculus-bot`
   - **Environment**: `Docker`
   - **Docker Build Context Path**: `./`
   - **Dockerfile Path**: `./Dockerfile`
   - **Plan**: Free

---

### **Step 6: Add Environment Variables**

In Render dashboard:

1. Go to your service → **"Environment"** tab
2. Click **"Add Environment Variable"**
3. Add each variable:

```
TELEGRAM_BOT_TOKEN = your_telegram_token_here
GEMINI_API_KEY_1 = your_gemini_key_1
GEMINI_API_KEY_2 = your_gemini_key_2
GEMINI_API_KEY_3 = your_gemini_key_3
GEMINI_API_KEY_4 = your_gemini_key_4
GEMINI_API_KEY_5 = your_gemini_key_5
```

4. Click **"Save Changes"**

---

### **Step 7: Deploy & Monitor**

1. Render will automatically build and deploy
2. **Build time**: 5-8 minutes (LaTeX installation)
3. Check logs:
   - Go to **"Logs"** tab
   - Look for: `✅ Loaded 5 Gemini API key(s)`
   - Look for: `🚀 JEE Calculus Bot starting...`

**Expected logs:**
```
✅ Loaded 5 Gemini API key(s)
✅ Knowledge base loaded
🚀 JEE Calculus Bot starting...
```

---

### **Step 8: Test Your Bot**

1. Open Telegram
2. Search for your bot (username you created)
3. Send `/start`
4. Send a calculus problem image
5. Wait 30-60 seconds
6. Receive PDF solution! 📄

---

## 🔧 Troubleshooting

### Issue: "LaTeX compilation failed"

**Check logs for:**
```
pdflatex not found
```

**Solution:**
- Verify Dockerfile has correct LaTeX packages
- Redeploy from scratch

---

### Issue: "Quota exceeded"

**Logs show:**
```
429 quota exceeded
```

**Solutions:**
1. Add more Gemini API keys (up to 5)
2. Wait 24 hours for quota reset
3. Each key resets daily at midnight UTC

---

### Issue: "Port scan timeout"

**This is NORMAL for background workers!**

Render shows this warning but **ignores it** for Background Workers. Your bot will work fine.

---

### Issue: Bot doesn't respond

**Check:**
1. Logs show bot started: `🚀 JEE Calculus Bot starting...`
2. Environment variables are set correctly
3. Telegram token is valid (test with @BotFather)
4. At least 1 Gemini API key is valid

---

## 📊 Monitoring

### Check Bot Status

```bash
# In Render dashboard:
1. Go to "Logs" tab
2. Look for errors
3. Check "Metrics" for memory/CPU usage
```

### Expected Performance

- **Build time**: 5-8 minutes
- **Response time**: 30-60 seconds per problem
- **Memory usage**: 150-300 MB
- **Daily capacity**: 250 problems (with 5 API keys)

---

## 🎯 Next Steps

1. ✅ Bot is running
2. Test with 10-20 different problems
3. Monitor logs for errors
4. Add more API keys if needed
5. Share with JEE students! 🚀

---

## 📧 Support

If issues persist:
1. Check Render logs
2. Verify all environment variables
3. Test locally first
4. Check GitHub repo for updates

**Your bot should now be working perfectly on Render! 🎉**
