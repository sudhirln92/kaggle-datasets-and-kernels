from fuel_rate import HistoricalPrice

# =============================================================================
# Get HistroyData
# =============================================================================

city_url = {
    "Bengaluru": "https://www.mypetrolprice.com/6/Diesel-price-in-Bengaluru?FuelType=1&LocationId=6",
    "Chennai": "https://www.mypetrolprice.com/5/Diesel-price-in-Chennai?FuelType=1&LocationId=5",
    "Mumbai": "https://www.mypetrolprice.com/3/Diesel-price-in-Mumbai?FuelType=1&LocationId=3",
    "Hyderabad": "https://www.mypetrolprice.com/8/Diesel-price-in-Hyderabad?FuelType=1&LocationId=8",
    "Delhi": "https://www.mypetrolprice.com/2/Diesel-price-in-Delhi?FuelType=1&LocationId=2",
    "Kolkata": "https://www.mypetrolprice.com/4/Diesel-price-in-Kolkata?FuelType=1&LocationId=4",
    "Coimbatore": "https://www.mypetrolprice.com/509/Diesel-price-in-Coimbatore?FuelType=1&LocationId=509",
    "Haridwar": "https://www.mypetrolprice.com/167/Diesel-price-in-Haridwar?FuelType=1&LocationId=167",
    "Allahabad": "https://www.mypetrolprice.com/442/Diesel-price-in-Allahabad?FuelType=1&LocationId=442",
    "Varanasi": "https://www.mypetrolprice.com/451/Diesel-price-in-Varanasi?FuelType=1&LocationId=451",
    "Meerut": "https://www.mypetrolprice.com/311/Diesel-price-in-Meerut?FuelType=1&LocationId=311",
    "Agartala": "https://www.mypetrolprice.com/9/Diesel-price-in-Agartala?FuelType=1&LocationId=9",
    "Nizamabad": "https://www.mypetrolprice.com/491/Diesel-price-in-Nizamabad?FuelType=1&LocationId=491",
    "Madurai": "https://www.mypetrolprice.com/478/Diesel-price-in-Madurai?FuelType=1&LocationId=478",
    "Gangtok": "https://www.mypetrolprice.com/17/Diesel-price-in-Gangtok?FuelType=1&LocationId=17",
    "Jaipur": "https://www.mypetrolprice.com/21/Diesel-price-in-Jaipur?FuelType=1&LocationId=21",
    "Amritsar": "https://www.mypetrolprice.com/159/Diesel-price-in-Amritsar?FuelType=1&LocationId=159",
    "Karaikal": "https://www.mypetrolprice.com/106/Diesel-price-in-Karaikal?FuelType=1&LocationId=106",
    "Pondicherry": "https://www.mypetrolprice.com/28/Diesel-price-in-Pondicherry?FuelType=1&LocationId=28",
    "Bhubhaneswar": "https://www.mypetrolprice.com/14/Diesel-price-in-Bhubhaneswar?FuelType=1&LocationId=14",
    "Dimapur": "https://www.mypetrolprice.com/107/Diesel-price-in-Dimapur?FuelType=1&LocationId=107",
    "Aizwal": "https://www.mypetrolprice.com/11/Diesel-price-in-Aizwal?FuelType=1&LocationId=11",
    "Shillong": "https://www.mypetrolprice.com/32/Diesel-price-in-Shillong?FuelType=1&LocationId=32",
    "Imphal": "https://www.mypetrolprice.com/19/Diesel-price-in-Imphal?FuelType=1&LocationId=19",
    "Gwalior": "https://www.mypetrolprice.com/48/Diesel-price-in-Gwalior?FuelType=1&LocationId=48",
    "Trivandrum": "https://www.mypetrolprice.com/35/Diesel-price-in-Trivandrum?FuelType=1&LocationId=35",
    "Udupi": "https://www.mypetrolprice.com/383/Diesel-price-in-Udupi?FuelType=1&LocationId=383",
    "Ranchi": "https://www.mypetrolprice.com/31/Diesel-price-in-Ranchi?FuelType=1&LocationId=31",
    "Srinagar": "https://www.mypetrolprice.com/34/Diesel-price-in-Srinagar?FuelType=1&LocationId=34",
    "Shimla": "https://www.mypetrolprice.com/33/Diesel-price-in-Shimla?FuelType=1&LocationId=33",
    "Panipat": "https://www.mypetrolprice.com/324/Diesel-price-in-Panipat?FuelType=1&LocationId=324",
    "Ahmedabad": "https://www.mypetrolprice.com/10/Diesel-price-in-Ahmedabad?FuelType=1&LocationId=10",
    "Margao": "https://www.mypetrolprice.com/274/Diesel-price-in-Margao?FuelType=1&LocationId=274",
    "Chandigarh": "https://www.mypetrolprice.com/15/Diesel-price-in-Chandigarh?FuelType=1&LocationId=15",
    "Raipur": "https://www.mypetrolprice.com/30/Diesel-price-in-Raipur?FuelType=1&LocationId=30",
    "Patna": "https://www.mypetrolprice.com/27/Diesel-price-in-Patna?FuelType=1&LocationId=27",
    "Guwahati": "https://www.mypetrolprice.com/18/Diesel-price-in-Guwahati?FuelType=1&LocationId=18",
    "Itanagar": "https://www.mypetrolprice.com/20/Diesel-price-in-Itanagar?FuelType=1&LocationId=20",
    "Port_Blair": "https://www.mypetrolprice.com/29/Diesel-price-in-Port_Blair?FuelType=1&LocationId=29",
}
param = {"till_date": "2000-01-01", "file_name": "diesel.csv", "city_url": city_url}

df = HistoricalPrice(**param).get_old_data()