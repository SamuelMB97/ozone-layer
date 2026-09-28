import numpy as np
import pandas as pd


class StatesRegistry():
    def __init__(self):
        self.df = pd.read_csv("state_codes.txt", header=None)
        self.df.columns = ['code', 'state']

    def state_from_code(self, cd:str):# TODO account for validating data
        """Takes a state code and returns the corresponding state name"""
        try:
            return self.df.loc[
                self.df['code'].str.upper() == cd.upper(), 'state'
                ].iloc[0]
        except:
            print(f"State code '{cd}' not found")
            return None

    def code_from_state(self, st:str):# TODO account for validating data
        """Takes a state name and returns the corresponding state code"""
        try:
            return self.df.loc[
                self.df['state'].str.upper() == st.upper(), 'code'
                ].iloc[0]
        except:
            print(f"State '{st}' not found")
            return None


"""
states = StatesRegistry()
code = 'AK'
state = states.state_from_code(code)
print(f"For code {code}, state is: {state}")

print()
state1 = 'Idaho'
code1 = states.code_from_state(state1)
print(f"For state {state1}, code is: {code1}")
states = StatesRegistry()

code = 'AN'
state = states.state_from_code(code)
print(f"For code {code}, state is: {state}")

print()
state1 = 'Idahoo'
code1 = states.code_from_state(state1)
print(f"For state {state1}, code is: {code1}")
#"""