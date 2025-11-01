import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class ExistenceMapper:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(0, 10)  # Existence spectrum: Matter (0) to Spirit (10)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlabel('Existence Spectrum (Matter ← Spirit)')
        self.ax.set_ylabel('Presence Intensity')
        self.ax.set_title('Existence Mapper - NeuroSina Project')
        
        # Different existence levels
        self.existence_points = ['Matter', 'Psyche', 'Intellect', 'Spirit', 'Truth']
        self.ax.set_xticks([0, 2.5, 5, 7.5, 10])
        self.ax.set_xticklabels(self.existence_points)
        
        self.position, = self.ax.plot([5], [0.5], 'ro', markersize=20, alpha=0.7)
        
    def simulate_eeg_data(self):
        """Simulate EEG data"""
        # In real implementation, use brainflow library here
        entropy = np.random.uniform(0, 1)  # Simulate entropy
        gamma_power = np.random.uniform(0.1, 0.9)  # Simulate gamma power
        
        # Map to existence spectrum
        existence_level = 2 + 8 * gamma_power - 3 * entropy
        existence_level = np.clip(existence_level, 0, 10)
        
        return existence_level, gamma_power
    
    def update(self, frame):
        existence_level, intensity = self.simulate_eeg_data()
        
        # Update position
        self.position.set_data([existence_level], [intensity])
        
        # Change color based on existence level
        if existence_level < 3:
            color = 'brown'  # Matter
        elif existence_level < 6:
            color = 'green'  # Psyche
        elif existence_level < 8:
            color = 'blue'   # Intellect
        else:
            color = 'gold'   # Spirit/Truth
            
        self.position.set_color(color)
        
        return self.position,

# Run animation
mapper = ExistenceMapper()
ani = FuncAnimation(mapper.fig, mapper.update, frames=100, interval=500, blit=True)
plt.show()