import networkx as nx
import pandas as pd
import json

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()
    
    def build_graph(self, df):
        """Build knowledge graph from NASA biology data"""
        G = nx.Graph()
        
        # Add nodes and edges based on relationships
        for _, row in df.iterrows():
            # Add experiment node
            exp_id = row['title'].replace(' ', '_')
            G.add_node(exp_id, type='experiment', label=row['title'], year=row['year'])
            
            # Add organism node
            org_id = f"org_{row['organism_type']}"
            G.add_node(org_id, type='organism', label=row['organism_type'])
            
            # Add environment node
            env_id = f"env_{row['environment']}"
            G.add_node(env_id, type='environment', label=row['environment'])
            
            # Add finding node
            finding_id = f"find_{hash(row['key_finding']) % 10000}"
            G.add_node(finding_id, type='finding', label=row['key_finding'])
            
            # Connect nodes
            G.add_edge(exp_id, org_id, relationship='studies')
            G.add_edge(exp_id, env_id, relationship='conducted_in')
            G.add_edge(exp_id, finding_id, relationship='discovered')
        
        return self._serialize_graph(G)
    
    def _serialize_graph(self, G):
        """Convert NetworkX graph to D3.js compatible format"""
        nodes = []
        for node_id, node_data in G.nodes(data=True):
            nodes.append({
                'id': node_id,
                'type': node_data.get('type', 'unknown'),
                'label': node_data.get('label', node_id),
                'group': node_data.get('type', 'unknown')
            })
        
        links = []
        for source, target, edge_data in G.edges(data=True):
            links.append({
                'source': source,
                'target': target,
                'relationship': edge_data.get('relationship', 'related_to')
            })
        
        return {'nodes': nodes, 'links': links}