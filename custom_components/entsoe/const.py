from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Callable
from homeassistant.helpers.selector import SelectOptionDict

from homeassistant.components.sensor import SensorEntityDescription, SensorDeviceClass
from homeassistant.const import (
    CURRENCY_EURO,
    ENERGY_KILO_WATT_HOUR,
    PERCENTAGE,
)
from homeassistant.helpers.typing import StateType

ATTRIBUTION = "Data provided by ENTSO-e Transparency Platform"
DOMAIN = "entsoe"
ICON = "mdi:currency-eur"
UNIQUE_ID = f"{DOMAIN}_component"
COMPONENT_TITLE = "ENTSO-e Transparency Platform"
CONF_API_KEY = "api_key"
CONF_AREA = "area"
CONF_COORDINATOR = "coordinator"
CONF_ADDITIONAL = "additional_cost"
DEFAULT_TEMPLATE = "{{0.0|float}}"

# Commented ones are not working at entsoe
TARGET_AREA_OPTIONS = [
    # SelectOptionDict(value="AL", label="Albania"),
    SelectOptionDict(value="AT", label="Austria"),
    SelectOptionDict(value="BE", label="Belgium"),
    # SelectOptionDict(value="BA", label="Bosnia and Herz."),
    SelectOptionDict(value="BG", label="Bulgaria"),
    SelectOptionDict(value="HR", label="Croatia"),
    # SelectOptionDict(value="CY", label="Cyprus"),
    SelectOptionDict(value="CZ", label="Czech Republic"),
    SelectOptionDict(value="DK_1", label="Denmark Eastern (DK1)"),
    SelectOptionDict(value="DK_2", label="Denmark Western (DK2)"),
    SelectOptionDict(value="EE", label="Estonia"),
    SelectOptionDict(value="FI", label="Finland"),
    SelectOptionDict(value="FR", label="France"),
    # SelectOptionDict(value="GE", label="Georgia"),
    SelectOptionDict(value="DE_LU", label="Luxembourg"),
    SelectOptionDict(value="DE_LU", label="Germany"),
    SelectOptionDict(value="GR", label="Greece"),
    SelectOptionDict(value="HU", label="Hungary"),
    # SelectOptionDict(value="IE", label="Ireland"),
    SelectOptionDict(value="IT_CNOR", label="Italy Centre North"),
    SelectOptionDict(value="IT_CSUD", label="Italy Centre South"),
    SelectOptionDict(value="IT_NORD", label="Italy North"),
    SelectOptionDict(value="IT_SUD", label="Italy South"),
    SelectOptionDict(value="IT_SICI", label="Italy Sicilia"),
    SelectOptionDict(value="IT_SARD", label="Italy Sardinia"),
    # SelectOptionDict(value="XK", label="Kosovo"),
    SelectOptionDict(value="LV", label="Latvia"),
    SelectOptionDict(value="LT", label="Lithuania"),
    # SelectOptionDict(value="MT", label="Malta"),
    # SelectOptionDict(value="MD", label="Moldova"),
    # SelectOptionDict(value="ME", label="Montenegro"),
    SelectOptionDict(value="NL", label="Netherlands"),
    # SelectOptionDict(value="MK", label="North Macedonia"),
    SelectOptionDict(value="NO_1", label="Norway Oslo (NO1"),
    SelectOptionDict(value="NO_2", label="Norway Kr.Sand (NO2)"),
    SelectOptionDict(value="NO_3", label="Norway Tr.heim (NO3)"),
    SelectOptionDict(value="NO_4", label="Norway Tromsø (NO4)"),
    SelectOptionDict(value="NO_5", label="Norway Bergen (NO5"),
    SelectOptionDict(value="PL", label="Poland"),
    SelectOptionDict(value="PT", label="Portugal"),
    SelectOptionDict(value="RO", label="Romania"),
    SelectOptionDict(value="RS", label="Serbia"),
    SelectOptionDict(value="SK", label="Slovakia"),
    SelectOptionDict(value="SI", label="Slovenia"),
    SelectOptionDict(value="ES", label="Spain"),
    SelectOptionDict(value="SE_1", label="Sweden Luleå (SE1)"),
    SelectOptionDict(value="SE_2", label="Sweden Sundsvall (SE2)"),
    SelectOptionDict(value="SE_3", label="Sweden Stockholm (SE3)"),
    SelectOptionDict(value="SE_4", label="Sweden Malmö (SE4)"),
    SelectOptionDict(value="CH", label="Switzerland"),
    # SelectOptionDict(value="TR", label="Turkey"),
    # SelectOptionDict(value="UA", label="Ukraine"),
    SelectOptionDict(value="UK", label="United Kingdom"),
]


@dataclass
class EntsoeEntityDescription(SensorEntityDescription):
    """Describes ENTSO-e sensor entity."""

    value_fn: Callable[[dict], StateType] = None


SENSOR_TYPES: tuple[EntsoeEntityDescription, ...] = (
    EntsoeEntityDescription(
        key="current_price",
        name="Current electricity market price",
        native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        value_fn=lambda data: data["current_price"],
    ),
    EntsoeEntityDescription(
        key="next_hour_price",
        name="Next hour electricity market price",
        native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        value_fn=lambda data: data["next_hour_price"],
    ),
    EntsoeEntityDescription(
        key="min_price",
        name="Lowest energy price today",
        native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        value_fn=lambda data: data["min_price"],
    ),
    EntsoeEntityDescription(
        key="max_price",
        name="Highest energy price today",
        native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        value_fn=lambda data: data["max_price"],
    ),
    EntsoeEntityDescription(
        key="avg_price",
        name="Average electricity price today",
        native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        value_fn=lambda data: data["avg_price"],
    ),
    EntsoeEntityDescription(
        key="percentage_of_max",
        name="Current percentage of highest electricity price today",
        native_unit_of_measurement=f"{PERCENTAGE}",
        icon="mdi:percent",
        value_fn=lambda data: round(
            data["current_price"] / data["max_price"] * 100, 1
        ),
    ),
    EntsoeEntityDescription(
        key="highest_price_time_today",
        name="Time of highest price today",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda data: data["time_max"],
    ),
    EntsoeEntityDescription(
        key="lowest_price_time_today",
        name="Time of lowest price today",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda data: data["time_min"],
    ),
)
