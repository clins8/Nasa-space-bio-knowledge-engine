# Nasa-space-bio-knowledge-engine
 
## 🌌 Overview

The Space Biology Knowledge Engine is a dynamic web application developed for the NASA Space Apps Challenge 2025 by Team Nova Lunox. This platform helps scientists, students, and space enthusiasts explore and understand NASA's bioscience experiments conducted in space environments like the ISS, Moon, and Mars simulations.

### 🎯 Mission
To democratize access to space biology research through AI-powered summarization, interactive visualizations, and intuitive data exploration tools.

## ✨ Features

### 🔍 Intelligent Data Exploration
- **AI-Powered Summarization**: Automatically generates concise summaries of complex research abstracts.
- **Advanced Filtering**: Filter by organism type, space environment, and time period.
- **Fuzzy Search**: Find relevant studies with intelligent text matching.

### 📊 Interactive Visualizations
- **Knowledge Graphs**: Visualize relationships between experiments, organisms, and findings.
- **Dynamic Charts**: Interactive plots showing research trends and distributions.
- **Timeline Analysis**: Track space biology research evolution over time.

### 🎨 Immersive Experience
- **Cosmic UI**: Dark theme with nebula backgrounds and starfield animations.
- **Responsive Design**: Works seamlessly on desktop and mobile devices.
- **Futuristic Interface**: Space-themed components with smooth animations.

### 📈 AI Insights
- **Trend Analysis**: ML-powered insights into space biology patterns.
- **Random Discovery**: Generate random fascinating facts from NASA research.
- **PDF Reports**: Export customized research summaries.

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python Flask |
| **Frontend** | HTML5, CSS3, JavaScript |
| **AI/ML** | HuggingFace Transformers, PyTorch |
| **Visualization** | Plotly, D3.js, NetworkX |
| **Styling** | Custom CSS with Space Theme |
| **Data Processing** | Pandas, NumPy |
| **PDF Generation** | ReportLab |

## 📁 Project Structure

```
/NovaLunox/
├── app.py
├── requirements.txt
├── run.py
├── /static
│   ├── css/
│   │   ├── style.css
│   │   └── stars.css
│   ├── js/
│   │   ├── script.js
│   │   ├── charts.js
│   │   └── graph.js
│   └── images/
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── graph.html
│   ├── insights.html
│   └── report.html
├── /data
│   ├── nasa_bio_sample.csv
│   └── sample_data.json
├── /utils
│   ├── data_loader.py
│   ├── summarizer.py
│   └── graph_builder.py
└── /reports

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation & Running on Replit

#### Method 1: One-Click Setup (Recommended)
1. **Fork this Replit template** (if available)
2. **Wait for dependencies to install automatically**
3. **Click "Run"** - the app will start on port 5000

#### Method 2: Manual Setup
1. **Create a new Python Repl**
2. **Upload all project files** maintaining the folder structure
3. **Open Shell** and install dependencies:
   ```bash
   pip install -r requirements.txt
````

4. **Run the application**:

   ```bash
   python run.py
   ```
5. **Open the web view** to see your application

### Local Development Setup

1. **Clone or download the project**
2. **Navigate to project directory**:

   ```bash
   cd NovaLunox
   ```
3. **Create virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
5. **Run the application**:

   ```bash
   python run.py
   ```
6. **Open your browser** and navigate to:

   ```
   http://localhost:5000
   ```

## 📊 Sample Dataset

The application includes a curated sample dataset of NASA space biology experiments featuring:

* **Human studies**: Bone density, cardiovascular changes, muscle atrophy
* **Plant research**: Growth in lunar simulant, hydroponics, genetic expression
* **Microbe experiments**: Radiation adaptation, extremophile survival
* **Multiple environments**: ISS, Lunar Analog, Mars Analog, Space Exposure

## 🎮 How to Use

1. **Explore the Dashboard** – summary stats, filters, and search
2. **Generate AI Summaries** – click "AI Summary" for concise explanations
3. **Visualize Knowledge Graphs** – interactive node-link diagrams
4. **Discover Random Facts** – click "Random Space Discovery"
5. **Generate Reports** – export PDF summaries of selected research

## 🔧 Configuration

### Environment Variables

Create a `.env` file for custom configuration:

```env
FLASK_ENV=development
HUGGINGFACE_TOKEN=your_token_here  # For enhanced AI features
```

### Custom Data Integration

Place new CSVs in `/data` with columns: `title`, `organism_type`, `environment`, `year`, `key_finding`, `abstract`. App auto-loads new datasets.

## 🐛 Troubleshooting

* **Module not found** → `pip install -r requirements.txt --force-reinstall`
* **App won’t start** → Check console for errors, ensure files are uploaded correctly
* **AI summarization not working** → Falls back to extractive summarization
* **Charts not displaying** → Check browser console and Plotly import

## 🌟 NASA Space Apps Challenge Judges

* **AI-Powered Accessibility** – makes space biology research understandable
* **Interactive Knowledge Graphs** – unique visualization of research connections
* **Cosmic UI** – immersive space-themed interface
* **Scalable Architecture** – ready for real NASA datasets

