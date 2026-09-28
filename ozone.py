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


def select_state(registry):
    state = None
    while not state:
        state_code = input("Enter 2-letter state code (Q to quit): ")
        if state_code.upper() == "Q":
            return "Q"
        else:
            state = registry.state_from_code(state_code)
    return state

        
def main():
    print("Loading data...")
    file = "daily_44201_2021.csv"
    df = pd.read_csv(file, usecols=['State Name', 'County Name', 'AQI'])
    #print(df.head())
    
    states_registry = StatesRegistry()

    state_name = select_state(states_registry)
    print(f"state name: {state_name}")
    print("MADE IT THIS FAR!! :)")
    assert 0
    
    county = select_county(state_name)

    states = df["State Name"].drop_duplicates()

    #print_states(states)



if __name__ == "__main__":
    main()