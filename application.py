import json, sys

from flask import Flask

from scripts.load_data import create_brand_posts

##### Import required blueprints ######
from blueprints.api import ads_analysis_api

###### Initialize flask app #########
# create flask app
application = Flask(__name__)

if len(sys.argv) > 1 and sys.argv[1] == "load_data":
	print('Creating JSON DB')
	count = 10_000
	if sys.argv[-1] != "load_data":
		count = int(sys.argv[-1])
	with open('data.json', 'w') as data_file:
		json.dump(create_brand_posts(count), data_file)
	print(f"Created {count} posts in data.json")

##### Register Application Blueprints ########
application.register_blueprint(ads_analysis_api)