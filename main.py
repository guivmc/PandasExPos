# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    df = pd.read_csv('winemag-data_first150k.csv')
    df.head()
    # df.info()
    print(df.columns)

    # PAISES:
    # print('Total de paises: ', len(df.groupby(by='country').groups.keys()))
    #
    # print('Total de vinhos por pais: ')
    # print(df.groupby(by='country').size().add_suffix(','))
    #
    # print('Media do preco do vinho por pais: ')
    # print(df.groupby(by='country')['price'].mean().add_suffix(','))
    #
    # print('Media de pontos do vinho por pais: ')
    # print(df.groupby(by='country')['points'].mean().add_suffix(','))

    # DESTILARIAS

    # print(df.groupby(by='winery')['price'].mean().add_suffix(','))

    # print(df.groupby(by='winery')['points'].mean().add_suffix(','))

    #Variacao

    # print(df.groupby(by='variety')['price'].mean().add_suffix(','))

    # print(df.groupby(by='variety')['country'].size().add_suffix(','))

    # print(df.groupby(by='variety')['country'].size().add_suffix(','))

    # print(df.groupby(by='variety')['country'].size().add_suffix(','))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
