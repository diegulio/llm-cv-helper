# Makefile
SHELL = /bin/bash

# Environment
.ONESHELL:
install_packages:
	pip install poetry
	poetry shell
	poetry install

# Run
.ONESHELL:
run:
	poetry shell
	streamlit run main.py
