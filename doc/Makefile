DATE=`date +%d.%m.%Y`
PARAMS=-s -N --pdf-engine=xelatex -V papersize=a4 -V documentclass=scrartcl -V classoption=12pt -V mainfont="DejaVu Serif" -V sansfont="DejaVu Sans" -V monofont="DejaVu Sans Mono" -V lang=de -V urlcolor=blue -V title='Mongomir Pytkovic' -V subtitle='Migration einer SQLite-Datenbank nach MongoDB mit Python' -V author='Modul Datenbanksysteme (DBS) \\ \\ Gruppe 7 \\ L. Arnold, P. Bucher, C. J. Christensen, J. Kaiser, M. Werthmüller \\ \\ Herbstsemester 2017'

Projekt_Gruppe_7_Mongomir-Pytkovic.pdf: Projekt_Gruppe_7_Mongomir-Pytkovic.md
	pandoc $(PARAMS) -V date=$(DATE) Projekt_Gruppe_7_Mongomir-Pytkovic.md -o Projekt_Gruppe_7_Mongomir-Pytkovic.pdf

clean:
	rm Projekt_Gruppe_7_Mongomir-Pytkovic.pdf
