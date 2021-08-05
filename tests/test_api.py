# def test_api(api_test_cases):
# 	"""
# 	Should assert type of each response value is correct, as well as the HTTP status code
# 	"""
# 	for case in api_test_cases:
# 		# TODO
# 		print(case) # remove



## before parsing format - client.get('/v1/ads_analysis?kpi=clicks&start_date=2021-01&end_date=2021-05&filters=ad_minimum,==,1'


### SPEND
def test_api(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2021-01&end_date=2021-05&filters=[["ad_minimum", "==", 1]]')
	assert res.status_code == 200

# ad spend ==
def test_case_1(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", "==", 1]]')
	assert res.status_code == 200

# ad spend <
def test_case_2(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", "<", 5]]')
	assert res.status_code == 200

# ad spend >
def test_case_3(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", ">", 5]]')
	assert res.status_code == 200

# ad minimum ==
def test_case_4(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", "==", 1]]')
	assert res.status_code == 200

# ad minimum <
def test_case_5(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", "<", 1000]]')
	assert res.status_code == 200
	
# ad minmum >
def test_case_6(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", ">", 1000]]')
	assert res.status_code == 200

# no filters
def test_case_7(application, client):
	res = client.get('/v1/ads_analysis?kpi=spend&start_date=2020-01&end_date=2021-05')
	assert res.status_code == 200


### CLICKS
# ad spend ==
def test_case_8(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", "==", 1]]')
	assert res.status_code == 200

# ad spend <
def test_case_9(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", "<", 5]]')
	assert res.status_code == 200

# ad spend >
def test_case_10(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_spend", ">", 5]]')
	assert res.status_code == 200

# ad minimum ==
def test_case_11(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", "==", 1]]')
	assert res.status_code == 200

# ad minimum <
def test_case_12(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", "<", 1000]]')
	assert res.status_code == 200
	

# ad minmum >
def test_case_13(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05&filters=[["ad_minimum", ">", 1000]]')
	assert res.status_code == 200

# no filters
def test_case_14(application, client):
	res = client.get('/v1/ads_analysis?kpi=clicks&start_date=2020-01&end_date=2021-05')
	assert res.status_code == 200
