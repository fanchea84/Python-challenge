# define variables
    month_count = 0
    total_value = 0
    PL_change_current = 0
    PL_change_total = 0
   # Read each row of data after the header
    for row in csvreader:
        # new_value = old_value + int(row[1])
        # read the value in each row
        month_count = month_count + 1
        total_value += int(row[1])
        # define average change over period of time
        old_month = new_month
        print(f"old month", old_month)
        new_month = int(row[1])
        print(f"new month",new_month)
        # PL_change_old = PL_change_current
        # print(f"Profit change old", PL_change_old)
        PL_change_current = new_month - old_month
        print(f"profit change current", PL_change_current)
        PL_change_total = PL_change_total + PL_change_current
        print(f"profit change total", PL_change_total)