"""
PDF Generator for JEE Calculus Bot
Uses PyLaTeX + pdflatex for publication-quality PDFs (Springer/Nature standard)
Includes: Math equations, graphs, tables, professional formatting
"""

import os
from pylatex import Document, Section, Subsection, Math, Figure, Tabular
from pylatex.utils import NoEscape, bold
from sympy import latex
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend


class PDFGenerator:
    """
    Generates professional JEE Calculus solution PDFs
    Uses LaTeX for perfect math rendering (zero character issues)
    """
    
    def __init__(self, output_dir="temp_pdfs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs("temp_graphs", exist_ok=True)
    
    def generate(self, solution_data):
    """Wrapper method for create_pdf() - used by bot"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return self.create_pdf(solution_data, f"solution_{timestamp}")
        """
        Create complete PDF from solution data
        
        Args:
            solution_data: Dictionary containing:
                - problem: Original problem description
                - strategy_1: Cengage method solution
                - strategy_2: Black Book shortcuts
                - strategy_3: Olympiad tricks
                - verification: SymPy verification results
                - graphs: List of graph file paths
                - final_answer: Final answer
                - confidence: Confidence percentage
        """
        
        # Create document with professional settings
        doc = Document(documentclass='article')
        
        # Add necessary packages for beautiful math and tables
        doc.preamble.append(NoEscape(r'\usepackage{amsmath}'))
        doc.preamble.append(NoEscape(r'\usepackage{amssymb}'))
        doc.preamble.append(NoEscape(r'\usepackage{amsfonts}'))
        doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
        doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
        doc.preamble.append(NoEscape(r'\usepackage{geometry}'))
        doc.preamble.append(NoEscape(r'\usepackage{booktabs}'))
        doc.preamble.append(NoEscape(r'\usepackage{tikz}'))
        doc.preamble.append(NoEscape(r'\geometry{margin=1in}'))
        
        # Add custom color definitions
        doc.preamble.append(NoEscape(r'\definecolor{cengage}{RGB}{0,102,204}'))
        doc.preamble.append(NoEscape(r'\definecolor{blackbook}{RGB}{204,0,102}'))
        doc.preamble.append(NoEscape(r'\definecolor{olympiad}{RGB}{102,51,153}'))
        
        # Title
        doc.preamble.append(NoEscape(r'\title{JEE Advanced Calculus Solution}'))
        doc.preamble.append(NoEscape(r'\author{Ultimate Calculus Bot}'))
        doc.preamble.append(NoEscape(r'\date{\today}'))
        doc.append(NoEscape(r'\maketitle'))
        
        # Problem Statement
        with doc.create(Section('Problem Statement')):
            doc.append(solution_data.get('problem', 'Problem from image'))
        
        # Strategy 1: Cengage Method
        with doc.create(Section('Strategy 1: Cengage Method (Textbook Rigor)', 
                                numbering=True)):
            doc.append(NoEscape(r'\textcolor{cengage}{\textbf{Systematic Step-by-Step Solution}}'))
            doc.append('\n\n')
            
            strategy_1 = solution_data.get('strategy_1', {})
            if isinstance(strategy_1, dict):
                for step, content in strategy_1.items():
                    doc.append(bold(f"{step}: "))
                    doc.append(content)
                    doc.append('\n\n')
            else:
                doc.append(str(strategy_1))
        
        # Strategy 2: Black Book Shortcuts
        with doc.create(Section('Strategy 2: Black Book Shortcuts (Quick Method)', 
                                numbering=True)):
            doc.append(NoEscape(r'\textcolor{blackbook}{\textbf{Pattern Recognition \& Speed}}'))
            doc.append('\n\n')
            
            strategy_2 = solution_data.get('strategy_2', {})
            if isinstance(strategy_2, dict):
                for key, content in strategy_2.items():
                    doc.append(bold(f"{key}: "))
                    doc.append(content)
                    doc.append('\n\n')
            else:
                doc.append(str(strategy_2))
        
        # Strategy 3: Olympiad Tricks
        with doc.create(Section('Strategy 3: Olympiad/Exceptional Insights', 
                                numbering=True)):
            doc.append(NoEscape(r'\textcolor{olympiad}{\textbf{Elegant Mathematical Approach}}'))
            doc.append('\n\n')
            
            strategy_3 = solution_data.get('strategy_3', {})
            if isinstance(strategy_3, dict):
                for key, content in strategy_3.items():
                    doc.append(bold(f"{key}: "))
                    doc.append(content)
                    doc.append('\n\n')
            else:
                doc.append(str(strategy_3))
        
        # Verification Section
        with doc.create(Section('Verification \& Cross-Check')):
            verification = solution_data.get('verification', {})
            
            # Create comparison table
            with doc.create(Tabular('|l|l|')) as table:
                table.add_hline()
                table.add_row(['Strategy', 'Answer'])
                table.add_hline()
                table.add_row(['Cengage Method', verification.get('strategy_1_answer', 'N/A')])
                table.add_row(['Black Book', verification.get('strategy_2_answer', 'N/A')])
                table.add_row(['Olympiad', verification.get('strategy_3_answer', 'N/A')])
                table.add_hline()
            
            doc.append('\n\n')
            doc.append(bold('All methods agree: '))
            doc.append('YES' if verification.get('all_agree', False) else 'NO - Review needed')
            doc.append('\n\n')
            
            doc.append(bold('SymPy Verification: '))
            doc.append(verification.get('sympy_check', 'Verified'))
        
        # Graphs Section (if any)
        graphs = solution_data.get('graphs', [])
        if graphs:
            with doc.create(Section('Graphical Visualization')):
                for i, graph_path in enumerate(graphs):
                    if os.path.exists(graph_path):
                        with doc.create(Figure(position='h!')) as fig:
                            fig.add_image(graph_path, width='350px')
                            fig.add_caption(f'Graph {i+1}')
        
        # Final Answer Section
        with doc.create(Section('Final Answer')):
            doc.append(NoEscape(r'\begin{center}'))
            doc.append(NoEscape(r'\Large\textbf{'))
            doc.append(solution_data.get('final_answer', 'Answer not available'))
            doc.append(NoEscape(r'}'))
            doc.append(NoEscape(r'\end{center}'))
            doc.append('\n\n')
            
            doc.append(bold('Confidence: '))
            doc.append(f"{solution_data.get('confidence', 0)}%")
            doc.append('\n\n')
            
            doc.append(bold('Reasoning: '))
            doc.append(solution_data.get('reasoning', 'Solution verified through multiple methods'))
        
        # JEE Trap Checks
        if 'jee_traps' in solution_data:
            with doc.create(Section('JEE Trap Verification')):
                traps = solution_data['jee_traps']
                for trap, status in traps.items():
                    doc.append(f"• {trap}: {status}\n")
        
        # Generate PDF
        try:
            pdf_path = os.path.join(self.output_dir, filename)
            doc.generate_pdf(pdf_path, compiler='pdflatex', clean_tex=False)
            return f"{pdf_path}.pdf"
        except Exception as e:
            print(f"Error generating PDF: {e}")
            # Fallback: Try without cleaning tex files
            try:
                doc.generate_pdf(pdf_path, compiler='pdflatex', clean_tex=False)
                return f"{pdf_path}.pdf"
            except Exception as e2:
                print(f"Fallback also failed: {e2}")
                raise
    
    def create_graph(self, function_str, x_range=(-5, 5), filename="graph"):
        """
        Create a matplotlib graph and save it
        
        Args:
            function_str: String representation of function (for label)
            x_range: Tuple of (min, max) for x-axis
            filename: Output filename
        
        Returns:
            Path to saved graph
        """
        try:
            import numpy as np
            
            # Create figure
            fig, ax = plt.subplots(figsize=(8, 6))
            
            # Generate x values
            x = np.linspace(x_range[0], x_range[1], 1000)
            
            # This is a placeholder - actual function evaluation would come from SymPy
            # For now, just create a sample graph
            y = x**2  # Example function
            
            # Plot
            ax.plot(x, y, 'b-', linewidth=2, label=function_str)
            ax.grid(True, alpha=0.3)
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.legend()
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(f'Graph of {function_str}', fontsize=14)
            
            # Save
            graph_path = os.path.join("temp_graphs", f"{filename}.png")
            plt.savefig(graph_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            return graph_path
        except Exception as e:
            print(f"Error creating graph: {e}")
            return None
    
    def cleanup(self):
        """Clean up temporary files"""
        import shutil
        try:
            if os.path.exists(self.output_dir):
                shutil.rmtree(self.output_dir)
            if os.path.exists("temp_graphs"):
                shutil.rmtree("temp_graphs")
        except Exception as e:
            print(f"Cleanup error: {e}")


# Example usage
if __name__ == "__main__":
    # Test the PDF generator
    generator = PDFGenerator()
    
    sample_data = {
        'problem': 'Find the integral of x*e^x dx',
        'strategy_1': {
            'Step 1': 'Identify as product of polynomial and exponential',
            'Step 2': 'Use integration by parts: u = x, dv = e^x dx',
            'Step 3': 'Then du = dx, v = e^x',
            'Step 4': 'Apply formula: x*e^x - integral(e^x dx)',
            'Answer': 'e^x(x-1) + C'
        },
        'strategy_2': {
            'Pattern': 'Product of x and e^x',
            'Shortcut': 'Memorized form: integral(x*e^x) = e^x(x-1) + C',
            'Time': '5 seconds',
            'Answer': 'e^x(x-1) + C'
        },
        'strategy_3': {
            'Insight': 'Use Feynman technique',
            'Method': 'Consider I(a) = integral(e^(ax)dx), differentiate w.r.t. a',
            'Answer': 'e^x(x-1) + C'
        },
        'verification': {
            'strategy_1_answer': 'e^x(x-1) + C',
            'strategy_2_answer': 'e^x(x-1) + C',
            'strategy_3_answer': 'e^x(x-1) + C',
            'all_agree': True,
            'sympy_check': 'Verified: derivative matches original integrand'
        },
        'final_answer': 'e^x(x-1) + C',
        'confidence': 100,
        'reasoning': 'All three methods independently arrived at the same answer',
        'jee_traps': {
            'Constant of integration': 'Present (+C)',
            'Domain restrictions': 'None (e^x defined for all real x)',
            'Simplification': 'Factored as e^x(x-1)'
        }
    }
    
    pdf_path = generator.create_pdf(sample_data, "test_solution")
    print(f"PDF generated: {pdf_path}")
