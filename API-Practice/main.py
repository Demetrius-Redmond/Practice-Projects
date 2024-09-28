import requests
# variable containing params to filter 
query_params = {} 

# used when using an endpoint multiple times contains base url and endpoint  
endpoint = "https://api.github.com/repos/octocat/Hello-World/issues/1347"

# used for custom headers to send or request additional custom information from clients
headers = {}

issues = requests.get(endpoint)

print(issues.text)