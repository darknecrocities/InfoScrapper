from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import concurrent.futures

# Template for parsing
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the model
model = OllamaLLM(model="llama3.1")

# Function to parse content using Ollama
def parse_with_ollama(dom_chunks, parse_description):
    # Create the prompt template using the provided template
    prompt = ChatPromptTemplate.from_template(template)
    # Chain the model with the prompt
    chain = prompt | model

    parsed_results = []

    # Using ThreadPoolExecutor to parallelize the parsing process
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Mapping each chunk to a future task
        future_to_chunk = {
            executor.submit(chain.invoke, {"dom_content": chunk, "parse_description": parse_description}): i
            for i, chunk in enumerate(dom_chunks, start=1)
        }

        # As each task is completed, retrieve and store the result
        for future in concurrent.futures.as_completed(future_to_chunk):
            i = future_to_chunk[future]
            try:
                response = future.result()
                # Append the result to the parsed results
                if response.strip():  # Check if the response is not empty
                    parsed_results.append(response)
                else:
                    parsed_results.append(f"Chunk {i}: No match found.")
                print(f"Parsed batch: {i} of {len(dom_chunks)}")
            except Exception as e:
                print(f"Error parsing chunk {i}: {e}")
                parsed_results.append(f"Chunk {i}: Error occurred.")

    # Return the combined parsed results as a string
    return "\n".join(parsed_results)

# Example usage:
if __name__ == "__main__":
    # Example list of DOM chunks (content to parse)
    dom_chunks = [
        "This is the first chunk with some information about apples.",
        "This is the second chunk with information about oranges and bananas.",
        "This is the third chunk with no relevant data."
    ]

    # Description of the information you want to extract
    parse_description = "information about apples"

    # Call the parse function and print the results
    results = parse_with_ollama(dom_chunks, parse_description)
    print("\nParsed Results:\n")
    print(results)
