import os
import pandas as pd


def label_ANI(row):
    if row["Direction"] in ["Internal", "Outgoing"]:
        return row["nvcStation"]

    elif row["Direction"] == "Incoming":
        return row["nvcPhoneNumber"]


def read_csv(filename, mappings):
    columns = mappings.keys()
    csvfile = pd.read_csv(filename)
    csvfile["ANI"] = csvfile.apply(lambda row: label_ANI(row), axis=1)
    csvfile = csvfile[columns]
    return csvfile.rename(columns=mappings)


mappings = {
    "nvcPath": "filename",
    "icompoundid": "ContactID",
    "iInteractionID": "SessionID",
    "dtInteractionLocalStartTime": "StartTime",
    "dtInteractionLocalStopTime": "EndTime",
    "Direction": "Direction",
    "iHoldCount": "NumberOfHolds",
    "iHoldDuration": "TotalHoldTime",
    "nvcStation": "Extension",
    "nvcUserLoginName": "PbxLoginId",
    "nvcLastName": "Attribute1",
    "nvcFirstName": "Attribute2",
}


def run():
    filename = input("Enter the metadata filepath to convert:")
    # csvfile = read_csv(filename, mappings)

    file_ext = os.path.splitext(filename)
    output_default = file_ext[0] + "_output" + file_ext[1]
    output_file_message = "Enter output filepath (default is '" + output_default + ")':"
    outputfile = input(output_file_message)
    if not outputfile:
        outputfile = output_default
    print(outputfile)
    # csvfile.to_csv(outputfile, index=False)
