import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from collections import defaultdict
from collections import OrderedDict
from models import setup_db, Question, Category
import sys

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  try:
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    print(len(questions))
    current_questions = questions[start:end]
    return current_questions
  except:
      abort(404)  
'''
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  questions = [question.format() for question in selection]
  print("in pagintate the current_questions",questions)
  current_questions = questions[start:end]

  return current_questions
''' 

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  '''
  # TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs - done
  '''
  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  ####### done   
  '''
 # @TODO: Use the after_request decorator to set Access-Control-Allow - done
  '''

  '''
  ########## done 
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_Category():
    selection = Category.query.order_by(Category.id).all()
    current_Category = paginate_questions(request, selection)   
    a_key ="id"
    b_key ="type"
    index= len(current_Category)
    values_of_id= [a_dict[a_key] for a_dict in current_Category]
    values_of_type = [b_dict[b_key] for b_dict in current_Category]
    zip_iterator = zip(values_of_id, values_of_type)
    a_dictionary = dict(zip_iterator)
    if len(current_Category) == 0:
         abort(404)
    return jsonify({
      'categories': a_dictionary,
      })
  ####### done 
  '''
  ###
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  
  @app.route('/questions/',methods=['GET'])
  def retrieve_Question():
    try: 
        selection = Question.query.order_by(Question.id).all()
        #print("selection =",selection)
        current_question = paginate_questions(request, selection)
        ###Category
        #selection = Category.query.order_by(Category.id).all()
        total_questions=Question.query.count()
        categories = Category.query.all()
        formatted_categories = {category.id:category.type for category in categories}
        #print(formatted_categories)
        #print(categories)
        d = {'questions': current_question,'total_questions': total_questions,'categories':formatted_categories,'currentCategory':None}
        if len(current_question) == 0:
          abort(404)
    except:
       print("the excppty statment",sys.exc_info())  
    return jsonify(d)
####### done 
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:id>', methods=['DELETE'])
  def delete_questions(id):
    try:
      questions = Question.query.filter(Question.id == id).one_or_none()

      if questions is None:
        abort(404)
     
      questions.delete()
      selection = Question.query.order_by(Question.id).all()
      #current_question = paginate_questions(request, selection)
      return jsonify(id)
    except:
      abort(422)
  
  
  #####done 
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    data = request.json
    if ((data.get('question') == '') or (data.get('answer') == '') or
                (data.get('category') == '') or
                (data.get('difficulty') == '')):
            abort(422)
    try:  
      body = request.get_json()
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty_score = body.get('difficulty', None)
      new_question = body.get('question', None)
      search = body.get('search', None)

      if search:
        selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
        current_question = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'questions': current_question,
          'total_questions': len(selection.all())
        })

      else:
        question = Question(answer=new_answer, category=new_category,difficulty=new_difficulty_score ,question=new_question)
        question.insert()

        selection = Question.query.order_by(Question.id).all()
        current_question = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'created': question.id,
          'question': current_question,
          'total_questions': len(Question.query.all())
        })

    except:
      abort(422)
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/search', methods=['POST'])
  def search():
      body = request.get_json()
      search = body.get('searchTerm', None)
      selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
      current_question = paginate_questions(request, selection)
      #print(current_question)
    ###Category
      totalQuestions=len(Question.query.all())
      current_Category = paginate_questions(request, selection)  
      ###Category
      ## object 
      d = {'questions': current_question,'totalQuestions': totalQuestions,'currentCategory':None}
      ############
      return jsonify(d)
#####done 
  '''
  #### done 
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:id>/questions', methods=['GET'])
  def retrieve_specific_category_questions(id):
    try:  
      selection = Question.query.filter(Question.category==id)
      current_typee = Category.query.filter_by(id=id).first()
      current_category=current_typee.type
      total_questions=len(Question.query.all())
      questions = paginate_questions(request, selection)
      d = {'questions': questions,'totalQuestions': total_questions,'currentCategory':current_category}

      if len(questions) == 0:
        abort(404)

      if selection is None:
              abort(404)
      else:
                return jsonify(d)
    except:
       abort(404)            
  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.route('/quizzes', methods=['POST'])
  def play_quizz():
    length = len(Question.query.all())

    body = request.get_json()
    previous_questions = body.get('previous_questions', None)
    quiz_category = body.get('quiz_category', None)
    #print(quiz_category)
    try:
        if quiz_category['id']==0:
          selection = Question.query.filter(Question.id.notin_(previous_questions)).all()
        else:
          selection = Question.query.filter(Question.category==quiz_category['id'],Question.id.notin_(previous_questions)).all()
        current_questions = selection[random.randrange(0, len(selection))].format()
        
    except:
       #print(sys.exc_info())
       abort(422)
    return jsonify({
          'previousQuestions': previous_questions,
          'question': current_questions,
        })           
  
#####done 
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
        "success": False, 
        "error": 400,
        "message": "bad request"
        }), 400

  @app.errorhandler(405)
  def not_found(error):
      return jsonify({
        "success": False, 
        "error": 405,
        "message": "method not allowed"
        }), 405
  return app

    