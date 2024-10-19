import streamlit as st

# Set the title of the app
st.title("🌡️ Temperature Converter")

# Create a sidebar for user input
st.sidebar.header("Convert Temperature")

# Create radio buttons for selecting the conversion type
conversion_type = st.sidebar.radio("Choose conversion:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Function to create a colored progress bar
def colored_progress_bar(percentage, color):
    bar_html = f"""
    <div style="border-radius: 10px; background-color: #ddd; padding: 5px;">
        <div style="width: {percentage}%; background-color: {color}; height: 20px; border-radius: 10px;">
        </div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

# Input fields for temperature
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.sidebar.number_input("Enter temperature in Celsius:", value=0.0)
    fahrenheit = (celsius * 9/5) + 32

    # Simulated thermometer with color-coded progress bar
    st.write(f"🌡️ **{celsius}°C is equal to {fahrenheit:.2f}°F**")

    # Color logic for Celsius
    if celsius <= 0:
        color = 'blue'
    elif 0 < celsius <= 25:
        color = 'green'
    else:
        color = 'red'

    # Scale progress between -30°C to 70°C
    celsius_percentage = min(max((celsius + 30) / 100 * 100, 0), 100)
    colored_progress_bar(celsius_percentage, color)

else:
    fahrenheit = st.sidebar.number_input("Enter temperature in Fahrenheit:", value=32.0)
    celsius = (fahrenheit - 32) * 5/9

    # Simulated thermometer with color-coded progress bar
    st.write(f"🌡️ **{fahrenheit}°F is equal to {celsius:.2f}°C**")

    # Color logic for Fahrenheit
    if fahrenheit <= 32:
        color = 'blue'
    elif 32 < fahrenheit <= 77:
        color = 'green'
    else:
        color = 'red'

    # Scale progress between 0°F to 160°F
    fahrenheit_percentage = min(max((fahrenheit + 20) / 180 * 100, 0), 100)
    colored_progress_bar(fahrenheit_percentage, color)

# Display a summary of the conversion
st.write("---")
st.subheader("📝 Conversion Summary")
if conversion_type == "Celsius to Fahrenheit":
    st.write(f"**Input:** {celsius:.2f}°C")
    st.write(f"**Output:** {fahrenheit:.2f}°F")
else:
    st.write(f"**Input:** {fahrenheit:.2f}°F")
    st.write(f"**Output:** {celsius:.2f}°C")

# Thermometer simulation with labels
st.write("---")
st.subheader("🌡️ Thermometer Simulation")
if conversion_type == "Celsius to Fahrenheit":
    if celsius <= 0:
        st.write("❄️ Cold")
    elif 0 < celsius <= 25:
        st.write("🌡️ Moderate")
    else:
        st.write("🔥 Hot")
else:
    if fahrenheit <= 32:
        st.write("❄️ Cold")
    elif 32 < fahrenheit <= 77:
        st.write("🌡️ Moderate")
    else:
        st.write("🔥 Hot")

# Additional information
st.write("---")
st.markdown("""
### How It Works:
- **Celsius to Fahrenheit**: Multiply the Celsius temperature by 9/5 and then add 32.
- **Fahrenheit to Celsius**: Subtract 32 from the Fahrenheit temperature and then multiply by 5/9.
""")

# Add a footer
st.write("---")
st.write("Made with ❤️ using Streamlit")
