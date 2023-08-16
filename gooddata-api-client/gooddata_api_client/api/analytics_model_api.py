"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_api_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_api_client.model.declarative_analytics import DeclarativeAnalytics


class AnalyticsModelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_analytics_model_endpoint = _Endpoint(
            settings={
                'response_type': (DeclarativeAnalytics,),
                'auth': [],
                'endpoint_path': '/api/v1/layout/workspaces/{workspaceId}/analyticsModel',
                'operation_id': 'get_analytics_model',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'exclude',
                ],
                'required': [
                    'workspace_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'exclude',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('exclude',): {

                        "ACTIVITY_INFO": "ACTIVITY_INFO"
                    },
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'exclude':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'exclude': 'exclude',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'exclude': 'query',
                },
                'collection_format_map': {
                    'exclude': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.set_analytics_model_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/api/v1/layout/workspaces/{workspaceId}/analyticsModel',
                'operation_id': 'set_analytics_model',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'declarative_analytics',
                ],
                'required': [
                    'workspace_id',
                    'declarative_analytics',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'declarative_analytics':
                        (DeclarativeAnalytics,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'declarative_analytics': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_analytics_model(
        self,
        workspace_id,
        **kwargs
    ):
        """Get analytics model  # noqa: E501

        Retrieve current analytics model of the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_analytics_model(workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str):

        Keyword Args:
            exclude ([str]): [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DeclarativeAnalytics
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['workspace_id'] = \
            workspace_id
        return self.get_analytics_model_endpoint.call_with_http_info(**kwargs)

    def set_analytics_model(
        self,
        workspace_id,
        declarative_analytics,
        **kwargs
    ):
        """Set analytics model  # noqa: E501

        Set effective analytics model of the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_analytics_model(workspace_id, declarative_analytics, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str):
            declarative_analytics (DeclarativeAnalytics):

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['declarative_analytics'] = \
            declarative_analytics
        return self.set_analytics_model_endpoint.call_with_http_info(**kwargs)

