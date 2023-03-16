import requests


# GET OPERAION
res = requests.get('https://crudcrud.com/api/2da518e568ae4369bfa6c4e238ac859c/unicorns')

assert res.status_code == 200, " Response status code is not expected "
assert res.json()[0]['name'] == 'Sparkle Angel', " Name is not expected "
