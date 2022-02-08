from  movies import is_movie_higher_5, sublist_of_movies_higher_5, sorted_by_category, avg_imdb_for_all, score_in_single_category
import unittest

class TestPractice2(unittest.TestCase):
    
    
    def test_is_movie_higher_5(self):
        result = is_movie_higher_5({
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        })
        self.assertTrue(result)

    def test_is_movie_higher_5(self):
        result = is_movie_higher_5({
        "name": "Usual Suspects", 
        "imdb": 5.0,
        "category": "Thriller"
        })
        self.assertFalse(result)


    def test_sublist_of_movies_higher_5(self):
        result = sublist_of_movies_higher_5([
        {
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        }])
        self.assertTrue(result)



    def test_sublist_of_movies_higher_5(self):
        result = sublist_of_movies_higher_5([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 2.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 3.0,
        "category": "Adventure"
        }])
        self.assertFalse(result)


    def test_sorted_by_category(self):
        result = sorted_by_category([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 2.3,
        "category": "Adventure"
        },
        {
        "name": "Dark Knight",
        "imdb": 3.0,
        "category": "Adventure"
        }],'Adventure')

        self.assertTrue(result)

    def test_sorted_by_category(self):
        result = sorted_by_category([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 2.3,
        "category": "Adventure"
        },
        {
        "name": "Dark Knight",
        "imdb": 3.0,
        "category": "Adventure"
        }],'Drama')

        self.assertFalse(result)

    def test_avg_imdb_for_all(self):
        result = avg_imdb_for_all([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 5.0,
        "category": "Adventure"
        },
        {
        "name": "Dark Knight",
        "imdb": 3.0,
        "category": "Adventure"
        }])


        self.assertEqual(result, 3.0)

    def test_avg_imdb_for_all(self):
        result = avg_imdb_for_all([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 5.0,
        "category": "Adventure"
        },
        {
        "name": "Dark Knight",
        "imdb": 3.0,
        "category": "Adventure"
        }])


        self.assertEqual(result, 5.0)



    def test_score_in_single_category(self):
        result = score_in_single_category([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 7.0,
        "category": 'Adventure'
        },
        {
        "name": "Dark Knight",
        "imdb": 5.0,
        "category": 'Adventure'
        }], 'Adventure')

        self.assertEqual(result, 6.0)

    

    def test_score_in_single_category(self):
        result = score_in_single_category([
        {
        "name": "Usual Suspects", 
        "imdb": 1.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 7.0,
        "category": 'Adventure'
        },
        {
        "name": "Dark Knight",
        "imdb": 5.0,
        "category": 'Adventure'
        }], 'Adventure')

        self.assertEqual(result, 9.0)

    




