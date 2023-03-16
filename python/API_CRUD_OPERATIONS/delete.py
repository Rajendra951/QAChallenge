import requests


# DELETE OPERAION
res = requests.delete('https://crudcrud.com/api/2da518e568ae4369bfa6c4e238ac859c', 
                    json={ "name":"Sparkle Angel", "age":2, "colour":"blue" })


assert res.status_code == 201, " Response status code is not expected "
assert res.json()['name'] == 'Sparkle Angel', " Name is not deleted successfully "
