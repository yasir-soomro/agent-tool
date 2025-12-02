
from agents import Agent , Runner  , AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig
from dotenv import load_dotenv , find_dotenv
import os 

load_dotenv(find_dotenv())


gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key= gemini_api_key , 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"


)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
   openai_client= provider
)

config = RunConfig(
    model=model , 
    model_provider= provider,
    tracing_disabled=True
)

agent = Agent(
    name= "AI ChatBot", 
    instructions="you are helpful assistant chatbot "
)


# result = Runner.run_sync(
#    agent , 
#    input= "how can i make AI customer chatbot",
#    run_config=config
# )

# print("here is final output of chatbot..1")
# print(result.final_output)




