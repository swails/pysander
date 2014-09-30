include ../config.h

install: clean
	$(PYTHON) setup.py install --prefix $(AMBERHOME)

clean:
	/bin/rm -fr build/

skip:
	@echo ""
	@echo "Skipping installation of pysander."
	@echo ""

