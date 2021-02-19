from io import TextIOWrapper
from recipe_scrapers import scrape_me as recipe
import os
import re
import codecs

url = input("Enter recipe url: ")

scraper = recipe(url, wild_mode=True)

title = scraper.title()
file_name = re.sub('[^a-z]', '', title.lower()) + '.md'
file_path = os.path.join(os.getcwd(),"docs",file_name)
total_time = scraper.total_time()
yields = scraper.yields()
ingredients = scraper.ingredients()
instructions = scraper.instructions()
image_url = scraper.image()
nutrients = scraper.nutrients()  # if available

# scraper.host()
# scraper.links()

def write_meta(f: TextIOWrapper):
    f.write('\n')
    f.write(f'- [Website]({url})\n')
    if total_time:
        f.write(f'- **Total time:** {total_time}\n')
    if yields:
        f.write(f'- **Yields:** {yields}\n')
    if nutrients and len(nutrients) > 0:
        f.write('\n')
        f.write('|Nutrient|Value|\n')
        f.write('|-|-|\n')
        for nutrient in nutrients:
            f.write(f'|{nutrient}|{nutrients[nutrient]}|\n')
    f.write('\n')

def write_ingredients(f: TextIOWrapper):
    f.write('\n')
    for ingredient in ingredients:
        f.write(f'- {ingredient}\n')
    f.write('\n')

def write_preperation(f: TextIOWrapper):
    f.write('\n')
    f.write(instructions)
    f.write('\n')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(f'# {title}\n')
    f.write('\n')
    f.write('## Meta\n')
    write_meta(f)
    f.write('## Ingredients\n')
    write_ingredients(f)
    f.write('## Preparation\n')
    write_preperation(f)

print('Done')