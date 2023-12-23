# This file contains a schema for all supported sensors, binary sensors and
# inputs of the OpenThermGW component.

from typing import Dict, Generic, Tuple, TypeVar, TypedDict, NotRequired

from esphome.const import (
    UNIT_CELSIUS,
    UNIT_PERCENT,
    DEVICE_CLASS_COLD,
    DEVICE_CLASS_HEAT,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_PROBLEM,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_WATER,    
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_NONE,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
)

T = TypeVar("T")
class Schema(Generic[T], Dict[str, T]):
    pass

class EntitySchema(TypedDict):
    description: str
    """Description of the item, based on the OpenTherm spec"""

    message: str
    """OpenTherm message id used to read or write the value"""    

    message_data: str
    """Instructions on how to interpret the data in the message
      - flag8_[hb|lb]_[0-7]: data is a byte of single bit flags, 
                             this flag is set in the high (hb) or low byte (lb),
                             at position 0 to 7
      - u8_[hb|lb]: data is an unsigned 8-bit integer, 
                    in the high (hb) or low byte (lb)
      - s8_[hb|lb]: data is an signed 8-bit integer, 
                    in the high (hb) or low byte (lb)
      - f88: data is a signed fixed point value with 
              1 sign bit, 7 integer bits, 8 fractional bits
      - u16: data is an unsigned 16-bit integer
      - s16: data is a signed 16-bit integer
    """

    init: bool
    """Whether the value should be read from boiler during the initialization phase
      Keep it to false for values written by thermostat      
    """

    update_time: int
    """Time in seconds for periodic updates (keep it to -1 for values written by thermostat)      
      When -1, read requests are sent by the thermostat at it's own rate
    """

class SensorSchema(EntitySchema):
    unit_of_measurement: NotRequired[str]
    accuracy_decimals: int
    device_class: NotRequired[str]
    icon: NotRequired[str]
    state_class: str

