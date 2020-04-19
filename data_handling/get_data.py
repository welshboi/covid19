import pandas as pd
from pathlib import Path
import xlrd


class CountryNamesMapper(object):
    def __init__(self):
        file = r"C:\Users\justin\work\2020_covid19\covid19\data\countries-20140629.csv"
        df = pd.read_csv(file, encoding='latin1')

        d_code2country = dict()
        d_country2code = dict()
        for ix, row in df.iterrows():
            d_code2country[row['Code']] = row['English Name']

        d_code2country['US'] = "United States of America"

        for k in d_code2country:
            d_country2code[d_code2country[k]] = k

        d_country2code['United States'] = 'US'
        d_country2code['US'] = 'US'

        self.country2code_dict = d_country2code
        self.code2country_dict = d_code2country

country_names_mapper = CountryNamesMapper()

def _get_covid_data(file, path=None):

    if not path:
        path = r"C:\Users\justin\work\2020_covid19\COVID-19\csse_covid_19_data\csse_covid_19_time_series"
        print(f"default path:{path}")

    # COVID-19 contains data pulled from https://github.com/CSSEGISandData/COVID-19
    _dir = Path(path)

    df = pd.read_csv(_dir / file)
    df.drop(['Lat', 'Long'], inplace=True, axis=1)
    df.set_index(['Province/State', 'Country/Region'], inplace=True)

    #for ix, row in df.iterrows():
    #    print(f"Recoding country from {ix[1]} to {country_to_code(ix[1])}")
    #    df.at[ix, 'code'] = country_to_code(ix[1])

    df.reset_index(level=['Province/State', 'Country/Region'], inplace=True)

    df.rename(columns={'Province/State': 'state'}, inplace=True)
    df['country'] = df['Country/Region'].map(country_names_mapper.country2code_dict)
    df.set_index(['country', 'state'], inplace=True)
    df = df.drop('Country/Region', 1)
    #df.reset_index(inplace=True)
    return df.T

def get_covid_data_cases_df():
    return _get_covid_data(file="time_series_covid19_confirmed_global.csv")

def get_covid_data_deaths_df():
    return _get_covid_data(file="time_series_covid19_deaths_global.csv")


def get_mortality_df():
    file = r"C:\Users\justin\work\2020_covid19\covid19\data\WPP2019_MORT_F02_CRUDE_DEATH_RATE.xlsx"

    df = pd.read_excel(file, header=16)
    return df


def get_populations_df():
    file = r"C:\Users\justin\work\2020_covid19\covid19\data\WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES.xlsx"
    df = pd.read_excel(file, header=16)
    return df

def get_country_to_states():
    country2states = {
        'US': ['New York'],
        'China': ['Hubei'],
        'Italy': [None],
        'Spain': [None]
    }

    return country2states


def get_country_codes_dicts():
    file = r"C:\Users\justin\work\2020_covid19\covid19\data\countries-20140629.csv"
    df = pd.read_csv(file, encoding='latin1')

    d_code2country = dict()
    d_country2code = dict()
    for ix, row in df.iterrows():
        d_code2country[row['Code']] = row['English Name']

    d_code2country['US'] = "United States of America"

    for k in d_code2country:
        d_country2code[d_code2country[k]] = k

    d_country2code['United States'] = 'US'
    d_country2code['US'] = 'US'

# encoding='iso-8859-1' or encoding='cp1252'
    return d_code2country, d_country2code