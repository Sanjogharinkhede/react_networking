from dotenv import load_dotenv
import os
from google import genai
from fastapi import APIRouter,Body,Path,Query,HTTPException
from starlette import status

load_dotenv()

api_key=os.getenv("GEMINI_KEY")
# print(api_key)



router= APIRouter(prefix="/gemini",tags=["Gemini"])

@router.get('/')
async def NMSData(topicText:str=Query(default="Netconf"),category:str="NMS"):
    prompt = f"""
Generate a single JSON object for a networking lab topic.
The topic is "{topicText}", under category "{category}".
Follow strict field structure: "full_form", "description", "features", "benefits", "disadvantages", "commands".
Return only the JSON, without extra nesting.

Rules:
- full_form: A string showing full name (even if topic is not abbreviated).
- description: 2–3 sentences with <br> for line breaks.
- features: Single string, items separated by <br>.
- benefits: Array with 2–3 points.
- disadvantages: Array with 2–3 points.
- commands: Array with 2–3 commands.

Example for abbreviated topic (NETCONF):
{{
    "full_form": "NETCONF (Network Configuration Protocol)",
    "description": "NETCONF is a network management protocol.<br>It enables device configuration via XML.<br>Enhances automation.",
    "features": "Device configuration<br>Transaction support<br>YANG modeling",
    "benefits": ["Automation", "Standardization", "Vendor-neutral"],
    "disadvantages": ["Complex to implement", "Overhead in small networks"],
    "commands": ["get-config", "edit-config", "commit"]
}}

Example for non-abbreviated topic (Static Route):
{{
    "full_form": "Static Route (Manually Configured Route)",
    "description": "A static route is manually added into the router.<br>It does not change dynamically.<br>Ensures predictable paths.",
    "features": "Manual setup<br>Fixed paths<br>No automatic updates",
    "benefits": ["Predictability", "Simple troubleshooting"],
    "disadvantages": ["No failover", "Manual maintenance"],
    "commands": ["ip route add", "show ip route"]
}}
"""

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response
