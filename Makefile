
ubuntu:
	cd ubuntu; \
	docker build -t ubuntubase .

python:
	cd miniconda3; \
	docker build -t pythonbase .

opencv:
	cd opencv3; \
	docker build -t opencv .
