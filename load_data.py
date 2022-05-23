import pandas as pd


def load(in_path, expected_path):
    df = pd.read_table(in_path, header=None,
                       names=[str(i) for i in range(101)])
    df_expeced = pd.read_table(expected_path, header=None,
                       names=['exp'])
    col_names = list(df.columns)
    X = []
    candidates_list = []
    for index, row in df.iterrows():
        candidates = []
        x = ''
        for nam in col_names:
            if nam != '0':
                candidates.append(row[nam])
            else:
                x = row[nam]
        X.append(x)
        candidates_list.append(candidates)

    return X, candidates_list, list(df_expeced['exp'])
