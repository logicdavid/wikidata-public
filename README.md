# LiteraryWorksMetaDataUploadBot

These notebooks aim to showcase how wikidata might be used to share metadata about literary works. 
The main tool we use is [WikibaseIntegrator](https://github.com/LeMyst/WikibaseIntegrator/).
Our project is still at an experimantal stage; we aim to eventually upload metadata for a corpus of about 4000 fictional works from Projekt Gutenberg-DE and Project Gutenberg. Currently we have uploaded only around 200 works.


### Installation

We have been using python 3.12, but the code should run on any version on which wikibaseintegrator runs. We provide a requirement file so you can install packages via
```
pip install -r requirements.txt
```
As of this writing, you should install wikibaseintegrator directly from github to get the latest bug fixes. You can do this using
```
pip install git+https://github.com/LeMyst/WikibaseIntegrator
```
The bot logs in to wikidata by taking credentials from a json file (see notebooks for details) which you have to create yourself.

### Running these notebooks

These notebooks showcases code we have used to create wikidata items for a small subset of our corpus. As such, you will have to make adaptations before it makes sense to run it.
To edit you will have to be logged into you own account with the proper permissions, see next section.



### Scripted access limitations

Be aware that making edits on wikidata in high volume can get your script banned from the site. If you only want to make a small number of edits this should not happen. 
You can also always test your script on the test instance or in a sandbox. 
Before making high volume edits on wikidata proper, it seems to us that you need to  obtain approval from wikidata via the so-called bot approval process.
Find more information at [the wikipedia bots page](https://en.wikipedia.org/wiki/Wikipedia:Bots), and especially on the [help page](https://en.wikipedia.org/wiki/Help:Creating_a_bot), as well as in [these instructions](https://heardlibrary.github.io/digital-scholarship/host/wikidata/bot/).  
The [README for WikibaseIntegrator](https://github.com/LeMyst/WikibaseIntegrator/) also has some instructions regarding using a bot.


### The notebooks

[WikiBaseIntegrator.ipynb](WikiBaseIntegrator.ipynb) is the most minimal demonstration of how we use WikibaseIntegrator to make an edit.

[Make_WikibaseItem_from_Metadata.ipynb](Make_WikibaseItem_from_Metadata.ipynb) demonstrates how to use wikibaseintegrator to obtain a python object representing a wikidata item and how write additional data for this item, taken from a CSV file, to wikidata.

[Mass_Upload.ipynb](Mass_Upload.ipynb) contains a longer script which demonstrates writing several books from a csv file, and updating a dataframe with data reflecting the items created on wikidata.
We create three entries for each book: One describing the work itself, one describing its first known edition, and one describing the edition in our corpus, the one hosted at the German or US Gutenberg site.

Further information is also found on [the bots wikidata userpage](https://www.wikidata.org/wiki/User:LiteraryWorksMetaDataUploadBot).





