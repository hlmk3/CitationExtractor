## Overview
    This script (main.py) uses the **SerpAPI Google Scholar API** to fetch a list of research papers that cite a specific paper, identified by its Google Scholar ID. It retrieves the citation data in batches. The citations are then saved to a text file with details such as the title, authors, publication information, and link to each citing paper. The other script (doc.py) gets the data in the text file and converts it to a table and saves as numbers file.
    - To get the Google Scholar ID:
        An example of link to the specific paper: https://scholar.google.com/scholar?cites=12345678901234567890
        Here the id is --> 12345678901234567890

## Prerequisites
    - Python 3.7 or higher
    - A valid SerpAPI API key (sign up at SerpAPI).
