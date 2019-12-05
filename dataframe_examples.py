import pandas as pd

def main():

    dd = get_all_driver_data()

    leading_three = get_leading_points_scorer(3)

    pass


def get_all_driver_data():

    try:

        driver_data = pd.read_csv(r"C:\Users\alan_\PycharmProjects\F1DataScience\F1KaggleData\drivers.csv")
        head = driver_data.head()
        return driver_data

    except Exception as e:
        print(e)


def get_leading_points_scorer(top_n):

    # at some point I will need to combine the id with the drivers table to pull out
    # some human recognisable identifier

    all_results_df = pd.read_csv(r"C:\Users\alan_\PycharmProjects\F1DataScience\F1KaggleData\results.csv")

    return 1

    pass



if __name__ == "__main__":
    main()
