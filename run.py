import networkx as nx
import pandas as pd
import os


def main():
    fpath = os.path.join("..", "data", "unicorn_company_invester.csv")
    df = pd.read_csv(fpath, conveters={"Select Investors": lambda x: x.split(,)})


if __name__ == "__main__":
    main()