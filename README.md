# Wikidata LitBot

These notebooks aim to showcase how wikidata might be used to share metadata about literary works. 
The main tool we use is [WikibaseIntegrator](https://github.com/LeMyst/WikibaseIntegrator/).
Our project is still at an experimantal stage; we aim to eventually upload metadata for a corpus of about 4000 fictional works from Projekt Gutenberg-DE and Project Gutenberg. Currently we have uploaded only around 200 works.


### Installation

We have been using python 3.12, but the code should run on any version on which wikibaseintegrator runs. We provide a requirement file so you can install packages via
```
pip install -r requirements.txt
'''
As of this writing, you should install wikibaseintegrator directly from github to get the latest bug fixes. You can do this using
```
pip install git+https://github.com/LeMyst/WikibaseIntegrator
'''
The bot logs in to wikidata by taking credentials from a json file (see notebooks for details) which you have to create yourself.

### Running these notebooks

These notebooks contain almost the exact code we used to create wikidata items for a small subset of our corpus. As such, you will have to make adaptations before it makes sense to run it.
To edit you will have to be logged into you own account with the proper permissions, see next section.



### Obtaining a bot

To run this with your own project data, you will have to register a bot with your wikipedia/wikidata user. You can [obtain login credentials here](https://www.wikidata.org/wiki/Special:BotPasswords) following [these instructions](https://heardlibrary.github.io/digital-scholarship/host/wikidata/bot/) after which you can test your bot on the test instance or in a sandbox; before making edits on wikidata proper, you should [describe your project and request bot access](https://www.wikidata.org/wiki/Wikidata:Requests_for_permissions/Bot). 
The [README for WikibaseIntegrator](https://github.com/LeMyst/WikibaseIntegrator/) also has some instructions regarding using a bot.


### The notebooks

[Make_WikibaseItem_from_Metadata.ipynb](Make_WikibaseItem_from_Metadata.ipynb) demonstrates how to use wikibaseintegrator to create a python object representing a new wikidata item with metadata for a single book and how use the object to write to wikidata.

[Mass_Upload.ipynb](Mass_Upload.ipynb) contains a longer script which demonstrates writing several books from a csv file, and updating a dataframe with data reflecting the items created on wikidata.
We create three entries for each book: One describing the work itself, one describing its first known edition, and one describing the edition in our corpus, the one hosted at the German or US Gutenberg site.

[Auto_Matching.ipynb](Auto_Matching.ipynb) contains a short script with the goal of matching works in our corpus of authors who already have a wikidata item with the works that have wikidata entries. This is done using very simplicistic string matching against titles, labels, and descriptions. Despite the simplicity, we obtain results that are hard to produce with Openrefine.



