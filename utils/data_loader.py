import pandas as pd
import json

class DataLoader:
    def __init__(self):
        self.sample_data = None
    
    def load_data(self, file_path):
        """Load NASA biology data from CSV or JSON"""
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                df = pd.read_json(file_path)
            else:
                raise ValueError("Unsupported file format")
            
            # Ensure required columns exist
            required_columns = ['title', 'organism_type', 'environment', 'year', 'key_finding', 'abstract']
            for col in required_columns:
                if col not in df.columns:
                    df[col] = f"Sample {col}"
            
            return df
        
        except Exception as e:
            print(f"Error loading data: {e}")
            return self._create_sample_data()
    
    def _create_sample_data(self):
        """Create sample NASA biology data"""
        sample_data = [
            {
                'title': 'Microgravity Effects on Human Bone Density',
                'organism_type': 'Human',
                'environment': 'ISS',
                'year': 2020,
                'key_finding': 'Bone density decreases 1-2% per month in microgravity',
                'abstract': 'Study of astronauts showing significant bone density loss during long-duration space missions.'
            },
            {
                'title': 'Plant Growth in Lunar Simulant',
                'organism_type': 'Plant',
                'environment': 'Lunar Analog',
                'year': 2021,
                'key_finding': 'Plants can grow in lunar regolith with nutrient supplements',
                'abstract': 'Experiments demonstrating plant viability in simulated lunar soil conditions.'
            },
            {
                'title': 'Microbial Adaptation to Space Radiation',
                'organism_type': 'Microbe',
                'environment': 'ISS',
                'year': 2019,
                'key_finding': 'Microbes develop enhanced DNA repair mechanisms',
                'abstract': 'Research on bacterial adaptation to increased cosmic radiation exposure.'
            },
            {
                'title': 'Cardiovascular Changes in Microgravity',
                'organism_type': 'Human',
                'environment': 'ISS',
                'year': 2022,
                'key_finding': 'Cardiac output increases initially, then normalizes',
                'abstract': 'Analysis of astronaut cardiovascular adaptation to weightlessness.'
            },
            {
                'title': 'Algae Biofuel Production in Space',
                'organism_type': 'Plant',
                'environment': 'Space Station',
                'year': 2023,
                'key_finding': 'Algae growth rates increase in microgravity conditions',
                'abstract': 'Investigation of algae-based biofuel production for sustainable space missions.'
            }
        ]
        return pd.DataFrame(sample_data)