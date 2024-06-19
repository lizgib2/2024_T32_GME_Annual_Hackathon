# 2024 T32 GME Annual Hackathon

Github repo for the Genetic Mechanisms and Evolution Training Grant 2024 annual hackathon! This repo will host the code used during the hackathon.

## Installing Dependencies

### Python instructions

Its optional, but you may want to create a new conda environment for the hackathon with:

```
conda create -n hackathon python=3.11
```

Then activate the environment with:

```
conda activate hackathon
```

Then install the following packages as…

```
conda install jupyter
conda install ipykernel
conda install plotly
pip install dash
conda install numpy
conda install pandas
conda install seaborn
conda install matplotlib
conda install nbformat
conda install orjson
pip install kaleido
```

### R instructions

Install the following libraries in the R Studio terminal…

```
install.packages(“plotly”)
install.packages(“shiny”)
install.packages(“ggplot2”)
install.packages(“dplyr”)
install.packages(“jsonlite”)
install.packages(“htmlwidgets”)
install.packages(“gapminder”)
install.packages(“quantmod”)
```

Dash isn’t on CRAN for some reason, so if you want to use Dash, you’ll need to execute the following. However, it requires that you have a GitHub account, generate an SSH token, and then add that to your computer’s SSH key list before it’ll let you download it. Alternatively, you may be able to download it directly from the dashR github page and install the file directly, but this hasn't been tested yet.

```
install.packages("devtools")
devtools::install_github(“plotly/dashR”, ref=“dev”, upgrade = TRUE) (edited) 
```


