import pandas as pd

df1  = pd.read_csv('Resources/201801-citibike-tripdata.csv')
df2  = pd.read_csv('Resources/201802-citibike-tripdata.csv')
df3  = pd.read_csv('Resources/201803-citibike-tripdata.csv')
df4  = pd.read_csv('Resources/201804-citibike-tripdata.csv')
df5  = pd.read_csv('Resources/201805-citibike-tripdata.csv')
df6  = pd.read_csv('Resources/201806-citibike-tripdata.csv')
df7  = pd.read_csv('Resources/201807-citibike-tripdata.csv')
df8  = pd.read_csv('Resources/201808-citibike-tripdata.csv')
df9  = pd.read_csv('Resources/201809-citibike-tripdata.csv')
df10 = pd.read_csv('Resources/2018010-citibike-tripdata.csv')
df11 = pd.read_csv('Resources/2018011-citibike-tripdata.csv')
df12 = pd.read_csv('Resources/2018012-citibike-tripdata.csv')

#df1.head()
#df2.head()
#df3.head()
#df4.head()
#df5.head()
#df6.head()
#df7.head()
#df8.head()
#df9.head()
#df10.head()
#df11.head()
#df12.head()

df1.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df2.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df3.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df4.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df5.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df6.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df7.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df8.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df9.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df10.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)
#df10.head()
df11.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

df12.rename(columns = {'tripduration': 'trip_duration',
                      'starttime': 'start_time',
                      'start station id': 'start_station_id',
                      'start station name': 'start_station_name',
                      'start station latitude': 'start_station_latitude',
                      'start station longitude': 'start_station_longitude',
                      'end station id': 'end_station_id',
                      'end station name': 'end_station_name',
                      'end station latitude': 'end_station_latitude',
                      'end station longitude': 'end_station_longitude',
                      'bikeid': 'bike_id',
                      'usertype': 'user_type',
                      'birth year': 'birth_year'
                      }, inplace = True)

#df1.head()
#df2.head()
#df3.head()
#df4.head()
#df5.head()
#df6.head()
#df7.head()
#df8.head()
#df9.head()
#df10.head()
#df11.head()
#df12.head()

citibike_2018 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
citibike_2018.to_csv('citibike2018', sep = ',')