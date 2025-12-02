


# from agents import Agent , Runner 
# from connection import config
 

# italain_agent = Agent(
#     name= ("Italain Translator"),
#     instructions= ("Translate any English sentence text into italain")
# ) 

# spanish_agent = Agent(
#     name= ("Spanish Translator"),
#     instructions= ("Translate any English sentence text into spanish")
# ) 

# french_agent = Agent(
#     name= ("French Translator"),
#     instructions= ("Translate any English sentence text into french")
# ) 

# translation_router = Agent(
#     name= (" Translation Router"),
#     instructions=""""
#     you are translation assistant. Route the translation request to the correct languae agent, Use the approprite tool to convert English text into either Italian, Spanish , or Freanch based on the request.""",
# tools=[
#     italain_agent.as_tool(
#         tool_name="translate_to_italian",
#         tool_description="Translate the user's message to Italian."
#     ),
#     spanish_agent.as_tool(
#         tool_name="translate_to_spanish",
#         tool_description="Translate the user's message to Spanish."
#     ),
#     french_agent.as_tool(
#         tool_name="translate_to_french",
#         tool_description="Translate the user's message to French."
#     ),
# ]
# ) 
# result = Runner.run_sync(
#     italain_agent,
#     input="Translate 'I Love openai agents sdk' into Italain",
#     run_config=config
# )
# print(result.final_output)




from agents import Agent, Runner
from connection import config

italian_agent = Agent(
    name="Italian Translator",
    instructions="Translate any English sentence into Italian."
)

spanish_agent = Agent(
    name="Spanish Translator",
    instructions="Translate any English sentence into Spanish."
)

french_agent = Agent(
    name="French Translator",
    instructions="Translate any English sentence into French."
)

translation_router = Agent(
    name="Translation Router",
    instructions=(
        "You are a translation assistant. Route the translation request to the correct language agent. "
        "Use the appropriate tool to convert English text into either Italian, Spanish, or French based on the request."
    ),
    tools=[
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian."
        ),
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish."
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French."
        ),
    ]
)

# If you want the Router to pick the correct language tool automatically:
result = Runner.run_sync(
    italian_agent,
    input="Translate 'I Love OpenAI Agents SDK' into Italian",
    run_config=config
)
print(result.final_output)
