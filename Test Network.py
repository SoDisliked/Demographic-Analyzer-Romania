import unittest 

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        def __demographic_data_analyzercalculate_demographic_data__(print_data = False)
            print_data = False 

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [1000, 2000, 5000, 10000, 20000, 50000]
        self.assertAlmostEqual(actual, expected, "Expected race count values to be[1000, 2000, 5000, 10000, 20000, 50000]")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 40,3
        self.assertAlmostEqual(actual, expected, "Expected different value for average age of men.")

    def test_percentage_education(self):
        actual = self.data['percentage_education']
        expected = 3.5
        self.assertAlmostEqual(actual, expected, "Expected percentage of people having an educational background.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 20000
        self.assertAlmostEqual(actual, expected, "Expected value of people having a higher pay depending on their educational background.")

    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 2000
        self.assertAlmostEqual(actual, expected, "Expected value of people having a lower pay depending on their educational background.")    

    def test_average_works_hours(self):
        actual = self.data['average_works_hours']
        expected = 35
        self.assertAlmostEqual(actual, expected, "Expected average hours of work for higher_education_rich")

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 0.25 
        self.assertAlmostEqual(actual, expected, "Expected percentage of people who have an income above 25000")

    def test_highest_earning_region(self):
        actual = self.data['highest_earning_region']
        expected = 'Bucharest'
        self.assertAlmostEqual(actual, expected, "Display of the highest earning region in Romania.")

    def test_highest_earning_region_percentage(self):
        actual = self.data['highest_earning_region_percentage']
        expected = 'Bucharest'
        self.assertAlmostEqual(actual, expected, "Expected highest earnign region in Romania and its total percentage compared to the country's level.")

    def test_top_in_region(self):
        actual = self.data['top_in_occupation']
        expected = 'IT'
        self.assertAlmostEqual(actual, expected, "Expected top job occupation into the most developed region.")