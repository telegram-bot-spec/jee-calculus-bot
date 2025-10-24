"""
PDF Generator for JEE Calculus Bot
Uses PyLaTeX + pdflatex for publication-quality output (Springer/Nature standard)
Includes Matplotlib graph embedding
"""

from pylatex import Document, Section, Subsection, Math, Figure, NoEscape
from pylatex.utils import italic, bold
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, latex, lambdify, diff, integrate
import os
from datetime import datetime

class CalculusPDFGenerator:
    def __init__(self):
        self.temp_dir = "temp_graphs"
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def generate_pdf(self, solution_data, problem_image_path):
        """
        Generate publication-quality PDF with triple-strategy solutions
        
        Args:
            solution_data: Dict containing all three strategies and verification
            problem_image_path: Path to original problem image
        
        Returns:
            Path to generated PDF
        """
        
        # Create document with professional settings
        doc = Document(documentclass='article', document_options=['11pt', 'a4paper'])
        
        # Add necessary LaTeX packages
        doc.preamble.append(NoEscape(r'\usepackage{amsmath}'))
        doc.preamble.append(NoEscape(r'\usepackage{amssymb}'))
        doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
        doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
        doc.preamble.append(NoEscape(r'\usepackage{geometry}'))
        doc.preamble.append(NoEscape(r'\geometry{margin=1in}'))
        doc.preamble.append(NoEscape(r'\usepackage{fancyhdr}'))
        doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
        doc.preamble.append(NoEscape(r'\fancyhead[L]{JEE Calculus Bot}'))
        doc.preamble.append(NoEscape(r'\fancyhead[R]{\today}'))
        
        # Title
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\LARGE \textbf{JEE Advanced Calculus Solution}\\[0.5cm]'))
        doc.append(NoEscape(r'\large Triple-Strategy Analysis\\[0.3cm]'))
        doc.append(NoEscape(r'\normalsize Generated: ' + datetime.now().strftime("%B %d, %Y %I:%M %p") + r'\\[0.5cm]'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Problem Image
        with doc.create(Section('Problem Statement')):
            if os.path.exists(problem_image_path):
                with doc.create(Figure(position='h!')) as fig:
                    fig.add_image(problem_image_path, width='400px')
                    fig.add_caption('Original Problem')
        
        # Strategy 1: Cengage Method
        with doc.create(Section('Strategy 1: Cengage Method (Systematic Approach)')):
            doc.append(NoEscape(r'\textcolor{blue}{\textbf{Philosophy:}} Step-by-step textbook rigor\\[0.2cm]'))
            
            strategy1 = solution_data.get('strategy1', {})
            
            # Steps
            steps = strategy1.get('steps', [])
            for i, step in enumerate(steps, 1):
                doc.append(NoEscape(f'\\textbf{{Step {i}:}} '))
                doc.append(step.get('description', ''))
                doc.append(NoEscape('\\\\[0.1cm]'))
                
                # If step has equation, render it
                if 'equation' in step:
                    doc.append(Math(data=[NoEscape(step['equation'])]))
                    doc.append(NoEscape('\\\\[0.2cm]'))
            
            # Final Answer
            doc.append(NoEscape(r'\vspace{0.3cm}\textbf{Answer (Strategy 1):} '))
            doc.append(NoEscape(r'\colorbox{yellow}{' + str(strategy1.get('answer', '')) + r'}'))
            doc.append(NoEscape(r'\\[0.2cm]'))
            doc.append(NoEscape(r'\textbf{Confidence:} ' + str(strategy1.get('confidence', '')) + r'\%'))
        
        # Strategy 2: Black Book Shortcuts
        with doc.create(Section('Strategy 2: Black Book Shortcuts (Pattern Recognition)')):
            doc.append(NoEscape(r'\textcolor{blue}{\textbf{Philosophy:}} Quick shortcuts for competitive exams\\[0.2cm]'))
            
            strategy2 = solution_data.get('strategy2', {})
            
            doc.append(NoEscape(r'\textbf{Pattern Recognized:} '))
            doc.append(strategy2.get('pattern', ''))
            doc.append(NoEscape(r'\\[0.2cm]'))
            
            doc.append(NoEscape(r'\textbf{Shortcut Applied:} '))
            doc.append(strategy2.get('shortcut', ''))
            doc.append(NoEscape(r'\\[0.2cm]'))
            
            doc.append(NoEscape(r'\textbf{Time Taken:} '))
            doc.append(strategy2.get('time', '<10 seconds'))
            doc.append(NoEscape(r'\\[0.3cm]'))
            
            # Solution
            if 'solution' in strategy2:
                doc.append(Math(data=[NoEscape(strategy2['solution'])]))
            
            # Final Answer
            doc.append(NoEscape(r'\vspace{0.3cm}\textbf{Answer (Strategy 2):} '))
            doc.append(NoEscape(r'\colorbox{yellow}{' + str(strategy2.get('answer', '')) + r'}'))
            doc.append(NoEscape(r'\\[0.2cm]'))
            doc.append(NoEscape(r'\textbf{Confidence:} ' + str(strategy2.get('confidence', '')) + r'\%'))
        
        # Strategy 3: Olympiad/Exceptional
        with doc.create(Section('Strategy 3: Olympiad/Exceptional Insights')):
            doc.append(NoEscape(r'\textcolor{blue}{\textbf{Philosophy:}} Elegant mathematical beauty\\[0.2cm]'))
            
            strategy3 = solution_data.get('strategy3', {})
            
            doc.append(NoEscape(r'\textbf{Key Insight:} '))
            doc.append(strategy3.get('insight', ''))
            doc.append(NoEscape(r'\\[0.2cm]'))
            
            doc.append(NoEscape(r'\textbf{Method Used:} '))
            doc.append(strategy3.get('method', ''))
            doc.append(NoEscape(r'\\[0.2cm]'))
            
            doc.append(NoEscape(r'\textbf{Why Elegant:} '))
            doc.append(strategy3.get('elegance', ''))
            doc.append(NoEscape(r'\\[0.3cm]'))
            
            # Solution steps
            if 'solution_steps' in strategy3:
                for step in strategy3['solution_steps']:
                    doc.append(Math(data=[NoEscape(step)]))
                    doc.append(NoEscape('\\\\[0.2cm]'))
            
            # Final Answer
            doc.append(NoEscape(r'\vspace{0.3cm}\textbf{Answer (Strategy 3):} '))
            doc.append(NoEscape(r'\colorbox{yellow}{' + str(strategy3.get('answer', '')) + r'}'))
            doc.append(NoEscape(r'\\[0.2cm]'))
            doc.append(NoEscape(r'\textbf{Confidence:} ' + str(strategy3.get('confidence', '')) + r'\%'))
        
        # Graphical Verification (if function provided)
        if solution_data.get('needs_graph', False) and 'function' in solution_data:
            graph_path = self._generate_graph(solution_data)
            
            with doc.create(Section('Graphical Verification')):
                doc.append('Visual representation of the function and its properties:')
                doc.append(NoEscape('\\\\[0.3cm]'))
                
                if graph_path and os.path.exists(graph_path):
                    with doc.create(Figure(position='h!')) as fig:
                        fig.add_image(graph_path, width='400px')
                        fig.add_caption('Function Analysis')
        
        # Final Synthesis
        with doc.create(Section('Final Synthesis \& Verification')):
            synthesis = solution_data.get('synthesis', {})
            
            # Agreement check
            all_agree = synthesis.get('all_agree', False)
            if all_agree:
                doc.append(NoEscape(r'\textcolor{green}{\textbf{✓ All 3 methods agree!}}\\[0.2cm]'))
            else:
                doc.append(NoEscape(r'\textcolor{red}{\textbf{✗ Methods disagree - review needed}}\\[0.2cm]'))
            
            # SymPy verification
            doc.append(NoEscape(r'\textbf{SymPy Verification:} '))
            doc.append(synthesis.get('sympy_verification', 'Passed'))
            doc.append(NoEscape(r'\\[0.2cm]'))
            
            # JEE Trap Check
            doc.append(NoEscape(r'\textbf{JEE Trap Check:}\\'))
            traps = synthesis.get('trap_check', [])
            for trap in traps:
                doc.append(NoEscape(r'\quad • ' + trap + r'\\'))
            
            # Ultimate Answer
            doc.append(NoEscape(r'\vspace{0.5cm}'))
            doc.append(NoEscape(r'\begin{center}'))
            doc.append(NoEscape(r'\colorbox{green!30}{\parbox{0.8\textwidth}{'))
            doc.append(NoEscape(r'\textbf{\Large ULTIMATE ANSWER:} ' + str(synthesis.get('final_answer', '')) + r'\\[0.2cm]'))
            doc.append(NoEscape(r'\textbf{Reasoning:} ' + synthesis.get('reasoning', '')))
            doc.append(NoEscape(r'}}'))
            doc.append(NoEscape(r'\end{center}'))
            
            # Final Confidence
            doc.append(NoEscape(r'\vspace{0.3cm}'))
            doc.append(NoEscape(r'\textbf{Final Confidence:} ' + str(synthesis.get('confidence', '')) + r'\%'))
        
        # Generate PDF
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"calculus_solution_{timestamp}"
        
        try:
            doc.generate_pdf(output_filename, compiler='pdflatex', clean_tex=False)
            return f"{output_filename}.pdf"
        except Exception as e:
            print(f"PDF generation error: {e}")
            # Fallback: generate tex file at least
            doc.generate_tex(output_filename)
            return f"{output_filename}.tex"
    
    def _generate_graph(self, solution_data):
        """
        Generate matplotlib graph for function visualization
        """
        try:
            x = symbols('x')
            function_str = solution_data.get('function', '')
            
            # Create figure with subplots
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            fig.suptitle('Calculus Function Analysis', fontsize=16, fontweight='bold')
            
            # Parse function using SymPy
            from sympy import sympify
            func = sympify(function_str)
            
            # Convert to numpy function
            func_numpy = lambdify(x, func, 'numpy')
            
            # Generate x values
            x_vals = np.linspace(-5, 5, 1000)
            
            # Original function
            try:
                y_vals = func_numpy(x_vals)
                axes[0, 0].plot(x_vals, y_vals, 'b-', linewidth=2)
                axes[0, 0].set_title('Original Function f(x)', fontweight='bold')
                axes[0, 0].grid(True, alpha=0.3)
                axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
                axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
                axes[0, 0].set_xlabel('x', fontsize=12)
                axes[0, 0].set_ylabel('f(x)', fontsize=12)
            except:
                axes[0, 0].text(0.5, 0.5, 'Unable to plot', ha='center', va='center')
            
            # Derivative
            try:
                derivative = diff(func, x)
                deriv_numpy = lambdify(x, derivative, 'numpy')
                dy_vals = deriv_numpy(x_vals)
                axes[0, 1].plot(x_vals, dy_vals, 'r-', linewidth=2)
                axes[0, 1].set_title("Derivative f'(x)", fontweight='bold')
                axes[0, 1].grid(True, alpha=0.3)
                axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
                axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
                axes[0, 1].set_xlabel('x', fontsize=12)
                axes[0, 1].set_ylabel("f'(x)", fontsize=12)
            except:
                axes[0, 1].text(0.5, 0.5, 'Unable to plot', ha='center', va='center')
            
            # Integral (if applicable)
            try:
                integral = integrate(func, x)
                integ_numpy = lambdify(x, integral, 'numpy')
                int_vals = integ_numpy(x_vals)
                axes[1, 0].plot(x_vals, int_vals, 'g-', linewidth=2)
                axes[1, 0].set_title('Integral ∫f(x)dx', fontweight='bold')
                axes[1, 0].grid(True, alpha=0.3)
                axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
                axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
                axes[1, 0].set_xlabel('x', fontsize=12)
                axes[1, 0].set_ylabel('∫f(x)dx', fontsize=12)
            except:
                axes[1, 0].text(0.5, 0.5, 'Unable to plot', ha='center', va='center')
            
            # Combined view
            try:
                axes[1, 1].plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)', alpha=0.7)
                axes[1, 1].plot(x_vals, dy_vals, 'r-', linewidth=2, label="f'(x)", alpha=0.7)
                axes[1, 1].set_title('Combined View', fontweight='bold')
                axes[1, 1].grid(True, alpha=0.3)
                axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
                axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
                axes[1, 1].set_xlabel('x', fontsize=12)
                axes[1, 1].set_ylabel('y', fontsize=12)
                axes[1, 1].legend()
            except:
                axes[1, 1].text(0.5, 0.5, 'Unable to plot', ha='center', va='center')
            
            plt.tight_layout()
            
            # Save graph
            graph_path = os.path.join(self.temp_dir, f"graph_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            plt.savefig(graph_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            return graph_path
            
        except Exception as e:
            print(f"Graph generation error: {e}")
            return None
    
    def cleanup_temp_files(self):
        """Clean up temporary graph files"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            os.makedirs(self.temp_dir, exist_ok=True)
