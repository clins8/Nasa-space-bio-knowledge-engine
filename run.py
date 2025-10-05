from app import app
import os

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('utils', exist_ok=True)
    
    print("🚀 Nova Lunox Space Biology Knowledge Engine Starting...")
    print("🌌 Available at: http://localhost:5000")
    print("📊 Features: AI Summarization, Knowledge Graphs, Interactive Dashboard")
    
    app.run(host='0.0.0.0', port=5000, debug=True)