from libs import get_data, export_xls

if __name__ == "__main__":
    all_data = get_data()

    export_xls("output-data.xlsx", all_data)

    print("Program finished!")
