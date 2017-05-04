#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from dependencies.utils import search_term, last_commit, five_newest

app = Flask(__name__, template_folder="./")


@app.route("/")
def github():
	# If there is not a search term, then default is 'arrow'
	q = request.args.get('search_term', 'arrow') 

	# Let's access the Github API searching the term
	data = search_term(q)

	# We just need the 5 newest in desc order
	data = five_newest(data)

	# We need to add the information about the last commit to each repo
	for item in data:
		item["last"] = last_commit(item["owner"]["login"], item["name"])

	# Ok, render the page using the results
	return render_template("template.html", data=data)


if __name__ == "__main__":
	app.run()
