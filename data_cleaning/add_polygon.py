import json

def update_geojson(wildfire_data, county_boundaries):
    updated_data = {"type": "FeatureCollection", "features": []}

    for wildfire_feature in wildfire_data["features"]:
        county_name = wildfire_feature["properties"]["COUNTY_LABEL_NM"]

        matching_counties = [county for county in county_boundaries["features"] if county_name.lower() in county["properties"]["JURISDICT_LABEL_NM"].lower()]

        if matching_counties:
            # For simplicity, we'll use the first matching county
            matching_county = matching_counties[0]

            # Update the geometry with the polygon coordinates from county boundaries
            wildfire_feature["geometry"] = matching_county["geometry"]
            # Remove the original MultiPoint geometry
            wildfire_feature.pop("original_geometry", None)

            updated_data["features"].append(wildfire_feature)

    return updated_data

def capitalize_county_names(county_boundaries):
    for feature in county_boundaries["features"]:
        if "JURISDICT_LABEL_NM" in feature["properties"]:
            feature["properties"]["JURISDICT_LABEL_NM"] = feature["properties"]["JURISDICT_LABEL_NM"].upper()

    return county_boundaries

def main():
    wildfire_file_path = "assets/2012_2022_by_county.geojson"
    county_boundaries_file_path = "assets/WA_County_Boundaries.geojson"
    output_file_path = "assets/with_stats_bycounty.geojson"

    with open(wildfire_file_path, "r") as wildfire_file, open(county_boundaries_file_path, "r") as county_file:
        wildfire_data = json.load(wildfire_file)
        county_boundaries = json.load(county_file)

        # Capitalize county names in county boundaries
        county_boundaries = capitalize_county_names(county_boundaries)

        updated_data = update_geojson(wildfire_data, county_boundaries)

        with open(output_file_path, "w") as output_file:
            json.dump(updated_data, output_file, indent=2)

if __name__ == "__main__":
    main()
