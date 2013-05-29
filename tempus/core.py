#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG_PATH', 'websiteconfig'))


@app.route("/")
def index():
    fore = request.args.get('fore') or '#666'
    bg = request.args.get('bg') or '#333'
    seconds = int(request.args.get('sec') or 60)
    return render_template('index.html', fore=fore, bg=bg, seconds=seconds)


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
