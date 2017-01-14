
ubuntu:
	cd ubuntu; \
	docker build -t ubuntubase .

python: ubuntu
	cd miniconda3; \
	docker build -t pythonbase .

opencv3: python
	cd opencv3; \
	docker build -t opencv .

nodejs: ubuntu
	cd nodejs; \
	docker build -t nodejs .

