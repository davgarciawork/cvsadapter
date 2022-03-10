def rule_ANI(row):
    if row["Direction"] in ["Internal", "Outgoing"]:
        return row["nvcStation"]

    elif row["Direction"] == "Incoming":
        return row["nvcPhoneNumber"]


def rule_ContactID(row):
    if row["Direction"] in ["Internal", "Outgoing"]:
        return row["nvcStation"]

    elif row["Direction"] == "Incoming":
        return row["nvcPhoneNumber"]


mappings = {
    "nvcPath": "filename",
    "icompoundid": "ContactID",
    "iInteractionID": "SessionID",
    "dtInteractionLocalStartTime": "StartTime",
    "dtInteractionLocalStopTime": "EndTime",
    "rule_ANI": "ANI",
    "Direction": "Direction",
    "iHoldCount": "NumberOfHolds",
    "iHoldDuration": "TotalHoldTime",
    "nvcStation": "Extension",
    "nvcUserLoginName": "PbxLoginId",
    "nvcLastName": "Attribute1",
    "nvcFirstName": "Attribute2",
}
