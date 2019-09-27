
all:
	make prepare
	make install
	make test

prepare:
	pip install virtualenv
	virtualenv venv

install:
	( source venv/bin/activate; python setup.py install )

test:
	( source venv/bin/activate; CUDA_VISIBLE_DEVICES=-1 python test/0.py )
