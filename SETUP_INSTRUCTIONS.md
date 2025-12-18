# 🤖 Physical AI & Humanoid Robotics Textbook - Setup Guide

## 📋 Project Overview
This project is a complete textbook for teaching **Physical AI & Humanoid Robotics**, created for the Panaversity Hackathon. It includes:
- 📚 4 comprehensive course modules
- 🤖 RAG-powered AI chatbot for interactive learning
- 👤 User authentication & personalization
- 🌐 Multi-language support (Urdu translation)

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ramais123/physical-ai-textbook.git
cd physical-ai-textbook/spec-kit-plus

Step 2: Install Dependencies
bash
pip install -r requirements.txt

Step 3: Configure API Keys
Get your Gemini API key from: https://ai.google.dev

Create .env file in spec-kit-plus/ folder:

env
# Gemini API for book generation
GEMINI_API_KEY=your_actual_gemini_api_key_here

# For RAG Chatbot (Optional)
QDRANT_API_KEY=your_qdrant_key_here
⚠️ IMPORTANT: Never commit .env to GitHub!

Step 4: Generate Textbook Content
bash
# Generate all 4 modules
python spec_kit.py --input module1_spec.md --output physical-ai-book/docs/module1-ros2.md
python spec_kit.py --input module2_spec.md --output physical-ai-book/docs/module2-gazebo.md
python spec_kit.py --input module3_spec.md --output physical-ai-book/docs/module3-isaac.md
python spec_kit.py --input module4_spec.md --output physical-ai-book/docs/module4-vla.md

Step 5: Deploy the Book
bash
cd physical-ai-book
npm install
npm run build
npm run deploy

