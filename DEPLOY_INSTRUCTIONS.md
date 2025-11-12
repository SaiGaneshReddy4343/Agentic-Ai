# 🚀 Deploy Your Student Wellbeing AI - Get Public Link

## Step 1: Create GitHub Repository
1. Go to [github.com](https://github.com) and sign in
2. Click "New repository" (green button)
3. Repository name: `student-wellbeing-ai`
4. Make it **Public**
5. Don't initialize with README (we already have files)
6. Click "Create repository"

## Step 2: Push Your Code
Copy and run these commands in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-wellbeing-ai.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Deploy on Streamlit Cloud (FREE!)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Click "New app"
4. Select your repository: `student-wellbeing-ai`
5. Main file path: `app.py`
6. Click "Advanced settings"
7. Add this secret:
   - Key: `GOOGLE_API_KEY`
   - Value: `AIzaSyBPjZ1QkwhgfVpvpVQOXaZNn8vcrUAAPpw`
8. Click "Deploy!"

## Step 4: Get Your Public Link
After deployment (2-3 minutes), you'll get a link like:
`https://YOUR_USERNAME-student-wellbeing-ai-app-xyz.streamlit.app`

This link will work on:
✅ Any laptop/computer
✅ Any mobile phone
✅ Any tablet
✅ From anywhere in the world

## Alternative: Railway (Also Free)
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable: `GOOGLE_API_KEY`
6. Deploy!

Your app will be live with a public URL in minutes!