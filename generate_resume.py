import json

def load_data(filename, is_json=False):
    with open(filename, "r") as file:
        return json.load(file) if is_json else file.read()

def define_variable(name, value):
    return f"\\def\\{name}{{{value}}}\n"

def retrieve_value(key, json_config):
    value = json_config[key]
    
    if isinstance(value, list):
        if len(value) <= 0: return ''
        if not isinstance(value[0], dict): return '{' + '}, {'.join(value) + '}' 

    return value

def define_variables(json_config, filter=lambda key, value: True):
    if json_config is None:
        return
    
    latex = ''

    for key in json_config:
        var_value = retrieve_value(key, json_config)
        if (not filter(key, var_value)): continue

        latex += define_variable(key, var_value)
    
    return latex

def load_heading(heading_config):
    latex = define_variables(heading_config)
    latex += load_data('./components/heading.tex')
    return latex

def load_subheading(subheading_config):
    latex = define_variables(subheading_config)
    latex += load_data('./components/subheading.tex')
    return latex

def load_subheadings(section_config):
    latex = ''

    for subheading in section_config['subheadings']:
        latex += load_subheading(subheading)

    return latex

def load_section(section_config):
    latex = define_variables(section_config, lambda key, value: key == "sectionName")
    latex += load_data('./components/section.tex')
    latex += load_subheadings(section_config)
    latex += load_data('./components/sectionEnd.tex')
    return latex

def load_sections(body_config):
    latex = ''

    for section in body_config:
        latex += load_section(section)

    return latex

def load_content():
    latex = ''
    latex += load_data('./components/base.tex')
    
    heading_config = load_data('./config/heading.json', True)
    latex += load_heading(heading_config)

    body_config = load_data('./config/sections.json', True)
    latex += load_sections(body_config)
    latex += load_data('./components/end.tex')

    return latex

def write_latex_resume(latex):
    with open('./resume.tex', 'w') as file:
        file.write(latex)

if __name__ == '__main__':
    latex = load_content()
    write_latex_resume(latex)