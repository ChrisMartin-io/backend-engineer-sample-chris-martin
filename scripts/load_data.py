import random, uuid
from dateutil import rrule
from datetime import datetime, timedelta

def create_brand_posts(count):
	"""Creates brand posts to add into the data.json file
	Args:
		count (int): total count of posts to add
	"""
	# setting random seed based on current timestamp
	random.seed(datetime.now().timestamp())
	now = datetime.now()
	start_date = (now - timedelta(2*365))
	end_date = now + timedelta(31)

	# setting possible values for features
	text_on_image_values = [['foil'], ['black'], ['pink'], ['red'], ['white']]
	video_persistent_objects_values = [['accessory'], ['advertisement'], ['animal'], ['apparel'], ['art'], ['bag'], ['computer'], ['electronics']]
	background_environment_in_image_values = [['indoor'], ['outdoor'], ['solid backdrop']]
	filming_style_in_video_values = [['boomerang'], ['single shot'], ['stop motion'], ['static images']]
	banner_color_in_video_values = [['beige'], ['black'], ['blue'], ['green'], ['purple'], ['white'], ['red'], ['yellow']]

	feature_names = [
		('text_on_image_style', text_on_image_values),
		('video_persistent_objects', video_persistent_objects_values),
		('background_environment_in_image', background_environment_in_image_values),
		('filming_style_in_video', filming_style_in_video_values),
		('banner_color_in_video', banner_color_in_video_values)
	]
	brand_posts = {'posts': []}
	for _ in range(count):
		brand_post = {
			'platform_id': str(uuid.uuid4()),
			'features': create_fake_features(feature_names),
			'temporal_kpis': create_fake_kpis(start_date, end_date)
		}
		brand_posts['posts'].append(brand_post)
	
	return brand_posts

def create_fake_features(feature_names):
	"""Creates a fake feature and feature value from the passed in features
		Args:
			feature_names (list): feature name: possible values (list)
		Returns:
			features dict
	"""
	features = {}
	for feature_name, possible_values in feature_names:
		features[feature_name] = random.choice(possible_values)
	
	return features


def create_fake_kpis(start_date, end_date):
	"""Creates a fake KPI in the desired format
		Returns:
			kpi_dict (dict)
	"""
	kpi_names = ['clicks', 'spend']
	temporal_kpis = {}
	for kpi in kpi_names:
		temporal_kpis[kpi] = {}
		for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
			temporal_kpis[kpi][dt.strftime('%Y-%m')] = create_fake_kpi_value(10)
	return temporal_kpis

def create_fake_kpi_value(max_value):
	"""Creates a fake KPI value for insertion into JSON file
		Args:
			max_value (int): ceiling for random value
		Returns:
			random value between 0 and max_value (float)
	"""
	return round(random.random()*max_value, 2)