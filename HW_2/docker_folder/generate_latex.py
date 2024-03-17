from latex_code_create import table_generation, picture_generation

data = [
        ['Firstname', 'Lastname', 'Age'],
        ['Ann', 'Smirnova', '28'],
        ['Ivan', 'Ivanov', '45'],
        ['Fedor', 'Sidorov', '32']
    ]

latex_table = table_generation(data)
latex_table_file = '\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}' + latex_table + '\n\\end{document}'


image_latex = picture_generation('/app/pic_for_pdf.png')

latex_code = '\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}' + latex_table + "\n\n\n" + image_latex + '\n\\end{document}'

with open('table_and_pic.tex', 'w') as f:
    f.write(latex_code)