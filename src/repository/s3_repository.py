from .base_repository import BaseRepository


class S3Repository(BaseRepository):
    @property
    def client(self):
        return self.session.client("s3")

    @property
    def resource(self):
        return self.session.resource("s3")

    def list_buckets(self):
        return self.resource.buckets.all()

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

            is_public = (
                len([grant for grant in acls["Grants"] if has_public_access(grant)]) > 0
            )

            data.append(
                {
                    "name": bucket.name,
                    "owner": acls["Owner"]["DisplayName"],
                    "is_public": is_public,
                }
            )

        return data
