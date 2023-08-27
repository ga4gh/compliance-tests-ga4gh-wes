"""Module compliance-tests-ga4gh-wes.models.v1_0_0_specs.py

Pydantic generated models for WES API Specs v1.0.0.
(https://github.com/ga4gh/workflow-execution-service-schemas/blob/1.0.0/openapi/workflow_execution_service.swagger.yaml)
"""

# Comment the annotations as a workaround to known pydantic issue - https://github.com/pydantic/pydantic/issues/704
# from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Model(BaseModel):
    __root__: Any


class DefaultWorkflowEngineParameter(BaseModel):
    name: Optional[str] = Field(None, description='The name of the parameter')
    type: Optional[str] = Field(
        None, description='Describes the type of the parameter, e.g. float.'
    )
    default_value: Optional[str] = Field(
        None,
        description='The stringified version of the default parameter. e.g. "2.45".',
    )


class Log(BaseModel):
    name: Optional[str] = Field(None, description='The task or workflow name')
    cmd: Optional[List[str]] = Field(
        None, description='The command line that was executed'
    )
    start_time: Optional[str] = Field(
        None,
        description='When the command started executing, in ISO 8601 format "%Y-%m-%dT%H:%M:%SZ"',
    )
    end_time: Optional[str] = Field(
        None,
        description='When the command stopped executing (completed, failed, or cancelled), in ISO 8601 format "%Y-%m-%dT%H:%M:%SZ"',
    )
    stdout: Optional[str] = Field(
        None,
        description='A URL to retrieve standard output logs of the workflow run or task.  This URL may change between status requests, or may not be available until the task or workflow has finished execution.  Should be available using the same credentials used to access the WES endpoint.',
    )
    stderr: Optional[str] = Field(
        None,
        description='A URL to retrieve standard error logs of the workflow run or task.  This URL may change between status requests, or may not be available until the task or workflow has finished execution.  Should be available using the same credentials used to access the WES endpoint.',
    )
    exit_code: Optional[int] = Field(None, description='Exit code of the program')


class State(Enum):
    UNKNOWN = 'UNKNOWN'
    QUEUED = 'QUEUED'
    INITIALIZING = 'INITIALIZING'
    RUNNING = 'RUNNING'
    PAUSED = 'PAUSED'
    COMPLETE = 'COMPLETE'
    EXECUTOR_ERROR = 'EXECUTOR_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'
    CANCELED = 'CANCELED'
    CANCELING = 'CANCELING'


class RunRequest(BaseModel):
    workflow_params: Optional[Dict[str, Any]] = Field(
        None,
        description='REQUIRED\nThe workflow run parameterizations (JSON encoded), including input and output file locations',
    )
    workflow_type: Optional[str] = Field(
        None,
        description='REQUIRED\nThe workflow descriptor type, must be "CWL" or "WDL" currently (or another alternative supported by this WES instance)',
    )
    workflow_type_version: Optional[str] = Field(
        None,
        description='REQUIRED\nThe workflow descriptor type version, must be one supported by this WES instance',
    )
    tags: Optional[Dict[str, str]] = Field(
        None,
        description='OPTIONAL\nA key-value map of arbitrary metadata outside the scope of `workflow_params` but useful to track with this run request',
    )
    workflow_engine_parameters: Optional[Dict[str, str]] = Field(
        None,
        description='OPTIONAL\nAdditional parameters can be sent to the workflow engine using this field. Default values for these parameters can be obtained using the ServiceInfo endpoint.',
    )
    workflow_url: Optional[str] = Field(
        None,
        description='REQUIRED\nThe workflow CWL or WDL document. When `workflow_attachments` is used to attach files, the `workflow_url` may be a relative path to one of the attachments.',
    )


class RunId(BaseModel):
    run_id: Optional[str] = Field(None, description='workflow run ID')


class RunStatus(BaseModel):
    run_id: str
    state: Optional[State] = None


class WorkflowTypeVersion(BaseModel):
    workflow_type_version: Optional[List[str]] = Field(
        None,
        description='an array of one or more acceptable types for the `workflow_type`',
    )


class ErrorResponse(BaseModel):
    msg: Optional[str] = Field(None, description='A detailed error message.')
    status_code: Optional[int] = Field(
        None,
        description='The integer representing the HTTP status code (e.g. 200, 404).',
    )


class ServiceInfo(BaseModel):
    workflow_type_versions: Optional[Dict[str, WorkflowTypeVersion]] = Field(
        None,
        description='A map with keys as the workflow format type name (currently only CWL and WDL are used although a service may support others) and value is a workflow_type_version object which simply contains an array of one or more version strings',
    )
    supported_wes_versions: Optional[List[str]] = Field(
        None, description='The version(s) of the WES schema supported by this service'
    )
    supported_filesystem_protocols: Optional[List[str]] = Field(
        None,
        description="The filesystem protocols supported by this service, currently these may include common protocols using the terms 'http', 'https', 'sftp', 's3', 'gs', 'file', or 'synapse', but others  are possible and the terms beyond these core protocols are currently not fixed.   This section reports those protocols (either common or not) supported by this WES service.",
    )
    workflow_engine_versions: Optional[Dict[str, str]] = Field(
        None,
        description='The engine(s) used by this WES service, key is engine name (e.g. Cromwell) and value is version',
    )
    default_workflow_engine_parameters: Optional[
        List[DefaultWorkflowEngineParameter]
    ] = Field(
        None,
        description='Each workflow engine can present additional parameters that can be sent to the workflow engine. This message will list the default values, and their types for each workflow engine.',
    )
    system_state_counts: Optional[Dict[str, int]] = Field(
        None,
        description='The system statistics, key is the statistic, value is the count of runs in that state. See the State enum for the possible keys.',
    )
    auth_instructions_url: Optional[str] = Field(
        None,
        description='A web page URL with human-readable instructions on how to get an authorization token for use with a specific WES endpoint.          ',
    )
    contact_info_url: Optional[str] = Field(
        None,
        description='An email address URL (mailto:) or web page URL with contact information for the operator of a specific WES endpoint.  Users of the endpoint should use this to report problems or security vulnerabilities.',
    )
    tags: Optional[Dict[str, str]] = Field(
        None,
        description='A key-value map of arbitrary, extended metadata outside the scope of the above but useful to report back',
    )


class RunListResponse(BaseModel):
    runs: Optional[List[RunStatus]] = Field(
        None,
        description='A list of workflow runs that the service has executed or is executing. The list is filtered to only include runs that the caller has permission to see.',
    )
    next_page_token: Optional[str] = Field(
        None,
        description='A token which may be supplied as `page_token` in workflow run list request to get the next page of results.  An empty string indicates there are no more items to return.',
    )


class RunLog(BaseModel):
    run_id: Optional[str] = Field(None, description='workflow run ID')
    request: Optional[RunRequest] = Field(
        None,
        description='The original request message used to initiate this execution.',
    )
    state: Optional[State] = Field(
        None, description='The state of the run e.g. RUNNING (see State)'
    )
    run_log: Optional[Log] = Field(
        None,
        description='The logs, and other key info like timing and exit code, for the overall run of this workflow.',
    )
    task_logs: Optional[List[Log]] = Field(
        None,
        description='The logs, and other key info like timing and exit code, for each step in the workflow run.',
    )
    outputs: Optional[Dict[str, Any]] = Field(
        None, description='The outputs from the workflow run.'
    )
