import streamlit as st

# Set the title of the app
st.title("🌡️ Temperature Converter")

# Create a sidebar for user input
st.sidebar.header("Convert Temperature")

# Create radio buttons for selecting the conversion type
conversion_type = st.sidebar.radio("Choose conversion:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input fields for temperature
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.sidebar.number_input("Enter temperature in Celsius:", value=0.0)
    fahrenheit = (celsius * 9/5) + 32

    # Simulated thermometer with progress bar
    st.write(f"🌡️ **{celsius}°C is equal to {fahrenheit:.2f}°F**")
    celsius_percentage = min(max((celsius + 30) / 100, 0), 1)  # Scale the temperature between -30°C to 70°C
    st.progress(celsius_percentage)

else:
    fahrenheit = st.sidebar.number_input("Enter temperature in Fahrenheit:", value=32.0)
    celsius = (fahrenheit - 32) * 5/9

    # Simulated thermometer with progress bar
    st.write(f"🌡️ **{fahrenheit}°F is equal to {celsius:.2f}°C**")
    fahrenheit_percentage = min(max((fahrenheit + 20) / 180, 0), 1)  # Scale the temperature between 0°F to 160°F
    st.progress(fahrenheit_percentage)

# Display a summary of the conversion
st.write("---")
st.subheader("📝 Conversion Summary")
if conversion_type == "Celsius to Fahrenheit":
    st.write(f"**Input:** {celsius:.2f}°C")
    st.write(f"**Output:** {fahrenheit:.2f}°F")
else:
    st.write(f"**Input:** {fahrenheit:.2f}°F")
    st.write(f"**Output:** {celsius:.2f}°C")

# Thermometer emoji to simulate temperature
st.write("---")
st.subheader("🌡️ Thermometer Simulation")
if conversion_type == "Celsius to Fahrenheit":
    temp_range = ["❄️", "🧊", "🌡️", "🔥", "☀️"]  # Cool to hot emojis
    temp_index = min(max(int((celsius + 30) / 25), 0), 4)
    st.write(temp_range[temp_index], f"{celsius:.2f}°C")
else:
    temp_index = min(max(int((fahrenheit + 20) / 40), 0), 4)
    st.write(temp_range[temp_index], f"{fahrenheit:.2f}°F")

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
