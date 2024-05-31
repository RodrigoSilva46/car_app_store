# streamlit_app.py

import streamlit as st

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.year} {self.brand} {self.model}'

class CarStore:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_cars(self):
        if not self.cars:
            return "No cars in the store."
        return '\n'.join([str(car) for car in self.cars])

    def find_cars_by_model(self, model):
        found_cars = [car for car in self.cars if car.model.lower() == model.lower()]
        if not found_cars:
            return f'No cars found with model {model}.'
        return '\n'.join([str(car) for car in found_cars])

    def remove_car(self, model):
        car_to_remove = None
        for car in self.cars:
            if car.model.lower() == model.lower():
                car_to_remove = car
                break
        if car_to_remove:
            self.cars.remove(car_to_remove)
            return f'{car_to_remove} has been removed.'
        return f'No car found with model {model}.'

def main():
    store = CarStore()
    st.title("Car Store App")

    menu = ["Add a new car", "List all cars", "Find cars by model", "Remove a car"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add a new car":
        st.subheader("Add a new car")
        brand = st.text_input("Enter car brand")
        model = st.text_input("Enter car model")
        year = st.text_input("Enter car year")

        if st.button("Add Car"):
            if not brand or not model or not year:
                st.error("All fields are required.")
            elif not year.isdigit():
                st.error("Year must be a number.")
            else:
                car = Car(brand, model, year)
                store.add_car(car)
                st.success(f'{car} has been added.')

    elif choice == "List all cars":
        st.subheader("All cars in the store")
        cars = store.list_cars()
        st.text(cars)

    elif choice == "Find cars by model":
        st.subheader("Find cars by model")
        model = st.text_input("Enter car model to search")
        if st.button("Search"):
            cars = store.find_cars_by_model(model)
            st.text(cars)

    elif choice == "Remove a car":
        st.subheader("Remove a car")
        model = st.text_input("Enter car model to remove")
        if st.button("Remove"):
            result = store.remove_car(model)
            st.success(result)

if __name__ == "__main__":
    main()
