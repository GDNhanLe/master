# gooddata_afm_client.ValidObjectsControllerApi

All URIs are relative to *https://staging.anywhere.gooddata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_valid_objects**](ValidObjectsControllerApi.md#compute_valid_objects) | **POST** /api/actions/workspaces/{workspaceId}/execution/afm/computeValidObjects | Valid objects


# **compute_valid_objects**
> AfmValidObjectsResponse compute_valid_objects(workspace_id, afm_valid_objects_query)

Valid objects

Returns list containing attributes, facts, or measures, which can be added to given AFM while still keeping it computable.

### Example

```python
import time
import gooddata_afm_client
from gooddata_afm_client.api import valid_objects_controller_api
from gooddata_afm_client.model.afm_valid_objects_query import AfmValidObjectsQuery
from gooddata_afm_client.model.afm_valid_objects_response import AfmValidObjectsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://staging.anywhere.gooddata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_afm_client.Configuration(
    host = "https://staging.anywhere.gooddata.com"
)


# Enter a context with an instance of the API client
with gooddata_afm_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = valid_objects_controller_api.ValidObjectsControllerApi(api_client)
    workspace_id = "26bUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awxoFZxHzs6ED.kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz9rEoBi0LnU8SsOWJ7wYrcziVQdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z.qKa_YppZepezJ0.VmLSUTLYyW" # str | Workspace identifier
    afm_valid_objects_query = AfmValidObjectsQuery(
        types=[
            "facts",
        ],
        afm=AFM(
            attributes=[
                AttributeItem(
                    local_identifier="2",
                    label=AfmObjectIdentifier(
                        identifier=ObjectIdentifier(
                            id="sample_item.price",
                            type="fact",
                        ),
                    ),
                ),
            ],
            filters=[
                FilterDefinition(),
            ],
            measures=[
                MeasureItem(
                    local_identifier="sampleAutoGenerated0123_ID",
                    definition=MeasureDefinition(),
                ),
            ],
            aux_measures=[
                MeasureItem(
                    local_identifier="sampleAutoGenerated0123_ID",
                    definition=MeasureDefinition(),
                ),
            ],
        ),
    ) # AfmValidObjectsQuery | 

    # example passing only required values which don't have defaults set
    try:
        # Valid objects
        api_response = api_instance.compute_valid_objects(workspace_id, afm_valid_objects_query)
        pprint(api_response)
    except gooddata_afm_client.ApiException as e:
        print("Exception when calling ValidObjectsControllerApi->compute_valid_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier |
 **afm_valid_objects_query** | [**AfmValidObjectsQuery**](AfmValidObjectsQuery.md)|  |

### Return type

[**AfmValidObjectsResponse**](AfmValidObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of attributes, facts and measures valid with respect to given AFM. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
