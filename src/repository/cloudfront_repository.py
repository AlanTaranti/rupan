from .base_repository import BaseRepository


class CloudfrontRepository(BaseRepository):
    @property
    def client(self):
        return self.session.client("cloudfront")

    def list_distributions(self):
        return self.client.list_distributions()["DistributionList"]["Items"]

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
                }
            )

        return data
