
# coding: utf-8

# In[1]:


from pathlib import Path
import pandas as pd
from ipywidgets import widgets
from ipywidgets import interact, interactive, fixed, interact_manual


# In[2]:

def main():
    # Pre-processed data saved in Parquet fomrat
    DATA = Path("../data")
    DRY = DATA / "dry-minute-2018.parquet"
    HUMID = DATA / "humid-minute-2018.parquet"

    if DRY.exists() and HUMID.exists():
        # This loads much faster than from CSV
        dry = pd.read_parquet(DRY)
        humid = pd.read_parquet(HUMID)
    else:

        #\\cfs2e.nist.gov\73_EL\731\internal\CONFOCAL\FS2\Data4\Sandia\Sandia Chamber Data-NIST\1 second data\Humid\1 minute mean
        # Path to 1-min raw data, you may need to adjust these accordingly.
        #DATA = Path("/Volumes/Sandia Chamber Data-NIST/1 second data/")
        #DRY = DATA / "Dry" / "1 minute mean" / "Dry 2018.csv"
        #HUMID = DATA / "Humid" / "1 minute mean" / "Humid 2018.csv"
        DRY = "Dry 2018.csv"
        HUMID = "Humid 2018.csv"
        # This could take a minute to load, depending on file location
        dry = pd.read_csv(DRY, parse_dates=[[0, 1]], index_col=0)
        humid = pd.read_csv(HUMID, parse_dates=[[0, 1]], index_col=0)
        dry.to_parquet("sandia-graph/dry-minute-2018.parquet")
        humid.to_parquet("sandia-graph/humid-minute-2018.parquet")


    # In[3]:


    # Aggregate Hourly
    dry_hourly = dry.resample('H').mean()
    humid_hourly = humid.resample('H').mean()

    # Column Names
    DRY_COLS = dry.columns.tolist()
    HUMID_COLS = humid.columns.tolist()


    # In[4]:


    drySelect = widgets.SelectMultiple(
        options=DRY_COLS,
        value=DRY_COLS[:1],
        description='Temperature:',
        disabled=False,
    )

    def plot_dry(cols):
        print(cols)
        dry_hourly.loc[:, cols].plot()
        
    iplot = interactive(plot_dry, cols=drySelect)
    output = iplot.children[-1]
    output.layout.height = '350px'
    iplot


    # In[5]:


    humidSelect = widgets.SelectMultiple(
        options=HUMID_COLS,
        value=HUMID_COLS[:1],
        description='Temperature:',
        disabled=False,
    )

    def plot_humid(cols):
        print(cols)
        humid_hourly.loc[:, cols].plot()

    iplot = interactive(plot_humid, cols=humidSelect)
    output = iplot.children[-1]
    output.layout.height = '350px'
    iplot

main()
