# from markdown_pdf import MarkdownPdf, Section

# pdf = MarkdownPdf(toc_level=2)

# q = ''
# with open('Строка.md', 'r', encoding='utf8') as f:
#     q = f.read()
# pdf.add_section(Section(q))
# pdf.save('test.pdf')
from markdown_it import MarkdownIt

md = (
    MarkdownIt('commonmark', {'breaks': True, 'html': True}).enable('table')
)
q = ''
with open('Строка.md', 'r', encoding='utf8') as f:
    q = f.read()
html_text = md.render(q)
print(html_text)
