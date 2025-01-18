Overview
    This script (main.py) uses the SerpAPI Google Scholar API to fetch a list of research papers that cite a specific paper, identified by its Google Scholar ID. It retrieves the citation data in batches and filters the results based on the year of publication (if a year threshold is provided). The filtered citations are then saved to a text file with details such as the title, authors, publication information, and link to each citing paper. The other script (doc.py) gets the data in the text file and converts it to a table and saves as numbers file.

Prerequisites
    Python 3.7 or higher
    A valid SerpAPI API key (sign up at SerpAPI).