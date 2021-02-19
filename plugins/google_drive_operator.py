import os

from airflow.models.dag import BaseOperator
from airflow.providers.google.suite.hooks.drive import GoogleDriveHook
from airflow.utils.decorators import apply_defaults
from typing import Optional, Union, Sequence


class GoogleDriveOperator(BaseOperator):
    """Upload a list of files to a Google Drive folder.

    This operator uploads a list of local files to a Google Drive folder.
    The local fils is deleted after upload (optional).

    Args:
        local_path: Python list of local file paths (templated)
        drive_folder: path of the Drive folder
        api_version: version of the Google Drive API
        gcp_conn_id: Airflow Connections ID for GCP
        delegate_to: Google Account to which to delegate the file upload
            requires Domain-Wide Delegation enabled
        impersonation_chain: service account to impersonate
        delete: should the local file be deleted after upload?
    """

    template_fields = ('local_path', )

    @apply_defaults
    def __init__(
        self,
        local_path: str,
        drive_folder: str,
        gcp_conn_id: str,
        delegate_to: Optional[str] = None,
        impersonation_chain: Optional[Union[str, Sequence[str]]] = None,
        api_version: str = 'v3',
        delete: bool = True,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.local_path = local_path
        self.drive_folder = drive_folder
        self.api_version = api_version
        self.gcp_conn_id = gcp_conn_id
        self.delegate_to = delegate_to
        self.impersonation_chain = impersonation_chain
        self.delete = delete

    def execute(self, context):
        hook = GoogleDriveHook(
            api_version=self.api_version,
            gcp_conn_id=self.gcp_conn_id,
            delegate_to=self.delegate_to,
            impersonation_chain=self.impersonation_chain
        )

        self.log.info(f'Uploading file: {self.local_path}')
        file_name = self.local_path.split('/')[-1]

        try:
            hook.upload_file(
                local_location=self.local_path,
                remote_location=os.path.join(self.drive_folder, file_name)
            )
        except FileNotFoundError:
            self.log.error(f"File {self.local_path} can't be found")

        if self.delete is True:
            os.remove(self.local_path)
            self.log.info(f'Deleted local file: {self.local_path}')
