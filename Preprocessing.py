#Tiền xử lý ordinal features
#OrdinalEncoder

from pandas import DataFrame
from sklearn.preprocessing import OrdinalEncoder

before = DataFrame(["XL", "L", "S", "M", "XS", "XS", "L", "M"])
values = ["XS", "S", "M", "L", "XL"]
scaler = OrdinalEncoder(categories = [values])
after = scaler.fit_transform(before)

for b, a in zip(before.values, after):
	print("Before: {}. After: {}".format(b, a))

