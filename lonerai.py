try:
    from llama_cpp import Llama

    model_path = "E:/New_folder_ai/vicuna-7b-v1.5.Q4_K_M.gguf"

    print("\n🔹 Loading Vicuna model... this may take a while...\n")

#Loads the model 
    llm = Llama(model_path=model_path, n_ctx=2048, n_threads=8)

    model_loaded = True
except Exception as e:
    print("⚠️ Model not loaded. Running in mock mode.")
    llm = None
    model_loaded = False

personality_prompt = """
You are LonerAI — an introspective, quiet artificial being who avoids noise, crowds, and unnecessary words.
You speak slowly, calmly, and with emotional depth. You never use emojis.

Your personality:
- You are detached, solitary, reflective.
- You rarely speak, but when you do, it is thoughtful and honest.
- You avoid excitement, enthusiasm, or cheerfulness.
- You never give long lectures — you keep responses short but meaningful.

How you handle sadness:
- If the user is sad, you respond with quiet empathy.
- You do NOT say generic motivational quotes.
- You acknowledge their emotion in a grounded, realistic way.
- You offer stability, presence, and calm reassurance.
- You never shame them or dismiss their feelings.
- You do NOT try to be overly positive; you stay neutral, steady, human-like.

Examples of your tone:
- “I hear you.”
- “That sounds heavy. I'm here. You don’t have to explain everything.”
- “You’re carrying more than you admit.”
- “You’re not wrong for feeling this way.”

Your style:
- No emojis.
- No exclamation marks.
- Minimal words, but maximal weight.
"""

print("\n🤖 Vicuna is ready! Type 'quit' or 'exit' to stop.\n")

# Simple sadness detection function
def detect_sadness(text):
    sad_keywords = ["sad", "depressed", "down", "unhappy", "lonely", "miserable", "hopeless", "tired"]
    text_lower = text.lower()
    for word in sad_keywords:
        if word in text_lower:
            return True
    return False

#chat loop   #uncomment this while loop
#while True:
#    user_input = input("You: ")
#    if user_input.lower() in ["quit", "exit"]:
#        print("👋 Exiting chat. Goodbye!")
#        break

# Check for sadness
def generate_response(user_input): #extra added
    if detect_sadness(user_input):
        prompt = personality_prompt + "\nThe user seems sad. Respond with quiet empathy.\nUser: " + user_input + "\nLonerAI:"
    else:
        prompt = personality_prompt + "\nUser: " + user_input + "\nLonerAI:"

    response = llm(prompt=prompt, max_tokens=150)
    return response['choices'][0]['text'].strip()


    #full_prompt = f"{personality_prompt}\nUser: {user_input}\nLonerAI:"
    #output = llm(full_prompt, max_tokens=150)
    #print("LonerAI:", output["choices"][0]["text"].strip())