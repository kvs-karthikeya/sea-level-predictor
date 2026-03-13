# Sea Level Predictor

A freeCodeCamp Data Analysis with Python project.

## What it does

Analyzes global average sea level change since 1880 and predicts sea level rise through 2050 using linear regression.

## Chart Generated

A scatter plot with two lines of best fit:
- **Red line** — uses all data from 1880 to present, extended to 2050
- **Green line** — uses only data from 2000 onwards, extended to 2050 (shows recent acceleration)

## How to run

```bash
pip install pandas matplotlib scipy
python main.py
```

## Output

- `sea_level_plot.png` — the generated chart

## Dataset

`epa-sea-level.csv` — Global Average Absolute Sea Level Change, 1880-2014.  
Source: US Environmental Protection Agency (CSIRO, 2015; NOAA, 2015)

## Built with

- Python
- Pandas
- Matplotlib
- SciPy (linregress)
