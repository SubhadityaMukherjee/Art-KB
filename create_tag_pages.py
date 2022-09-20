import os
from glob import glob
from pathlib import Path
from tqdm import tqdm
import re
#%%
main_dir = Path("./docs/")
# %%
files = glob(str(main_dir) + "/**/*.md", recursive=True)
files.sort()

tag_list = ["performanceart","deity", "chinese", "humanexperiments", "botany", "drawing", "greek", "folklore"]

dict_tags = {x:[] for x in tag_list}

# Create a dictionary with files and their tags
print("Creating index")
for i in tqdm(files, total = len(files)):
    with open(i, "r+") as myfile:
        print(i)
        try:
            head = [next(myfile) for x in range(5)] # read first n lines
            head = [x for x in head if "tag" in x][0].strip().split(" ")[1::]
            for tag in head:
                try:
                    dict_tags[tag].append(i)
                except:
                    pass
        except StopIteration:
            pass
#print(dict_tags)

# Create files with tag pages
f_string = """
---
tags: anchor
___

"""

for tag in tag_list:
    print(tag)
    files_in_tag = dict_tags[tag]
    with open(f"docs/{tag}.md", "w+") as tagfile:
        tagfile.write(f_string)
        for fle in files_in_tag:
            fle = fle.replace('docs/','').replace(" ", "%20")
            tagfile.write(f"- [{fle.replace('%20', ' ')}]({fle})\n")
