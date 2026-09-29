import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from states import StatesRegistry


def print_states(states):# TODO Either adapt this or kill it
    """not fully functional yet..."""
    state_codes = pd.read_csv("state_codes.txt", header=None)
    state_codes.columns = ['code', 'state']

    for n, state in enumerate(list(states)):
        code = state_codes.loc[
            state_codes['state'] == state, 'code'
            ].iloc[0]
        print(f"{n+1:<3}{state} ({code})")


def select_state(registry):# TODO if returning Q, quit
    state = None
    while not state:
        state_code = input("Enter 2-letter state code (Q to quit): ")
        if state_code.upper() == "Q":
            return "Q"
        else:
            state = registry.state_from_code(state_code)
    return state


def select_county(state, df):
    print("Initiating select_county...")
    counties = df.loc[df["State Name"].str.upper() == state.upper()]\
        ["County Name"].drop_duplicates().to_list()
    
    for n, c in enumerate(counties):
        print(f"{n+1}:\t{c}")

    choice = 0
    while not choice:
        try:
            choice = int(input("Enter number for county: "))
        except:
            print("Enter an integer")
        if choice not in range(len(counties)+1):
            choice = 0
    return counties[choice-1]


def select_destination(): # TODO if returning Q, quit
    destination = None
    while destination not in [1, 2]:
        print(
            """Choose destination for plot
        1   Display to Screen
        2   Save to File"""
            )
        destination = input()
        if destination.upper() == "Q":
            return "Q"
        else:
            try:
                destination = int(destination)
            except:
                print("Invalid input, try again...")
    if destination == 1:
        return "screen"
    elif destination == 2:
        return "file"
    else:
        print("This should never happen... Oops")
        return -1


def plot_county_data(state, county, df, dest):
    """Takes a state and county, a dataframe, and a destination.
    Plots county data either to screen or file depending on dest."""
    c_aqi_df = df.loc[
        (df["State Name"].str.upper() == state.upper()) \
            & (df["County Name"].str.upper() == county.upper())
        ]["AQI"]
    # print(f"Plotting data for {county} county, {state} to a/the {dest} from dataframe:")
    # print(c_aqi_df)

    avg_aqi = round(float(c_aqi_df.mean()))
    # print(f"Average AQI: {avg_aqi}")
    
    color = 'green'
    if avg_aqi > 50:
        color = 'red'

    plt.plot(c_aqi_df, color)
    plt.title(
        f"AQI in {county} County, {state} (avg AQI = {avg_aqi})")
    plt.ylabel("AQI")
    plt.xticks([])

    if dest == 'file':
        file_name = None
        while not file_name:
            file_name = \
                input("Enter file with extension of jpg|png|pdf: ")
            if file_name == "":
                print("No file name entered. Using default...")
                file_name = f"AQI_for_{"_".join(county.split())}_County_{"_".join(state.split())}.png"
            elif not file_name.endswith((".jpg", ".png", ".pdf")):
                print("Please enter valid file format.")
                file_name = None

        plt.savefig(file_name)
    else:
        plt.show()

    plt.clf()


def county_loop(state_name, df):
    county = select_county(state_name, df)
    # print(f"County selected: {county}")
    destination = select_destination()
    # print(f"Destination set: {destination}")

    plot_county_data(state_name, county, df, destination)


def main_loop(states_registry, df):
    state_name = select_state(states_registry)
    if state_name == "Q":
        return -1
    # print(f"State Chosen: {state_name}")
    
    # county_loop(state_name, df)

    same_state = "y"
    while same_state not in ["n", "q"]:
        if same_state == "y":
            county_loop(state_name, df)
        same_state = "n"
        same_state = input(f"Enter another {state_name} county? (y/n): ").lower()
    if same_state == "n":
        main_loop(states_registry, df)
    elif same_state == "q":
        print("Quitting...")
    

        
def main():
    print("Loading data...")
    file = "daily_44201_2021.csv"
    df = pd.read_csv(file, usecols=['State Name', 'County Name', 'AQI'])
    #print(df.head())
    
    states_registry = StatesRegistry()

    main_loop(states_registry, df)
    
    



if __name__ == "__main__":
    main()