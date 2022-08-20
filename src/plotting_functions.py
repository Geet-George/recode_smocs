import numpy as np
import scipy as sp


def reg_line(
    ax,
    x,
    y,
    print_r=True,
    text_title=True,
    r_loc=(0.75, 0.75),
    kwargs_for_text={},
    kwargs_for_axline={},
):
    """Plots regression line"""

    m, b = np.polyfit(x, y, 1)

    if print_r:
        r, _ = sp.stats.pearsonr(x, y)

        if text_title:
            ax.set_title("r={:.2f}".format(r), **kwargs_for_text)
        else:
            ax.text(
                r_loc[0],
                r_loc[1],
                "r={:.2f}".format(r),
                transform=ax.transAxes,
                **kwargs_for_text
            )

    ax.axline(xy1=(0, b), slope=m, **kwargs_for_axline)

    return ax


def sci_exp_axis(i, axis="x", x_pad=0.75, y_pad=0.01, scilimits=(-1, 1)):
    """Returns exponents in scientific notation
    
    :param i: Matplotlib axis object  
    
    :return: Matplotlib axis object with ticklabels formatted in scientific notation and exponent as string
    """

    if axis == "x":
        exponent_int = np.floor(np.log10(np.max(i.get_xlim()))).astype(int)

        if exponent_int < -2:

            i.ticklabel_format(axis=axis, style="sci", scilimits=scilimits)
            i.xaxis.major.formatter._useMathText = True

            exponent_text = str(exponent_int)
            i.annotate(
                r"$\times$10$^{%s}$" % (exponent_text),
                xy=(x_pad, y_pad),
                xycoords="axes fraction",
            )

            i.get_xaxis().get_offset_text().set_visible(False)

    elif axis == "y":

        exponent_int = np.floor(np.log10(np.max(i.get_ylim()))).astype(int)

        if exponent_int < -2:

            i.ticklabel_format(axis=axis, style="sci", scilimits=scilimits)
            i.yaxis.major.formatter._useMathText = True

            exponent_text = str(exponent_int)
            i.annotate(
                r"$\times$10$^{%s}$" % (exponent_text),
                xy=(x_pad, y_pad),
                xycoords="axes fraction",
            )

            i.get_yaxis().get_offset_text().set_visible(False)
    else:
        print("specified axis should be either x or y")

    return i, exponent_int
