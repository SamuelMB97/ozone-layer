import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def print_states(states):
    """not fully functional yet..."""
    state_codes_file = "state_codes.txt"
    state_codes = pd.read_csv(state_codes_file, header=None)
    state_codes.columns = ['code', 'state']

    for n, state in enumerate(list(states)):
        code = state_codes.loc[
            state_codes['state'] == state, 'code'
            ].iloc[0]
        print(f"{n+1:<3}{state} ({code})")

        
def main():
    file = "daily_44201_2021.csv"
    df = pd.read_csv(file)

    states = df["State Name"].drop_duplicates()
    #print_states(states)



if __name__ == "__main__":
    main()