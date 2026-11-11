extract_subset(tas_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], full_timeseries)
extract_subset(tasmax_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], full_timeseries)
extract_subset(rainfall_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], full_timeseries)

extract_subset(tas_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 50 years post)
extract_subset(tasmax_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 50 years post)
extract_subset(rainfall_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 50 years post)

extract_subset(tas_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 100 years post)
extract_subset(tasmax_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 100 years post)
extract_subset(rainfall_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 100 years post)

extract_subset(tas_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 300 years post)
extract_subset(tasmax_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 300 years post)
extract_subset(rainfall_data, land_mask_path, IPCC_mask_path, [all, land, ocean, Aus, IPCC_Aus_1, IPCC_Aus_2, ...], 300 years post)


# Generate time series of global ZEC compared to Australian ZEC
generate_figures([derived/temp/variable=tas/all/full_timeseries, derived/temp/variable=tas/Aus/full_timeseries], index_to_compute = mean, figure_type = time_series)
# Generate time series of global land ZEC compared to Australian ZEC
generate_figures([derived/temp/variable=tas/land/full_timeseries, derived/temp/variable=tas/Aus/full_timeseries], index_to_compute = mean, figure_type = time_series)

# Generate map of mean surface temperature 
generate_figures([derived/temp/tas/all/50_years_post, derived/temp/tas/all/100_years_post, derived/temp/tas/all/300_years_post], index_to_compute = mean, figure_type = map)

# Generate time series of mean surface temperature over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/full_timeseries, derived/temp/variable=tas/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = time_series)

# Generate distribution change in mean temperature over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/full_timeseries, derived/temp/variable=tas/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = hist)
# Generate distribution change in tasmax over Aus IPCC regions
generate_figures([derived/temp/variable=tasmax/IPCC_Aus_1/full_timeseries, derived/temp/variable=tasmax/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = hist)
# Generate distribution change in rainfall over Aus IPCC regions
generate_figures([derived/temp/variable=rainfall/IPCC_Aus_1/full_timeseries, derived/temp/variable=rainfall/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = hist)



def extract_subset(raw_data_path, land_mask, IPCC_mask, region_list, time_range):
    """Extract subset from input data"""
    data = xr.open_mfdataset("raw_data_path/*.nc")
    data = data.sel(time=slice(time_range))
    for region in region_list:
        if region == "all":
            data = data
        elif region == "land":
            data = data.where(land_mask == 1)
        elif region == "ocean":
            data = data.where(land_mask == 1)
        elif region == "Aus": 
            data = data.where(land_mask == 1).sel(lon=slice(), lat=slice())
        elif region == (IPCC name 1) or region == (IPCC name 2) or ...: 
            data = data.where(IPCC_mask = IPCC name)
    # Write data to derived/temp/variable/region/time_range folder
    return data

def generate_figures([data_1, data_2, ...], index_to_compute, figure_type):
    # List [data_1, data_2] may point to relevant data in derived/temp, or input data using extract_subset()
    # Data is to be added to one figure
    """Generate figures from input data"""
    # Initialise figure
    
    # Initialise output data
    output_data = []
    if figure_type == time_series:
        # Extract index from data
        for i in np.arange([data_1, data_2, ...]):
            output_data[i] = compute_index(data[i], index_to_compute, dimensions=["lat", "lon", "realization"])
            # Add time series to figure axis

    elif figure_type == map: 
                # Extract index from data
        for i in np.arange([data_1, data_2, ...]):
            # Initialise one map for each dataset
            output_data[i] = compute_index(data[i], index_to_compute, dimensions=["time", "realization"])
            # Add each map to figure axis (with map projection) 
            
    elif figure_type == hist: 
                # Extract index from data
        for i in np.arange([data_1, data_2, ...]):
            # Add distribution to figure axis 

    # Save figure to specific data path
    # Save output data to temp
    return

def compute_index(data, index_to_compute, dimensions):
    if index_to_compute == TXx: 
        output = data.(dim=dimensions)
    elif index_to_compute == RX1day:
        output = data.(dim=dimensions)
    elif index_to_compute == mean:
        output = data.(dim=dimensions)
    elif index_to_compute == "":
        output = data
    return output
    
