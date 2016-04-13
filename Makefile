###############################################
### DOCONCE MAKEFILE V 1.0 - Daniel-M. 2015 ###
###############################################


################################
## Doconce Sources
################################

# Name of the main doconce file without extension
PROJECT = README

######################
## Compilation Options
######################

# Command to compile latex source
DOCONCE = doconce

# List of formats to include

FORMATS = pandoc

# Commmand to build the latex project into PDF (or DVI according to $(DOCONCE).
BUILD_DOCONCE = $(DOCONCE) format $(FORMATS) $(PROJECT).do.txt --encoding=utf-8

# Command to build pandoc
PANDOC = pandoc
PANDOC_OPTIONS = --toc -V geometry:letterpaper -V geometry:margin=3cm 
BUILD_PANDOC_PDF = pandoc $(PROJECT).md $(PANDOC_OPTIONS) -o $(PROJECT).pdf

TARGETS = $(PROJECT).do.txt

##############################
## DEFINING TARGETS OPERATIONS
##############################

all: $(TARGETS)
	echo "$(TARGETS)"
	echo "$(PROJECT)"
	$(BUILD_DOCONCE)
	$(BUILD_PANDOC_PDF)
	rm -f tmp_*.do.txt 

$(PROJECT).pdf: $(TARGETS)
	$(BUILD_DOCONCE)
	$(BUILD_PANDOC_PDF)
	rm -f tmp_*.do.txt 

# Clean all temporary resource files created during the compilation of the master file
clean:
	rm -f tmp_*.do.txt *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.lof *.lot *.nlo *.nls *.ist *.ilg
	rm -f $(CHAPTERSDIR)/*.log $(CHAPTERSDIR)/*.bak $(CHAPTERSDIR)/*.aux $(CHAPTERSDIR)/*.bbl $(CHAPTERSDIR)/*.blg $(CHAPTERSDIR)/*.idx $(CHAPTERSDIR)/*.toc $(CHAPTERSDIR)/*.out $(CHAPTERSDIR)/*~  $(CHAPTERSDIR)/*.nlo $(CHAPTERSDIR)/*.nls $(CHAPTERSDIR)/*.ist $(CHAPTERSDIR)/*.ilg
	rm -f $(TABLES)/*.log $(TABLES)/*.bak $(TABLES)/*.aux $(TABLES)/*.bbl $(TABLES)/*.blg $(TABLES)/*.idx $(TABLES)/*.toc $(TABLES)/*.out $(TABLES)/*~ $(TABLES)/*.nlo $(TABLES)/*.nls $(TABLES)/*.ist $(TABLES)/*.ilg
	rm -f $(APPENDICESDIR)/*.log $(APPENDICESDIR)/*.bak $(APPENDICESDIR)/*.aux $(APPENDICESDIR)/*.bbl $(APPENDICESDIR)/*.blg $(APPENDICESDIR)/*.idx $(APPENDICESDIR)/*.toc $(APPENDICESDIR)/*.out $(APPENDICESDIR)/*~ $(APPENDICESDIR)/*.nlo $(APPENDICESDIR)/*.nls $(APPENDICESDIR)/*.ist $(APPENDICESDIR)/*.ilg

# Clean all temporary resource files created during compilation and delete the latex output.
clean-all:
	rm -f tmp_*.do.txt *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.lof *.lot *.nlo *.nls *.ist *.ilg
	rm -f $(CHAPTERSDIR)/*.dvi $(CHAPTERSDIR)/*.log $(CHAPTERSDIR)/*.bak $(CHAPTERSDIR)/*.aux $(CHAPTERSDIR)/*.bbl $(CHAPTERSDIR)/*.blg $(CHAPTERSDIR)/*.idx $(CHAPTERSDIR)/*.ps $(CHAPTERSDIR)/*.eps $(CHAPTERSDIR)/*.pdf $(CHAPTERSDIR)/*.toc $(CHAPTERSDIR)/*.out $(CHAPTERSDIR)/*~  $(CHAPTERSDIR)/*.nlo $(CHAPTERSDIR)/*.nls $(CHAPTERSDIR)/*.ist $(CHAPTERSDIR)/*.ilg
	rm -f $(TABLES)/*.dvi $(TABLES)/*.log $(TABLES)/*.bak $(TABLES)/*.aux $(TABLES)/*.bbl $(TABLES)/*.blg $(TABLES)/*.idx $(TABLES)/*.ps $(TABLES)/*.eps $(TABLES)/*.pdf $(TABLES)/*.toc $(TABLES)/*.out $(TABLES)/*~ $(TABLES)/*.nlo $(TABLES)/*.nls $(TABLES)/*.ist $(TABLES)/*.ilg
	rm -f $(APPENDICESDIR)/*.dvi $(APPENDICESDIR)/*.log $(APPENDICESDIR)/*.bak $(APPENDICESDIR)/*.aux $(APPENDICESDIR)/*.bbl $(APPENDICESDIR)/*.blg $(APPENDICESDIR)/*.idx $(APPENDICESDIR)/*.ps $(APPENDICESDIR)/*.eps $(APPENDICESDIR)/*.pdf $(APPENDICESDIR)/*.toc $(APPENDICESDIR)/*.out $(APPENDICESDIR)/*~ $(APPENDICESDIR)/*.nlo $(APPENDICESDIR)/*.nls $(APPENDICESDIR)/*.ist $(APPENDICESDIR)/*.ilg

