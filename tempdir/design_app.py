from flask import Flask, json, render_template

design = Flask('design_app')

@design.route("/")

def index():
    return render_template('index.html')

if __name__ == '__main__':
    design.run(host='0.0.0.0', port=5050)