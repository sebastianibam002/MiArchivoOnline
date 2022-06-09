from .models import UploadedFile
import uuid

"""
Checks that the given url is is not with the ones already in
the database
"""
def generateUrl() -> None:
    value = uuid.uuid4().hex
    queryset = UploadedFile.objects.filter(unique_link=value)
    if not queryset.exists():
        return value
    return uuid.uuid4().hex

