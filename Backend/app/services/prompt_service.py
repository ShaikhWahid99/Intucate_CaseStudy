from app.db.database import prompts_collection

async def build_prompt(user_input: str):

    prompt_doc = await prompts_collection.find_one({
        "_id": "Education_Prompt"
    })

    template = prompt_doc["template"]

    final_prompt = template.replace(
        "{userInput}",
        user_input
    )

    return final_prompt