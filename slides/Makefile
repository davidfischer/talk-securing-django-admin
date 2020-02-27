.PHONY: pdf clean
RM = /bin/rm -rf

# Latex utils
PDFLATEX = pdflatex
OPTIONS = --shell-escape

FINAL_TITLE = securing-the-django-admin.pdf

all: pdf

pdf:
	$(PDFLATEX) $(OPTIONS) talk.tex
	cp talk.pdf $(FINAL_TITLE)

clean:
	$(RM) *.aux *.log *.dvi *.pdf *.txt *.gz *.nav *.out *.snm *.toc *.vrb _minted-talk
