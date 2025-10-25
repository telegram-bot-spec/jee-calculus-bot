"""
PDF Generator for JEE Calculus Bot
FINAL VERSION with all UTF-8 and LaTeX fixes (STABLE RELEASE)
"""

import os
import subprocess
from pylatex import Document, Section, Figure, Tabular
from pylatex.utils import NoEscape, bold
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


class PDFGenerator:
    def __init__(self, output_dir="temp_pdfs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs("temp_graphs", exist_ok=True)
    
    def escape_latex(self, text):
        """Escape special LaTeX characters + handle Unicode math symbols"""
        if not text:
            return ""
        
        text = str(text)
        
        # First: Replace Unicode math symbols with LaTeX equivalents
        unicode_replacements = {
            '⁻¹': r'$^{-1}$',
            '∫': r'$\int$',
            '∑': r'$\sum$',
            '∏': r'$\prod$',
            '√': r'$\sqrt{}$',
            '≤': r'$\leq$',
            '≥': r'$\geq$',
            '≠': r'$\neq$',
            '∈': r'$\in$',
            '∞': r'$\infty$',
            'π': r'$\pi$',
            '²': r'$^2$',
            '³': r'$^3$',
            '°': r'$^\circ$',
            '±': r'$\pm$',
            '×': r'$\times$',
            '÷': r'$\div$',
            '≈': r'$\approx$',
            'α': r'$\alpha$',
            'β': r'$\beta$',
            'γ': r'$\gamma$',
            'θ': r'$\theta$',
            'λ': r'$\lambda$',
            'μ': r'$\mu$',
            'σ': r'$\sigma$',
            'Δ': r'$\Delta$',
        }
        
        for unicode_char, latex_cmd in unicode_replacements.items():
            text = text.replace(unicode_char, latex_cmd)
        
        # Second: Escape LaTeX special characters (but not if already in math mode)
        if '$' not in text:
            latex_special = {
                '&': r'\&',
                '%': r'\%',
                '#': r'\#',
                '_': r'\_',
                '{': r'\{',
                '}': r'\}',
                '~': r'\textasciitilde{}',
                '^': r'\^{}',
                '\\': r'\textbackslash{}',
            }
            
            for char, escaped in latex_special.items():
                text = text.replace(char, escaped)
        
        return text
    
    def safe_read_file(self, filepath):
        """Safely read a file with fallback encodings"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for enc in encodings:
            try:
                with open(filepath, 'r', encoding=enc, errors='replace') as f:
                    return f.read()
            except:
                continue
        
        try:
            with open(filepath, 'rb') as f:
                return f.read().decode('utf-8', errors='replace')
        except:
            return "Could not read file"
    
    def generate(self, solution_data):
        """Main entry point - called by bot"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return self.create_pdf(solution_data, f"solution_{timestamp}")
    
    def create_pdf(self, solution_data, filename="calculus_solution"):
        """Create PDF from solution data"""
        
        print("\n" + "="*60)
        print("PDF Generator: Starting...")
        print("="*60)
        
        try:
            # Create LaTeX document
            doc = Document(
                documentclass='article',
                document_options=['10pt'],
                geometry_options={'margin': '1in'}
            )
            
            doc.packages.clear()
            doc.preamble.append(NoEscape(r'\usepackage{amsmath}'))
            doc.preamble.append(NoEscape(r'\usepackage{amssymb}'))
            doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
            doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
            doc.preamble.append(NoEscape(r'\usepackage{booktabs}'))
            
            # Custom colors
            doc.preamble.append(NoEscape(r'\definecolor{cengage}{RGB}{0,102,204}'))
            doc.preamble.append(NoEscape(r'\definecolor{blackbook}{RGB}{204,0,102}'))
            doc.preamble.append(NoEscape(r'\definecolor{olympiad}{RGB}{102,51,153}'))
            
            # Title
            doc.append(NoEscape(r'\begin{center}'))
            doc.append(NoEscape(r'\LARGE\textbf{JEE Advanced Calculus Solution}\\[0.5cm]'))
            doc.append(NoEscape(r'\large Ultimate Calculus Bot\\[0.3cm]'))
            doc.append(NoEscape(r'\today'))
            doc.append(NoEscape(r'\end{center}'))
            doc.append(NoEscape(r'\vspace{1cm}'))
            
            # Problem Statement
            with doc.create(Section('Problem Statement')):
                problem = self.escape_latex(solution_data.get('problem', 'Problem from image'))
                doc.append(problem)
            
            # Strategy 1
            with doc.create(Section('Strategy 1: Cengage Method')):
                doc.append(NoEscape(r'\textcolor{cengage}{\textbf{Systematic Solution}}'))
                doc.append('\n\n')
                self._add_strategy_content(doc, solution_data.get('strategy_1', 'N/A'))
            
            # Strategy 2
            with doc.create(Section('Strategy 2: Black Book Shortcuts')):
                doc.append(NoEscape(r'\textcolor{blackbook}{\textbf{Quick Method}}'))
                doc.append('\n\n')
                self._add_strategy_content(doc, solution_data.get('strategy_2', 'N/A'))
            
            # Strategy 3
            with doc.create(Section('Strategy 3: Olympiad Insights')):
                doc.append(NoEscape(r'\textcolor{olympiad}{\textbf{Elegant Approach}}'))
                doc.append('\n\n')
                self._add_strategy_content(doc, solution_data.get('strategy_3', 'N/A'))
            
            # Verification
            with doc.create(Section('Verification')):
                doc.append('All three strategies agree: ')
                doc.append(bold('YES' if solution_data.get('all_agree') else 'NO'))
            
            # Graphs
            graphs = solution_data.get('graphs', [])
            if graphs:
                with doc.create(Section('Graphs')):
                    for i, graph_path in enumerate(graphs):
                        if os.path.exists(graph_path):
                            with doc.create(Figure(position='h!')) as fig:
                                fig.add_image(graph_path, width='300px')
                                fig.add_caption(f'Visualization {i+1}')
            
            # Final Answer
            with doc.create(Section('Final Answer')):
                doc.append(NoEscape(r'\begin{center}\Large\textbf{'))
                doc.append(self.escape_latex(str(solution_data.get('final_answer', 'N/A'))))
                doc.append(NoEscape(r'}\end{center}'))
                doc.append('\n\n')
                doc.append(bold('Confidence: '))
                doc.append(f"{solution_data.get('confidence', 0)}")
                doc.append(NoEscape(r'\%'))
                doc.append('\n\n')
                doc.append(bold('Reason: '))
                doc.append(self.escape_latex(str(solution_data.get('one_sentence_reason', 'N/A'))))
            
            # Generate .tex file
            pdf_path = os.path.join(self.output_dir, filename)
            doc.generate_tex(pdf_path)
            print("✓ LaTeX file generated")

            tex_file = f"{pdf_path}.tex"

            # FIX: Use pdflatex instead of xelatex (more compatible)
            if not os.path.exists(tex_file):
                raise Exception(f"LaTeX source file not found: {tex_file}")
            
            try:
                # Try pdflatex first (more reliable)
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', self.output_dir, tex_file],
                    cwd=self.output_dir,
                    capture_output=True,
                    timeout=120,
                    text=True
                )
                
                if result.returncode != 0:
                    # If pdflatex fails, print detailed error
                    print(f"\n{'='*60}")
                    print("LaTeX Compilation Error:")
                    print("STDOUT:", result.stdout[-1500:] if result.stdout else "No output")
                    print("STDERR:", result.stderr[-1500:] if result.stderr else "No errors")
                    print(f"{'='*60}\n")
                    
                    # Try to read log file for more details
                    log_file = f"{pdf_path}.log"
                    if os.path.exists(log_file):
                        log_content = self.safe_read_file(log_file)
                        print("Log file (last 1000 chars):")
                        print(log_content[-1000:])
                    
                    raise Exception(f"LaTeX compilation failed with return code {result.returncode}")
                
            except FileNotFoundError:
                raise Exception("pdflatex not found. Make sure texlive-latex-base is installed in Dockerfile")
            
            pdf_output = f"{pdf_path}.pdf"
            if not os.path.exists(pdf_output):
                raise Exception("PDF was not created despite successful compilation")
            
            print(f"✓ PDF created: {pdf_output}")
            return pdf_output
            
        except subprocess.TimeoutExpired:
            raise Exception("LaTeX compilation timed out (120s limit exceeded)")
        except Exception as e:
            print(f"PDF generation error: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def _add_strategy_content(self, doc, content):
        """Add strategy content to document"""
        if isinstance(content, dict):
            for key, value in content.items():
                doc.append(bold(self.escape_latex(str(key)) + ': '))
                doc.append(self.escape_latex(str(value)))
                doc.append('\n\n')
        elif isinstance(content, str):
            lines = content.split('\n')
            for line in lines:
                if line.strip():
                    doc.append(self.escape_latex(line.strip()))
                    doc.append('\n')
        else:
            doc.append(self.escape_latex(str(content)))
