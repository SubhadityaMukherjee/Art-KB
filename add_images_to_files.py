import os
from pathlib import Path
from fastcore.all import *
import time
from fastdownload import download_url
from tqdm import tqdm
from fastai.vision.all import *
from fastai.vision.widgets import *


def search_images(term, max_images=1):
    url = 'https://duckduckgo.com/'
    res = urlread(url,data={'q':term})
    searchObj = re.search(r'vqd=([\d-]+)\&', res)
    requestUrl = url + 'i.js'
    params = dict(l='us-en', o='json', q=term, vqd=searchObj.group(1), f=',,,', p='1', v7exp='a')
    urls,data = set(),{'next':1}
    while len(urls)<max_images and 'next' in data:
        data = urljson(requestUrl,data=params)
        urls.update(L(data['results']).itemgot('image'))
        requestUrl = url + data['next']
        time.sleep(0.2)
    return L(urls)[:max_images]

def temp_image(term):
    term = term.replace(".md","")
    down_path = Path("/tmp/")
    image_folder_path = Path("/Users/eragon/Dropbox/Obsidian/art/assets/")
    download_images(down_path/"temp.png", urls=search_images(f'{term} photo'))
    resize_images(down_path/"temp.png", max_size=400, dest=down_path/"temp.png")
    shutil.copy(down_path/"temp.png", image_folder_path/f"{term}.png")
    

search_images("A Bad Dream")