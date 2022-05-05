import requests
import json

from typing import Any, Dict
from bs4 import BeautifulSoup


class InvalidStateName(Exception):
    pass


class StateScraper:
    STATES = [
        "Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware",
        "Florida", "Georgia_(U.S._state)", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky",
        "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
        "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico",
        "Nevada", "New York_(state)", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington_(state)", "Wisconsin",
        "West Virginia", "Wyoming"
    ]

    @staticmethod
    def get_raw_state_info(state: str, base_url: str ="https://en.wikipedia.org/wiki") -> Dict[str, Any]:
        """
        Rerieves general information about a state contained within a table on the associated
        wikipedia page
        """
        if state not in StateScraper.STATES:
            raise InvalidStateName

        state_info = {"state": state}

        resp = requests.get(f"{base_url}/{state.title()}")
        soup = BeautifulSoup(resp.content, "html.parser")

        # get the table with info from wiki page
        tables = soup.find("table", {"class": "infobox ib-settlement vcard"})

        # parse table to get general information
        for table in tables:
            rows = table.find_all("tr")

            for row in rows:
                cells = row.find("th"), row.find("td")
                if cells[0] is not None and cells[1] is not None:
                    # encode to ascii to remove special characters
                    key = cells[0].text.encode("ascii", "ignore")
                    value = cells[1].text.encode("ascii", "ignore")
                    state_info[key.decode()] = value.decode()

        return state_info

    @staticmethod
    def clean_state_info(state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Given a dictionary of general information about a state, cleans and standardizes key values
        and contains atleast the defaults defined initially even if unknown.
        """
        # cleaned_dict should have atleast the values set here, even if unknown
        cleaned_dict = {
            "capital": "Unknown",
            "largest_city": "Unknown",
            "governor": "Unknown",
            "admitted": "Unknown",
            "area": "Unknown"
        }

        for k, v in state.items():
            if k == "Capital(and largest city)":
                cleaned_dict["capital"] = v
                cleaned_dict["largest_city"] = v
            elif k == "Total":
                cleaned_dict["area"] = v
            elif k == "Admitted to the Union":
                cleaned_dict["admitted"] = v
            else:
                key = k.replace(" ", "_").lower()
                cleaned_dict[key] = v
            
        return cleaned_dict


if __name__ == "__main__":
    all_states_info = list()
    scraper = StateScraper()
    state = "Arizona"

    s = scraper.get_raw_state_info(state)
    clean_state = scraper.clean_state_info(s)

    print(clean_state)
