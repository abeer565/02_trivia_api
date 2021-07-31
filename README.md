# Full Stack API Final Project


## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter) and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.
>Once you're ready, you can submit your project on the last page.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend
The [./backend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads? 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. *./frontend/src/components/QuestionView.js*
2. *./frontend/src/components/FormView.js*
3. *./frontend/src/components/QuizView.js*


By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API. 



>View the [README within ./frontend for more details.](./frontend/README.md)



Endpoints
GET //questions
      return list of the categories whicc contain the id and the type of it , currentCategor which is null and the questions. 
      Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1
sample
curl http://127.0.0.1:5000/questions
            {
              "categories": {
                "1": "Science", 
                "2": "Art", 
                "3": "Geography", 
                "4": "History", 
                "5": "Entertainment", 
                "6": "Sports"
              }, 
              "currentCategory": null, 
              "questions": [
                {
                  "answer": "Tom Cruise", 
                  "category": 5, 
                  "difficulty": 4, 
                  "id": 4, 
                  "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                  "answer": "Maya Angelou", 
                  "category": 4, 
                  "difficulty": 2, 
                  "id": 5, 
                  "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }, 
                {
                  "answer": "Edward Scissorhands", 
                  "category": 5, 
                  "difficulty": 3, 
                  "id": 6, 
                  "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }, 
                {
                  "answer": "Muhammad Ali", 
                  "category": 4, 
                  "difficulty": 1, 
                  "id": 9, 
                  "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                  "answer": "Brazil", 
                  "category": 6, 
                  "difficulty": 3, 
                  "id": 10, 
                  "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                  "answer": "Uruguay", 
                  "category": 6, 
                  "difficulty": 4, 
                  "id": 11, 
                  "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                  "answer": "George Washington Carver", 
                  "category": 4, 
                  "difficulty": 2, 
                  "id": 12, 
                  "question": "Who invented Peanut Butter?"
                }, 
                {
                  "answer": "The Palace of Versailles", 
                  "category": 3, 
                  "difficulty": 3, 
                  "id": 14, 
                  "question": "In which royal palace would you find the Hall of Mirrors?"
                }, 
                {
                  "answer": "Agra", 
                  "category": 3, 
                  "difficulty": 2, 
                  "id": 15, 
                  "question": "The Taj Mahal is located in which Indian city?"
                }, 
                {
                  "answer": "Escher", 
                  "category": 2, 
                  "difficulty": 1, 
                  "id": 16, 
                  "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
                }
              ], 
              "total_questions": 26

POST /question
Creates a new questions using the submitted the answer,  category , difficulty_score and the question. Returns the id of the created question, success value, total questions, to update the frontend.

curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"new_answer":"Riyadh", "new_category":"1", "new_difficulty_score":"2","new_question":"What is the captal city of Saudia Arabia"}'
 
 
     {
      "created": 35, 
      "question": [
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }, 
        {
          "answer": "Agra", 
          "category": 3, 
          "difficulty": 2, 
          "id": 15, 
          "question": "The Taj Mahal is located in which Indian city?"
        }, 
        {
          "answer": "Escher", 
          "category": 2, 
          "difficulty": 1, 
          "id": 16, 
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        }
      ], 
      "success": true, 
      "total_questions": 28
    }

DELETE /questions/{question_id}
General:

Deletes the question of the given ID if it exists. Returns the id of the deleted question to update the frontend.

curl -X DELETE http://127.0.0.1:5000/questions/33

    33


POST/search
General:
this seaech will saerch based on search term that has been entered by the user which will requsted like this for example {searchTerm: "author"}
return currentCategory , questions , totalQuestions
http://localhost:3000/search
the reqeust in the forntend that has been sent from the frontend will be like that 
{searchTerm: "Butter"}

the retrun will be like that for this example 

      {currentCategory: null,…}
      currentCategory: null
      questions: [{answer: "George Washington Carver", category: 4, difficulty: 2, id: 12,…}]
      0: {answer: "George Washington Carver", category: 4, difficulty: 2, id: 12,…}
      answer: "George Washington Carver"
      category: 4
      difficulty: 2
      id: 12
      question: "Who invented Peanut Butter?"
      totalQuestions: 27

GET/categories/<int:id>/questions

General:
retrun all the questions in the id category 
the retrun will be like this  tquestions , totalQuestions ,currentCategory

Sample:curl http://127.0.0.1:5000/categories/3/questions

    {
      "currentCategory": "Geography", 
      "questions": [
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }, 
        {
          "answer": "Agra", 
          "category": 3, 
          "difficulty": 2, 
          "id": 15, 
          "question": "The Taj Mahal is located in which Indian city?"
        }, 
        {
          "answer": "Riyadh", 
          "category": 3, 
          "difficulty": null, 
          "id": 24, 
          "question": "what is the capital city of Saudi Arabia "
        }, 
        {
          "answer": "kuwait", 
          "category": 3, 
          "difficulty": 2, 
          "id": 25, 
          "question": "what is the capital city of kuwait "
        }, 
        {
          "answer": "washiton", 
          "category": 3, 
          "difficulty": 3, 
          "id": 32, 
          "question": "what is the captial city of usa"
        }
      ], 
      "totalQuestions": 27
    }

POST/quizzes'
General:
in this page the user will play based on specific category he chose
the requtse will be like the sample below and the retrun previousQuestions and question
Sample:{previous_questions: [], quiz_category: {type: "Science", id: "1"}}

    {previousQuestions: [],…}
    previousQuestions: []
    question: {answer: "london", category: 1, difficulty: 3, id: 31, question: "what is the capital city of UK"}
    answer: "london"
    category: 1
    difficulty: 3
    id: 31
    question: "what is the capital city of UK"








