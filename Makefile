
all:
	make prepare
	make install
	make example

prepare:
	pip install virtualenv
	virtualenv venv

install:
	( source venv/bin/activate; venv/bin/python setup.py install)

example:
	( source venv/bin/activate; CUDA_VISIBLE_DEVICES=-1 venv/bin/python test/0.py )
