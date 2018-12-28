from markdown import markdown
import pdfkit

input_filename = 'frequency.md'
output_filename = 'frequency.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)