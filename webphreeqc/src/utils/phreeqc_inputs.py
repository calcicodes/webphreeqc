from pathlib import Path

template_path = Path(__file__).parent / 'input_templates'

PHREEQC_INPUT_TEMPLATES = {
    "Blank": ""
}

for template in template_path.glob('*.phreeqc'):
    with open(template, 'r') as f:
        PHREEQC_INPUT_TEMPLATES[template.stem] = f.read()
