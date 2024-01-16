import aiohttp
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


async def get_vehicles() -> list:
    """ Returns information for all WTA vehicles. """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.ridewta.com/vehicles") as response:
            
            if response.status != 200:
                print(f"Error grabbing vehicles from WTA's API - STATUS CODE {response.status}")
                return []

            response_text = await response.text()
            response_obj = json.loads(response_text, object_hook = lambda d: Namespace(**d))

            return response_obj.vehicles
        

async def get_vehicle_info(vehicle_id: str) -> Namespace | None:
    """
    Gets information about a specific WTA vehicle
    
    Args:
        vehicle_id (str): ID of the vehicle
    
    Returns:
        Namespace: Namespace containing the information for the vehicle
        None: Nonetype, usually is the result of an error or bad status code
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.ridewta.com/vehicles/{vehicle_id}") as response:
            
            if response.status != 200:
                print(f"Error grabbing information for vehicle {vehicle_id} - STATUS CODE {response.status}")
                return None
            
            response_text = await response.text()
            response_obj = json.loads(response_text, object_hook = lambda d: Namespace(**d))

            return response_obj.vehicles[0]
        

async def get_vehicle_by_route(route_number: str) -> Namespace | None:
    """
    Gets vehicle information based off a specified route number

    Args:
        route_number (str): Route number to find the vehicle by
    
    Returns:
        Namespace: Namespace containing the information for the vehicle
        None: Nonetype, usually is the result of an error or bad status code
    """

    vehicles = await get_vehicles()

    if len(vehicles) == 0:
        return None

    for vehicle in vehicles:
        if vehicle.routeNumber != route_number:
            continue

        return vehicle
        
    return None


async def get_vehicle_predictions(vehicle_id: str) -> list:
    """
    Gets upcoming arrivals for a specified vehicle. If data is available,
    the function will return up to the next 3 predicted arrivals.

    Args:
        vehicle_id (str): ID of the vehicle
    
    Returns:
        list: List of predicted bus arrivals
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.ridewta.com/vehicles/{vehicle_id}/predictions") as response:
            
            if response.status != 200:
                print(f"Error grabbing vehicle predictions for {vehicle_id} - STATUS CODE {response.status}")
                return []
            
            response_text = await response.text()
            response_text = response_text[20:-1]

            response_obj = json.loads(response_text, object_hook = lambda d: Namespace(**d))

            return response_obj.prd


async def get_vehicle_history(vehicle_id: str, timestamp: int):
    """
    Gets the history of a vehicle for the day specified by the timestamp.
    Not currently implemented.

    Args:
        vehicle_id (str): ID of the vehicle
        timestamp (int): Unix Timestamp in milliseconds
    """

    # TODO: This is unimplemented for the time being due to not really being
    #       able to test the actual functionality of it because the API
    #       keeps returning null no matter the timestamp or vehicle provided.

    raise NotImplementedError