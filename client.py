import requests

# call localhost API
response = requests.get('http://127.0.0.1:5000/phen2gene', params={"HPO_list": ["HP:0002459","HP:0010522","HP:0001662"]})
if response.status_code == 200:
    if 'results' in response.json():
        genes = response.json()['results']
        print(genes)
else:
    print(response.status_code)
    
# call phen2gene API
# response = requests.get('https://phen2gene.wglab.org/api', params={"HPO_list": ["HP:0002459","HP:0010522","HP:0001662"]})
# if response.status_code == 200:
#     if 'results' in response.json():
#         genes = response.json()['results']
#         print(genes)
# else:
#     print(response.status_code)
    