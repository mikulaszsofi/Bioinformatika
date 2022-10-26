import requests

resp = requests.get("http://rest.uniprot.org/uniprotkb/B5ZC00.fasta")

print(resp.text)