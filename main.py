import streamlit as st

def main():
    st.title("Comments Box")
    # Create a text input for the commenter's name
    name = st.text_input("Name:")

    # Create a text input for the comment
    comment = st.text_area("Leave a comment:")

    # Create a button to submit the comment
    if st.button("Submit"):
        # Save the comment to a file or database
        with open("comments.txt", "a") as f:
            f.write(f"{name}: {comment}\n")
        st.success("Comment submitted!")

    # Display existing comments
    st.write("Existing comments:")
    with open("comments.txt", "r") as f:
        comments = f.readlines()
    for comment in comments:
        st.write(comment)

if __name__ == "__main__":
    main()