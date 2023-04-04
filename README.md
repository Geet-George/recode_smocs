[![pip](https://github.com/Geet-George/recode_smocs/actions/workflows/pip.yml/badge.svg)](https://github.com/Geet-George/recode_smocs/actions/workflows/pip.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Geet-George/recode_smocs/HEAD)
# recode_smocs

This repo contains the src files and notebooks that will help reproduce the analysis and plots in the SMOCs manuscript, i.e "Widespread shallow mesoscale circulations amplify moisture variance in the trades". 

Click on the `launch binder` badge above to run the notebooks interactively. Give it 5-7 minutes to start up the interactive notebook session. Note that the JOANNE notebook accesses data solely from the [EUREC4A intake-catalog](https://github.com/eurec4a/eurec4a-intake) and therefore, would run straight out of the box. However, the ERA5 notebook will not as it needs a `CONFIG` file which provides the path to downloaded reanalyses data. The dataset is publicly and freely accessible. Details are provided in the manuscript. 
