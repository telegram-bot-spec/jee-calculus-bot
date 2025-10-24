import os
import google.generativeai as genai
from PIL import Image
import io
import base64
import json
from knowledge_base import CALCULUS_KNOWLEDGE
from sympy_verifier import SympyVerifier

class CalculusSolver:
    def __init__(self):
        # Setup API keys rotation
        self.api_keys = [
            os.getenv('GEMINI_API_KEY_1'),
            os.getenv('GEMINI_API_KEY_2'),
            os.getenv('GEMINI_API_KEY_3'),
            os.getenv('GEMINI_API_KEY_4'),
            os.getenv('GEMINI_API_KEY_5'),
        ]
        self.current_key_index = 0
        self.verifier = SympyVerifier()
        
        # Configure Gemini
        self.setup_gemini()
        
    def setup_gemini(self):
        """Setup Gemini API with current key"""
        genai.configure(api_key=self.api_keys[self.current_key_index])
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
    def rotate_api_key(self):
        """Rotate to next API key"""
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        self.setup_gemini()
    
    def build_ultimate_prompt(self):
        """Build the triple-strategy prompt with all knowledge"""
        knowledge = CALCULUS_KNOWLEDGE
        
        prompt = f"""
YOU ARE THE ULTIMATE JEE CALCULUS EXPERT

KNOWLEDGE BASE LOADED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DIFFERENTIATION RULES:
{json.dumps(knowledge['differentiation_rules'], indent=2)}

📚 INTEGRATION TECHNIQUES:
{json.dumps(knowledge['integration_techniques'], indent=2)}

⚠️ JEE CALCULUS TRAPS:
{json.dumps(knowledge['jee_traps'], indent=2)}

⚡ SHORTCUTS & PATTERNS:
{json.dumps(knowledge['shortcuts'], indent=2)}

🎯 SPECIAL SUBSTITUTIONS:
{json.dumps(knowledge['substitutions'], indent=2)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TASK: Analyze the calculus problem in the image using THREE DISTINCT STRATEGIES.

═════════════════════════════════════════════════
TRIPLE-STRATEGY ANALYSIS FRAMEWORK:
═════════════════════════════════════════════════

STRATEGY 1️⃣ - CENGAGE METHOD (Textbook Rigor):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal: Systematic, step-by-step, 100% rigorous solution
Approach: Standard calculus rules, show every algebraic step

Step 1: OBSERVE & EXTRACT
- Read the problem carefully
- Identify: What function? Differentiate or integrate?
- List all given information
- Note domain restrictions

Step 2: CLASSIFY FUNCTION TYPE
- Polynomial? Trigonometric? Exponential? Logarithmic?
- Product? Quotient? Composite?

Step 3: SELECT TECHNIQUE
- For differentiation: Power rule? Chain rule? Product rule? Quotient rule?
- For integration: Direct formula? Substitution? By parts? Partial fractions?

Step 4: EXECUTE STEP-BY-STEP
- Show EVERY algebraic manipulation
- Simplify at each step
- Check domain restrictions

Step 5: FINALIZE ANSWER
- Add +C for indefinite integrals
- Evaluate limits for definite integrals
- Verify domain is valid

ANSWER 1: [Your systematic answer]
CONFIDENCE 1: [70-100%]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRATEGY 2️⃣ - BLACK BOOK SHORTCUTS (JEE Speed Tricks):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal: Solve in 3-10 seconds using pattern recognition
Approach: Memorized patterns, symmetry, shortcuts

PATTERN RECOGNITION:
- Is this a standard form I've memorized?
- Can I use King's Property: ∫[a,b] f(x)dx = ∫[a,b] f(a+b-x)dx?
- Is the function even/odd? (Use symmetry)
- Is there f'(x) in the numerator? (Quick substitution)
- Is this (f(x))^n · f'(x)? (Power rule for integration)

SHORTCUT APPLIED:
- Which specific shortcut from the knowledge base applies?
- Why is this faster than standard method?

QUICK SOLUTION:
- Execute the shortcut
- Get answer in minimal steps

ANSWER 2: [Your shortcut answer]
CONFIDENCE 2: [70-100%]
TIME SAVED: [Estimate how much faster this is]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRATEGY 3️⃣ - OLYMPIAD/EXCEPTIONAL (Elegant Insights):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal: Beautiful, insightful, "wow" solution
Approach: Advanced techniques, clever tricks

EXCEPTIONAL TECHNIQUES TO CONSIDER:
- Feynman's trick (differentiation under integral sign)
- Weierstrass substitution (t = tan(θ/2))
- Complex variable methods
- Symmetry exploitation
- Geometric interpretation
- Series expansion approach

THE INSIGHT:
- What makes this problem special?
- Is there a hidden symmetry?
- Can we transform it cleverly?

ELEGANT METHOD:
- Apply the exceptional technique
- Show why this is more beautiful than standard

ANSWER 3: [Your elegant answer]
CONFIDENCE 3: [70-100%]
ELEGANCE FACTOR: [Why is this method superior?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

═════════════════════════════════════════════════
FINAL SYNTHESIS & VERIFICATION:
═════════════════════════════════════════════════

CROSS-VERIFICATION:
✓ Strategy 1 Answer: [...]
✓ Strategy 2 Answer: [...]
✓ Strategy 3 Answer: [...]

DO ALL THREE AGREE? [YES/NO]
- If YES: High confidence, all methods converge
- If NO: Identify discrepancy, recheck calculations

JEE TRAP CHECKLIST:
✓ Did I add +C for indefinite integral?
✓ Did I check domain restrictions (ln, sqrt, tan)?
✓ Did I use |x| for ln(1/x) integration?
✓ Did I evaluate limits correctly for definite integrals?
✓ Did I simplify completely?

GRAPHICAL CHECK (if applicable):
- Should I visualize this function?
- Does the derivative make sense? (positive where increasing, etc.)
- Does the integral area match intuition?

═════════════════════════════════════════════════
ULTIMATE ANSWER:
═════════════════════════════════════════════════

FINAL ANSWER: Option [A/B/C/D] OR [Numerical value]

ONE-SENTENCE CLEAR REASON:
[Explain in ONE clear sentence why this is the answer]

FINAL CONFIDENCE: [85-100%]

VERIFICATION STATUS:
✓ All 3 strategies agree: [YES/NO]
✓ JEE traps checked: [YES/NO]
✓ SymPy will verify: [Mention key steps to verify]

═════════════════════════════════════════════════

CRITICAL INSTRUCTIONS:
1. You MUST provide all 3 strategies, even if they're similar
2. Show actual calculation steps, not just descriptions
3. Be specific with formulas (use proper notation)
4. Check for JEE-specific traps (they love catching +C, domain issues)
5. If strategies disagree, LOWER confidence and explain why
6. Give a clear, definitive answer at the end

Begin analysis now! 🧮
"""
        return prompt
    
    async def solve(self, image_path: str):
        """Solve calculus problem with triple-strategy approach"""
        try:
            # Open image from path
            image = Image.open(image_path)
            
            # Convert image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG', quality=98)
            img_byte_arr = img_byte_arr.getvalue()
            
            # Build prompt
            prompt = self.build_ultimate_prompt()
            
            # Call Gemini with image
            response = self.model.generate_content(
                [prompt, image],
                generation_config=genai.types.GenerationConfig(
                    temperature=0.05,  # Low temperature for consistency
                    top_p=0.95,
                    top_k=40,
                    max_output_tokens=8192,
                )
            )
            
            analysis = response.text
            
            # Parse response
            solution_data = self.parse_response(analysis)
            
            # Verify with SymPy
            verification_result = self.verifier.verify_solution(solution_data)
            solution_data['sympy_verification'] = verification_result
            
            # Generate graphs if needed
            solution_data['graphs'] = self.verifier.generate_graphs(solution_data)
            
            return solution_data
            
        except Exception as e:
            # Try rotating API key on error
            self.rotate_api_key()
            raise e
    
    def parse_response(self, analysis: str):
        """Parse Gemini's response into structured data"""
        # Extract key information from the response
        solution_data = {
            'full_analysis': analysis,
            'strategy_1': self.extract_section(analysis, 'STRATEGY 1', 'STRATEGY 2'),
            'strategy_2': self.extract_section(analysis, 'STRATEGY 2', 'STRATEGY 3'),
            'strategy_3': self.extract_section(analysis, 'STRATEGY 3', 'FINAL SYNTHESIS'),
            'final_synthesis': self.extract_section(analysis, 'FINAL SYNTHESIS', 'ULTIMATE ANSWER'),
            'final_answer': self.extract_final_answer(analysis),
            'one_sentence_reason': self.extract_reason(analysis),
            'confidence': self.extract_confidence(analysis),
            'all_agree': 'YES' in analysis and 'ALL THREE AGREE' in analysis.upper(),
        }
        
        return solution_data
    
    def extract_section(self, text: str, start_marker: str, end_marker: str):
        """Extract text between two markers"""
        try:
            start_idx = text.find(start_marker)
            end_idx = text.find(end_marker, start_idx)
            if start_idx != -1 and end_idx != -1:
                return text[start_idx:end_idx].strip()
            return ""
        except:
            return ""
    
    def extract_final_answer(self, text: str):
        """Extract final answer"""
        try:
            if 'FINAL ANSWER:' in text:
                answer_line = text.split('FINAL ANSWER:')[1].split('\n')[0]
                return answer_line.strip()
            return "Unable to extract answer"
        except:
            return "Unable to extract answer"
    
    def extract_reason(self, text: str):
        """Extract one-sentence reason"""
        try:
            if 'ONE-SENTENCE' in text.upper():
                reason_section = text.split('ONE-SENTENCE')[1]
                reason_line = reason_section.split('\n')[1]
                return reason_line.strip()
            return "See detailed analysis above"
        except:
            return "See detailed analysis above"
    
    def extract_confidence(self, text: str):
        """Extract confidence percentage"""
        try:
            if 'FINAL CONFIDENCE:' in text:
                conf_line = text.split('FINAL CONFIDENCE:')[1].split('\n')[0]
                # Extract number
                import re
                numbers = re.findall(r'\d+', conf_line)
                if numbers:
                    return int(numbers[0])
            return 90  # Default
        except:
            return 90
