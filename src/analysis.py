def compute_over_layer(
    dataset, 
    variable=None, 
    layer_base=0, 
    layer_top=600, 
    function="mean"
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

def fit_pressure_to_altitude(
    source_ds:"xr.Dataset",
    recipient_ds:"xr.Dataset",
    mean:"bool"=True,
    source_alt_dim='alt',
    source_pressure_dim='p',
    recipient_alt_dim='alt',
    recipient_pressure_dim='level',
):

    """
    returns recipient_ds with dims swapped from pressure to altitude

    pressure is for nearest altitude level (not interpolated),
    so this function only works for profiles with high vertical resolution

    if there are multiple pressure profiles, keep mean=True;
    otherwise provide single pressure profile

    altitude to pressure profile is taken by estimating mean pressure over all dimensions 
    except provided source_alt_dim (default = 'alt')

    Units of pressure are assumed to be Pa for source and hPa for recipient

    The dataset is returned with altitude coordinates in ascending order
    """
    if mean:
        mean_dims = list(source_ds.dims)
        mean_dims.remove('alt')

        alt_for_recipient = source_ds.mean(dim=mean_dims).swap_dims(
            {source_alt_dim:source_pressure_dim}).dropna(dim=source_pressure_dim,how='any').reindex(
            {source_pressure_dim:recipient_ds[recipient_pressure_dim].values*100},method='nearest')[source_alt_dim].values.astype('float')
    else:
        alt_for_recipient = source_ds.swap_dims(
            {source_alt_dim:source_pressure_dim}).dropna(dim=source_pressure_dim,how='any').reindex(
            {source_pressure_dim:recipient_ds[recipient_pressure_dim].values*100},method='nearest')[source_alt_dim].values.astype('float')

    recipient_ds[recipient_alt_dim] = ([recipient_pressure_dim],alt_for_recipient)

    recipient_ds = recipient_ds.swap_dims({recipient_pressure_dim:recipient_alt_dim}).sortby(recipient_alt_dim)
    
    return recipient_ds


def r_value(x,y):  
    """Returns Pearson's r-value after removing NaNs from the input arrays

    Parameters
    ----------
    x : ndArray
    y : ndArray

    Returns
    -------
    float64
        Pearson's r-value between x & y
    """
    import numpy as np
    import scipy as sp

    nas = np.logical_or(np.isnan(x), np.isnan(y))
    if sum(~nas) > 1 :
        return sp.stats.pearsonr(x[~nas],y[~nas])[0]