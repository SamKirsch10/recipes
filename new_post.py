#!/usr/bin/env python3

import itertools
import inquirer
from datetime import datetime
import jinja2
import os
import tkinter as tk
import yaml

SCRIPT_DIR_PATH=os.path.dirname(os.path.abspath(__file__))

def gather_categories():
    categories = list()
    for _, _, files in os.walk(f"{SCRIPT_DIR_PATH}/docs/recipes/posts"):
        for recipe_file in files:
            with open(f"{SCRIPT_DIR_PATH}/docs/recipes/posts/{recipe_file}", 'r') as fh:
                raw = yaml.safe_load_all(fh)
                tmp = next(itertools.islice(raw, 0, None))
                if 'categories' not in tmp:
                    continue
                for c in tmp['categories']:
                    if c not in categories:
                        categories.append(c)
    return categories

def render_template(data):
    templateLoader = jinja2.FileSystemLoader(searchpath=SCRIPT_DIR_PATH)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "recipe.md.tmpl"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(data)

data = dict()

questions = [
    inquirer.Text('title', message="Recipe name"),
    inquirer.Checkbox(
        "categories",
        message="Categories",
        choices=gather_categories(),
    ),
    inquirer.Text('add_categories', message="New categories (comma-separated)"),
    inquirer.Text('servings', message="Servings"),
    inquirer.Text('total_time', message="Cook time (ex. 25 mins)"),
    inquirer.Editor('ingredients', message="Ingredients"),
    inquirer.Editor('steps', message="Steps"),
]

answers = inquirer.prompt(questions)


answers['categories'] = answers['categories'] + answers['add_categories'].split(',')
while "" in answers['categories']:
    answers['categories'].remove("")

answers['ingredients'] = answers['ingredients'].split('\n')
answers['steps'] = [f"{i+1}. {step}" for i, step in enumerate(answers['steps'].split('\n'))]

answers['date'] = str(datetime.now())

file_name = answers["title"].replace(" ", "_").replace("'", "_")
loc = f"{SCRIPT_DIR_PATH}/docs/recipes/posts/{file_name}.md"
with open(loc, "w") as fh:
    fh.write(render_template(answers))

print("Started new recipe file at "+ loc)
