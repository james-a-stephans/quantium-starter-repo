import csv
from pathlib import Path

with open("./output_file.csv", "w") as new_file:
    #Print header for output file.
    print("sales,date,region", file=new_file)

    #Get all csv files in the data folder.
    data_path = Path("./data")
    csv_files = data_path.glob("*.csv")

    #Process all csv files into the designated output file.
    for file in csv_files:
        with open(file) as file:
            data_reader = csv.reader(file)

            for row in data_reader:
                #Only process rows for the pink morsel product. This also skips the header row.
                if "pink morsel" in row:
                    #Slice the $ character out of the price column of this row, then convert it into a floating point number.
                    price = float(row[1][1:])
                    quantity = int(row[2])

                    #Prepare a new row to go into the output file.
                    output = str(price * quantity) + "," + row[3] + "," + row[4]

                    #Print the new row into the output file.
                    print(output, file=new_file)