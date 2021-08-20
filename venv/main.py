import pandas as pd
import argparse
import sys
import datetime as dt

def crude(args):
    #Import CSV
   raw_csv = pd.read_csv("MSW.CSV")
    #CSV to Dataframes
   df = pd.DataFrame(raw_csv)
    #Change the Date format from str
    #startdate
   start_date_str = args.start_date
   start = dt.datetime.strptime(start_date_str, "%Y-%m-%d")
   start = start.date()
   start = start.isoformat()
    #End date
   end_date_str = args.end_date
   end = dt.datetime.strptime(end_date_str, "%Y-%m-%d")
   end = end.date()
   end = end.isoformat()

    #Filter the dates based on input
   after_start = df[2] >= start
   before_end = df[2] <= end
   filtred_date_data = after_start & before_end

    #Final result using loc
   df.loc[(df[5] > args.limit) & filtred_date_data & (df[1] == args.crude_acronym)]

# Python code as Command utility
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # Input from user as args
    parser.add_argument('--crude_acronym', type=str, default='msw')
    parser.add_argument('--start_date', default='2011-07-13', help="Enter the date in YYYY-MM-DD format")
    parser.add_argument('--end_date', default='2021-07-13', help="Enter the date in YYYY-MM-DD format")
    parser.add_argument('--operation', type=str, default='greater_than')
    parser.add_argument('--limit', type=int, default=833)

    args = parser.parse_args()
    sys.stdout.write(str(crude(args)))
