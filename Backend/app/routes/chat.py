from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    ChatRequest,
    BulkChatRequest
)

from app.services.prompt_service import build_prompt
from app.services.ai_service import get_ai_response

from app.db.database import history_collection

import asyncio

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):

    try:

        final_prompt = await build_prompt(
            request.userInput
        )

        ai_response = await get_ai_response(
            final_prompt
        )

        await history_collection.insert_one({
            "userInput": request.userInput,
            "finalPrompt": final_prompt,
            "response": ai_response
        })

        return {
            "response": ai_response
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



async def process_single_input(user_input: str):

    final_prompt = await build_prompt(user_input)

    ai_response = await get_ai_response(
        final_prompt
    )

    await history_collection.insert_one({
        "userInput": user_input,
        "finalPrompt": final_prompt,
        "response": ai_response
    })

    return ai_response


@router.post("/bulk-chat")
async def bulk_chat(request: BulkChatRequest):

    # Input Validation
    if not request.inputs:
        raise HTTPException(
            status_code=400,
            detail="Inputs list cannot be empty"
        )

    try:

        tasks = [
            process_single_input(user_input)
            for user_input in request.inputs
        ]

        responses = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        final_responses = []

        for response in responses:

            if isinstance(response, Exception):

                final_responses.append({
                    "error": str(response)
                })

            else:

                final_responses.append({
                    "response": response
                })

        return {
            "responses": final_responses
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )