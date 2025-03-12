from config import conn_pinecorn,conn_gemini


pc = conn_pinecorn()
client = conn_gemini()
index_name = "dense-index"
query = "what is Corrosion"

# Search the dense index

def LLMresponce():
    dense_index = pc.Index(index_name)
    results = dense_index.search(
    namespace="example-namespace",
    query={
        "top_k": 5,
        "inputs": {
            'text': query
        }
    }
    )
    llmtext = ""
    for hit in results['result']['hits']:
        llmtext = llmtext +" "+hit['fields']['chunk_text']

    prompt = f"""you are a joiner teacher in a government school having exprience of 10 year in teaching.currently you are teaching class 8th student.answer the
    question delimitted by double backticks and the context for the quesition is delimitted by triple backticks.do not use your own knowledge and keepit sort
    question :''{query}'' \n
    context : '''{llmtext} '''
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )

    return response.text
print(LLMresponce())

# # Print the results