import pandas as pd

# data = {
#     'body': {
#         'batch_id': 'fson_20220823/23',
#         'start_date_time': '10-08-2022',
#         'end_date_time': '18-08-2022',
#         'vendor_name': 'dfg'
#     },
#     'headers': {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'client_id': '670',
#         'client_secret': '560',
#         'Content-Type': 'application/json',
#         'Host': 'dev',
#         'Postman-Token': 'f',
#         'User-Agent': 'PostmanRuntime/7.29.2',
#         'X-Amzn-Trace-Id': 'Root=1-63333cd1-41dfefe13ef426d6107572b5',
#         'x-api-key': 'bla-bla',
#         'X-Forwarded-For': 'glhoto',
#         'X-Forwarded-Port': '560',
#         'X-Forwarded-Proto': 'https'
#     }
# }

data =[
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]

df = pd.json_normalize(data)

print(df)

df_list = [i.split('.')[1] for i in df.columns]
print(df_list)

df_list1 = df.columns
print(df_list1)

df_keys = df.keys()
print(df_keys) 
