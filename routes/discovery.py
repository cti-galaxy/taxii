from fastapi import APIRouter
from fastapi.responses import JSONResponse

from controllers.discovery import Discovery

from config.schema.taxii import DiscoveryModel, APIRootModel, \
    StatusModel, ErrorMessageModel

MEDIA_TYPE = "application/taxii+json;version=2.1"

router = APIRouter()


@router.get("/taxii2",
            response_model=DiscoveryModel,
            responses={500: {"model": ErrorMessageModel}},
            summary="Get information about the TAXII Server and any advertised API Roots",
            tags=["Discovery"])
async def roots_discovery():
    """
    Defines TAXII API - Server Information:
    Server Discovery section (4.1) `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107526>`__

    Returns:
        discovery: A Discovery Resource upon successful requests. Additional information
        `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107527>`__.

    """
    response = Discovery.roots_discovery()
    if response.get('error_code'):
        return JSONResponse(status_code=int(response.get('error_code')), content=response)
    else:
        return JSONResponse(status_code=200, media_type=MEDIA_TYPE, content=response)


@router.get("/{api_root}/status/{status_id}",
            response_model=StatusModel,
            responses={500: {"model": ErrorMessageModel}},
            summary="Get status information for a specific status ID",
            tags=["Discovery"])
async def get_status(api_root: str, status_id: str):
    """
    Defines TAXII API - Server Information:
    Get Status section (4.3) `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107530>`__

    Args:
        api_root (str): the base URL of the API Root
        status_id (str): the `identifier` of the Status message being requested

    Returns:
        status: A Status Resource upon successful requests. Additional information
        `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107531>`__.

    """
    response = Discovery.get_status(api_root, status_id)
    if response.get('error_code'):
        return JSONResponse(status_code=int(response.get('error_code')), content=response)
    else:
        return JSONResponse(status_code=200, media_type=MEDIA_TYPE, content=response)


@router.get("/{api_root}",
            response_model=APIRootModel,
            responses={500: {"model": ErrorMessageModel}},
            summary="Get information about a specific API Root",
            tags=["Discovery"])
async def get_api_root_information(api_root: str):
    """
    Defines TAXII API - Server Information:
    Get API Root Information section (4.2) `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107528>`__

    Args:
        api_root (str): the base URL of the API Root

    Returns:
        api-root: An API Root Resource upon successful requests. Additional information
        `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107529>`__.

    """
    response = Discovery.get_api_root_information(api_root)
    if response.get('error_code'):
        return JSONResponse(status_code=int(response.get('error_code')), content=response)
    else:
        return JSONResponse(status_code=200, media_type=MEDIA_TYPE, content=response)


@router.get("/",
            response_model=APIRootModel,
            responses={500: {"model": ErrorMessageModel}},
            summary="Get information about the Default API Root",
            tags=["Discovery"])
async def get_default_root_information():
    """
    Defines TAXII API - Server Information:
    Get Default API Root Information section (4.2) `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107528>`__

    Returns:
        api-root: An API Root Resource upon successful requests. Additional information
        `here <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107529>`__.

    """
    response = Discovery.get_default_root_information()
    if response.get('error_code'):
        return JSONResponse(status_code=int(response.get('error_code')), content=response)
    else:
        return JSONResponse(status_code=200, media_type=MEDIA_TYPE, content=response)
