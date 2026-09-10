from client import PetriNet
import json

def handle_request(req):
    places = req.get("places", {})
    transitions = req.get("transitions", {})
    pn = PetriNet(places, transitions)
    action = req.get("action")
    if action == "reachable":
        c = pn.reachable_markings()
        return {"status": "ok", "reachable_count": c}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "reachable", "places": {"p1": 1}, "transitions": {}})))
