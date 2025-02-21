def num_days(month):
    month = month.lower()
    
    print(month)
    if month in ["january", "march", "may", "july", "august", "october", "december"]:
        return 31
    elif month in ["april", "june", "september", "november"]:
        return 30
    elif month == "february":
        return 28
    else:
        return None 
    
print(num_days(input('Write Month: \n')))