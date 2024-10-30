from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML

def render_pdf_view(request):
    # Load the template
    template = get_template('index.html')
    html = template.render({'name': 'Tobias', 'info': 'This is a sample PDF.'})
    
    # Convert HTML to PDF using WeasyPrint
    pdf = HTML(string=html).write_pdf()
    
    # Create the HTTP response with PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="template_pdf.pdf"'
    return response
