import requests

def fetch_citations(cited_by_id, api_key, num_results=170):
    """
    Fetches the list of articles citing a specific paper from the SerpAPI Google Scholar API with pagination.

    Parameters:
        cited_by_id (str): The unique identifier of the paper (Google Scholar ID).
        api_key (str): Your SerpAPI API key.
        num_results (int): Total number of citations to fetch.

    Returns:
        list: A list of dictionaries with citation details.
    """
    url = "https://serpapi.com/search"
    citations = []

    for start in range(0, num_results, 10):  # Fetch in batches of 10
        params = {
            "engine": "google_scholar",
            "cites": cited_by_id,
            "api_key": api_key,
            "start": start
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            page_citations = response.json().get("organic_results", [])
            citations.extend(page_citations)  # Add the citations from this page
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break

    return citations

def save_citations_to_file(citations, file_name="citations.txt"):
    """
    Saves the citation details to a text file.

    Parameters:
        citations (list): A list of dictionaries containing citation details.
        file_name (str): The name of the text file to save the citations.
    """
    with open(file_name, "w") as file:
        for i, citation in enumerate(citations, start=1):
            title = citation.get("title", "No Title")
            authors = citation.get("publication_info", {}).get("authors", "No Authors")
            link = citation.get("link", "No Link")
            
            # Extract the entire summary for publication information (journal, publisher, year, etc.)
            summary = citation.get("publication_info", {}).get("summary", "No Summary")
            
            file.write(f"{i}. Title: {title}\n")
            file.write(f"   Authors: {authors}\n")
            file.write(f"   Publication Info: {summary}\n")
            file.write(f"   Link: {link}\n")
            file.write("\n")

    print(f"Citations have been saved to {file_name}")

def main():
    # Replace with your actual SerpAPI key
    api_key = "#######"
    
    # Replace with the Google Scholar ID of the paper you are analyzing
    cited_by_id = "#############"

    # Fetch citations
    citations = fetch_citations(cited_by_id, api_key)

    if citations:
        # Save the citations to a text file
        save_citations_to_file(citations)
    else:
        print("No citations found or an error occurred.")

if __name__ == "__main__":
    main()
