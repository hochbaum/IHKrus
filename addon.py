from mitmproxy import ctx, http
from mitmproxy import flowfilter
import json

ENDPOINT = "https://dibe.services.ihk.de/berichtsheft/erstellen-api/v1/berichtswoche"
SKILLS = [5, 4, 11, 1, 10, 12, 27]


class IHKrus:
    def __init__(self):
        self.filter: flowfilter.TFilter = flowfilter.FMethod("PUT")

    def request(self, flow: http.HTTPFlow) -> None:
        if not flowfilter.match(self.filter, flow) or flow.request.url != ENDPOINT: 
            return

        data = flow.request.json()

        # Checked skills are located at `tagesBerichte[].eintraege[].qualifikationen[]`.
        # They are encoded as `{"berufsbildPositionId": <ID of the checked box>}`.
        [
            entry["qualifikationen"].append({"berufsbildPositionId": skill}) 
            for report in data["tagesBerichte"] 
            for entry in report["eintraege"] 
            for skill in SKILLS

            # Don't send duplicate skills (it works but might look sus).
            if {"berufsbildPositionId": skill} not in entry["qualifikationen"]
        ]

        flow.request.content = json.dumps(data).encode()
        ctx.master.commands.call("replay.client", [flow])
        ctx.log.info("IHKrus: You are one qualified man!")


addons = [IHKrus()]
