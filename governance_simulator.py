import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

class NeuroGovernanceSimulator:
    def __init__(self):
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        plt.suptitle('Neuro-Governance Simulator Dashboard', fontsize=16, fontweight='bold')
        
        # Governance scenario
        self.projects = ['Cultural Project A', 'Cultural Project B', 'Cultural Project C']
        self.budget_total = 1000
        self.current_votes = {project: 0 for project in self.projects}
        
        # Simulate 5 users
        self.users = [f'User {i+1}' for i in range(5)]
        self.user_states = {}
        
        # Decision history
        self.decision_history = []
        self.neural_index_history = []
        
    def simulate_user_neural_state(self, user):
        """Simulate user neural state"""
        stress = np.random.uniform(0, 1)
        focus = np.random.uniform(0, 1)
        coherence = np.random.uniform(0, 1)
        
        return {
            'stress': stress,
            'focus': focus, 
            'coherence': coherence,
            'neural_index': focus * coherence * (1 - stress)  # Combined neural index
        }
    
    def calculate_collective_neural_index(self):
        """Calculate collective neural index"""
        if not self.user_states:
            return 0
        
        neural_indices = [state['neural_index'] for state in self.user_states.values()]
        return np.mean(neural_indices)
    
    def simulate_voting(self):
        """Simulate voting based on neural state"""
        self.current_votes = {project: 0 for project in self.projects}
        self.user_states = {}
        
        for user in self.users:
            # Simulate user neural state
            neural_state = self.simulate_user_neural_state(user)
            self.user_states[user] = neural_state
            
            # Voting based on neural state
            if neural_state['stress'] > 0.7:
                # High-stress users vote conservatively
                vote = self.projects[0]  # Known project
            elif neural_state['focus'] > 0.6:
                # Focused users vote logically
                vote = self.projects[1]  # Moderate project
            else:
                # Other users vote randomly
                vote = np.random.choice(self.projects)
            
            self.current_votes[vote] += 1
        
        return self.current_votes
    
    def analyze_decision_pattern(self, votes, neural_index):
        """Analyze decision pattern"""
        winning_project = max(votes, key=votes.get)
        
        if neural_index > 0.7:
            decision_quality = "Excellent - Decision based on neural harmony"
        elif neural_index > 0.5:
            decision_quality = "Good - Logical balance"
        else:
            decision_quality = "Conservative - Stress influenced"
        
        return winning_project, decision_quality
    
    def update_dashboard(self, frame):
        # Clear plots
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.clear()
        
        # Simulate new voting
        votes = self.simulate_voting()
        neural_index = self.calculate_collective_neural_index()
        
        # Analyze decision
        winning_project, decision_quality = self.analyze_decision_pattern(votes, neural_index)
        
        # Save history
        self.decision_history.append(winning_project)
        self.neural_index_history.append(neural_index)
        
        # Plot 1: Voting results
        self.ax1.bar(votes.keys(), votes.values(), color=['red', 'blue', 'green'])
        self.ax1.set_title('Voting Results')
        self.ax1.set_ylabel('Vote Count')
        
        # Plot 2: Collective neural index
        self.ax2.plot(self.neural_index_history, 'o-', linewidth=2, markersize=8)
        self.ax2.set_title('Collective Neural Index')
        self.ax2.set_ylabel('Neural Coherence Level')
        self.ax2.set_ylim(0, 1)
        
        # Plot 3: User neural states
        user_names = list(self.user_states.keys())
        stress_levels = [state['stress'] for state in self.user_states.values()]
        focus_levels = [state['focus'] for state in self.user_states.values()]
        
        x = range(len(user_names))
        width = 0.35
        
        self.ax3.bar([i - width/2 for i in x], stress_levels, width, label='Stress', color='red', alpha=0.7)
        self.ax3.bar([i + width/2 for i in x], focus_levels, width, label='Focus', color='blue', alpha=0.7)
        self.ax3.set_title('User Neural States')
        self.ax3.set_xticks(x)
        self.ax3.set_xticklabels(user_names, rotation=45)
        self.ax3.legend()
        
        # Plot 4: Decision analysis
        decision_text = f"""
        Winning Project: {winning_project}
        Decision Quality: {decision_quality}
        Neural Index: {neural_index:.2f}
        
        Analysis:
        - Collective Stress: {np.mean([s['stress'] for s in self.user_states.values()]):.2f}
        - Collective Focus: {np.mean([s['focus'] for s in self.user_states.values()]):.2f}
        - Coherence: {np.mean([s['coherence'] for s in self.user_states.values()]):.2f}
        """
        
        self.ax4.text(0.1, 0.5, decision_text, fontsize=12, verticalalignment='center')
        self.ax4.set_title('Decision Analysis')
        self.ax4.axis('off')
        
        plt.tight_layout()
        
        return []

# Run simulator
simulator = NeuroGovernanceSimulator()
ani = FuncAnimation(simulator.fig, simulator.update_dashboard, interval=2000, blit=False)
plt.show()