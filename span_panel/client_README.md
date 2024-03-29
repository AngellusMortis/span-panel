# span-panel.client
Span Panel REST API

The `span_panel.client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* aiohttp
* pydantic
* aenum

## Getting Started

In your own code, to use this library to connect and interact with span-panel.client,
you can run the following:

```python

import time
import span_panel.client
from span_panel.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = span_panel.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = span_panel.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
async with span_panel.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = span_panel.client.DefaultApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete Client
        api_response = await api_instance.delete_client_api_v1_auth_clients_name_delete(name)
        print("The response of DefaultApi->delete_client_api_v1_auth_clients_name_delete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_client_api_v1_auth_clients_name_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_client_api_v1_auth_clients_name_delete**](span_panel/client/docs/DefaultApi.md#delete_client_api_v1_auth_clients_name_delete) | **DELETE** /api/v1/auth/clients/{name} | Delete Client
*DefaultApi* | [**deprecated_spaces_endpoint_stub_api_v1_spaces_get**](span_panel/client/docs/DefaultApi.md#deprecated_spaces_endpoint_stub_api_v1_spaces_get) | **GET** /api/v1/spaces | Deprecated Spaces Endpoint Stub
*DefaultApi* | [**deprecated_spaces_endpoint_stub_api_v1_spaces_spaces_id_get**](span_panel/client/docs/DefaultApi.md#deprecated_spaces_endpoint_stub_api_v1_spaces_spaces_id_get) | **GET** /api/v1/spaces/{spaces_id} | Deprecated Spaces Endpoint Stub
*DefaultApi* | [**deprecated_spaces_endpoint_stub_api_v1_spaces_spaces_id_post**](span_panel/client/docs/DefaultApi.md#deprecated_spaces_endpoint_stub_api_v1_spaces_spaces_id_post) | **POST** /api/v1/spaces/{spaces_id} | Deprecated Spaces Endpoint Stub
*DefaultApi* | [**generate_jwt_api_v1_auth_register_post**](span_panel/client/docs/DefaultApi.md#generate_jwt_api_v1_auth_register_post) | **POST** /api/v1/auth/register | Generate Jwt
*DefaultApi* | [**get_all_clients_api_v1_auth_clients_get**](span_panel/client/docs/DefaultApi.md#get_all_clients_api_v1_auth_clients_get) | **GET** /api/v1/auth/clients | Get All Clients
*DefaultApi* | [**get_circuit_state_api_v1_circuits_circuit_id_get**](span_panel/client/docs/DefaultApi.md#get_circuit_state_api_v1_circuits_circuit_id_get) | **GET** /api/v1/circuits/{circuitId} | Get Circuit State
*DefaultApi* | [**get_circuits_api_v1_circuits_get**](span_panel/client/docs/DefaultApi.md#get_circuits_api_v1_circuits_get) | **GET** /api/v1/circuits | Get Circuits
*DefaultApi* | [**get_client_api_v1_auth_clients_name_get**](span_panel/client/docs/DefaultApi.md#get_client_api_v1_auth_clients_name_get) | **GET** /api/v1/auth/clients/{name} | Get Client
*DefaultApi* | [**get_islanding_state_api_v1_islanding_state_get**](span_panel/client/docs/DefaultApi.md#get_islanding_state_api_v1_islanding_state_get) | **GET** /api/v1/islanding-state | Get Islanding State
*DefaultApi* | [**get_main_relay_state_api_v1_panel_grid_get**](span_panel/client/docs/DefaultApi.md#get_main_relay_state_api_v1_panel_grid_get) | **GET** /api/v1/panel/grid | Get Main Relay State
*DefaultApi* | [**get_panel_meter_api_v1_panel_meter_get**](span_panel/client/docs/DefaultApi.md#get_panel_meter_api_v1_panel_meter_get) | **GET** /api/v1/panel/meter | Get Panel Meter
*DefaultApi* | [**get_panel_power_api_v1_panel_power_get**](span_panel/client/docs/DefaultApi.md#get_panel_power_api_v1_panel_power_get) | **GET** /api/v1/panel/power | Get Panel Power
*DefaultApi* | [**get_panel_state_api_v1_panel_get**](span_panel/client/docs/DefaultApi.md#get_panel_state_api_v1_panel_get) | **GET** /api/v1/panel | Get Panel State
*DefaultApi* | [**get_storage_nice_to_have_threshold_api_v1_storage_nice_to_have_thresh_get**](span_panel/client/docs/DefaultApi.md#get_storage_nice_to_have_threshold_api_v1_storage_nice_to_have_thresh_get) | **GET** /api/v1/storage/nice-to-have-thresh | Get Storage Nice To Have Threshold
*DefaultApi* | [**get_storage_soe_api_v1_storage_soe_get**](span_panel/client/docs/DefaultApi.md#get_storage_soe_api_v1_storage_soe_get) | **GET** /api/v1/storage/soe | Get Storage Soe
*DefaultApi* | [**get_wifi_scan_api_v1_wifi_scan_get**](span_panel/client/docs/DefaultApi.md#get_wifi_scan_api_v1_wifi_scan_get) | **GET** /api/v1/wifi/scan | Get Wifi Scan
*DefaultApi* | [**run_panel_emergency_reconnect_api_v1_panel_emergency_reconnect_post**](span_panel/client/docs/DefaultApi.md#run_panel_emergency_reconnect_api_v1_panel_emergency_reconnect_post) | **POST** /api/v1/panel/emergency-reconnect | Run Panel Emergency Reconnect
*DefaultApi* | [**run_wifi_connect_api_v1_wifi_connect_post**](span_panel/client/docs/DefaultApi.md#run_wifi_connect_api_v1_wifi_connect_post) | **POST** /api/v1/wifi/connect | Run Wifi Connect
*DefaultApi* | [**set_circuit_state_api_v1_circuits_circuit_id_post**](span_panel/client/docs/DefaultApi.md#set_circuit_state_api_v1_circuits_circuit_id_post) | **POST** /api/v1/circuits/{circuitId} | Set Circuit State
*DefaultApi* | [**set_main_relay_state_api_v1_panel_grid_post**](span_panel/client/docs/DefaultApi.md#set_main_relay_state_api_v1_panel_grid_post) | **POST** /api/v1/panel/grid | Set Main Relay State
*DefaultApi* | [**set_storage_nice_to_have_threshold_api_v1_storage_nice_to_have_thresh_post**](span_panel/client/docs/DefaultApi.md#set_storage_nice_to_have_threshold_api_v1_storage_nice_to_have_thresh_post) | **POST** /api/v1/storage/nice-to-have-thresh | Set Storage Nice To Have Threshold
*DefaultApi* | [**set_storage_soe_api_v1_storage_soe_post**](span_panel/client/docs/DefaultApi.md#set_storage_soe_api_v1_storage_soe_post) | **POST** /api/v1/storage/soe | Set Storage Soe
*DefaultApi* | [**system_status_api_v1_status_get**](span_panel/client/docs/DefaultApi.md#system_status_api_v1_status_get) | **GET** /api/v1/status | System Status


## Documentation For Models

 - [AllowedEndpointGroups](span_panel/client/docs/AllowedEndpointGroups.md)
 - [AuthIn](span_panel/client/docs/AuthIn.md)
 - [AuthOut](span_panel/client/docs/AuthOut.md)
 - [BatteryStorage](span_panel/client/docs/BatteryStorage.md)
 - [BodySetCircuitStateApiV1CircuitsCircuitIdPost](span_panel/client/docs/BodySetCircuitStateApiV1CircuitsCircuitIdPost.md)
 - [BooleanIn](span_panel/client/docs/BooleanIn.md)
 - [Branch](span_panel/client/docs/Branch.md)
 - [Circuit](span_panel/client/docs/Circuit.md)
 - [CircuitNameIn](span_panel/client/docs/CircuitNameIn.md)
 - [CircuitsOut](span_panel/client/docs/CircuitsOut.md)
 - [Client](span_panel/client/docs/Client.md)
 - [Clients](span_panel/client/docs/Clients.md)
 - [DoorState](span_panel/client/docs/DoorState.md)
 - [FeedthroughEnergy](span_panel/client/docs/FeedthroughEnergy.md)
 - [HTTPValidationError](span_panel/client/docs/HTTPValidationError.md)
 - [IslandingState](span_panel/client/docs/IslandingState.md)
 - [MainMeterEnergy](span_panel/client/docs/MainMeterEnergy.md)
 - [NetworkStatus](span_panel/client/docs/NetworkStatus.md)
 - [NiceToHaveThreshold](span_panel/client/docs/NiceToHaveThreshold.md)
 - [PanelMeter](span_panel/client/docs/PanelMeter.md)
 - [PanelPower](span_panel/client/docs/PanelPower.md)
 - [PanelState](span_panel/client/docs/PanelState.md)
 - [Priority](span_panel/client/docs/Priority.md)
 - [PriorityIn](span_panel/client/docs/PriorityIn.md)
 - [RelayState](span_panel/client/docs/RelayState.md)
 - [RelayStateIn](span_panel/client/docs/RelayStateIn.md)
 - [RelayStateOut](span_panel/client/docs/RelayStateOut.md)
 - [SoftwareStatus](span_panel/client/docs/SoftwareStatus.md)
 - [StateOfEnergy](span_panel/client/docs/StateOfEnergy.md)
 - [StatusOut](span_panel/client/docs/StatusOut.md)
 - [SystemStatus](span_panel/client/docs/SystemStatus.md)
 - [ValidationError](span_panel/client/docs/ValidationError.md)
 - [WifiAccessPoint](span_panel/client/docs/WifiAccessPoint.md)
 - [WifiConnectIn](span_panel/client/docs/WifiConnectIn.md)
 - [WifiConnectOut](span_panel/client/docs/WifiConnectOut.md)
 - [WifiScanOut](span_panel/client/docs/WifiScanOut.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication


## Author




