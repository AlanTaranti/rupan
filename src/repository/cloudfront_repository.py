from .base_repository import BaseRepository


class CloudfrontRepository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("cloudfront")

    def list_distributions(self):
        distribuicoes = self.client.list_distributions()["DistributionList"]
        if "Items" in distribuicoes:
            return distribuicoes["Items"]
        return []

    def get_distribution(self, distribuition_id):
        return self.client.get_distribution(Id=distribuition_id)["Distribution"]

    def list_distributions_logging(self):
        distributions = self.list_distributions()

        data = []

        for distribution in distributions:
            distribution_data = self.get_distribution(distribution["Id"])
            logging_enabled = distribution_data["DistributionConfig"]["Logging"][
                "Enabled"
            ]

            data.append(
                {
                    "Name": distribution["Id"],
                    "LoggingEnabled": logging_enabled,
                    "Region": None,
                }
            )

        return data
