"""
JEE Calculus Knowledge Base
Contains: Rules, shortcuts, traps, patterns, substitutions
Similar to chemistry bot's NGP rules but for calculus
"""

CALCULUS_KNOWLEDGE = {
    "differentiation_rules": {
        "power_rule": "d/dx(x^n) = n·x^(n-1)",
        "constant_rule": "d/dx(c) = 0",
        "constant_multiple": "d/dx(c·f(x)) = c·f'(x)",
        "sum_rule": "d/dx(f + g) = f' + g'",
        "product_rule": "d/dx(u·v) = u'·v + u·v'",
        "quotient_rule": "d/dx(u/v) = (u'·v - u·v')/v²",
        "chain_rule": "d/dx(f(g(x))) = f'(g(x))·g'(x)",
        
        "standard_derivatives": {
            "sin": "d/dx(sin x) = cos x",
            "cos": "d/dx(cos x) = -sin x",
            "tan": "d/dx(tan x) = sec² x",
            "exp": "d/dx(e^x) = e^x",
            "ln": "d/dx(ln x) = 1/x, x > 0",
            "sqrt": "d/dx(√x) = 1/(2√x), x > 0",
        },
        
        "implicit_differentiation": "Differentiate both sides with respect to x, use dy/dx terms",
        "parametric": "dy/dx = (dy/dt)/(dx/dt)",
        "logarithmic": "For complex products/quotients, take ln first, then differentiate",
    },
    
    "integration_techniques": {
        "power_rule": "∫x^n dx = x^(n+1)/(n+1) + C, n ≠ -1",
        "logarithmic": "∫(1/x) dx = ln|x| + C",
        "exponential": "∫e^x dx = e^x + C",
        
        "standard_integrals": {
            "sin": "∫sin x dx = -cos x + C",
            "cos": "∫cos x dx = sin x + C",
            "sec²": "∫sec² x dx = tan x + C",
            "cosec²": "∫cosec² x dx = -cot x + C",
            "sec_tan": "∫sec x tan x dx = sec x + C",
            "1_over_sqrt": "∫1/√(a²-x²) dx = sin⁻¹(x/a) + C",
            "1_over_sum": "∫1/(a²+x²) dx = (1/a)tan⁻¹(x/a) + C",
        },
        
        "substitution": {
            "when_to_use": "When you see f'(x) in the integrand along with f(x)",
            "pattern": "∫f'(x)·g(f(x)) dx → substitute u = f(x)",
            "example": "∫(2x)/(x²+1) dx = ln|x²+1| + C instantly",
        },
        
        "f_prime_times_f_power": {
            "formula": "∫f'(x)·[f(x)]^n dx = [f(x)]^(n+1)/(n+1) + C",
            "pattern": "Derivative times power of function",
            "time_saved": "Direct integration without substitution",
            "example": "∫2x·(x²)^3 dx = (x²)^4/4 + C",
        },
        
        "linear_over_linear": {
            "formula": "∫(ax+b)/(cx+d) dx = (a/c)x + ((bc-ad)/c²)ln|cx+d| + C",
            "when_to_use": "Linear numerator, linear denominator",
            "time_saved": "5 seconds with memorized formula",
        },
        
        "trigonometric_products": {
            "sin_cos": "∫sin(mx)cos(nx) dx → Use product-to-sum formulas",
            "sin_sin": "∫sin(mx)sin(nx) dx → Use product-to-sum formulas",
            "cos_cos": "∫cos(mx)cos(nx) dx → Use product-to-sum formulas",
        },
    },
    
    "substitutions": {
        "sqrt_a2_minus_x2": {
            "form": "√(a² - x²)",
            "substitution": "x = a·sin(θ)",
            "result": "√(a² - x²) = a·cos(θ)",
            "use_case": "Integrals involving √(a² - x²)",
        },
        
        "sqrt_a2_plus_x2": {
            "form": "√(a² + x²)",
            "substitution": "x = a·tan(θ)",
            "result": "√(a² + x²) = a·sec(θ)",
            "use_case": "Integrals involving √(a² + x²)",
        },
        
        "sqrt_x2_minus_a2": {
            "form": "√(x² - a²)",
            "substitution": "x = a·sec(θ)",
            "result": "√(x² - a²) = a·tan(θ)",
            "use_case": "Integrals involving √(x² - a²)",
        },
        
        "weierstrass": {
            "form": "Rational function of sin(x) and cos(x)",
            "substitution": "t = tan(x/2)",
            "formulas": {
                "sin_x": "sin(x) = 2t/(1+t²)",
                "cos_x": "cos(x) = (1-t²)/(1+t²)",
                "dx": "dx = 2dt/(1+t²)",
            },
            "use_case": "Complex trigonometric integrals",
            "note": "Very powerful but algebraically intensive",
        },
        
        "exponential_trick": {
            "form": "∫e^x·f(x) dx where f can be repeatedly differentiated",
            "method": "∫e^x(f + f') dx = e^x·f + C",
            "use_case": "e^x times polynomial or trigonometric",
        },
    },
    
    "olympiad_tricks": {
        "feynman_technique": {
            "name": "Differentiation under integral sign",
            "description": "Introduce parameter, differentiate with respect to it",
            "example": "To find ∫x·e^x dx, consider I(a) = ∫e^(ax)dx, then dI/da",
            "difficulty": "Advanced",
        },
        
        "symmetry_exploitation": {
            "description": "Use geometric/algebraic symmetry to simplify",
            "example": "∫[0,1] x^4(1-x)^4/(1+x²) dx uses symmetry x → 1-x",
        },
        
        "series_expansion": {
            "description": "Expand integrand as Taylor series, integrate term-by-term",
            "when_to_use": "When standard methods fail",
            "example": "∫e^(-x²) dx → expand e^(-x²) as series",
        },
        
        "complex_variables": {
            "description": "Use Euler's formula: e^(ix) = cos(x) + i·sin(x)",
            "when_to_use": "Products of trigonometric functions",
            "note": "Very elegant but requires complex number knowledge",
        },
    },
    
    "common_functions": {
        "recognize_derivatives": {
            "e^x_times_stuff": "If you see e^x·[...], check if [...] = f(x) + f'(x)",
            "ln_patterns": "d/dx[x·ln(x) - x] = ln(x), useful for ∫ln(x)dx",
            "inverse_trig": "Recognize derivatives of sin⁻¹, tan⁻¹, sec⁻¹",
        },
        
        "common_antiderivatives": {
            "x_ln_x": "∫ln(x) dx = x·ln(x) - x + C",
            "x_e^x": "∫x·e^x dx = (x-1)·e^x + C",
            "e^x_sin_x": "∫e^x·sin(x) dx = (e^x/2)·(sin(x) - cos(x)) + C",
            "e^x_cos_x": "∫e^x·cos(x) dx = (e^x/2)·(sin(x) + cos(x)) + C",
        },
    },
    
    "graph_indicators": {
        "increasing_decreasing": {
            "increasing": "f'(x) > 0 → function increasing",
            "decreasing": "f'(x) < 0 → function decreasing",
            "critical_points": "f'(x) = 0 → local max/min candidates",
        },
        
        "concavity": {
            "concave_up": "f''(x) > 0 → concave up (cup shape)",
            "concave_down": "f''(x) < 0 → concave down (cap shape)",
            "inflection_point": "f''(x) = 0 → possible inflection point",
        },
        
        "integral_interpretation": {
            "area": "∫[a,b] f(x)dx = area between curve and x-axis",
            "positive_area": "f(x) > 0 → positive area",
            "negative_area": "f(x) < 0 → negative area (below axis)",
        },
    },
    
    "jee_specific_patterns": {
        "definite_integral_zero": [
            "∫[-a,a] f(x)dx = 0 if f is odd",
            "∫[0,2a] f(x)dx = 0 if f(x) + f(2a-x) = 0",
        ],
        
        "reduction_formulas": {
            "sin_n": "∫sin^n(x)dx involves reduction using sin²(x) = 1 - cos²(x)",
            "cos_n": "∫cos^n(x)dx involves reduction using cos²(x) = 1 - sin²(x)",
            "note": "Often tested in JEE Advanced",
        },
        
        "parametric_tricks": {
            "dx_dt_and_dy_dt": "Given x(t) and y(t), find dy/dx = (dy/dt)/(dx/dt)",
            "area_parametric": "Area = ∫y·(dx/dt)·dt",
        },
    },
}

