from .base_repository import BaseRepository


class ElasticLoadBalancingV2Repository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("elbv2")

    def list_load_balancers(self):
        return self.client.describe_load_balancers()["LoadBalancers"]

    def get_load_balancer_attributes(self, load_balancers_arn):
        return self.client.describe_load_balancer_attributes(
            LoadBalancerArn=load_balancers_arn
        )["Attributes"]

    def list_load_balancer_logging(self):
        load_balancers = self.list_load_balancers()

        data = []

        def has_logging_enabled(attributes):
            attributes_filtered = [
                attribute
                for attribute in attributes
                if attribute["Key"] == "access_logs.s3.enabled"
            ]

            if len(attributes_filtered) == 0:
                return False

            return attributes_filtered[0]["Value"] == "true"

        for load_balancer in load_balancers:
            load_balancer_attributes = self.get_load_balancer_attributes(
                load_balancer["LoadBalancerArn"]
            )

            logging_enabled = has_logging_enabled(load_balancer_attributes)

            data.append(
                {
                    "Name": load_balancer["LoadBalancerName"],
                    "LoggingEnabled": logging_enabled,
                    "Region": None,
                }
            )

        return data
