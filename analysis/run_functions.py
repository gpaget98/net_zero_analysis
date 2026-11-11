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

# Generate maps of mean surface temperature 
generate_figures([derived/temp/tas/all/50_years_post, derived/temp/tas/all/100_years_post, derived/temp/tas/all/300_years_post], index_to_compute = mean, figure_type = map)

# Generate time series of mean surface temperature over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/full_timeseries, derived/temp/variable=tas/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = time_series)

# Generate time series of TXx over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/full_timeseries, derived/temp/variable=tas/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = time_series)

# Generate time series of RX1day over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/full_timeseries, derived/temp/variable=tas/IPCC_Aus_2/full_timeseries, ...], index_to_compute = mean, figure_type = time_series)


# Generate distribution change in mean temperature over Aus IPCC regions
generate_figures([derived/temp/variable=tas/IPCC_Aus_1/50_years_post, derived/temp/variable=tas/IPCC_Aus_1/100_years_post, ...], index_to_compute = "", figure_type = hist)
generate_figures([derived/temp/variable=tas/IPCC_Aus_2/50_years_post, derived/temp/variable=tas/IPCC_Aus_2/100_years_post, ...], index_to_compute = "", figure_type = hist)

# Generate distribution change in tasmax over Aus IPCC regions
generate_figures([derived/temp/variable=tasmax/IPCC_Aus_1/50_years_post, derived/temp/variable=tasmax/IPCC_Aus_1/100_years_post, ...], index_to_compute = "", figure_type = hist)
generate_figures([derived/temp/variable=tasmax/IPCC_Aus_2/50_years_post, derived/temp/variable=tasmax/IPCC_Aus_2/100_years_post, ...], index_to_compute = "", figure_type = hist)

# Generate distribution change in rainfall over Aus IPCC regions
generate_figures([derived/temp/variable=rainfall/IPCC_Aus_1/50_years_post, derived/temp/variable=rainfall/IPCC_Aus_1/100_years_post, ...], index_to_compute = "", figure_type = hist)
generate_figures([derived/temp/variable=rainfall/IPCC_Aus_2/50_years_post, derived/temp/variable=rainfall/IPCC_Aus_2/100_years_post, ...], index_to_compute = "", figure_type = hist)