# Additional knowledge sources (loaded on demand)
GITHUB_KNOWLEDGE_SOURCES = {
    "deepmind_math": "https://github.com/google-deepmind/mathematics_dataset",
    "awesome_math": "https://github.com/rossant/awesome-math",
    "integration_tricks": "https://brilliant.org/wiki/integration-tricks/",
}

# JEE exam statistics
JEE_STATS = {
    "calculus_weightage": "35-40% of JEE Advanced paper",
    "common_topics": [
        "Definite integrals with limits",
        "Area between curves",
        "Differentiation of implicit functions",
        "Integration by parts",
        "Substitution methods",
    ],
    "difficulty_distribution": {
        "easy": "20% - Direct formula application",
        "medium": "50% - Requires technique selection",
        "hard": "30% - Multiple steps, tricky substitutions",
    },
}
∫2x·e^(x²) dx → u = x², du = 2x dx",
        },
        
        "by_parts": {
            "formula": "∫u dv = uv - ∫v du",
            "when_to_use": "Product of polynomial and (e^x, ln x, sin/cos)",
            "ILATE_priority": "I=Inverse trig, L=Logarithmic, A=Algebraic, T=Trigonometric, E=Exponential",
            "choose_u": "Pick u from higher priority in ILATE",
        },
        
        "partial_fractions": {
            "when_to_use": "Rational function (polynomial/polynomial) with degree(numerator) < degree(denominator)",
            "linear_factors": "(x-a)(x-b) → A/(x-a) + B/(x-b)",
            "repeated_linear": "(x-a)² → A/(x-a) + B/(x-a)²",
            "quadratic": "(x²+bx+c) → (Ax+B)/(x²+bx+c)",
        },
        
        "decision_tree": {
            "check_1": "Is there f'(x) in numerator? → Use substitution",
            "check_2": "Is it a product? → Consider by parts or substitution",
            "check_3": "Is it rational? → Partial fractions",
            "check_4": "Is there √(a²±x²)? → Trigonometric substitution",
            "check_5": "Can it be simplified first? → Do algebraic manipulation",
        },
    },
    
    "jee_traps": {
        "trap_1_constant": {
            "description": "Forgetting +C in indefinite integrals",
            "impact": "CRITICAL - Answer is WRONG without +C",
            "check": "ALWAYS add +C for indefinite integrals",
        },
        
        "trap_2_domain": {
            "description": "Ignoring domain restrictions",
            "examples": [
                "ln(x) only defined for x > 0",
                "√x only defined for x ≥ 0",
                "tan(x) undefined at x = π/2 + nπ",
                "1/x undefined at x = 0",
            ],
            "check": "State domain explicitly",
        },
        
        "trap_3_absolute_value": {
            "description": "∫(1/x)dx = ln|x| + C, NOT ln(x) + C",
            "reason": "x can be negative, need absolute value",
            "check": "Use |x| inside ln when integrating 1/x",
        },
        
        "trap_4_limits": {
            "description": "Incorrectly evaluating definite integrals",
            "common_mistakes": [
                "Forgetting to substitute both upper and lower limits",
                "Sign errors when subtracting F(a) from F(b)",
                "Not checking if function is continuous in [a,b]",
            ],
            "formula": "∫[a,b] f(x)dx = F(b) - F(a)",
        },
        
        "trap_5_simplification": {
            "description": "Not simplifying final answer completely",
            "check": "Factor, cancel common terms, rationalize denominators",
        },
        
        "trap_6_implicit": {
            "description": "Forgetting dy/dx terms in implicit differentiation",
            "example": "d/dx(y²) = 2y·(dy/dx), NOT just 2y",
        },
        
        "trap_7_chain_rule": {
            "description": "Forgetting inner derivative in chain rule",
            "example": "d/dx(sin(x²)) = cos(x²)·2x, NOT just cos(x²)",
        },
    },
    
    "shortcuts": {
        "kings_property": {
            "formula": "∫[a,b] f(x)dx = ∫[a,b] f(a+b-x)dx",
            "when_to_use": "Definite integrals with limits a to b",
            "time_saved": "Can reduce complex integrals to simple forms in seconds",
            "example": "∫[0,π] x·sin(x)dx = ∫[0,π] (π-x)·sin(π-x)dx",
        },
        
        "even_function": {
            "formula": "∫[-a,a] f(x)dx = 2∫[0,a] f(x)dx if f(-x) = f(x)",
            "when_to_use": "Symmetric limits and even function",
            "time_saved": "Halves the integration range",
        },
        
        "odd_function": {
            "formula": "∫[-a,a] f(x)dx = 0 if f(-x) = -f(x)",
            "when_to_use": "Symmetric limits and odd function",
            "time_saved": "Answer is instantly 0!",
        },
        
        "f_prime_over_f": {
            "formula": "∫f'(x)/f(x) dx = ln|f(x)| + C",
            "pattern": "Derivative of denominator in numerator",
            "time_saved": "Instant answer without substitution",
            "example": "
