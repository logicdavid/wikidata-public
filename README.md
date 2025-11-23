# Wikidata LitBot

These notebooks aim to provide a simple workflow for storing and thereby sharing metadata about literary works using wikidata. We aim to upload metadata for a corpus of about 4000 fictional works from Projekt Gutenberg-DE and Project Gutenberg. Currently, this is still in a preliminary stage and we have uploaded around 200 works, all by authors who had not previously had any works associated with them on wikidata.
The main tool we use is [WikibaseIntegrator](https://github.com/LeMyst/WikibaseIntegrator/).

### Installation

You can install using the requirement file. We have been using python 3.12, but the code should run on any version on which wikibaseintegrator runs. Currently, we recommend installing wikibaseintegrator directly from github, a bug or two have only very recently been fixed. 
The bot logs in to wikidata by looking for credentials in a json file (see notebooks for details) which you will have to create.

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



