import os
from csv_adapter import csv_adapter
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

filename = "test/1row_sample.csv"


@pytest.mark.skip
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
    # assert headers
    assert list(mappings.values()) == list(fields)
    # assert values


def test_runs_ok():
    columns = [
        "nvcPath",
        "iInteractionID",
        "dtInteractionLocalStartTime",
        "dtInteractionLocalStopTime",
        "nvcFirstName",
        "nvcLastName",
        "nvcPhoneNumber",
        "nvcAgentId",
        "Duration",
        "iHoldCount",
        "iHoldDuration",
        "nvcUserLoginName",
        "nvcStation",
        "Queue",
        "Queue Name",
        "Call_SUB_CD",
        "Call_TYP_CD",
        "Cust_ID",
        "CUST_PHN_NBR",
        "",
        "CUST_ACCT_NUM",
        "Direction",
        "icompoundid",
        "iLogger",
        "Segment_UCID",
    ]
    data = [
        [
            "Audio\\sample.wav",
            "456",
            "4/4/20 10:52 AM",
            "4/4/20 11:04 AM",
            "Simone",
            "Baptiste",
            "404",
            "",
            "0",
            "0",
            "0",
            "U133033_3",
            "9876",
            "NULL",
            "NULL",
            "0",
            "40011",
            "875683008",
            "7819641963",
            "",
            "281947005",
            "Incoming",
            "1234",
            "98",
            "1022081586015210",
        ]
    ]
    orig_df = pd.DataFrame(data, columns=columns)
    orig_df.to_csv(temp_dir("NICE_export.csv"), index=False)

    output_file = csv_adapter.run(temp_dir("NICE_export.csv"))

    expected_data = {
        "filename": ["Audio\\sample.wav"],
        "ContactID": ["1234"],
        "SessionID": ["456"],
        "StartTime": ["4/4/20 10:52 AM"],
        "EndTime": ["4/4/20 11:04 AM"],
        "ANI": ["404"],
        "Direction": ["Incoming"],
        "NumberOfHolds": ["0"],
        "TotalHoldTime": ["0"],
        "Extension": ["9876"],
        "PbxLoginId": ["U133033_3"],
        "Attribute1": ["Baptiste"],
        "Attribute2": ["Simone"],
    }
    assert_file_matches(expected_data, output_file)


def temp_dir(filename=None):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tmp_dir = os.path.join(dir_path, ".temp")
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    if filename:
        tmp_dir = os.path.join(tmp_dir, filename)
    return tmp_dir


def assert_file_matches(expected_data, filepath):
    expected_df = pd.DataFrame(expected_data)
    actual_df = pd.read_csv(filepath)
    actual_df = actual_df.astype(
        str
    )  # convert all to string, e.g long numbers treated as str
    assert_frame_equal(expected_df, actual_df)
