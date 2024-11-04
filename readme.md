# JSON TeX Resume

This project abstracts LaTeX resume creation into JSON configuration definitions. 

## Template

The resume template is defined through generic `.tex` components in the [components folder](./components/). These are used as the building blocks for the candidate's final resume. The components are meant to use minimal static values and rely on LaTeX variable definitions to populate the resume sections. These variable values are defined in our JSON configs. 

## JSON Configuration

Most LaTeX components are not self sufficient and will not compile without their variable definitions. The definitions are housed in JSON files in the [config folder](./config/). The field names follow the required variable uses in the LaTeX template, and the values defined are reflected in the final PDF. 

The resume sections are defined in the [sections.json](./config/sections.json) file and needs to follow this format:

```json
[
    {
        "sectionName": "Experience",
        "subheadings": [
            {
                "company": "No Name Legacy Software Inc.",
                "period": "May 2023 - Next Layoff Round",
                "position": "Internal Tools Developer",
                "location": "localhost",
                "resumeItems": [
                    "Did this and that",
                    "Achieved this and that"
                ]
            },
            ...
        ]
    },
    ...
]
```

If any of the fields are not required, they need to be defined and can be kept empty. 

[heading.json](./config/heading.json) is kept separate to define the candidate's information separate from the rest of the content. Following format is required:

```json
{
    "candidateFirstName": "Raging",
    "candidateLastName": "Chipmunk",
    "candidateAddress": "Non Doxable Address",
    "candidatePhone": "+1 (123) 456-7812",
    "candidateEmail": "email@personal.com",
    "linkedin": "linkedin",
    "github": "github"
}
```
## Python Script

[generate_resume.py](./generate_resume.py) is the main script that glues all the components and their respective configurations together. It iterates over the configuration files, translates them into variable definitions in LaTeX, and adds all the components to one single file called `resume.tex`. 

## Create Your Resume

### Pre-requisites
- Python3
- LaTeX

> This repo will be containerized at a later point. For now, you have to deal with this mediocre setup :)

1. Populate [JSON configs as defined above](#json-configuration).
2. Run `python3 generate_resume.py`
3. Run `pdflatex resume.tex`

## License

MIT License.
