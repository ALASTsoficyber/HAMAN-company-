import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class NeuroFocusAssistant:
    def __init__(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # First plot: Brain waves
        self.ax1.set_title('Brain Waves - Focus Monitoring')
        self.ax1.set_xlabel('Time (seconds)')
        self.ax1.set_ylabel('Amplitude')
        self.ax1.set_ylim(-2, 2)
        
        self.time = np.linspace(0, 10, 100)
        self.beta_wave, = self.ax1.plot([], [], 'b-', label='Beta (Focus)')
        self.theta_wave, = self.ax1.plot([], [], 'r-', label='Theta (Distraction)')
        self.ax1.legend()
        
        # Second plot: Focus index
        self.ax2.set_title('Focus Index')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Focus Level')
        self.ax2.set_ylim(0, 100)
        
        self.focus_data = []
        self.focus_line, = self.ax2.plot([], [], 'g-', linewidth=2)
        
        self.concentration_threshold = 60
        
    def simulate_brain_waves(self):
        """Simulate brain waves"""
        t = time.time()
        
        # Simulate beta wave (focus)
        beta = 0.5 * np.sin(2 * np.pi * 20 * t) + 0.3 * np.random.randn()
        
        # Simulate theta wave (distraction)
        theta = 0.8 * np.sin(2 * np.pi * 6 * t) + 0.5 * np.random.randn()
        
        return beta, theta
    
    def calculate_focus_index(self, beta, theta):
        """Calculate focus index"""
        beta_power = np.abs(beta)
        theta_power = np.abs(theta)
        
        if theta_power == 0:
            return 100
        
        focus_index = 100 * (beta_power / (beta_power + theta_power))
        return np.clip(focus_index, 0, 100)
    
    def update(self, frame):
        # Simulate new data
        beta, theta = self.simulate_brain_waves()
        focus_index = self.calculate_focus_index(beta, theta)
        
        # Update wave plot
        current_time = time.time()
        self.beta_wave.set_data([current_time], [beta])
        self.theta_wave.set_data([current_time], [theta])
        
        # Update focus index
        self.focus_data.append(focus_index)
        if len(self.focus_data) > 50:
            self.focus_data.pop(0)
        
        times = list(range(len(self.focus_data)))
        self.focus_line.set_data(times, self.focus_data)
        
        self.ax2.set_xlim(0, max(50, len(self.focus_data)))
        
        # Audio/visual feedback
        if focus_index > self.concentration_threshold:
            plt.suptitle('✅ Focus Mode Active - Continue!', fontsize=14, color='green')
        else:
            plt.suptitle('❌ Distraction Detected - Take Deep Breath', fontsize=14, color='red')
        
        return self.beta_wave, self.theta_wave, self.focus_line

# Run system
assistant = NeuroFocusAssistant()
ani = FuncAnimation(assistant.fig, assistant.update, interval=200, blit=True)
plt.tight_layout()
plt.show()