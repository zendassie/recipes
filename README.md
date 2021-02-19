# Recipes

- Convert recipe url to a markdown file.
- Convert markdown files to wiki pages using MKDocs.

> NOTE: The goal of this project is to be "good enough". In other words, do just enough to get the job done. No added fluff or features. Thus, I execute everything from VS Code.

## Prerequisites

- Clone this repository to your local computer.
- You can host your recipes for free if your repo is public on GitHub Pages. Follow the instructions [here](https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site) to set it up.

### PIP Dependencies

- [recipe_scrapers](https://pypi.org/project/recipe-scrapers/)
- [mkdocs](https://pypi.org/project/mkdocs/)

## Usage

- If you want to convert a web page of a recipe, execute `./code/recipe_saver.py` from VS Code and enter the recipe url. It will then save the file in `./docs/` with the filename being the recipe titles scrapes from the web page.
- You can manually add more recipes by simply adding markdown files in `./docs/` youself.
- Customize the site structure of the MKDocs site in `mkdocs.yml`.
- Convert the markdown documents by running `mkdocs build`
- Deploy to GitHub Pages with `mkdocs gh-deploy --theme readthedocs`
- You're done. Easy as Pie (see what I did there?). Enjoy.
