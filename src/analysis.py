def compute_over_layer(
    dataset, variable=None, layer_base=0, layer_top=600, function="mean"
):
    """Returns bulk values for a layer

    altitude dimension name must be 'alt'
    """

    if function == "mean":

        if variable is None:
            return dataset.sel(alt=slice(layer_base, layer_top)).mean(dim="alt")

        return dataset[variable].sel(alt=slice(layer_base, layer_top)).mean(dim="alt")

    elif function == "std":

        if variable is None:
            return dataset.sel(alt=slice(layer_base, layer_top)).std(dim="alt")

        return dataset[variable].sel(alt=slice(layer_base, layer_top)).std(dim="alt")

    else:

        print("specified function should be either mean or std")
