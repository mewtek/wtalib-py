import asyncio
import pytest

from wtalib import vehicles


@pytest.mark.asyncio
async def test_get_vehicles():
    v = await vehicles.get_vehicles()

    assert len(v) > 0

@pytest.mark.asyncio
async def test_get_vehicle_info():
    v = await vehicles.get_vehicle_info("801")

    assert v.vehicleType == "bus"

@pytest.mark.asyncio
async def test_get_vehicle_by_route():
    v = await vehicles.get_vehicle_by_route("190")

    assert v != None

@pytest.mark.asyncio
async def test_get_vehicle_predictions():
    # This test will fail if we choose a vehicle without a route,
    # lets find one that does
    v_list = await vehicles.get_vehicles()
    v = str()

    for vehicle in v_list:
        if vehicle.routeNumber == "":
            continue

        v = vehicle.vehicle
        break

    predictions = await vehicles.get_vehicle_predictions(v)

    assert len(predictions) >= 3
