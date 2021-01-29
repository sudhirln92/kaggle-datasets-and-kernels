from fuel_rate import HistoricalPrice

# =============================================================================
# Get HistroyData
# =============================================================================

city_url = {
    # "Bengaluru": "https://www.mypetrolprice.com/6/Petrol-price-in-Bengaluru?FuelType=0&LocationId=6",
    # "Chennai": "https://www.mypetrolprice.com/5/Petrol-price-in-Chennai?FuelType=0&LocationId=5",
    # "Mumbai": "https://www.mypetrolprice.com/3/Petrol-price-in-Mumbai?FuelType=0&LocationId=3",
    # "Hyderabad": "https://www.mypetrolprice.com/8/Petrol-price-in-Hyderabad?FuelType=0&LocationId=8",
    # "Delhi": "https://www.mypetrolprice.com/2/Petrol-price-in-Delhi?FuelType=0&LocationId=2",
    "Kolkata": "https://www.mypetrolprice.com/4/Petrol-price-in-Kolkata?FuelType=0&LocationId=4",
    # "Coimbatore": "https://www.mypetrolprice.com/509/Petrol-price-in-Coimbatore?FuelType=0&LocationId=509",
    # "Haridwar": "https://www.mypetrolprice.com/167/Petrol-price-in-Haridwar?FuelType=0&LocationId=167",
    # "Allahabad": "https://www.mypetrolprice.com/442/Petrol-price-in-Allahabad?FuelType=0&LocationId=442",
    # "Varanasi": "https://www.mypetrolprice.com/451/Petrol-price-in-Varanasi?FuelType=0&LocationId=451",
    # "Meerut": "https://www.mypetrolprice.com/311/Petrol-price-in-Meerut?FuelType=0&LocationId=311",
    # "Agartala": "https://www.mypetrolprice.com/9/Petrol-price-in-Agartala?FuelType=0&LocationId=9",
    # "Nizamabad": "https://www.mypetrolprice.com/491/Petrol-price-in-Nizamabad?FuelType=0&LocationId=491",
    # "Madurai": "https://www.mypetrolprice.com/478/Petrol-price-in-Madurai?FuelType=0&LocationId=478",
    # "Gangtok": "https://www.mypetrolprice.com/17/Petrol-price-in-Gangtok?FuelType=0&LocationId=17",
    # "Jaipur": "https://www.mypetrolprice.com/21/Petrol-price-in-Jaipur?FuelType=0&LocationId=21",
    # "Amritsar": "https://www.mypetrolprice.com/159/Petrol-price-in-Amritsar?FuelType=0&LocationId=159",
    # "Karaikal": "https://www.mypetrolprice.com/106/Petrol-price-in-Karaikal?FuelType=0&LocationId=106",
    # "Pondicherry": "https://www.mypetrolprice.com/28/Petrol-price-in-Pondicherry?FuelType=0&LocationId=28",
    # "Bhubhaneswar": "https://www.mypetrolprice.com/14/Petrol-price-in-Bhubhaneswar?FuelType=0&LocationId=14",
    # "Dimapur": "https://www.mypetrolprice.com/107/Petrol-price-in-Dimapur?FuelType=0&LocationId=107",
    # "Aizwal": "https://www.mypetrolprice.com/11/Petrol-price-in-Aizwal?FuelType=0&LocationId=11",
    # "Shillong": "https://www.mypetrolprice.com/32/Petrol-price-in-Shillong?FuelType=0&LocationId=32",
    # "Imphal": "https://www.mypetrolprice.com/19/Petrol-price-in-Imphal?FuelType=0&LocationId=19",
    # "Gwalior": "https://www.mypetrolprice.com/48/Petrol-price-in-Gwalior?FuelType=0&LocationId=48",
    # "Trivandrum": "https://www.mypetrolprice.com/35/Petrol-price-in-Trivandrum?FuelType=0&LocationId=35",
    # "Udupi": "https://www.mypetrolprice.com/383/Petrol-price-in-Udupi?FuelType=0&LocationId=383",
    # "Ranchi": "https://www.mypetrolprice.com/31/Petrol-price-in-Ranchi?FuelType=0&LocationId=31",
    # "Srinagar": "https://www.mypetrolprice.com/34/Petrol-price-in-Srinagar?FuelType=0&LocationId=34",
    # "Shimla": "https://www.mypetrolprice.com/33/Petrol-price-in-Shimla?FuelType=0&LocationId=33",
    # "Panipat": "https://www.mypetrolprice.com/324/Petrol-price-in-Panipat?FuelType=0&LocationId=324",
    # "Ahmedabad": "https://www.mypetrolprice.com/10/Petrol-price-in-Ahmedabad?FuelType=0&LocationId=10",
    # "Margao": "https://www.mypetrolprice.com/274/Petrol-price-in-Margao?FuelType=0&LocationId=274",
    # "Chandigarh": "https://www.mypetrolprice.com/15/Petrol-price-in-Chandigarh?FuelType=0&LocationId=15",
    # "Raipur": "https://www.mypetrolprice.com/30/Petrol-price-in-Raipur?FuelType=0&LocationId=30",
    # "Patna": "https://www.mypetrolprice.com/27/Petrol-price-in-Patna?FuelType=0&LocationId=27",
    # "Guwahati": "https://www.mypetrolprice.com/18/Petrol-price-in-Guwahati?FuelType=0&LocationId=18",
    # "Itanagar": "https://www.mypetrolprice.com/20/Petrol-price-in-Itanagar?FuelType=0&LocationId=20",
    # "Port_Blair": "https://www.mypetrolprice.com/29/Petrol-price-in-Port_Blair?FuelType=0&LocationId=29",
}
param = {"till_date": "2000-01-01", "file_name": "petrol.csv", "city_url": city_url}

df = HistoricalPrice(**param).get_old_data()