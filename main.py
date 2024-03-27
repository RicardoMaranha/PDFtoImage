from pdf2image import convert_from_path

pages = convert_from_path('conformidades.pdf', dpi=200)
i = 0
for img in pages:
       img.save(f'teste_{i}.png', 'PNG')
       i += 1
       