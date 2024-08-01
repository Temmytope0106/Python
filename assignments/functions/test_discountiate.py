from discountiate import*

def test_discountiate():
	assert discountiate(5000, 10) == 4500
	assert discountiate(30000, 10) == 27000
	