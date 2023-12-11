import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPoint
from datetime import datetime

# Load GeoJSON data into a GeoDataFrame using GeoPandas
geojson_file = 'assets/DNR_Fire_Statistics_2008_-_Present.geojson'
gdf = gpd.read_file(geojson_file)

# Convert the 'DSCVR_DT' column to datetime format
gdf['DSCVR_DT'] = pd.to_datetime(gdf['DSCVR_DT'])

# Iterate over the years from 2012 to 2022
for year in range(2012, 2023):
    # Filter data for the current year
    filtered_gdf = gdf[gdf['DSCVR_DT'].dt.year == year]

    # Create a GeoDataFrame with Point geometries for each wildfire incident
    points_gdf = gpd.GeoDataFrame(filtered_gdf, geometry=gpd.points_from_xy(filtered_gdf['LON_COORD'], filtered_gdf['LAT_COORD']))

    # Group by county and sum acres burned, also create a list of Point geometries for each group
    grouped_data = points_gdf.groupby('COUNTY_LABEL_NM').agg({
        'ACRES_BURNED': 'sum',
        'geometry': lambda x: list(x),
        'FIRESCAUSE_LABEL_NM': lambda x: ', '.join(x.value_counts().index[:3])  # Convert list to comma-separated string
    }).reset_index()

    # Apply MultiPoint constructor to create MultiPoint geometries
    grouped_data['geometry'] = grouped_data['geometry'].apply(MultiPoint)

    # Create a GeoDataFrame with MultiPoint geometries
    gdf_county_multi_points = gpd.GeoDataFrame(grouped_data, geometry='geometry')

    # Save the county, total acres burned, top three reasons, coordinates, and MultiPoint geometry to a new GeoJSON file
    output_geojson_file = f'{year}_by_county.geojson'
    gdf_county_multi_points.to_file(output_geojson_file, driver='GeoJSON')


# # Filter data for the year range 2012 to 2022
# filtered_gdf = gdf[(gdf['DSCVR_DT'].dt.year >= 2012) & (gdf['DSCVR_DT'].dt.year <= 2022)]

# # Create a GeoDataFrame with Point geometries for each wildfire incident
# points_gdf = gpd.GeoDataFrame(filtered_gdf, geometry=gpd.points_from_xy(filtered_gdf['LON_COORD'], filtered_gdf['LAT_COORD']))

# # Group by county and sum acres burned, also create a list of Point geometries for each group
# grouped_data = points_gdf.groupby('COUNTY_LABEL_NM').agg({
#     'ACRES_BURNED': 'sum',
#     'geometry': lambda x: list(x),
#     'FIRESCAUSE_LABEL_NM': lambda x: ', '.join(x.value_counts().index[:3])  # Convert list to comma-separated string
# }).reset_index()

# # Apply MultiPoint constructor to create MultiPoint geometries
# grouped_data['geometry'] = grouped_data['geometry'].apply(MultiPoint)

# # Create a GeoDataFrame with MultiPoint geometries
# gdf_county_multi_points = gpd.GeoDataFrame(grouped_data, geometry='geometry')

# # Save the county, total acres burned, top three reasons, coordinates, and MultiPoint geometry to a new GeoJSON file
# output_geojson_file = '2012_2022_by_county.geojson'
# gdf_county_multi_points.to_file(output_geojson_file, driver='GeoJSON')

# # Optional: Display the new GeoDataFrame
# print(gdf_county_multi_points)
