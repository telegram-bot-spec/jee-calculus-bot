"""
PDF Generator - WITH COMPLETE DEBUG LOGGING
This will show us EXACTLY what's failing
"""

import os
import subprocess
import tempfile
from datetime import datetime

class PDFGenerator:
    def __init__(self, output_dir="temp_pdfs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate(self, solution_data):
        """Main entry point - called by bot.py"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return self.create_pdf_local(solution_data, f"solution_{timestamp}")
    
    def create_pdf_local(self, solution_data, filename):
        """Create PDF using local pdflatex with FULL ERROR REPORTING"""
        
        print("\n" + "="*60)
        print("PDF Generator: Creating PDF with pdflatex...")
        print("="*60)
        
        try:
            # Step 1: Build LaTeX content
            latex_content = self.build_latex_document(solution_data)
            
            # Step 2: Write to temp .tex file
            tex_path = os.path.join(self.output_dir, f"{filename}.tex")
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            
            print(f"✓ LaTeX file written: {tex_path}")
            print(f"✓ LaTeX content length: {len(latex_content)} chars")
            
            # DEBUG: Save a copy for inspection
            debug_tex = os.path.join(self.output_dir, "DEBUG_last_compile.tex")
            with open(debug_tex, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            print(f"✓ DEBUG copy saved: {debug_tex}")
            
            # Step 3: Compile with pdflatex (run twice for TOC)
            for run in [1, 2]:
                print(f"\nRunning pdflatex (pass {run}/2)...")
                result = subprocess.run(
                    [
                        'pdflatex',
                        '-interaction=nonstopmode',
                        '-output-directory', self.output_dir,
                        '-jobname', filename,
                        tex_path
                    ],
                    cwd=self.output_dir,
                    capture_output=True,
                    timeout=120,
                    text=True
                )
                
                print(f"Return code: {result.returncode}")
                
                if result.returncode != 0:
                    # FULL ERROR REPORTING
                    print(f"\n{'='*60}")
                    print(f"❌ PDFLATEX FAILED ON PASS {run}/2")
                    print(f"{'='*60}")
                    
                    print("\n📄 STDOUT (last 2000 chars):")
                    print(result.stdout[-2000:] if result.stdout else "No stdout")
                    
                    print("\n📄 STDERR (last 2000 chars):")
                    print(result.stderr[-2000:] if result.stderr else "No stderr")
                    
                    # Try to find the .log file for more details
                    log_file = os.path.join(self.output_dir, f"{filename}.log")
                    if os.path.exists(log_file):
                        print("\n📄 LOG FILE (last 3000 chars):")
                        with open(log_file, 'r', encoding='utf-8', errors='replace') as f:
                            log_content = f.read()
                            print(log_content[-3000:])
                    
                    print(f"\n{'='*60}\n")
                    
                    if run == 2:
                        raise Exception(
                            f"pdflatex failed with return code {result.returncode}\n"
                            f"Check logs above for details.\n"
                            f"Debug .tex file saved at: {debug_tex}"
                        )
            
            # Step 4: Verify PDF was created
            pdf_path = os.path.join(self.output_dir, f"{filename}.pdf")
            if not os.path.exists(pdf_path):
                raise Exception(
                    f"PDF was not created despite successful compilation\n"
                    f"Expected: {pdf_path}\n"
                    f"Directory contents: {os.listdir(self.output_dir)}"
                )
            
            # Verify it's a valid PDF
            with open(pdf_path, 'rb') as f:
                header = f.read(4)
                if header != b'%PDF':
                    raise Exception(f"Generated file is not a valid PDF. Header: {header}")
            
            file_size = os.path.getsize(pdf_path)
            print(f"✓ PDF created successfully: {pdf_path}")
            print(f"✓ PDF size: {file_size} bytes")
            return pdf_path
            
        except subprocess.TimeoutExpired:
            raise Exception("pdflatex timeout (120s). LaTeX content too complex.")
        except FileNotFoundError:
            raise Exception(
                "pdflatex not found!\n"
                "Make sure texlive-latex-base is installed in Dockerfile.\n"
                "Run: apt-get install texlive-latex-base"
            )
        except Exception as e:
            print(f"\n{'='*60}")
            print(f"❌ PDF GENERATION ERROR")
            print(f"{'='*60}")
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            print(f"{'='*60}\n")
            raise
    
    def build_latex_document(self, solution_data):
        """Build complete LaTeX document - PROPERLY ESCAPED"""
        
        print("Building LaTeX document...")
        
        # Extract data
        strategy_1 = solution_data.get('strategy_1', 'N/A')
        strategy_2 = solution_data.get('strategy_2', 'N/A')
        strategy_3 = solution_data.get('strategy_3', 'N/A')
        final_answer = solution_data.get('final_answer', 'N/A')
        confidence = solution_data.get('confidence', 90)
        reason = solution_data.get('one_sentence_reason', 'See analysis')
        all_agree = solution_data.get('all_agree', False)
        
        print(f"Strategy 1 length: {len(str(strategy_1))} chars")
        print(f"Strategy 2 length: {len(str(strategy_2))} chars")
        print(f"Strategy 3 length: {len(str(strategy_3))} chars")
        
        # Clean and escape text
        strategy_1 = self.escape_for_latex(self.clean_text(strategy_1))
        strategy_2 = self.escape_for_latex(self.clean_text(strategy_2))
        strategy_3 = self.escape_for_latex(self.clean_text(strategy_3))
        final_answer = self.escape_for_latex(str(final_answer))
        reason = self.escape_for_latex(str(reason))
        
        print(f"After escaping - Strategy 1: {len(strategy_1)} chars")
        print(f"After escaping - Strategy 2: {len(strategy_2)} chars")
        print(f"After escaping - Strategy 3: {len(strategy_3)} chars")
        
        # Build document
        latex = r'''\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}
\usepackage{geometry}
\geometry{margin=1in}

\definecolor{cengage}{RGB}{0,102,204}
\definecolor{blackbook}{RGB}{204,0,102}
\definecolor{olympiad}{RGB}{102,51,153}

\title{\textbf{JEE Calculus Solution}}
\author{Ultimate Calculus Bot}
\date{\today}

\begin{document}

\maketitle

\section{Strategy 1: Cengage Method}

\textcolor{cengage}{\textbf{Systematic Approach}}

\vspace{0.3cm}

''' + strategy_1 + r'''

\section{Strategy 2: Black Book Shortcuts}

\textcolor{blackbook}{\textbf{Quick Method}}

\vspace{0.3cm}

''' + strategy_2 + r'''

\section{Strategy 3: Olympiad Insights}

\textcolor{olympiad}{\textbf{Elegant Solution}}

\vspace{0.3cm}

''' + strategy_3 + r'''

\section{Final Answer}

\begin{center}
\Large\textbf{''' + final_answer + r'''}
\end{center}

\vspace{0.3cm}

\textbf{Confidence:} ''' + str(confidence) + r'''\%

\textbf{Reason:} ''' + reason + r'''

\vspace{0.5cm}

\textbf{All strategies agree:} ''' + ('Yes' if all_agree else 'No') + r'''

\end{document}'''
        
        print("✓ LaTeX document built successfully")
        return latex
    
    def clean_text(self, text):
        """Clean text before escaping"""
        if not text:
            return ""
        
        text = str(text)
        
        # Remove excessive newlines
        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')
        
        # Remove control characters except newlines
        text = ''.join(char for char in text if char == '\n' or (ord(char) >= 32 and ord(char) < 127) or ord(char) > 127)
        
        return text.strip()
    
    def escape_for_latex(self, text):
        """Escape text for LaTeX - COMPREHENSIVE VERSION"""
        if not text:
            return ""
        
        text = str(text)
        
        # First pass: Handle backslashes (must be first!)
        text = text.replace('\\', r'\textbackslash{}')
        
        # Second pass: Escape LaTeX special characters
        replacements = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
        }
        
        for char, escaped in replacements.items():
            text = text.replace(char, escaped)
        
        # Third pass: Handle problematic Unicode characters
        unicode_replacements = {
            '\u2019': "'",  # Right single quotation
            '\u2018': "'",  # Left single quotation  
            '\u201c': '"',  # Left double quotation
            '\u201d': '"',  # Right double quotation
            '\u2013': '--', # En dash
            '\u2014': '---', # Em dash
            '\u2026': '...', # Ellipsis
            '\u00a0': ' ',  # Non-breaking space
            '\u00b0': r'$^\circ$',  # Degree symbol
            '\u00b2': r'$^2$',  # Superscript 2
            '\u00b3': r'$^3$',  # Superscript 3
            '\u221e': r'$\infty$',  # Infinity
            '\u03c0': r'$\pi$',  # Pi
            '\u222b': r'$\int$',  # Integral
            '\u2211': r'$\sum$',  # Sum
            '\u221a': r'$\sqrt{}$',  # Square root
            '\u2264': r'$\leq$',  # Less than or equal
            '\u2265': r'$\geq$',  # Greater than or equal
            '\u2260': r'$\neq$',  # Not equal
            '\u00d7': r'$\times$',  # Multiplication
            '\u00f7': r'$\div$',  # Division
            '\u00b1': r'$\pm$',  # Plus-minus
        }
        
        for unicode_char, replacement in unicode_replacements.items():
            text = text.replace(unicode_char, replacement)
        
        # Fourth pass: Remove any remaining high Unicode that might cause issues
        safe_text = []
        for char in text:
            code = ord(char)
            # Keep: ASCII (0-127), newlines, common Latin (128-255)
            if code < 256 or char == '\n':
                safe_text.append(char)
            elif code in range(0x0391, 0x03A9):  # Greek uppercase
                safe_text.append(char)
            elif code in range(0x03B1, 0x03C9):  # Greek lowercase  
                safe_text.append(char)
            else:
                # Replace unknown Unicode with space
                safe_text.append(' ')
        
        return ''.join(safe_text)
