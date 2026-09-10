from client import PetriNet

def main():
    print("=== Testing Petri Net Reachability Analyzer ===")
    pn = PetriNet(
        places={'idle': 1, 'active': 0},
        transitions={
            'start': ({'idle': 1}, {'active': 1}),
            'finish': ({'active': 1}, {'idle': 1})
        }
    )
    states = pn.reachable_markings()
    print(f"Reachable Marking Count: {states}")
    assert states == 2
    print("=== Petri Net Verification Complete ===")

if __name__ == "__main__":
    main()
