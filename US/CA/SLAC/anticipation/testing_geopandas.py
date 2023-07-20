import geopandas as gpd
from shapely.geometry import Point

def get_zipcode_geopandas(lat, lon, shapefile_path):
    point = Point(lon, lat)
    gdf = gpd.read_file(shapefile_path)
    print(gdf.columns)
    print(gdf.index)

    # Check if the point is within any polygon (zipcode boundary)
    for idx, row in gdf.iterrows():
        if point.within(row['geometry']):
            return gdf['ZIP_CODE']
    
    return ""
# Example usage:
latitude = 37.41504514168805
longitude = -122.2056472090359
shapefile_path = "USA_ZIP_Code_Boundaries.shp"
zipcode = get_zipcode_geopandas(latitude, longitude, shapefile_path)
print(f"Zip Code: {zipcode}")
