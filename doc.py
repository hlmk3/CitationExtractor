import openpyxl
from openpyxl.styles import Font
import re

def create_table_from_file(input_file, output_file):
    # Open the citation.txt file and read the contents
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Create a new Excel workbook and sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Citations"

    # Add the header row with an additional Journal column
    sheet.append(["Title", "Authors", "Publication Info", "Link", "Journal"])

    citation_data = []
    citation = {}

    # Define a regex pattern to capture lines starting with a number
    title_pattern = re.compile(r'^\d+\.\s*Title:\s*(.*)|^Title:\s*(.*)')

    # Process each line in the citation file
    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        
        # Skip blank lines
        if not line:
            continue
        
        # Check for a line that starts with a number and extract the title
        title_match = title_pattern.match(line)
        if title_match:
            if citation:  # Save the current citation if it exists
                citation_data.append(citation)
            citation = {"Title": title_match.group(1)}

        elif line.startswith("Authors:"):
            authors = line.replace("Authors: ", "")
            citation["Authors"] = authors
        elif line.startswith("Publication Info:"):
            citation["Publication Info"] = line.replace("Publication Info: ", "")
        elif line.startswith("Link:"):
            citation["Link"] = line.replace("Link: ", "")

    # Add the last citation if there is any
    if citation:
        citation_data.append(citation)

    # Ensure all required fields are present in each citation
    for citation in citation_data:
        # Set default empty values for missing fields
        title = citation.get("Title", "No Title")
        authors = citation.get("Authors", "No Authors")
        publication_info = citation.get("Publication Info", "No Publication Info")
        link = citation.get("Link", "No Link")

        # Add the citation to the Excel sheet
        row = [title, authors, publication_info, link]

        # Extract the journal name (everything after "- ")
        journal_name = ""
        if "- " in publication_info:  # Check for the presence of "- " (journal prefix)
            journal_name = publication_info.split("- ")[1].split(",")[0].strip()

        row.append(journal_name)  # Add the journal name to the new Journal column
        sheet.append(row)

        # Apply bold to the journal name in the Journal column
        for cell in sheet.iter_rows(min_row=2, min_col=5, max_col=5):  # The Journal column
            for cell in cell:
                if cell.value == journal_name:  # If the journal name matches
                    cell.font = Font(bold=True)

    # Save the workbook
    wb.save(output_file)

    print(f"Table has been saved to {output_file}")

# Example usage
create_table_from_file("citations.txt", "citations_table.xlsx")
