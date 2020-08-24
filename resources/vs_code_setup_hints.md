# Handy hints for setting up VS Code

## line lengths
Python PEP8 suggests a maximum line length of 79 characters for code and 72 characters for comments and docstrings. You can set up a vertical ruler to help you comply with this by opening file-preferences-settings, searching for settings.json then adding a new line with:

`"editor.rulers": [72,79]`

you may need to put a comma at the end of the line above

When not behind proxy:
download and install [git](https://git-scm.com/download/win)

Open a command terminal and
```
> pip install pytest
```