import requests


# PUT OPERAION
res = requests.put('https://crudcrud.com/api/2da518e568ae4369bfa6c4e238ac859c/unicorns', 
                    json={ "name":"Rajendra", "age":2, "colour":"blue" })

assert res.status_code == 201, " Response status code is not expected "
assert res.json()['name'] == 'Rajendra', " Name is not updated successfully "
