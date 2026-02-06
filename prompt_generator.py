from langchain_core.prompts import PromptTemplate 

#Templates
template= PromptTemplate(
    template="""
Please summarize the research paper titled {paper_input} with the Following Specifications:
Explaination Style: {style_input}
Explaination Length: {length_input}
1. Mathematical details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where
    applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
if certain informarion is not available in the paper, respond with: "Insufficient information available" instead of guessing.   
Ensure the summary is clear, accurate, and aligned with the provided. style and lengt.
""",
input_variables = ["paper_input", "style_input", "length_input"],
validate_template=True
) 

template.save("template.json")