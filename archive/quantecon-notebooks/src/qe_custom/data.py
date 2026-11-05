from pathlib import Path

import pandas as pd
import requests

from .paths import data_dir


def load_data(version="2020", sheet="Full data"):
    """
    Load the data for the first course in QuantEcon.
    """
    if version == "2020":
        # check if the 2020 data file exists
        path = Path(f"{data_dir('external')}/mpd2020.xlsx")
        if not path.exists():
            # download the 2020 data file from the course website
            data_url = (
                "https://github.com/QuantEcon/data-lectures/raw/main/"
                "lectures/mpd2020.xlsx"
            )
            response = requests.get(data_url)
            with open(f"{data_dir('external')}/mpd2020.xlsx", "wb") as f:
                f.write(response.content)

    elif version == "2023":
        # load the 2023 data file
        path = Path(f"{data_dir('external')}/mpd2023.xlsx")
        if not path.exists():
            raise FileNotFoundError(
                "The 2023 data file does not exist. Please download it from"
                " the course website."
            )
    else:
        raise ValueError(
            "Invalid version specified. Please choose '2020' or '2023'."
        )

    if sheet == "Regional data":
        # load the regional data sheet
        data = pd.read_excel(
            path, sheet_name=sheet, header=(0, 1, 2), index_col=0
        )
        data.columns = data.columns.droplevel(level=2)
    else:
        # load the full data sheet
        data = pd.read_excel(path, sheet_name=sheet)
    return data
