import math
import streamlit as st

def regular_converter(meters: float, kg: float):
    feet = meters * 3.28084  # Convert meters to feet
    pounds = kg * 2.20462  # Convert kg to pounds
    return feet, pounds

def length_converter(meters: float):
    planck_length = meters / 1.616e-35  # Convert meters to Planck Lengths
    light_years = meters / 9.461e15  # Convert meters to Light-Years
    return planck_length, light_years

def mass_converter(kg: float):
    electron_mass = kg / 9.109e-31  # Convert kg to Electron Masses
    solar_mass = kg / 1.989e30  # Convert kg to Solar Masses
    return electron_mass, solar_mass

def schwarzschild_radius(mass_kg: float):
    G = 6.674e-11  # Gravitational constant
    c = 3.0e8  # Speed of light
    radius = (2 * G * mass_kg) / (c ** 2)  # Schwarzschild radius formula
    return radius

def time_dilation(velocity: float):
    c = 3.0e8  # Speed of light in m/s
    if velocity >= c:
        return "Impossible! Speed cannot be equal to or exceed the speed of light."
    dilation_factor = 1 / math.sqrt(1 - (velocity ** 2 / c ** 2))
    return dilation_factor

def main():
    st.title("A regular unit converter converts meters to feet, kilograms to pounds, etc.")
    st.header("Quantum & Cosmic Unit Converter 🌌")
    
    meters = st.number_input("Enter length in meters:", min_value=0.0, format="%.2f")
    kg = st.number_input("Enter mass in kg:", min_value=0.0, format="%.2f")
    velocity = st.number_input("Enter speed in m/s for time dilation:", min_value=0.0, format="%.2f")
    
    if meters:
        feet, _ = regular_converter(meters, 0)
        planck, ly = length_converter(meters)
        st.write(f"{meters} meters = {feet:.3f} feet")
        st.write(f"{meters} meters = {planck:.3e} Planck Lengths")
        st.write(f"{meters} meters = {ly:.3e} Light-Years")
    
    if kg:
        _, pounds = regular_converter(0, kg)
        e_mass, s_mass = mass_converter(kg)
        schwarz_radius = schwarzschild_radius(kg)
        st.write(f"{kg} kg = {pounds:.3f} pounds")
        st.write(f"{kg} kg = {e_mass:.3e} Electron Masses")
        st.write(f"{kg} kg = {s_mass:.3e} Solar Masses")
        st.write(f"A black hole with {kg} kg would have a Schwarzschild Radius of {schwarz_radius:.3e} meters")
    
    if velocity:
        dilation = time_dilation(velocity)
        st.write(f"Time dilation factor: {dilation}")

if __name__ == "__main__":
    main()
