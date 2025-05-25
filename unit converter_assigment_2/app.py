import streamlit as st

st.title("Unit Converter App")
import streamlit as st

# st.title("Unit Converter")

# Select category and units
category = st.selectbox("Select category", ["distance", "weight"])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Conversion function
def convert(category, value, unit):
    if category == "distance":
        if unit == "kilometers to miles":
            return value * 0.6214
        elif unit == "miles to kilometers":
            return value / 0.6214
    elif category == "weight":
        if unit == "kilograms to pounds":
            return value * 2.2046
        elif unit == "pounds to kilograms":
            return value / 2.2046
    elif category == "time":
        if unit =="second to minutes":
            return value *60
        elif unit =="minutes to hour":
            return value /60
        elif unit =="hour to minutes":
            return value *60
        elif unit =="hour to days":
            return value /24
        elif unit =="days to hours":
            return value *24

if category == "length":
 unit = st.selectbox("select conversation",["kilometers to miles","miles to kilometers"])

elif category == "weight":
    unit = st.selectbox("Select conversion", ["kilograms to pounds", "pounds to kilograms"])
     
elif category == "time":
 unit = st.selectbox("select conversation",["seconds to minutes","minutes to seconds"])
       
value = st.text_input("enter the value to convert")
if st.button("convert"):
    

 category = st.selectbox("Choose category", ["Length", "Temperature"])
unit = st.selectbox("Choose conversion", ["meters_to_feet", "feet_to_meters", "celsius_to_fahrenheit", "fahrenheit_to_celsius"])
value = st.text_input("Enter the value to convert")


result = convert (category, value, unit)
st.success(f"the result is {result}")


# # Output
# if value:
#     result = convert(category, value, unit)
#     st.write(f"Result: {result}")

#     return "Unsupported conversion"
     