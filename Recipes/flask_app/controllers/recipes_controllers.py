from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/add_recipe')
def add_recipe():
    return render_template('/add_recipe.html')

@app.route('/all_recipes')
def all_recipes():
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    user_id = User.get_one_by_id(data)
    all_recipes = Recipe.get_all()
    return render_template('all_recipes.html', all_recipes = all_recipes, user_id = user_id)

@app.route('/edit_recipes/<int:id>')
def edit_recipes(id):
    data = {
        'id' : id
    }
    recipe = Recipe.get_one(data)
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/one_recipe/<int:id>')
def one_recipe(id):
    if not Recipe.validate_recipe(request.form)
        return
    data = {
        'id' : id
    }
    user_data = {
        'id' : id
    }
    user_id = User.get_one_by_id(user_data)
    recipe = Recipe.get_one(data)
    return render_template('one_recipe.html', recipe = recipe, user_id = user_id)

@app.route('/submit_recipe', methods=["POST"])
def submit_recipe():
    data = {
        **request.form,
        'users_id' : session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/all_recipes')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    Recipe.delete_recipe(data)
    return redirect('/all_recipes')

@app.route('/update_recipe', methods=['POST'])
def update():
    Recipe.update(request.form)
    return redirect('/all_recipes')