from flask import Blueprint, jsonify, request, json

# load JSON data
data = open('data.json')
data = json.load(data)

ads_analysis_api = Blueprint("ads_analysis_api", __name__)

@ads_analysis_api.route("/v1/ads_analysis", methods=["GET"])
def overview_statistic():
	"""
	Computes overall average statistic for a brand given a KPI.
	Request Parameters:
		kpi (str): kpi_name - use cpc
		start_date (timestamp): start date
		end_date (timestamp): end date
		filters (list): list of filters
			- ex. [['ad_minimum','>',3],['ad_spend','>', 200]]
	Returns:
		response: response with kpi information
			- format: {
				'feature_name': {
					"feature value": ___,
						...},
					...}
				}
	"""

	# get request args
	kpi = request.args.get('kpi')
	start_date = request.args.get('start_date')
	end_date = request.args.get('end_date')
	filters = request.args.get('filters')

	# result dict setup
	result = {}
	filter = None
	filter_op = None
	filter_arg = None

	# check if filters exist, parse
	if filters != None and filters != '[]':
		filters = filters[2:][:-2]
		filters = filters.split(',')
		filter = filters[0].replace('"', '')
		filter_op = filters[1].replace('"', '')[1:]
		filter_arg = int(filters[2])

	print('filters sthings', filter, filter_op, filter_arg)
	
	# main loop
	for post in data['posts']:

		# set total for post
		total = 0
		
		# iterate over specified kpi, add totals for valid dates
		for item in post['temporal_kpis'][kpi]:

			# if date in range
			if item > start_date and item < end_date:

				### check for ad minimum filter
				if filter == 'ad_spend':

					# filter operator <
					if filter_op == '>':
						if post['temporal_kpis'][kpi][item] > filter_arg:
							total += post['temporal_kpis'][kpi][item]

					# filter operator >
					elif filter_op == '<':
						if post['temporal_kpis'][kpi][item] < filter_arg:
							total += post['temporal_kpis'][kpi][item]	
					
					# filter operator ==
					elif filter_op == '==':
						if post['temporal_kpis'][kpi][item] == filter_arg:
							total += post['temporal_kpis'][kpi][item]	

				else:
					# add to total
					total += post['temporal_kpis'][kpi][item]

		### add to result dict
		# iterate over features
		for feature in post['features']:

			# check if exists in result dict
			if feature not in result:

				# create dict in result
				result[feature] = { 
					post['features'][feature][0]: {
					'total': total,
					'count': 1
					}
				}

			else:
				# check if category exists
				if post['features'][feature][0] not in result[feature]:
					# create dict in result
					result[feature][post['features'][feature][0]] = { 
						'total': total,
						'count': 1
					}
				else:
					# add to existing dict
					result[feature][post['features'][feature][0]]['total'] += total
					result[feature][post['features'][feature][0]]['count'] += 1

	# end result dict
	filter_result = None
	extra_filter_result = None

	### check for minimum ad count
	if filter == 'ad_minimum':

		# setup filter result
		filter_result = {}

		# iterate through result object
		for item in result:

			# add type
			filter_result[item] = {}

			for type in result[item]:

				### check minimum count
				# filter operator >
				if filter_op == '>':
					if result[item][type]['count'] > filter_arg:
						# calculate average, 2 decimal places
						filter_result[item][type] = round(result[item][type]['total'] / result[item][type]['count'], 2)
				
				# filter operator <
				elif filter_op == '<':
					if result[item][type]['count'] < filter_arg:
						# calculate average, 2 decimal places
						filter_result[item][type] = round(result[item][type]['total'] / result[item][type]['count'], 2)

				# filter operator ==
				elif filter_op == '==':
					if result[item][type]['count'] >= filter_arg:
						# calculate average, 2 decimal places
						filter_result[item][type] = round(result[item][type]['total'] / result[item][type]['count'], 2)

		# check for empty types
		filter_result = {k: v for k, v in filter_result.items() if v}

	## no minimum ad filter
	else:
		# process result dict
		for item in result:
			for type in result[item]:	

				# calculate average, 2 decimal places
				result[item][type] = round(result[item][type]['total'] / result[item][type]['count'], 2)

	# Response
	response = jsonify(result if filter_result == None else filter_result)
	response.status_code = 200
	return response

