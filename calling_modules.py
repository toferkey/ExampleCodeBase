import HelperFunctions as hf

my_csv = r'C:\Users\lasko\Documents\GPHY_471\GPHY-491-591-main\data\anomalyTrend_VA.csv'

my_df = hf.csv_to_df(my_csv)
print(my_df.head())