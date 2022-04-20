from mitmproxy import ctx, http
from mitmproxy import flowfilter
import json

ENDPOINT = "https://dibe.services.ihk.de/berichtsheft/erstellen-api/v1/berichtswoche"
SKILLS = [5, 4, 11, 1, 10, 12, 27]


class IHKrus:
    def __init__(self):
        self.filter: flowfilter.TFilter = flowfilter.FMethod("PUT")

    def request(self, flow: http.HTTPFlow) -> None:
        if not flowfilter.match(self.filter, flow):
            return

        if flow.request.url == ENDPOINT:
            data = flow.request.json()
            daily_reports = data["tagesBerichte"]

            for report in daily_reports:
                entries = report["eintraege"]

                for entry in entries:
                    skills = entry["qualifikationen"]
                    skills.clear()

                    for skill in SKILLS:
                        skills.append({"berufsbildPositionId": skill})

            flow.request.content = json.dumps(data).encode()
            ctx.master.commands.call("replay.client", [flow])
            ctx.log.info("IHKrus: You are one qualified man!")


addons = [IHKrus()]
