from starlette.responses import FileResponse
import tempfile
import jinja2
import pdfkit


def create_pdf(template_path: str, data: dict, css_path: str, name_file: str):
    template_name = template_path.split('/')[-1]
    template_path = template_path.replace(template_name, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
    template = env.get_template(template_name)
    html = template.render(data)
    
    options = {
        'page-size': 'Letter',
        'margin-top': '0.15in',
        'margin-right': '0.15in',
        'margin-bottom': '0.15in',
        'margin-left': '0.15in',
        'encoding': 'UTF-8'
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    pdf = pdfkit.from_string(html, False, css=css_path, options=options, configuration=config)

    with tempfile.NamedTemporaryFile(mode='w+b', suffix='.pdf', delete=False) as TPDF:
        TPDF.write(pdf)
        return FileResponse(
                TPDF.name,
                media_type='application/pdf',
                filename=f'{name_file}.pdf'
            )
