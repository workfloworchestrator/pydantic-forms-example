# Pydantic forms example

This repository contains a working example of a [FastAPI][1] application with the pydantic forms frontend and backend modules working together.
It shows how you can use the [pydantic forms pypy module][2] on top of pydantic models to automatically generate forms on the frontend using the [pydantic forms npm module][3] that ask for user input. It also show validation and processing of the user input.

[1]: https://fastapi.tiangolo.com/
[2]: https://pypi.org/project/pydantic-forms
[3]: https://www.npmjs.com/package/pydantic-forms

## installation

To install using a virtual environment:

```
$ python venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ fastapi dev main.py
```
