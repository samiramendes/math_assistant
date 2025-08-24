import math
import numexpr
from langchain.tools import tool

@tool("calculator-tool")
def calculator(expression: str) -> str:
    """Calculate expression using Python's numexpr library.

    The expression must be a valid mathematical string (e.g., "128 * 46", "2**3 + 5", "pi * 2**2").

    Examples:
        "37593 * 67" for "37593 times 67"
        "37593**(1/5)" for "37593^(1/5)"
    """
    try:
        local_dict = {
            "pi": math.pi,
            "e": math.e,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "abs": abs,
            "pow": pow
        }
        result = numexpr.evaluate(
                expression.strip(),
                global_dict={},  # restrict access to globals
                local_dict=local_dict,  # add common mathematical functions
            )
        return str(result)
    
    except Exception as e:
        return (f"Failed to calculate the expression. Make sure it's a valid math expression using numbers and operators only (Error: {str(e)})"
)