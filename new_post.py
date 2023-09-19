#!/usr/bin/env python3

import jinja2
from datetime import datetime
import os

SCRIPT_DIR_PATH=os.path.dirname(os.path.abspath(__file__))


def render_template(data):
    templateLoader = jinja2.FileSystemLoader(searchpath=SCRIPT_DIR_PATH)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "recipe.md.tmpl"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(data)

data = dict()
data["title"] = input("Recipe name: ")
data["date"] = str(datetime.now())
data["categories"] = input("Categories (comma-separated): ").split(",")
site = input("From site (leave empty if not): ")
if site:
    data["site"] = site
data["servings"] = input("Number of servings: ")
data["total_time"] = input("Cook time (ex. 25 mins): ")

print("Enter/Paste Ingredients. Ctrl-D or Ctrl-Z ( windows ) to save it.")
data["ingredients"] = []
while True:
    try:
        line = input().lstrip().rstrip()
    except EOFError:
        break
    data["ingredients"].append(line)

print("Enter/Paste Steps. Ctrl-D or Ctrl-Z ( windows ) to save it.")
data["steps"] = []
step_count = 1
while True:
    try:
        line = input().lstrip().rstrip()
    except EOFError:
        break
    if line:
        data["steps"].append(f"{step_count}. {line}")
        step_count = step_count + 1


file_name = data["title"].replace(" ", "_").replace("'", "_")
loc = f"{SCRIPT_DIR_PATH}/docs/recipes/posts/{file_name}.md"
with open(loc, "w") as fh:
    fh.write(render_template(data))

print("Started new recipe file at "+ loc)
