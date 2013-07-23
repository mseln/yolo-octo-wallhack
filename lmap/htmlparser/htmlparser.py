import re

def itemize(s) :
	return s.group()
#	print s.group()
#	s = re.sub(re.compile(r'\\begin{itemize}(.*?)\\end{itemize}', re.S), r'<ul>\1</ul>', s.group())
#	s = re.sub(re.compile(r'(?:(?!\\item\w).)(.*)', re.S), r'<li>\1</li>\n', s)
#	print s
#	return s
#
f = open('test.tex')

s = f.read()
# print s

s = re.sub(r'\\documentclass{(.*?)}', r'', s)
s = re.sub(r'\\usepackage{(.*?)}', r'', s)
s = re.sub(r'\\author{(.*?)}', r'', s)
s = re.sub(r'\\maketitle', r'', s)

s = re.sub(r'\\section{(.*?)}', r'<h1>\1</h1>', s)
s = re.sub(r'\\subsection{(.*?)}', r'<h2>\1</h2>', s)

s = re.sub(r'\\emph{(.*?)}', r'<b>\1</b>', s)
s = re.sub(r'\\textbf{(.*?)}', r'<b>\1</b>', s)
s = re.sub(r'\\texttt{(.*?)}', r'<code>\1</code>', s)

s = re.sub(r'\\dots', r'...', s)
s = re.sub(r'\\link{(.*?)}', r'<a href="\1">\1</a>', s)
s = re.sub(r'\\url{(.*?)}', r'<a href="\1">\1</a>', s)
s = re.sub(r'\\newline', '<br>', s)
s = re.sub(r'(\\\\)', r'<br>', s)

s = re.sub(re.compile(r'\\begin{itemize}(.*?)\\end{itemize}', re.S), itemize, s, re.S)

