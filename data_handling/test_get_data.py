import unittest
from data_handling import get_data


class TestGetData(unittest.TestCase):



    def test_get_mortality_data(self):
        mortality = get_data.get_mortality_df()
        self.assertGreater(len(mortality), 0)

    def test_get_country_codes_dicts(self):
        d1, d2 = get_data.get_country_codes_dicts()
        self.assertGreater(len(d1), 0)
        self.assertGreater(len(d2), 0)
        self.assertIn("GB", d1.keys())
        self.assertIn("United Kingdom", d2.keys())

    def test_country_to_code(self):
        self.assertEqual(get_data.country_names_mapper.country2code_dict['United Kingdom'], 'GB')

    def test_get_population_data(self):
        df = get_data.get_populations_df()
        self.assertGreater(len(df), 0)

    def test_get_covid_data(self):
        cases = get_data.get_covid_data_cases_df()
        self.assertGreater(len(cases), 0)

        deaths = get_data.get_covid_data_deaths_df()
        self.assertGreater(len(deaths), 0)

if __name__ == '__main__':
    unittest.main()
