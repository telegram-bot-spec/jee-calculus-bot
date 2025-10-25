"""
PDF Generator - LaTeX.Online API Version (BULLETPROOF)
No local LaTeX installation needed!
Works 100% on Railway/Render without any LaTeX packages
"""

import os
import requests
import tempfile
from datetime import datetime

class PDFGenerator:
    def __init__(self, output_dir="temp_pdfs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        # LaTeX.Online API - FREE, no authentication needed!
        self.api_url = "https://latexonline.cc/compile"
    
    def generate(self, solution_data):
        """Main entry point - called by bot.py"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return self.create_pdf_via_api(solution_data, f"solution_{timestamp}")
    
    def create_pdf_via_api(self, solution_data, filename):
        """Create PDF using LaTeX.Online API - No local LaTeX needed!"""
        
        print("\n" + "="*60)
        print("PDF Generator: Using LaTeX.Online API...")
        print("="*60)
        
        try:
            # Step 1: Build complete LaTeX document as string
            latex_content = self.build_latex_document(solution_data)
            
            # Step 2: Send to LaTeX.Online API
            files = {
                'file': (f'{filename}.tex', latex_content, 'text/plain')
            }
            
            print("Sending to LaTeX.Online API...")
            response = requests.post(
                self.api_url,
                files=files,
                timeout=60  # 60 second timeout
            )
            
            # Step 3: Check response
            if response.status_code != 200:
                error_msg = f"LaTeX.Online returned status {response.status_code}"
                if response.text:
                    error_msg += f"\nResponse: {response.text[:200]}"
                raise Exception(error_msg)
            
            # Step 4: Save PDF
            pdf_path = os.path.join(self.output_dir, f"{filename}.pdf")
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ PDF created successfully: {pdf_path}")
            print(f"✓ PDF size: {len(response.content)} bytes")
            return pdf_path
            
        except requests.exceptions.Timeout:
            raise Exception("LaTeX.Online API timeout (60s). Try again or simplify content.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"LaTeX.Online API error: {str(e)}")
        except Exception as e:
            print(f"PDF generation error: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def build_latex_document(self, solution_data):
        """Build complete LaTeX document as string"""
        
        print("Building LaTeX document...")
        
        # Extract data from solution
        strategy_1 = solution_data.get('strategy_1', 'N/A')
        strategy_2 = solution_data.get('strategy_2', 'N/A')
        strategy_3 = solution_data.get('strategy_3', 'N/A')
        final_synthesis = solution_data.get('final_synthesis', 'N/A')
        final_answer = solution_data.get('final_answer', 'N/A')
        confidence = solution_data.get('confidence', 90)
        reason = solution_data.get('one_sentence_reason', 'See analysis')
        all_agree = solution_data.get('all_agree', False)
        
        # Build LaTeX document
        latex = r'''\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{fancyhdr}
\geometry{margin=1in}

% Custom colors
\definecolor{cengage}{RGB}{0,102,204}
\definecolor{blackbook}{RGB}{204,0,102}
\definecolor{olympiad}{RGB}{102,51,153}
\definecolor{success}{RGB}{0,153,0}
\definecolor{warning}{RGB}{204,102,0}

% Header/Footer
\pagestyle{fancy}
\fancyhf{}
\lhead{JEE Calculus Bot}
\rhead{\today}
\cfoot{\thepage}

\title{\textbf{\Large JEE Advanced Calculus Solution}}
\author{\textbf{Ultimate Calculus Bot with Triple-Strategy Analysis}}
\date{\today}

\begin{document}

\maketitle

\tableofcontents
\newpage

%=================================================================
\section{Strategy 1: Cengage Method (Systematic)}
%=================================================================

\textcolor{cengage}{\textbf{\large Textbook Approach - Step by Step}}

\vspace{0.3cm}

''' + self.safe_escape(self.clean_text(strategy_1)) + r'''

\vspace{0.5cm}

%=================================================================
\section{Strategy 2: Black Book Shortcuts (Speed)}
%=================================================================

\textcolor{blackbook}{\textbf{\large Pattern Recognition - Quick Method}}

\vspace{0.3cm}

''' + self.safe_escape(self.clean_text(strategy_2)) + r'''

\vspace{0.5cm}

%=================================================================
\section{Strategy 3: Olympiad Insights (Elegant)}
%=================================================================

\textcolor{olympiad}{\textbf{\large Advanced Techniques - Beautiful Solution}}

\vspace{0.3cm}

''' + self.safe_escape(self.clean_text(strategy_3)) + r'''

\vspace{0.5cm}

%=================================================================
\section{Verification \& Synthesis}
%=================================================================

''' + self.safe_escape(self.clean_text(final_synthesis)) + r'''

\vspace{0.3cm}

\textbf{Do all three strategies agree?} ''' + (r'\textcolor{success}{YES}' if all_agree else r'\textcolor{warning}{NO - See analysis}') + r'''

\vspace{0.5cm}

%=================================================================
\section{Final Answer}
%=================================================================

\begin{center}
\fbox{\parbox{0.8\textwidth}{
\centering
\Large\textbf{ANSWER}

\vspace{0.3cm}

\Huge ''' + self.safe_escape(str(final_answer)) + r'''

\vspace{0.3cm}

\normalsize\textbf{Confidence: ''' + str(confidence) + r'''\%}
}}
\end{center}

\vspace{0.5cm}

\textbf{One-Sentence Explanation:}

''' + self.safe_escape(str(reason)) + r'''

\vspace{1cm}

\hrule

\vspace{0.3cm}

\small
\textit{Generated by JEE Calculus Bot - Triple-Strategy Analysis System}

\textit{Powered by: Gemini 2.0 Flash + SymPy Verification + LaTeX.Online}

\end{document}'''
        
        print("✓ LaTeX document built successfully")
        return latex
    
    def clean_text(self, text):
        """Clean text before LaTeX escaping"""
        if not text:
            return ""
        
        text = str(text)
        
        # Remove excessive newlines
        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        return text
    
    def safe_escape(self, text):
        """
        Escape special LaTeX characters
        This prevents compilation errors
        """
        if not text:
            return ""
        
        text = str(text)
        
        # Order matters! Backslash must be first
        replacements = [
            ('\\', r'\textbackslash{}'),
            ('&', r'\&'),
            ('%', r'\%'),
            ('$', r'\$'),
            ('#', r'\#'),
            ('_', r'\_'),
            ('{', r'\{'),
            ('}', r'\}'),
            ('~', r'\textasciitilde{}'),
            ('^', r'\^{}'),
        ]
        
        for char, escaped in replacements:
            text = text.replace(char, escaped)
        
        # Handle common Unicode math symbols
        unicode_math = {
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
        
        for unicode_char, latex_cmd in unicode_math.items():
            text = text.replace(unicode_char, latex_cmd)
        
        return text
