import requests
import json
session = requests.Session()

idle_checker_url = "http://localhost:8888/jupyter/default/sagemaker-studio-autoshutdown/idle_checker"
get_response = session.get(idle_checker_url)
print(get_response)
print(get_response.json())
