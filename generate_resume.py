import json

def load_data(filename, is_json=False):
    with open(filename, "r") as file:
        return json.load(file) if is_json else file.read()

def define_variable(latex, name, value):
    return latex + f"\\def\\{name}{{{value}}}\n"

def retrieve_value(key, json_config):
    value = json_config[key]
    
    if isinstance(value, list) and not isinstance(value[0], dict):
        return ', '.join(value)

    return value

def define_variables(latex, json_config, filter=lambda key, value: True):
    if json_config is None:
        return
    
    if latex is None:
        latex = ""

    for key in json_config:
        var_value = retrieve_value(key, json_config)
        if (not filter(key, var_value)): continue

        latex = define_variable(latex, key, var_value)
    
    return latex

def load_subheading(latex, subheading_config):
    latex = define_variables(latex, subheading_config)
    latex += load_data('./components/subheading.tex')
    return latex

def load_subheadings(latex, section_config):
    for subheading in section_config['subheadings']:
        latex = load_subheading(latex, subheading)

    return latex

def load_section(latex, section_config):
    latex = define_variables(latex, section_config, lambda key, value: key == "sectionName")
    latex += load_data('./components/section.tex')
    latex = load_subheadings(latex, section_config)
    latex += load_data('./components/sectionEnd.tex')
    latex += load_data('./components/end.tex')    
    return latex

def load_sections(latex, body_config):
    for section in body_config:
        latex = load_section(latex, section)

    return latex

def load_content():
    latex = ''
    latex += load_data('./components/base.tex')
    
    heading_config = load_data('./config/heading.json', True)
    latex = define_variables(latex, heading_config)
    latex += load_data('./components/heading.tex')

    body_config = load_data('./config/sections.json', True)
    latex = load_sections(latex, body_config)
    return latex

def write_latex_resume(latex):
    with open('./resume.tex', 'w') as file:
        file.write(latex)

latex = load_content()
write_latex_resume(latex)