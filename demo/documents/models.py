import uuid

from django.db import models


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.JSONField(default=dict, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "teams.User", related_name="documents", on_delete=models.CASCADE
    )
    org_id = models.ForeignKey(
        "organizations.Organization", related_name="documents", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "documents"
