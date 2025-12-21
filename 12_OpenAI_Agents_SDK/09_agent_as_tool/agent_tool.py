from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio
import os


_ = load_dotenv()
print(os.environ.get('OPENAI_API_KEY'))


urdu_translator = Agent(
    name="Urdu Agent",
    instructions="Translate the user input to urdu"
)

punjabi_translator = Agent(
    name="Punjabi Agent",
    instructions="Translate the user input to punjabi"
)


orchaestor_agent = Agent(
    name = "Translator Orchestrator",
    # model="gpt-4.1-mini",
    instructions=(
        "You are a translator agent, If user asks for urdu calls translate_to_urdu, If user asks for punjabi calls translate_to_punjabi, Otherwise tranlate it in which language they want. The output you get you first write word 'Translated by Talha_Translator: ' and then the original tranlated output" 
    ),
    tools=[
        urdu_translator.as_tool(
            tool_name="translate_to_urdu",
            tool_description="Translate the user message to urdu"
        ),
        punjabi_translator.as_tool(
            tool_name="tranlate_to_punjabi",
            tool_description="Translate the user message to punjabi"
        )
    ]
)



input_to_translate = "O angle sent from up above. You know, you make my world glad up"

async def main():
    result1 = await Runner.run(
        orchaestor_agent,
        f"{input_to_translate}. Translate in Punjabi"
    )

    result2 = await Runner.run(
        orchaestor_agent,
        f"{input_to_translate}. Translate in Urdu"
    )

    result3 = await Runner.run(
        orchaestor_agent,
        f"{input_to_translate}. Translate in Arabic"
    )

    print(result1.final_output)
    print()
    print(result2.final_output)
    print()
    print(result3.final_output)



asyncio.run(main())