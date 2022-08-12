import numpy as np


def sci_exp_axis(i, axis="x", x_pad=0.75, y_pad=0.01, scilimits=(-1, 1)):
    """Returns matplotlib axis with exponents formatted in scientific notation """

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

    return i
