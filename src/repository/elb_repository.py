from .base_repository import BaseRepository


class ElasticLoadBalancingRepository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("elb")

    def list_load_balancers(self):
        return self.client.describe_load_balancers()["LoadBalancerDescriptions"]

    def get_load_balancer_attributes(self, load_balancers_name):
        return self.client.describe_load_balancer_attributes(
            LoadBalancerName=load_balancers_name
        )["LoadBalancerAttributes"]

    def list_load_balancer_logging(self):
        load_balancers = self.list_load_balancers()

        data = []

        def has_logging_enabled(attributes):
            return attributes["AccessLog"]["Enabled"]

        for load_balancer in load_balancers:
            load_balancer_attributes = self.get_load_balancer_attributes(
                load_balancer["LoadBalancerName"]
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
