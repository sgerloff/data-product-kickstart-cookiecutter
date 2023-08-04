#!/bin/bash
curl -X POST http://0.0.0.0:8080{{cookiecutter.endpoint_name}} --header "Content-Type: application/json" -d '{"someInput": "asdf"}'