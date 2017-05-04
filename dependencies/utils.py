import requests

def search_term(q):
	# This funtion queries GitHub API with this 
	# search_term to look for repositories
	url = "https://api.github.com/search/repositories?q=" + q
	json_data = requests.get(url)
	return json_data.json()["items"]


def last_commit(user, repo):
	# We also need the last commit information, so we 
	# need to query the Github API again
	url = "https://api.github.com/repos/"+user+"/"+repo+"/commits"
	json_data = requests.get(url)
	return json_data.json()[0] # Last commit


def five_newest(data):
	# This funtion takes first page of search result and 
	# sorts items by the creation date in descending order
	data = sorted(data, key=lambda data: data['created_at'], reverse=True)
	return data[:5]
