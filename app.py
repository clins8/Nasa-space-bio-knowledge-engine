from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import json
import os
from utils.data_loader import DataLoader
from utils.summarizer import TextSummarizer
from utils.graph_builder import KnowledgeGraph
import plotly.express as px
import plotly.utils
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'

# Initialize components
data_loader = DataLoader()
summarizer = TextSummarizer()
knowledge_graph = KnowledgeGraph()

# Load sample data
SAMPLE_DATA_PATH = 'data/nasa_bio_sample.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    summary_stats = {
        'total_studies': len(df),
        'human_studies': len(df[df['organism_type'] == 'Human']),
        'plant_studies': len(df[df['organism_type'] == 'Plant']),
        'microbe_studies': len(df[df['organism_type'] == 'Microbe'])
    }
    return render_template('dashboard.html', summary=summary_stats)

@app.route('/api/data')
def get_data():
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    return jsonify(df.to_dict('records'))

@app.route('/api/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')
    summary = summarizer.summarize(text)
    return jsonify({'summary': summary})

@app.route('/api/graph-data')
def get_graph_data():
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    graph_data = knowledge_graph.build_graph(df)
    return jsonify(graph_data)

@app.route('/api/insights')
def get_insights():
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    
    # Generate basic insights
    insights = {
        'top_organisms': df['organism_type'].value_counts().to_dict(),
        'environment_distribution': df['environment'].value_counts().to_dict(),
        'yearly_trends': df['year'].value_counts().sort_index().to_dict(),
        'common_findings': df['key_finding'].value_counts().head(5).to_dict()
    }
    
    return jsonify(insights)

@app.route('/api/filter-data', methods=['POST'])
def filter_data():
    filters = request.json
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    
    # Apply filters
    if filters.get('organism_type'):
        df = df[df['organism_type'] == filters['organism_type']]
    if filters.get('environment'):
        df = df[df['environment'] == filters['environment']]
    if filters.get('year_range'):
        min_year, max_year = filters['year_range']
        df = df[(df['year'] >= min_year) & (df['year'] <= max_year)]
    
    return jsonify(df.to_dict('records'))

@app.route('/generate-report', methods=['POST'])
def generate_report():
    from utils.report_generator import generate_pdf_report
    data = request.json
    pdf_buffer = generate_pdf_report(data)
    
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name='nova_lunox_space_biology_report.pdf',
        mimetype='application/pdf'
    )

@app.route('/random-fact')
def random_fact():
    df = data_loader.load_data(SAMPLE_DATA_PATH)
    random_study = df.sample(1).iloc[0]
    
    fact = f"In {random_study['year']}, NASA found that {random_study['organism_type'].lower()}s " \
           f"in {random_study['environment'].lower()} showed: {random_study['key_finding'].lower()}"
    
    return jsonify({'fact': fact})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)