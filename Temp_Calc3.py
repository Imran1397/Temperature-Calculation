import streamlit as st
import plotly.graph_objects as go

# Set the title of the app
st.title("🌡️ Temperature Converter with Dynamic Background and Graph")

# Create a sidebar for user input
st.sidebar.header("Convert Temperature")

# Create radio buttons for selecting the conversion type
conversion_type = st.sidebar.radio("Choose conversion:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Function to determine color and background based on temperature
def get_temperature_data(temp_celsius):
    if temp_celsius <= 0:
        return 'blue', "https://www.publicdomainpictures.net/pictures/320000/velka/winter-snow-background.jpg"  # Example snowy image
    elif 0 < temp_celsius <= 25:
        return 'green', "https://www.publicdomainpictures.net/pictures/300000/velka/pleasant-meadow.jpg"  # Example pleasant image
    else:
        return 'red', "https://www.publicdomainpictures.net/pictures/300000/velka/sunny-desert.jpg"  # Example hot image

# Apply custom CSS for background and progress bar color
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True
    )

# Input fields for temperature and conversions
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.sidebar.number_input("Enter temperature in Celsius:", value=0.0)
    fahrenheit = (celsius * 9/5) + 32
    st.write(f"🌡️ **{celsius}°C is equal to {fahrenheit:.2f}°F**")
    color, background = get_temperature_data(celsius)
else:
    fahrenheit = st.sidebar.number_input("Enter temperature in Fahrenheit:", value=32.0)
    celsius = (fahrenheit - 32) * 5/9
    st.write(f"🌡️ **{fahrenheit}°F is equal to {celsius:.2f}°C**")
    color, background = get_temperature_data(celsius)

# Set background image based on temperature
set_background(background)

# Create a dynamic graph that changes color based on temperature
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=celsius,
    gauge={
        'axis': {'range': [-30, 50]},
        'bar': {'color': 'black'},  # Set gauge line color to black
        'steps': [
            {'range': [-30, 0], 'color': "lightblue"},
            {'range': [0, 25], 'color': "lightgreen"},
            {'range': [25, 50], 'color': "lightcoral"}
        ],
    },
    title={'text': "Celsius Temperature"}
))

# Display the graph
st.plotly_chart(fig)

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
        st.write("🌡️ Pleasant")
    else:
        st.write("🔥 Hot")
else:
    if fahrenheit <= 32:
        st.write("❄️ Cold")
    elif 32 < fahrenheit <= 77:
        st.write("🌡️ Pleasant")
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
