import streamlit as st

# Streamlit app
def largest_among_three(num1, num2, num3):
    # Find the largest number
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    return largest

def main():
   
    st.title("Largest Among Three Numbers")
    st.write("Enter three numbers, and the app will find the largest among them.")


    num1 = st.number_input("Enter the first number:", key="1")
    num2 = st.number_input("Enter the second number:", key="2")
    num3 = st.number_input("Enter the third number:", key="3")

    
    result = largest_among_three(num1, num2, num3)

    st.write(f"The largest number is: {result}")

# Run the app
if __name__ == "__main__":
    main()
