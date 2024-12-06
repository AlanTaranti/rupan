from .base_repository import BaseRepository


class CloudwatchRepository(BaseRepository):
    @property
    def client(self):
        return self.get_session().client("logs")

    def describe_log_streams(self, log_group_name: str):
        try:
            return self.client.describe_log_streams(
                logGroupName=log_group_name,
                orderBy="LastEventTime",
                descending=True,
                limit=1
            )
        except Exception:
            # Log group doesn't exist
            pass
        return None
