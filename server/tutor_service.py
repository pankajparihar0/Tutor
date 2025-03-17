from config import conn_pinecorn,conn_gemini
import json 
import re
class TutorService():
    index_name = "dense-index"

    # function for sementic Search in the vector DB
    def __semantic_search(self, question):
        pc = conn_pinecorn()
        dense_index = pc.Index(self.index_name)
        results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 5,
            "inputs": {
                'text': question
            }
        }
    )
        return results
    
    # function to create prompt for the llm model
    def __get_prompt(self, question, context):
        prompt = f"""you are a joiner teacher in a government school having exprience of 10 year in teaching.currently you are teaching class 8th \n
        student.answer the question delimitted by double backticks and the context for the quesition is delimitted by triple backticks.do not use \n 
        your own knowledge use the context and explain it and keep it sort.insted of mentioning a activity or figer in you answer or question give \n
        a brief about it as the student dont have access to context givin to you.
        question :''{question}'' \n
        context : '''{context} '''
        """
        return prompt
    
    # function to generate prompt for the Quiz
    def __get_quiz_promt(self,topic,context,number):
        print("\n")
        formet = [ {
           "id" :'id of the quesion',
           'Question':"question",
            'options':['four options for the Question'],
            'correct_answer' :'Correct answer for the qusetion'
        }]
        prompt = f"""you are a joiner teacher in a government school having exprience of 10 year in teaching.currently you are teaching class 8th \n
        student.your are given  a task to make  a {number} question quiz for the students.topic for the Quiz is delimitted by double backticks and the context for the quiz \n
        is delimitted by triple backticks.do not use your own knowledge use the context and create a quiz according to the formet givin below.\n
        insted of mentioning a activity or figer in you answer or question give a brief about it as the student dont have access to context given to you.\n
        your respons should be strictly in and only json forment . 
        number of question i want in the Quiz :{number} 
        formet : {formet}
        question :''{topic}'' \n
        context : '''{context} '''
        """

        return prompt

    # function for creating context from chunks
    def __get_context(self, chunks):
        llmtext = ""
        for hit in chunks['result']['hits']:
            llmtext = llmtext +" "+hit['fields']['page_content']
        return llmtext
    
    # function that return the responce of llm model
    def __execute_prompt(self, prompt):
        client = conn_gemini()
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
        )
        return response.text
    
    def get_question_answer(self, question):
        semantic_result = self.__semantic_search(question)
        context = self.__get_context(semantic_result)
        prompt = self.__get_prompt(question,context)
        response = self.__execute_prompt(prompt)
        return response
    
    def get_quiz(self,topic,number):
        sementic_result = self.__semantic_search(topic)
        context = self.__get_context(sementic_result)
        prompt = self.__get_quiz_promt(topic,context,number)
        response = self.__execute_prompt(prompt)
        print(number)
        return response