import csv

def process_csv(file_path, dest_file):
    data_reader = csv.reader(file_path)

    for row in data_reader:
        if row[0] == "pink morsel":
            price = float(row[1][1:])
            quantity = int(row[2])
            output = str(price * quantity) + "," + row[3] + "," + row[4]
            print(output, file=dest_file)

with open("./output_file.csv", "w") as new_file:
    print("sales,date,region", file=new_file)
    with open("./data/daily_sales_data_0.csv") as data_one:
        process_csv(data_one, new_file)

    with open("./data/daily_sales_data_1.csv") as data_two:
        process_csv(data_two, new_file)

    with open("./data/daily_sales_data_2.csv") as data_three:
        process_csv(data_three, new_file)