SENSORS: Schema[SensorSchema] = Schema({
    "fault_oem": SensorSchema({
        "description": "Fault: OEM Fault code",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "accuracy_decimals": 0,
        "icon": "mdi:water-boiler-alert",
        "state_class": STATE_CLASS_NONE,  
        "message": "ASFflags",
        "message_data": "u8_lb",
        "init": True,
        "update_time": 60,
    }),    
    "t_set": SensorSchema({
        "description": "Temperature setpoint for the boiler's supply water",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TSet",
        "message_data": "f88",
        "init": False,
        "update_time": -1,
    }),
    "tr_override": SensorSchema({
        "description": "Remote override room setpoint",
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_EMPTY,
        "state_class": STATE_CLASS_NONE,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "message": "TrOverride",
        "message_data": "f88",
        "init": True,
        "update_time": -1,
    }),
    "t_set_ch2": SensorSchema({
	"description": "Control setpoint 2: temperature setpoint for the boiler's supply water on the second heating circuit",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TsetCH2",
        "message_data": "f88",
        "init": False,
        "update_time": -1,        
    }),
    "t_set_dhw": SensorSchema({
        "description": "Domestic hot water temperature setpoint (°C)",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "description": "Domestic hot water temperature setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TdhwSet",
        "message_data": "f88",
        "init": True,
        "update_time": 300,
    }),
    "diag_oem": SensorSchema({
        "description": "An OEM-specific diagnostic/service code",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "accuracy_decimals": 0,
        "icon": "mdi:water-boiler-alert",
        "state_class": STATE_CLASS_NONE,  
        "message": "OEMDiagnosticCode",
        "message_data": "u16",
        "init": True,
        "update_time": 300,
    }),    
    "master_ot_version": SensorSchema({
        "description": "OpenTherm version Master",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "accuracy_decimals": 1,
	"icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,   
        "message": "OpenThermVersionMaster",
        "message_data": "f88",
        "init": False,
        "update_time": -1,
    }),
    "slave_ot_version": SensorSchema({
        "description": "OpenTherm version Slave",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 1,
        "message": "OpenThermVersionSlave",
        "message_data": "f88",
        "init": True,
        "update_time": -1,        
    }),
    "t_roomset": SensorSchema({
        "description": "Current room temperature setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TrSet",
        "message_data": "f88",
        "init": False,
        "update_time": -1,
    }),
    "pc_relmod": SensorSchema({
        "description": "Relative Modulation Level (%)",
        "unit_of_measurement": UNIT_PERCENT,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_EMPTY,
        "state_class": STATE_CLASS_NONE,
        "message": "RelModLevel",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),   
    "bar_chpress": SensorSchema({
        "description": "Water pressure in CH circuit (bar)",
        "unit_of_measurement": "bar",
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_PRESSURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "CHPressure",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),   
    "ls_dhwflowrate": SensorSchema({
        "description": "Water flow rate in DHW circuit. (litres/minute)",
        "unit_of_measurement": "l/s",
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_WATER,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "DHWFlowRate",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),       
    "t_room": SensorSchema({
        "description": "Room temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tr",
        "message_data": "f88",
        "init": False,
        "update_time": -1,        
    }),
    "t_boiler": SensorSchema({
        "description": "Boiler water temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tboiler",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),
    "t_dhw": SensorSchema({
        "description": "DHW temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tdhw",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),
    "t_outside": SensorSchema({
        "description": "Outside temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Toutside",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),
    "t_ret": SensorSchema({
        "description": "Return water temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tret",
        "message_data": "f88",
        "init": True,
        "update_time": 60,        
    }),    
    "t_exhaust": SensorSchema({
        "description": "Exhaust temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Texhaust",
        "message_data": "s16",
        "init": True,
        "update_time": 60,        
    }),        
    "t_dhw_set_ub": SensorSchema({
        "description": "Upper bound for adjustment of DHW setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TdhwSetUBTdhwSetLB",
        "message_data": "s8_hb",
        "init": True,
        "update_time": -1,        
    }),
    "t_dhw_set_lb": SensorSchema({
        "description": "Lower bound for adjustment of DHW setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TdhwSetUBTdhwSetLB",
        "message_data": "s8_lb",
        "init": True,
        "update_time": -1,        
    }),
    "max_t_set_ub": SensorSchema({
        "description": "Upper bound for adjustment of max CH setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSetUBMaxTSetLB",
        "message_data": "s8_hb",
        "init": True,
        "update_time": -1,        
    }),
    "max_t_set_lb": SensorSchema({
        "description": "Lower bound for adjustment of max CH setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSetUBMaxTSetLB",
        "message_data": "s8_lb",
        "init": True,
        "update_time": -1,        
    }),
    "max_t_set": SensorSchema({
        "description": "Maximum allowable CH water setpoint (°C)",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSet",
        "message_data": "f88",
        "init": True,
        "update_time": -1,        
    }),    
    "nb_startburner": SensorSchema({
        "description": "Number of starts burner",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:fire",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "BurnerStarts",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_startchpump": SensorSchema({
        "description": "Number of starts CH pump",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:water-pump",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "CHPumpStarts",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_startdhwpump": SensorSchema({
        "description": "Number of starts DHW pump/valve",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:water-pump",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "DHWPumpValveStarts",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_burnerhours": SensorSchema({
        "description": "Number of hours that burner is in operation (i.e. flame on)",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:fire",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "BurnerOperationHours",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_chpumphours": SensorSchema({
        "description": "Number of hours that CH pump has been running",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:water-pump",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "CHPumpOperationHours",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_dhwpumphours": SensorSchema({
        "description": "Number of hours that DHW pump has been running or DHW valve has been opened",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:water-pump",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "DHWPumpValveOperationHours",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),   
    "nb_dhwburnerhours": SensorSchema({
        "description": "Number of hours that burner is in operation during DHW mode",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:fire",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "DHWBurnerOperationHours",
        "message_data": "u16",
        "init": True,
        "update_time": -1,
    }),       
    "master_memberid": SensorSchema({
        "description": "MemberID code of the master",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "MConfigMMemberIDcode",
        "message_data": "u8_lb",
        "init": False,
        "update_time": -1,        
    }),   
    "slave_memberid": SensorSchema({
        "description": "MemberID code of the slave",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "SConfigSMemberIDcode",
        "message_data": "u8_lb",
        "init": True,
        "update_time": -1,        
    }),   
    
    "Unknown99": SensorSchema({
        "description": "Unknown99",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown99",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    
    "Unknown140": SensorSchema({
        "description": "Unknown140",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown140",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown141": SensorSchema({
        "description": "Unknown141",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 3,
        "message": "Unknown141",
        "message_data": "f88",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown142": SensorSchema({
        "description": "Unknown142",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown142",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown143": SensorSchema({
        "description": "Unknown143",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown143",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown144": SensorSchema({
        "description": "Unknown144",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown144",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown145": SensorSchema({
        "description": "Unknown145",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown145",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown146": SensorSchema({
        "description": "Unknown146",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown146",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown147": SensorSchema({
        "description": "Unknown147",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 3,
        "message": "Unknown147",
        "message_data": "f88",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown148": SensorSchema({
        "description": "Unknown148",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown148",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown149": SensorSchema({
        "description": "Unknown149",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown149",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown150": SensorSchema({
        "description": "Unknown150",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown150",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown151": SensorSchema({
        "description": "Unknown151",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown151",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),   
    "Unknown152": SensorSchema({
        "description": "Unknown152",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 3,
        "message": "Unknown152",
        "message_data": "f88",
        "init": True,
        "update_time": -1,        
    }),       
    
    "Unknown161": SensorSchema({
        "description": "Unknown161",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown161",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),       
    
    "Unknown180": SensorSchema({
        "description": "Unknown180",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,        
        "icon": "mdi:tag",
        "state_class": STATE_CLASS_NONE,
        "accuracy_decimals": 0,
        "message": "Unknown180",
        "message_data": "u16",
        "init": True,
        "update_time": -1,        
    }),       
})

class SwitchSchema(EntitySchema):
    device_class: NotRequired[str]
    icon: NotRequired[str]
    entity_category: NotRequired[str]

SWITCHES: Schema[SwitchSchema] = Schema({
    "ch_enable": SwitchSchema({
        "description": "Central Heating enabled",
        "message": "Status",
        "message_data": "flag8_hb_0",
        "init": False,
        "update_time": -1,        
    }),
    "dhw_enable": SwitchSchema({
        "description": "Domestic Hot Water enabled",
        "message": "Status",
        "message_data": "flag8_hb_1",
        "init": False,
        "update_time": -1,        
    }),
    "cooling_enable": SwitchSchema({
        "description": "Cooling enabled",
        "message": "Status",
        "message_data": "flag8_hb_2",
        "init": False,
        "update_time": -1,        
    }),
    "otc_active": SwitchSchema({
        "description": "Outside temperature compensation active",
        "message": "Status",
        "message_data": "flag8_hb_3",        
        "init": False,
        "update_time": -1,        
    }),
    "ch2_active": SwitchSchema({
        "description": "Central Heating 2 active",
        "message": "Status",
        "message_data": "flag8_hb_4",
        "init": False,
        "update_time": -1,        
    }),
})

class BinarySensorSchema(EntitySchema):
    device_class: NotRequired[str]
    icon: NotRequired[str]
    entity_category: NotRequired[str]

BINARY_SENSORS: Schema[BinarySensorSchema] = Schema({
#    "ch_enable": BinarySensorSchema({
#        "description": "Central Heating enabled",
#        "message": "Status",
#        "message_data": "flag8_hb_0",
#        "init": False,
#        "update_time": -1,        
#    }),
#    "dhw_enable": BinarySensorSchema({
#        "description": "Domestic Hot Water enabled",
#        "message": "Status",
#        "message_data": "flag8_hb_1",
#        "init": False,
#        "update_time": -1,        
#    }),
#    "cooling_enable": BinarySensorSchema({
#        "description": "Cooling enabled",
#        "message": "Status",
#        "message_data": "flag8_hb_2",
#        "init": False,
#        "update_time": -1,        
#    }),
#    "otc_active": BinarySensorSchema({
#        "description": "Outside temperature compensation active",
#        "message": "Status",
#        "message_data": "flag8_hb_3",        
#        "init": False,
#        "update_time": -1,        
#    }),
#    "ch2_active": BinarySensorSchema({
#        "description": "Central Heating 2 active",
#        "message": "Status",
#        "message_data": "flag8_hb_4",
#        "init": False,
#        "update_time": -1,        
#    }),


    "fault_indication": BinarySensorSchema({
        "description": "Status: Fault indication",
        "device_class": DEVICE_CLASS_PROBLEM,
        "icon": "mdi:water-boiler-alert",
        "message": "Status",
        "message_data": "flag8_lb_0",
        "init": True,
        "update_time": -1,        
    }),
    "ch_active": BinarySensorSchema({
        "description": "Status: Central Heating active",
        "device_class": DEVICE_CLASS_EMPTY,
        "icon": "mdi:radiator",
        "message": "Status",
        "message_data": "flag8_lb_1",
        "init": True,
        "update_time": -1,        
    }),
    "dhw_active": BinarySensorSchema({
        "description": "Status: Domestic Hot Water active",
        "device_class": DEVICE_CLASS_EMPTY,
        "icon": "mdi:faucet",
        "message": "Status",
        "message_data": "flag8_lb_2",
        "init": True,
        "update_time": -1,        
    }),
    "flame_on": BinarySensorSchema({
        "description": "Status: Flame on",
        "device_class": DEVICE_CLASS_EMPTY,
        "icon": "mdi:fire",
        "message": "Status",
        "message_data": "flag8_lb_3",
        "init": True,
        "update_time": -1,        
    }),
    "cooling_active": BinarySensorSchema({
        "description": "Status: Cooling active",
        "device_class": DEVICE_CLASS_EMPTY,
        "message": "Status",
        "message_data": "flag8_lb_4",
        "init": True,
        "update_time": -1,
    }),
    "ch2_active": BinarySensorSchema({
        "description": "Status: Central Heating 2 active",
        "device_class": DEVICE_CLASS_EMPTY,
        "icon": "mdi:radiator",
        "message": "Status",
        "message_data": "flag8_lb_5",
        "init": True,
        "update_time": -1,
    }),
    "diagnostic_indication": BinarySensorSchema({
        "description": "Status: Diagnostic event",
        "device_class": DEVICE_CLASS_PROBLEM,
        "message": "Status",
        "message_data": "flag8_lb_6",
        "init": True,
        "update_time": -1,
    }),
    "fault_service": BinarySensorSchema({
        "description": "Fault: Service required",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:wrench",
        "message": "ASFflags",
        "message_data": "flag8_hb_0",
        "init": True,
        "update_time": 60,
    }),
    "fault_lockout": BinarySensorSchema({
        "description": "Fault: Lockout reset enabled",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:wrench",
        "message": "ASFflags",
        "message_data": "flag8_hb_1",
        "init": True,
        "update_time": 60,
    }),
    "fault_waterpress": BinarySensorSchema({
        "description": "Fault: Water pressure fault",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:water-alert",
        "message": "ASFflags",
        "message_data": "flag8_hb_2",
        "init": True,
        "update_time": 60,
    }),
    "fault_gasflame": BinarySensorSchema({
        "description": "Fault: Gas/flame fault",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:fire",        
        "message": "ASFflags",
        "message_data": "flag8_hb_3",
        "init": True,
        "update_time": 60,
    }),
    "fault_airpress": BinarySensorSchema({
        "description": "Fault: Air pressure fault",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "message": "ASFflags",
        "message_data": "flag8_hb_4",
        "init": True,
        "update_time": 60,
    }),
    "fault_watertemp": BinarySensorSchema({
        "description": "Fault: Water over-temp fault",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:water-thermometer",
        "message": "ASFflags",
        "message_data": "flag8_hb_5",
        "init": True,
        "update_time": 60,
    }),    
    "fault_watertemp": BinarySensorSchema({
        "description": "Fault: Water over-temp fault",
        "device_class": DEVICE_CLASS_PROBLEM,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:water-thermometer",
        "message": "ASFflags",
        "message_data": "flag8_hb_5",
        "init": True,
        "update_time": 60,
    }),    
    "func_manualoverridepriority": BinarySensorSchema({
        "description": "Remote override manual change priority",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "message": "RemoteOverrideFunction",
        "message_data": "flag8_lb_0",
        "init": True,
        "update_time": 300,
    }),
    "func_programoverridepriority": BinarySensorSchema({
        "description": "Remote override program change priority",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "message": "RemoteOverrideFunction",
        "message_data": "flag8_lb_1",
        "init": True,
        "update_time": 300,
    }),
})

class TextSensorSchema(EntitySchema):
    device_class: NotRequired[str]
    icon: NotRequired[str]
    entity_category: NotRequired[str]

TEXT_SENSORS: Schema[TextSensorSchema] = Schema({
    "time_date": SensorSchema({
        "description": "Time & Date",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:calendar-clock-outline",
        "message": "DayTime",
        "message_data": "str_date",
        "init": True,
        "update_time": -1,
    }),
    "dhw_present": SensorSchema({
        "description": "Config: Domestic Hot Water",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:faucet",
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_0_str",
        "init": True,
        "update_time": 300,
    }),    
    "control_type": SensorSchema({
        "description": "Config: Control type",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_1_str",
        "init": True,
        "update_time": 300,
    }),
    "cooling_supported": SensorSchema({
        "description": "Config: Cooling supported",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:snowflake",        
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_2_str",
        "init": True,
        "update_time": 300,
    }),
    "dhw_config": SensorSchema({
        "description": "Config: Domestic Hot Water instantaneous/not specified or storage tank",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "icon": "mdi:water-boiler",        
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_3_str",
        "init": True,
        "update_time": 300,
    }),
    "lowoff_pumpcontrol_allowed": SensorSchema({
        "description": "Config: Master low-off&pump control function",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_4_str",
        "init": True,
        "update_time": 300,
    }),
    "ch2_present": SensorSchema({
        "description": "Config: CH2 present",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
	"icon": "mdi:water-boiler",
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_5_str",
        "init": True,
        "update_time": 300,
    }),        
    "ch2_present": SensorSchema({
        "description": "Config: CH2 present",
        "device_class": DEVICE_CLASS_EMPTY,
        "entity_category": ENTITY_CATEGORY_DIAGNOSTIC,
	"icon": "mdi:water-boiler",
        "message": "SConfigSMemberIDcode",
        "message_data": "flag8_hb_5_str",
        "init": True,
        "update_time": 300,
    }),        
})    

class AutoConfigure(TypedDict):
    message: str
    message_data: str
    
class InputSchema(EntitySchema):
    unit_of_measurement: str
    range: Tuple[int, int]
    auto_max_value: NotRequired[AutoConfigure]
    auto_min_value: NotRequired[AutoConfigure]

INPUTS: Schema[InputSchema] = Schema({
    "t_set": InputSchema({
        "description": "Control setpoint: temperature setpoint for the boiler's supply water",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TSet",
        "message_data": "f88",
        "range": (0, 100),
        "auto_max_value": { "message": "MaxTSet", "message_data": "f88" },
    }),
    "t_set_ch2": InputSchema({
        "description": "Control setpoint 2: temperature setpoint for the boiler's supply water on the second heating circuit",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TsetCH2",
        "message_data": "f88",
        "range": (0, 100),
        "auto_max_value": { "message": "MaxTSet", "message_data": "f88" },
    }),
    "cooling_control": InputSchema({
        "description": "Cooling control signal",
        "unit_of_measurement": UNIT_PERCENT,
        "message": "CoolingControl",
        "message_data": "f88",
        "range": (0, 100),
    }),
    "t_dhw_set": InputSchema({
        "description": "Domestic hot water temperature setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TdhwSet",
        "message_data": "f88",
        "range": (0, 127),
        "auto_min_value": { "message": "TdhwSetUBTdhwSetLB", "message_data": "s8_lb" },
        "auto_max_value": { "message": "TdhwSetUBTdhwSetLB", "message_data": "s8_hb" },
    }),
    "max_t_set": InputSchema({
        "description": "Maximum allowable CH water setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "MaxTSet",
        "message_data": "f88",
        "range": (0, 127),
        "auto_min_value": { "message": "MaxTSetUBMaxTSetLB", "message_data": "s8_lb" },
        "auto_max_value": { "message": "MaxTSetUBMaxTSetLB", "message_data": "s8_hb" },
    }),
    "t_room_set": InputSchema({
        "description": "Current room temperature setpoint (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TrSet",
        "message_data": "f88",
        "range": (-40, 127),
    }),
    "t_room_set_ch2": InputSchema({
        "description": "Current room temperature setpoint on CH2 (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "TrSetCH2",
        "message_data": "f88",
        "range": (-40, 127),
    }),
    "t_room": InputSchema({
        "description": "Current sensed room temperature (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "message": "Tr",
        "message_data": "f88",
        "range": (-40, 127),
    }),
})
