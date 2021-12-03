from .base_repository import BaseRepository


class S3Repository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("s3")

    @property
    def resource(self):
        return self.get_session().resource("s3")

    def list_buckets(self):
        return self.resource.buckets.all()

    def list_buckets_logging(self):
        buckets = self.list_buckets()

        data = []

        for bucket in buckets:
            logging = self.client.get_bucket_logging(Bucket=bucket.name)
            location = self.get_bucket_location(bucket.name)

            data.append(
                {
                    "Name": bucket.name,
                    "LoggingEnabled": "LoggingEnabled" in logging,
                    "Region": location,
                }
            )

        return data

    def get_bucket_location(self, bucket_name):
        return self.client.get_bucket_location(Bucket=bucket_name)["LocationConstraint"]

    def list_buckets_data(self):
        buckets = self.list_buckets()

        data = []

        def has_public_access(grant):
            grantee = grant["Grantee"]

            if grantee["Type"] == "Group":
                uri = grantee["URI"]

                if (
                    uri == "http://acs.amazonaws.com/groups/global/AllUsers"
                    or uri
                    == "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"
                ):
                    return True

            return False

        for bucket in buckets:
            acls = self.client.get_bucket_acl(Bucket=bucket.name)
            location = self.get_bucket_location(bucket.name)

            is_public = (
                len([grant for grant in acls["Grants"] if has_public_access(grant)]) > 0
            )

            data.append(
                {
                    "Name": bucket.name,
                    "DisplayName": acls["Owner"]["DisplayName"],
                    "LocationConstraint": location,
                    "IsPublic": is_public,
                }
            )

        return data
