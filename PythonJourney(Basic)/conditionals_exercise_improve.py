def num_days(month):
    if month in ["January", "March", "May", "July", "August", "October", "December"]:
        return 31
    elif month in ["April", "June", "September", "November"]:
        return 30
    elif month == "February":
        return 28
    else:
        return None