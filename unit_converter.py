import streamlit as st
from forex_python.converter import CurrencyRates

st.title("🌎 Google Unit Converter")

# Conversion categories
categories = ["Length", "Weight", "Temperature", "Currency"]

selected_category = st.selectbox("Select Conversion Type:", categories)

# Length Conversion
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

# Weight Conversion
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

# Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

# Currency Conversion
def convert_currency(value, from_currency, to_currency):
    c = CurrencyRates()
    return c.convert(from_currency, to_currency, value)

# Input from user
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

if selected_category == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif selected_category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif selected_category == "Temperature":
    units = ["Celsius", "Fahrenheit"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

elif selected_category == "Currency":
    currencies = ["USD", "EUR", "GBP", "INR", "PKR"]
    from_currency = st.selectbox("From:", currencies)
    to_currency = st.selectbox("To:", currencies)
    if st.button("Convert"):
        try:
            result = convert_currency(value, from_currency, to_currency)
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")
        except:
            st.error("Error fetching currency data. Try again later!")
