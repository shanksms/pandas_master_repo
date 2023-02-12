"""
You've been asked by Amazon to find the shipment_id and weight of the third heaviest package.
Output the shipment_id, and total_weight for that shipment_id.
In the event of a tie, do not skip ranks.
there could be multiple line items for the given shipment id

shipment_id	sub_id	weight	shipment_date
101	1	10	2021-08-30 00:00:00
101	2	20	2021-09-01 00:00:00
101	3	10	2021-09-05 00:00:00
102	1	50	2021-09-02 00:00:00
103	1	25	2021-09-01 00:00:00
103	2	30	2021-09-02 00:00:00
104	1	30	2021-08-25 00:00:00
104	2	10	2021-08-26 00:00:00
105	1	20	2021-09-02 00:00:00
"""
import pandas as pd
amazon_shipment = pd.read_csv('../data_files/shipment.csv')
amazon_shipment = amazon_shipment.groupby(['shipment_id']).agg({'weight': 'sum'}).reset_index()
amazon_shipment['rank'] = amazon_shipment['weight'].rank(method='dense', ascending=False)
amazon_shipment = amazon_shipment[amazon_shipment['rank'] == 3]
print(amazon_shipment.loc[:, ['shipment_id', 'weight']])