import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


def create_prompt(tasks):
    return f"""
You are an academic planner agent.

Given these student tasks, create a realistic 7-day plan.

Tasks:
{json.dumps(tasks, indent=2)}

Return:
1. Priority summary
2. 7-day plan
3. Risks
4. Adjustment advice
"""


def generate_plan(tasks):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful academic planning agent."
            },
            {
                "role": "user",
                "content": create_prompt(tasks)
            }
        ],
    )

    return response.choices[0].message.content


def save_plan(plan):
    with open("weekly_plan.md", "w") as file:
        file.write(plan)


def main():
    tasks = load_tasks()
    plan = generate_plan(tasks)

    print(plan)

    approve = input("\nSave this plan to weekly_plan.md? (yes/no): ")

    if approve.lower() == "yes":
        save_plan(plan)
        print("Plan saved to weekly_plan.md")
    else:
        print("Plan not saved.")


if __name__ == "__main__":
    main()