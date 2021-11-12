from datetime import datetime, timedelta

import pandas as pd
from botocore.exceptions import ClientError

from .repository.sts_repository import StsRepository
from .repository.s3_repository import S3Repository
from .repository.cloudfront_repository import CloudfrontRepository
from .repository.elbv2_repository import ElasticLoadBalancingV2Repository
from .repository.elb_repository import ElasticLoadBalancingRepository


class LoggingService:
    def __format_get_logging(self, dataframe: pd.DataFrame):
        dataframe = dataframe.rename(
            columns={
                "Name": "name",
                "Region": "region",
                "LoggingEnabled": "logging_enabled",
            }
        )

        columns = [
            "account_id",
            "service",
            "name",
            "region",
            "logging_enabled",
        ]

        dataframe = dataframe.reindex(columns=columns)

        return dataframe

    def get_logging(self):
        s3_repository = S3Repository()
        sts_repository = StsRepository()
        cloudfront_repository = CloudfrontRepository()
        elbv2_repository = ElasticLoadBalancingV2Repository()
        elb_repository = ElasticLoadBalancingRepository()

        try:
            buckets_logging = s3_repository.list_buckets_logging()
        except ClientError as error:
            exit(error)

        try:
            cloudfront_logging = cloudfront_repository.list_distributions_logging()
        except ClientError as error:
            exit(error)

        try:
            elbv2_logging = elbv2_repository.list_load_balancer_logging()
        except ClientError as error:
            exit(error)

        try:
            elb_logging = elb_repository.list_load_balancer_logging()
        except ClientError as error:
            exit(error)

        buckets_logging = pd.DataFrame(buckets_logging)
        buckets_logging.insert(0, "service", "s3")

        cloudfront_logging = pd.DataFrame(cloudfront_logging)
        cloudfront_logging.insert(0, "service", "cloudfront")

        elbv2_logging = pd.DataFrame(elbv2_logging)
        elbv2_logging.insert(0, "service", "elbv2")

        elb_logging = pd.DataFrame(elb_logging)
        elb_logging.insert(0, "service", "elb")

        dataframe = pd.concat(
            [
                buckets_logging,
                cloudfront_logging,
                elbv2_logging,
                elb_logging,
            ]
        )
        account_id = sts_repository.get_account_id()
        dataframe.insert(0, "account_id", account_id)

        dataframe = self.__format_get_logging(dataframe)

        return dataframe
