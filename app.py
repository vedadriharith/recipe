from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to hold recipes
recipes = []

# Route to display all recipes
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

# Route to add a new recipe
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        recipes.append({'name': recipe_name, 'ingredients': ingredients, 'instructions': instructions})
        return redirect(url_for('index'))
    return render_template('add.html')

# Route to delete a recipe
@app.route('/delete/<int:index>')
def delete_recipe(index):
    del recipes[index]
    return redirect(url_for('index'))

# Route to search for a recipe
@app.route('/search', methods=['GET', 'POST'])
def search_recipe():
    if request.method == 'POST':
        query = request.form['query']
        results = [recipe for recipe in recipes if query.lower() in recipe['name'].lower()]
        return render_template('search.html', recipes=results, query=query)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)