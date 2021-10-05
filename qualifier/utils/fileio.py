# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(csvpath, header, loans):
    """Save bank loan data to a CSV file.

    Args:
        csvpath (Path): The CSV file path
        header (list):  Descriptive list of value fields
        loans: Bank data, list of lists 
    """

    print("\nSaving loans\n")
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)

        for item in loans:
            csvwriter.writerow(item)

