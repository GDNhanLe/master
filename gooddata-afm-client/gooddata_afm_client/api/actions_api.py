"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_afm_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_afm_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_afm_client.model.afm_execution import AfmExecution
from gooddata_afm_client.model.afm_execution_response import AfmExecutionResponse
from gooddata_afm_client.model.afm_valid_objects_query import AfmValidObjectsQuery
from gooddata_afm_client.model.afm_valid_objects_response import AfmValidObjectsResponse
from gooddata_afm_client.model.elements_request import ElementsRequest
from gooddata_afm_client.model.elements_response import ElementsResponse
from gooddata_afm_client.model.error_message import ErrorMessage
from gooddata_afm_client.model.execution_result import ExecutionResult


class ActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.compute_label_elements_post_endpoint = _Endpoint(
            settings={
                'response_type': (ElementsResponse,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/collectLabelElements',
                'operation_id': 'compute_label_elements_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'elements_request',
                    'offset',
                    'limit',
                    'skip_cache',
                ],
                'required': [
                    'workspace_id',
                    'elements_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                    'offset',
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                    ('offset',): {

                        'inclusive_maximum': 10000,
                        'inclusive_minimum': 0,
                    },
                    ('limit',): {

                        'inclusive_maximum': 10000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'elements_request':
                        (ElementsRequest,),
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'skip_cache':
                        (bool,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'offset': 'offset',
                    'limit': 'limit',
                    'skip_cache': 'skip-cache',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'elements_request': 'body',
                    'offset': 'query',
                    'limit': 'query',
                    'skip_cache': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.compute_report_endpoint = _Endpoint(
            settings={
                'response_type': (AfmExecutionResponse,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/execute',
                'operation_id': 'compute_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'afm_execution',
                    'skip_cache',
                    'timestamp',
                ],
                'required': [
                    'workspace_id',
                    'afm_execution',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'afm_execution':
                        (AfmExecution,),
                    'skip_cache':
                        (bool,),
                    'timestamp':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'skip_cache': 'skip-cache',
                    'timestamp': 'timestamp',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'afm_execution': 'body',
                    'skip_cache': 'header',
                    'timestamp': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.compute_valid_objects_endpoint = _Endpoint(
            settings={
                'response_type': (AfmValidObjectsResponse,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/computeValidObjects',
                'operation_id': 'compute_valid_objects',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'afm_valid_objects_query',
                ],
                'required': [
                    'workspace_id',
                    'afm_valid_objects_query',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'afm_valid_objects_query':
                        (AfmValidObjectsQuery,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'afm_valid_objects_query': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.explain_afm_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/explain',
                'operation_id': 'explain_afm',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'afm_execution',
                    'explain_type',
                ],
                'required': [
                    'workspace_id',
                    'afm_execution',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'afm_execution':
                        (AfmExecution,),
                    'explain_type':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'explain_type': 'explainType',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'afm_execution': 'body',
                    'explain_type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/zip'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.retrieve_result_endpoint = _Endpoint(
            settings={
                'response_type': (ExecutionResult,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/execute/result/{resultId}',
                'operation_id': 'retrieve_result',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'result_id',
                    'offset',
                    'limit',
                ],
                'required': [
                    'workspace_id',
                    'result_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'result_id':
                        (str,),
                    'offset':
                        ([int],),
                    'limit':
                        ([int],),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'result_id': 'resultId',
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'result_id': 'path',
                    'offset': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                    'offset': 'csv',
                    'limit': 'csv',
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def compute_label_elements_post(
        self,
        workspace_id,
        elements_request,
        **kwargs
    ):
        """Listing of label values. The resulting data are limited by the static platform limit to the maximum of 10000 rows.  # noqa: E501

        Returns paged list of elements (values) of given label satisfying given filtering criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.compute_label_elements_post(workspace_id, elements_request, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): Workspace identifier
            elements_request (ElementsRequest):

        Keyword Args:
            offset (int): Request page with this offset. Must be positive integer. The API is limited to the maximum of 10000 items. Therefore this parameter is limited to this number as well.. [optional] if omitted the server will use the default value of 0
            limit (int): Return only this number of items. Must be positive integer. The API is limited to the maximum of 10000 items. Therefore this parameter is limited to this number as well.. [optional] if omitted the server will use the default value of 1000
            skip_cache (bool): Ignore all caches during execution of current request.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ElementsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['elements_request'] = \
            elements_request
        return self.compute_label_elements_post_endpoint.call_with_http_info(**kwargs)

    def compute_report(
        self,
        workspace_id,
        afm_execution,
        **kwargs
    ):
        """Executes analytical request and returns link to the result  # noqa: E501

        AFM is a combination of attributes, measures and filters that describe a query you want to execute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.compute_report(workspace_id, afm_execution, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): Workspace identifier
            afm_execution (AfmExecution):

        Keyword Args:
            skip_cache (bool): Ignore all caches during execution of current request.. [optional] if omitted the server will use the default value of False
            timestamp (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AfmExecutionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['afm_execution'] = \
            afm_execution
        return self.compute_report_endpoint.call_with_http_info(**kwargs)

    def compute_valid_objects(
        self,
        workspace_id,
        afm_valid_objects_query,
        **kwargs
    ):
        """Valid objects  # noqa: E501

        Returns list containing attributes, facts, or metrics, which can be added to given AFM while still keeping it computable.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.compute_valid_objects(workspace_id, afm_valid_objects_query, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): Workspace identifier
            afm_valid_objects_query (AfmValidObjectsQuery):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AfmValidObjectsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['afm_valid_objects_query'] = \
            afm_valid_objects_query
        return self.compute_valid_objects_endpoint.call_with_http_info(**kwargs)

    def explain_afm(
        self,
        workspace_id,
        afm_execution,
        **kwargs
    ):
        """AFM explain resource.  # noqa: E501

        The resource provides static structures needed for investigation of a problem with given AFM. The structures differs for AQE and for Calcique. They are either MAQL (internal form of AFM) and logical and physical models (LDM and PDM) of corresponding workspace or MAQL and GRPC and WDF models.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.explain_afm(workspace_id, afm_execution, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): Workspace identifier
            afm_execution (AfmExecution):

        Keyword Args:
            explain_type (str): Requested explain type (LDM, PDM, GRPC_MODEL, WDF or MAQL). If not specified all types are bundled in a ZIP archive.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['afm_execution'] = \
            afm_execution
        return self.explain_afm_endpoint.call_with_http_info(**kwargs)

    def retrieve_result(
        self,
        workspace_id,
        result_id,
        **kwargs
    ):
        """Get a single execution result  # noqa: E501

        Gets a single execution result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_result(workspace_id, result_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): Workspace identifier
            result_id (str): Result ID

        Keyword Args:
            offset ([int]): Request page with these offsets. Format is offset=1,2,3,... - one offset for each dimensions in ResultSpec from originating AFM.. [optional] if omitted the server will use the default value of []
            limit ([int]): Return only this number of items. Format is limit=1,2,3,... - one limit for each dimensions in ResultSpec from originating AFM.. [optional] if omitted the server will use the default value of []
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ExecutionResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['result_id'] = \
            result_id
        return self.retrieve_result_endpoint.call_with_http_info(**kwargs)

