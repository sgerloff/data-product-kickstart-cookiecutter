# Kickstart for Data Products (ML)

Personal template for developing in production data products. Generates boilerplate code for arbitrary projects, i.e.
- Installable python module to easily share code with inference systems
- Training script skeleton making use of hydra and mlflow
- FastAPI service for inference, including docker setup
- Github actions to manage the module version

Note, that this template is tuned to my personal taste and to some extent prone to change.

## Kickstart Your Project
```commandline
cookiecutter gh:sgerloff/data-product-kickstart-cookiecutter
```