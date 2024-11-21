#%%
import requests

# %%

url = "https://www.tabnews.com.br/api/v1/contents"

resp = requests.get(url)

# %%

resp.text
# %%


