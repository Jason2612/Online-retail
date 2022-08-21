import pandas as pd

data=pd.read_csv('data\OnlineRetail.csv', encoding = "ISO-8859-1")
# print(data.head())
# print(data.info())

"""
Công ty bán hàng tại bao nhiêu quốc gia
"""
country = data.Country.unique()
# print("số lượng các quốc gia: " + str(country.size))


"""
Số lượng đơn hàng bán ra và tổng doanh thu
"""
data['total'] = data['Quantity'] * data['UnitPrice']

# total_invoices = data['total'].sum()
# print ("Số lượng đơn hàng bán ra: " + str(total_invoices.size))
# print ("Tổng doanh thu: " + str(total_invoices.sum()))

"""
Top 10 mắt hàng có số lượng bán ra lớn nhất
"""
# quantity_product = data.groupby(['StockCode', 'Description']) ['Quantity'].sum().sort_values(ascending = False)
# print(quantity_product.head(10))

"""
Top 10 mặt hàng có doanh thu lớn nhất
"""
quantity_product = data.groupby(['StockCode', 'Description'])['total'].sum().sort_values(ascending = False)
print(quantity_product.head(10))


