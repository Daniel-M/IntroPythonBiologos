TARGETS=IntroPythonBiologos.do.txt $(find sections -type f -name "*.do.txt")

IntroPythonBiologos.ipynb: $(TARGETS) 
	doconce format ipynb IntroPythonBiologos.do.txt --encoding=utf-8

IntroPythonBiologos.md: $(TARGETS) 
	doconce format pandoc IntroPythonBiologos.do.txt --encoding=utf-8

IntroPythonBiologos.html: $(TARGETS) 
	doconce format html IntroPythonBiologos.do.txt --encoding=utf-8

clean:
	rm -rf tmp_* *.dolog

clean-all:
	rm -rf tmp_* *.dolog *.html *.pdf *.ipynb *.md 
