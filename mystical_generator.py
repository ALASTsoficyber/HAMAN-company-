import random
import numpy as np

class MysticalTextGenerator:
    def __init__(self):
        self.heart_rate_zones = {
            'calm': (60, 70),      # Stillness and Annihilation
            'normal': (71, 85),    # Worship
            'excited': (86, 100)   # Passion and Spiritual Journey
        }
        
        # Database of mystical texts
        self.mystical_templates = {
            'calm': [
                "In the silence of heart, I glimpsed the Truth...",
                "My existence dissolved in the endless ocean...",
                "A silence where the voice of Truth resonates...",
                "I became a particle in the radiant sun of Reality..."
            ],
            'normal': [
                "My heart finds peace in remembering You...",
                "With every breath, I chant Your name...",
                "My worship is beholding Your face...",
                "I am a candle lit by Your beauty's light..."
            ],
            'excited': [
                "The passion for union set my heart ablaze...",
                "In seeking You, I left the world behind...",
                "The spiritual journey begins, O guide of the path...",
                "Your love ignited like fire in my chest..."
            ]
        }
    
    def get_heart_rate_zone(self, heart_rate):
        for zone, (min_hr, max_hr) in self.heart_rate_zones.items():
            if min_hr <= heart_rate <= max_hr:
                return zone
        return 'normal'
    
    def generate_text(self, heart_rate):
        zone = self.get_heart_rate_zone(heart_rate)
        template = random.choice(self.mystical_templates[zone])
        
        # Add random elements for variety
        adjectives = ['pure', 'luminous', 'sacred', 'divine', 'celestial']
        names = ['Truth', 'Beloved', 'Companion', 'God', 'Loved One']
        
        text = template
        if random.random() > 0.5:
            text = text.replace('Truth', f'{random.choice(adjectives)} Truth')
        
        return {
            'text': text,
            'zone': zone,
            'heart_rate': heart_rate
        }

# Usage
generator = MysticalTextGenerator()

# Simulate heart rate data
for i in range(5):
    simulated_heart_rate = random.randint(60, 100)
    result = generator.generate_text(simulated_heart_rate)
    print(f"Heart Rate: {result['heart_rate']} - State: {result['zone']}")
    print(f"Generated Text: {result['text']}")
    print("-" * 50)