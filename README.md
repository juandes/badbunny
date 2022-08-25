# When do I listen to Bad Bunny?

## Description

This repo contains all the resources I used for my experiment "When do I listen to Bad Bunny?" 

Bad Bunny is an urban and Puerto Rican singer who has become a global star in the last few years. As the title indicates, in this project, I'm using Spotify data I've been collecting since late 2017 to find out when I listen to his music. To solve this mystery, I did a data analysis using Python and R, which includes data exploration, visualizations, time series, and anomaly detection.

## Structure

The repo has the following structure:

- `bqWriter/`: the script I used to read my Spotify account's recently played track and write the results to BigQuery.
- `data/`: the datasets I used for the experiment.
    - `df.csv`: the dataset containing all the Bad Bunny data. Each row represents a song I listened to.
    - `results.csv`: the outputs from the anomaly detection algorithm (isolation forest). The first column, `predictions` is the prediction (`-1` = anomaly, `1` = non-anomalous), and `scores` is the prediction score (the lowest the score, the more anomalous).
    - `timeseries_data.csv`: the data I used to train the time series model. The first column, `ds`, is the date, and the second column, `y`, is the number of Bad Bunny songs I listened to on that day.
    - `weekdays_hours.csv`: the data I used to train the anomaly detection model. It has two features, `hour`, the hour (in 24 hours) when I listened to a song, and `weekday`, the day of the week. I'm using one-hot encoding in the training script to transform the `weekday` column into seven columns (one per day).
- `notebooks/`:  the notebooks I wrote during the analysts.
  - `analysis.Rmd`: the data analysis (written in R). It has the code that summarizes the dataset, explores it, and visualizes it.
  - `analysis_ES.Rmd`: a copy of the previous script with the visualizations translated to Spanish.
  - `isolation_forest.ipynb`: the script that trains the isolation forest model.
  - `timeseries.ipynb`: the script that trains the time series model.
- `plots/`: all the plots I created as part of the analysis. There's an English and Spanish (these files are suffixed with "_ES") version of each chart.
- `service/`: an incomplete skeleton code of a service I want to build with **FastAPI** to serve the model's predictions. Here you will find an exported copy (`model.joblib`) of the isolation model I trained.

## Library used
- [scikit-learn](https://scikit-learn.org/): to train the isolation forest model.
- [Prophet](https://facebook.github.io/prophet/docs/quick_start.html): to train the time series model.
- [ggplot2](https://ggplot2.tidyverse.org/): to create the visualizations in R.
- [skimr](https://cran.r-project.org/web/packages/skimr/vignettes/skimr.html): An R package that provide summary statistics.
- [tidyr](https://tidyr.tidyverse.org/) and [dplyr](https://dplyr.tidyverse.org/): to manipulate my data.


### Notes

I presented this work (in Spanish) at PyCon Latam 2022. For details, see: https://pylatam.org/#schedule.