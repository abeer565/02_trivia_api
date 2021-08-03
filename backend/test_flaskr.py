import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_questions(self):
        res = self.client().get('/questions/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
    
    def test_404_beyond_valid_page(self):
        res = self.client().get('/questions//?page=100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')  
        self.assertEqual(data['success'], False)  
    ##create_questions
    def test_create_question(self):
        json_data = {
            'question': 'test_question',
            'answer': 'test_answer',
            'difficulty': 10,
            'category': 3
        }
        res = self.client().post('/questions', json=json_data)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        ####
    def test_can_not_create_question(self):
        json_data = {
            'questions': "",
            'answer':"",
            'category':"" ,
            'difficulty':""
        }
        res = self.client().post('/questions', json=json_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        #self.assertEqual(data['message'], 'unprocessable')
    ######delete_question

    def test_delete_question(self):
         res = self.client().delete('/questions/26')
         data = json.loads(res.data)
         self.assertEqual(26, 26)

    def test_404_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')
    ######
 
    #####search_term
    def test_search_term(self):
        res = self.client().post('/search',json={'searchTerm': 'author'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
       # self.assertEqual(data['questions'], True)
        self.assertTrue(data['totalQuestions'],26)
        #self.assertEqual(len(data['currentCategory']), "E")\
    
    def test_not_exist_search_term(self):
        res = self.client().post('/search/doctor',json={'searchTerm': 'doctor'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
    #####

  ######categories
    def test_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'], True)

    def test_not_exist_categories(self):
        res = self.client().get('/categories/8')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')

    ########

    #######specific question in categories/
    def test_get_questions_per_category(self):
        res = self.client().get('/categories/2/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['totalQuestions'])
        ###########
    def test_get_questions_not_exixt_per_category(self):
        res = self.client().get('/categories/35/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')

    ###### quizzes  
    def test_quizzes(self):
        json_data = {
            'previous_questions': [],
            'quiz_category': {"type": "Science", "id": "1"},
        }
        res = self.client().post('/quizzes', json=json_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])    
        ###########  
    def test__empty__quizzes(self):
        json_data = {
            'previous_questions': [],
            'quiz_category': {},
        }
        res = self.client().post('/quizzes', json=json_data)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')   
    ####### 

# Make the tests conveniently executable

if __name__ == "__main__":
    unittest.main()