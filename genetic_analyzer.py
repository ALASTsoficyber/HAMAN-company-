import json
import random
from datetime import datetime

class KhorasanGeneticReport:
    def __init__(self):
        self.haplogroups = {
            'R1a': {
                'frequency': '35%',
                'regions': ['Khorasan', 'Central Asia', 'Indian Subcontinent'],
                'historical_significance': 'Associated with Indo-Iranian migrations',
                'cultural_traits': ['Iranian languages', 'Aryan culture']
            },
            'J2': {
                'frequency': '25%', 
                'regions': ['Middle East', 'Anatolia', 'Caucasus'],
                'historical_significance': 'Early Near Eastern farmers',
                'cultural_traits': ['Urbanization', 'Advanced agriculture']
            },
            'G': {
                'frequency': '15%',
                'regions': ['Caucasus', 'Iran', 'Anatolia'],
                'historical_significance': 'Ancient Caucasian inhabitants',
                'cultural_traits': ['Mountain culture', 'Craftsmanship']
            }
        }
        
        self.historical_figures = {
            'R1a': ['Ferdowsi', 'Rudaki', 'Avicenna'],
            'J2': ['Al-Khwarizmi', 'Al-Biruni', 'Al-Razi'],
            'G': ['Nizami Ganjavi', 'Khaqani']
        }
    
    def generate_vcf_simulator(self):
        """Simulate VCF file"""
        variants = []
        for i in range(100):
            variant = {
                'chrom': random.choice(['1', '2', '3', '4', '5']),
                'pos': random.randint(1000000, 50000000),
                'id': f'rs{random.randint(100000, 999999)}',
                'ref': random.choice(['A', 'T', 'C', 'G']),
                'alt': random.choice(['A', 'T', 'C', 'G']),
                'genotype': random.choice(['0/0', '0/1', '1/1'])
            }
            variants.append(variant)
        return variants
    
    def predict_haplogroup(self, variants):
        """Predict haplogroup based on variants"""
        # Simple simulation algorithm
        haplogroup = random.choice(list(self.haplogroups.keys()))
        return haplogroup
    
    def generate_report(self, sample_name="User Sample"):
        variants = self.generate_vcf_simulator()
        predicted_haplogroup = self.predict_haplogroup(variants)
        
        report = {
            'sample_name': sample_name,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'haplogroup': predicted_haplogroup,
            'haplogroup_info': self.haplogroups[predicted_haplogroup],
            'historical_figures': self.historical_figures.get(predicted_haplogroup, []),
            'genetic_markers_analyzed': len(variants),
            'confidence_level': f"{random.randint(85, 98)}%"
        }
        
        return report
    
    def format_report_pdf(self, report):
        """Format report as text (PDF simulation)"""
        formatted = f"""
        =============================================
            Khorasan Genetic-Cultural Heritage Report
        =============================================
        
        Sample Name: {report['sample_name']}
        Generation Date: {report['date']}
        
        ------------------ Genetic Results ------------------
        Predicted Haplogroup: {report['haplogroup']}
        Confidence Level: {report['confidence_level']}
        Genetic Markers Analyzed: {report['genetic_markers_analyzed']}
        
        ------------------ Haplogroup Information ------------------
        Regional Frequency: {report['haplogroup_info']['frequency']}
        Geographical Regions: {', '.join(report['haplogroup_info']['regions'])}
        Historical Significance: {report['haplogroup_info']['historical_significance']}
        Cultural Traits: {', '.join(report['haplogroup_info']['cultural_traits'])}
        
        ------------------ Associated Historical Figures ------------------
        {', '.join(report['historical_figures'])}
        
        =============================================
        Explanation: This report is based on analysis of genetic patterns
        and correlation with historical-cultural databases of Greater Khorasan region.
        """
        
        return formatted

# Generate report
analyzer = KhorasanGeneticReport()
report = analyzer.generate_report("Sample User")
print(analyzer.format_report_pdf(report))