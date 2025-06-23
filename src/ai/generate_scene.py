import subprocess

def generate_scene_prompt(character, location, mission_summary, previous_context):
    """
    Fill the scene prompt template with the character and mission details.
    """
    with open("src/ai/scene_prompt_template.txt", "r", encoding="utf-8") as f:
        template = f.read()

    filled_prompt = template.format(
        character_name=character.name,
        rank=character.rank,
        clan=character.clan,
        element=character.element,
        location=location,
        mission_summary=mission_summary,
        previous_context=previous_context
    )

    return filled_prompt

def run_ollama_mistral(prompt):
    """
    Send the prompt to the local Ollama LLM using Mistral model and return the response.
    """
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"  # Windows'ta Unicode desteği için gerekli
    )

    output, error = process.communicate(input=prompt)

    if error:
        print("⚠️ Ollama returned an error:\n", error)
    return output

# Example usage for testing
if __name__ == "__main__":
    # Dummy test character
    character = {
        "name": "Uchiha Ren",
        "rank": "Genin",
        "clan": "Uchiha",
        "element": "Fire"
    }

    location = "Hidden Leaf Forest"
    mission_summary = "Locate and retrieve a missing medic-nin who disappeared during a supply run."
    previous_context = "Ren recently survived a bandit ambush near the village outskirts."

    prompt = generate_scene_prompt(character, location, mission_summary, previous_context)
    scene = run_ollama_mistral(prompt)

    print("\n🔆 GENERATED SCENE 🔆\n")
    print(scene)
