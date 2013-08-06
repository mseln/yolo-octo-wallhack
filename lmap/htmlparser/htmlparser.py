import re

f = open('stat.tex')

s = f.read()

s = re.sub(r'\\documentclass{(.*?)}', r'', s)
s = re.sub(r'\\usepackage{(.*?)}', r'', s)
s = re.sub(r'\\author{(.*?)}', r'', s)
s = re.sub(r'\\maketitle', r'', s)
s = re.sub(r'\%.*', r'', s)

s = re.sub(r'\\section{(.*?)}', r'<h2>\1</h2>', s)
s = re.sub(r'\\subsection{(.*?)}', r'<h3>\1</h3>', s)
s = re.sub(r'\\xcise{(.*?)}', r'<h4>\1</h4>', s)
s = re.sub(r'\\ptask{(.*?)}', r'<h5>\1</h5>', s)

s = re.sub(r'$(.*?)$', r'<i>\1</i>', s)
s = re.sub(r'\\emph{(.*?)}', r'<b>\1</b>', s)
s = re.sub(r'\\textbf{(.*?)}', r'<b>\1</b>', s)
s = re.sub(r'\\texttt{(.*?)}', r'<code>\1</code>', s)
s = re.sub(r'\\texttt{(.*?)}', r'<code>\1</code>', s)

s = re.sub(r'\\dots', r'...', s)
s = re.sub(r'\\link{(.*?)}', r'<a href="\1">\1</a>', s)
s = re.sub(r'\\url{(.*?)}', r'<a href="\1">\1</a>', s)
s = re.sub(r'\\newline', '<br>', s)
s = re.sub(r'(\\\\)', r'<br>', s)

o = open('parsed.html', 'r+')
o.write(s)
