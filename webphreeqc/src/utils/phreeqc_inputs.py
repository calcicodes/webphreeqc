from pathlib import Path

template_path = Path(__file__).parent / 'input_templates'

PHREEQC_INPUT_TEMPLATES = {
    "Blank": """# Write your PHREEQC input file here, or select a template from the dropdown above. 
    
# See the PHREEQC documentation for details: https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3.htm

# The EXAMPLES pages are particularly useful: https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3-62.htm
"""
}

for template in sorted(template_path.glob('*.phreeqc')):
    with open(template, 'r') as f:
        PHREEQC_INPUT_TEMPLATES[template.stem] = f.read()

