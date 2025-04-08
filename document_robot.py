# Import the Streamlit library, which gives us tools to create web apps
# We'll refer to it as "st" to make it shorter to type
import streamlit as st

# Create a title for our web app that will appear at the top of the page
# The 🤖 is an emoji that will show up next to our title
st.title("My Document Chatbot 🤖")

# Display a welcome message to the user
# st.write() is how we put text on the screen
st.write("Hello! I can help you find things in your documents!")

# Create a file upload button that only accepts .txt files
# This assigns the uploaded file to a variable called "file"
file = st.file_uploader("Upload a story or homework", type="txt")

# This is a conditional statement - it checks if a file was uploaded
# The code inside this block will only run if there is a file
if file:
    # Read the contents of the file and convert it from bytes to a string
    # decode("utf-8") converts the raw file data into readable text
    text = file.read().decode("utf-8")
    
    # Show a preview of the document to the user
    # We're displaying a message first
    st.write("I read your document! Here's a bit of it:")
    # Then showing the first 100 characters of the text, followed by "..."
    # The [:100] means "take only the first 100 characters"
    st.write(text[:100] + "...")
    
    # Create a text input box where the user can type their question
    # The text they enter will be stored in the variable "question"
    question = st.text_input("What do you want to know about it?")
    
    # Another conditional - this code only runs if the user typed a question
    if question:
        # Create an empty list to store important words from the question
        important_words = []
        # Split the question into individual words and process each one
        for word in question.split():
            # Only keep words that are longer than 3 characters
            # This helps filter out small words like "the", "and", "is"
            if len(word) > 3:
                # Convert the word to lowercase and add it to our list
                important_words.append(word.lower())
        
        # Create an empty list to store parts of the document that match the question
        found_parts = []
        # Split the document into sentences (using periods as dividers)
        # Then check each sentence for matches
        for sentence in text.split("."):
            # Look for each important word in the current sentence
            for word in important_words:
                # If we find a match, add this sentence to our results
                # .lower() converts the sentence to lowercase so we can match regardless of capitalization
                if word in sentence.lower():
                    found_parts.append(sentence)
                    # Break out of the inner loop once we find a match
                    # This prevents adding the same sentence multiple times
                    break
        
        # Display the matching parts to the user
        if found_parts:
            # Show a message indicating we found matches
            st.write("I found these parts that might help:")
            # Loop through the first 3 matches (or fewer if we found less than 3)
            # [:3] means "take only the first 3 items from the list"
            for part in found_parts[:3]:
                # Display each matching sentence with an arrow in front of it
                st.write("→ " + part)
        else:
            # If we didn't find any matches, show a message suggesting they try again
            st.write("Hmm, I couldn't find anything about that. Try asking differently!")

# This else belongs to the first if statement
# It runs if no file was uploaded
else:
    # Show instructions to the user about uploading a file
    st.write("Please upload a text file to start!")
    st.write("You can ask me questions about your file after uploading.")

    