import os
from csv_adapter.csv_adapter import read_csv


filename = "test/1row_sample.csv"


def test_remove_one_column():
    mappings = {
        "nvcPath": "filename",
        "icompoundid": "ContactID",
        "iInteractionID": "SessionID",
        "dtInteractionLocalStartTime": "StartTime",
        "dtInteractionLocalStopTime": "EndTime",
        "ANI": "ANI",
        "Direction": "Direction",
        "iHoldCount": "NumberOfHolds",
        "iHoldDuration": "TotalHoldTime",
        "nvcStation": "Extension",
        "nvcUserLoginName": "PbxLoginId",
        "nvcLastName": "Attribute1",
        "nvcFirstName": "Attribute2",
    }
    csvfile = read_csv(filename, mappings)
    file_ext = os.path.splitext(filename)
    csvfile.to_csv(file_ext[0] + "_output" + file_ext[1], index=False)

    fields = csvfile.columns
    assert list(mappings.values()) == list(fields)
