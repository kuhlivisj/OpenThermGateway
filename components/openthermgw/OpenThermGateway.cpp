#include "OpenThermGateway.h"
#include "esphome/core/log.h"
 
namespace esphome { 
namespace message_data {
    bool parse_flag8_lb_0(const unsigned long response) { return response & 0b0000000000000001; }
    bool parse_flag8_lb_1(const unsigned long response) { return response & 0b0000000000000010; }
    bool parse_flag8_lb_2(const unsigned long response) { return response & 0b0000000000000100; }
    bool parse_flag8_lb_3(const unsigned long response) { return response & 0b0000000000001000; }
    bool parse_flag8_lb_4(const unsigned long response) { return response & 0b0000000000010000; }
    bool parse_flag8_lb_5(const unsigned long response) { return response & 0b0000000000100000; }
    bool parse_flag8_lb_6(const unsigned long response) { return response & 0b0000000001000000; }
    bool parse_flag8_lb_7(const unsigned long response) { return response & 0b0000000010000000; }
    bool parse_flag8_hb_0(const unsigned long response) { return response & 0b0000000100000000; }
    bool parse_flag8_hb_1(const unsigned long response) { return response & 0b0000001000000000; }
    bool parse_flag8_hb_2(const unsigned long response) { return response & 0b0000010000000000; }
    bool parse_flag8_hb_3(const unsigned long response) { return response & 0b0000100000000000; }
    bool parse_flag8_hb_4(const unsigned long response) { return response & 0b0001000000000000; }
    bool parse_flag8_hb_5(const unsigned long response) { return response & 0b0010000000000000; }
    bool parse_flag8_hb_6(const unsigned long response) { return response & 0b0100000000000000; }
    bool parse_flag8_hb_7(const unsigned long response) { return response & 0b1000000000000000; }

    std::string get_flag_str_value(esphome::text_sensor::TextSensor* sensor, bool bActive)
    {
    	if(bActive)
    		return "ON";
	else
    		return "OFF";
    }
    std::string parse_flag8_lb_0_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_0(response)); }
    std::string parse_flag8_lb_1_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_1(response)); }
    std::string parse_flag8_lb_2_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_2(response)); }
    std::string parse_flag8_lb_3_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_3(response)); }
    std::string parse_flag8_lb_4_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_4(response)); }
    std::string parse_flag8_lb_5_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_5(response)); }
    std::string parse_flag8_lb_6_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_6(response)); }
    std::string parse_flag8_lb_7_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_lb_7(response)); }
    std::string parse_flag8_hb_0_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_0(response)); }
    std::string parse_flag8_hb_1_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_1(response)); }
    std::string parse_flag8_hb_2_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_2(response)); }
    std::string parse_flag8_hb_3_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_3(response)); }
    std::string parse_flag8_hb_4_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_4(response)); }
    std::string parse_flag8_hb_5_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_5(response)); }
    std::string parse_flag8_hb_6_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_6(response)); }
    std::string parse_flag8_hb_7_str(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return get_flag_str_value(sensor, parse_flag8_hb_7(response)); }

    uint8_t parse_u8_lb(const unsigned long response) { return (uint8_t) (response & 0xff); }
    uint8_t parse_u8_hb(const unsigned long response) { return (uint8_t) ((response >> 8) & 0xff); }
    int8_t parse_s8_lb(const unsigned long response) { return (int8_t) (response & 0xff); }
    int8_t parse_s8_hb(const unsigned long response) { return (int8_t) ((response >> 8) & 0xff); }
    uint16_t parse_u16(const unsigned long response) { return (uint16_t) (response & 0xffff); }
    int16_t parse_s16(const unsigned long response) { return (int16_t) (response & 0xffff); }
    float parse_f88(const unsigned long response) {
        unsigned int data = response & 0xffff;
        return (data & 0x8000) ? -(0x10000L - data) / 256.0f : data / 256.0f; 
    }

    std::string parse_str_date(esphome::text_sensor::TextSensor* sensor, const unsigned long response) { return "00:00 00/00/0000"; }

    unsigned int write_flag8_lb_0(const bool value, const unsigned int data) { return value ? data | 0b0000000000000001 : data & 0b1111111111111110; }
    unsigned int write_flag8_lb_1(const bool value, const unsigned int data) { return value ? data | 0b0000000000000010 : data & 0b1111111111111101; }
    unsigned int write_flag8_lb_2(const bool value, const unsigned int data) { return value ? data | 0b0000000000000100 : data & 0b1111111111111011; }
    unsigned int write_flag8_lb_3(const bool value, const unsigned int data) { return value ? data | 0b0000000000001000 : data & 0b1111111111110111; }
    unsigned int write_flag8_lb_4(const bool value, const unsigned int data) { return value ? data | 0b0000000000010000 : data & 0b1111111111101111; }
    unsigned int write_flag8_lb_5(const bool value, const unsigned int data) { return value ? data | 0b0000000000100000 : data & 0b1111111111011111; }
    unsigned int write_flag8_lb_6(const bool value, const unsigned int data) { return value ? data | 0b0000000001000000 : data & 0b1111111110111111; }
    unsigned int write_flag8_lb_7(const bool value, const unsigned int data) { return value ? data | 0b0000000010000000 : data & 0b1111111101111111; }
    unsigned int write_flag8_hb_0(const bool value, const unsigned int data) { return value ? data | 0b0000000100000000 : data & 0b1111111011111111; }
    unsigned int write_flag8_hb_1(const bool value, const unsigned int data) { return value ? data | 0b0000001000000000 : data & 0b1111110111111111; }
    unsigned int write_flag8_hb_2(const bool value, const unsigned int data) { return value ? data | 0b0000010000000000 : data & 0b1111101111111111; }
    unsigned int write_flag8_hb_3(const bool value, const unsigned int data) { return value ? data | 0b0000100000000000 : data & 0b1111011111111111; }
    unsigned int write_flag8_hb_4(const bool value, const unsigned int data) { return value ? data | 0b0001000000000000 : data & 0b1110111111111111; }
    unsigned int write_flag8_hb_5(const bool value, const unsigned int data) { return value ? data | 0b0010000000000000 : data & 0b1101111111111111; }
    unsigned int write_flag8_hb_6(const bool value, const unsigned int data) { return value ? data | 0b0100000000000000 : data & 0b1011111111111111; }
    unsigned int write_flag8_hb_7(const bool value, const unsigned int data) { return value ? data | 0b1000000000000000 : data & 0b0111111111111111; }
    unsigned int write_u8_lb(const uint8_t value, const unsigned int data) { return (data & 0xff00) | value; }
    unsigned int write_u8_hb(const uint8_t value, const unsigned int data) { return (data & 0x00ff) | (value << 8); }
    unsigned int write_s8_lb(const int8_t value, const unsigned int data) { return (data & 0xff00) | value; }
    unsigned int write_s8_hb(const int8_t value, const unsigned int data) { return (data & 0x00ff) | (value << 8); }
    unsigned int write_u16(const uint16_t value, const unsigned int data) { return value; }
    unsigned int write_s16(const int16_t value, const unsigned int data) { return value; }
    unsigned int write_f88(const float value, const unsigned int data) { return (unsigned int) (value * 256.0f); }    
    
    unsigned int write_str_date(const std::string value, const unsigned int data) { return 0; }
} // namespace message_data
}
#define OPENTHERMGW_IGNORE_1(x)
#define OPENTHERMGW_IGNORE_2(x, y)

namespace esphome {
    namespace OpenThermGateway {
        static const char * TAG = "OpenThermGateway";
	OpenTherm *OpenThermGateway::m_otThermostat=NULL;
	OpenTherm *OpenThermGateway::m_otBoiler=NULL;

        OpenThermGateway::OpenThermGateway() : PollingComponent(100)
	{
	}

        OpenThermGateway::~OpenThermGateway()
	{
		if(m_otThermostat!=NULL)
		{
			delete m_otThermostat;
			m_otThermostat=NULL;
		}
		
		if(m_otBoiler!=NULL)
		{
			delete m_otBoiler;
			m_otBoiler=NULL;
		}		
	}

	void OpenThermGateway::dump_config() 
	{
		#define ID(x) x
		#define SHOW2(x) #x
		#define SHOW(x) SHOW2(x)
	
		ESP_LOGCONFIG(TAG, "OpenTherm:");
		ESP_LOGCONFIG(TAG, "  Thermostat In: GPIO%d", m_pinThermostatIn);
		ESP_LOGCONFIG(TAG, "  Thermostat Out: GPIO%d", m_pinThermostatOut);
		ESP_LOGCONFIG(TAG, "  Boiler In: GPIO%d", m_pinBoilerIn);
		ESP_LOGCONFIG(TAG, "  Boiler Out: GPIO%d", m_pinBoilerOut);
		ESP_LOGCONFIG(TAG, "  Sensors: %s", SHOW(OPENTHERMGW_SENSOR_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Binary sensors: %s", SHOW(OPENTHERMGW_BINARY_SENSOR_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Text sensors: %s", SHOW(OPENTHERMGW_TEXT_SENSOR_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Switches: %s", SHOW(OPENTHERMGW_SWITCH_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Input sensors: %s", SHOW(OPENTHERMGW_INPUT_SENSOR_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Outputs: %s", SHOW(OPENTHERMGW_OUTPUT_LIST(ID, )));
		ESP_LOGCONFIG(TAG, "  Numbers: %s", SHOW(OPENTHERMGW_NUMBER_LIST(ID, )));
	}

        void OpenThermGateway::setup() 
        {
	        m_otThermostat=new OpenTherm(m_pinThermostatIn, m_pinThermostatOut, true);
	        m_otThermostat->begin(handleInterruptThermostat, processRequestThermostat, this);

	        m_otBoiler=new OpenTherm(m_pinBoilerIn, m_pinBoilerOut);
	        m_otBoiler->begin(handleInterruptBoiler);	        
	        
		m_msLastLoop=millis();
		
		m_current_message_iterator = m_initial_messages.begin();
		m_auto_update_message_iterator = m_map_auto_update_messages.begin();		
        }
 
	void OpenThermGateway::on_shutdown() 
	{
		if(m_otThermostat!=NULL)
			m_otThermostat->end();

		if(m_otBoiler!=NULL)
			m_otBoiler->end();
	}

	void OpenThermGateway::add_initial_message(OpenThermMessageID message_id)
	{			
		ESP_LOGD("OpenThermGateway", "Adding initial message %d", message_id);
		if(std::find(m_initial_messages.begin(), m_initial_messages.end(), message_id)==m_initial_messages.end())
			m_initial_messages.insert(message_id); 
	}

	void OpenThermGateway::add_auto_update_message(OpenThermMessageID message_id, int32_t secUpdateTime)
	{
		ESP_LOGD("OpenThermGateway", "Adding auto update message %d every %d sec", message_id, secUpdateTime);
		m_map_auto_update_messages[message_id].msTimeSinceLastUpdate=0;
		if(m_map_auto_update_messages[message_id].msTimeUpdate==0 || m_map_auto_update_messages[message_id].msTimeUpdate>secUpdateTime*1000)
			m_map_auto_update_messages[message_id].msTimeUpdate=secUpdateTime*1000;
	}

	void IRAM_ATTR OpenThermGateway::handleInterruptThermostat()
	{
		if(m_otThermostat!=NULL)
			m_otThermostat->handleInterrupt();
	}

	void IRAM_ATTR OpenThermGateway::handleInterruptBoiler()
	{
		if(m_otBoiler!=NULL)
			m_otBoiler->handleInterrupt();
	}

	void OpenThermGateway::processRequestThermostat(unsigned long request, OpenThermResponseStatus status)
	{
		if(request==0)
			return;				
		
		OpenThermMessageType requestType=m_otThermostat->getMessageType(request);
		OpenThermMessageID requestDataID=m_otThermostat->getDataID(request);
		uint16_t requestData=(uint16_t)request;

		ESP_LOGD(TAG, "Thermostat request (%08X) : MessageType: %s, DataID: %d, Data: %x] (%s)", request, m_otThermostat->messageTypeToString(requestType), requestDataID, requestData, m_otThermostat->statusToString(status));

		if(status==OpenThermResponseStatus::SUCCESS)
		{			
			parseRequest(requestType, requestDataID, requestData);
			if(m_otBoiler!=NULL)
			{
				// Handle overrides
#ifdef OPENTHERMGW_HAS_NUMBER_t_roomset_override
				if(requestDataID==OpenThermMessageID::TrSet)
				{
					if(this->t_roomset_override_number->has_state())
					{
						float fValue=this->t_roomset_override_number->state;
						if(fValue!=0.)
						{
							unsigned int data = m_otBoiler->temperatureToData(fValue);
							unsigned int requestOverride=m_otBoiler->buildRequest(OpenThermMessageType::WRITE_DATA, requestDataID, data);
							ESP_LOGD(TAG, "t_roomsetoverride : %f (%x -> %x)", fValue, request, requestOverride);

							request=requestOverride;
						}
					}
				}
#endif
				unsigned long response = m_otBoiler->sendRequest(request);
				if (response!=0)
				{
					OpenThermMessageType responseType=m_otThermostat->getMessageType(response);
					OpenThermMessageID responseDataID=m_otThermostat->getDataID(response);
					uint16_t responseData=(uint16_t)response;
					m_otThermostat->sendResponse(response);
					parseResponse(responseType, responseDataID, responseData);
				}
			}
		}
	}

	void OpenThermGateway::parseRequest(OpenThermMessageType type, OpenThermMessageID dataID, uint16_t data)
	{
	}

	void OpenThermGateway::parseResponse(OpenThermMessageType type, OpenThermMessageID dataID, uint16_t data)
	{
		bool bHandled=false;

		ESP_LOGD(TAG, "Boiler response [MessageType: %s, DataID: %d, Data: %x]", m_otBoiler->messageTypeToString(type), dataID, data);
		
		if(dataID==OpenThermMessageID::Status)
		{
			m_bCHEnable = message_data::parse_flag8_hb_0(data);
			m_bDHWEnable = message_data::parse_flag8_hb_1(data);
			m_bCoolingEnable = message_data::parse_flag8_hb_2(data);
			m_bOTCActive = message_data::parse_flag8_hb_3(data);
			m_bCH2Active = message_data::parse_flag8_hb_4(data);
			m_bStatusReceived=true;
		}			
		
		// Special messages
		switch(dataID)
		{
			case OpenThermMessageID::DayTime:
				m_dateDOW=(data>>13)&0x03;
				m_dateHour=(uint8_t)data;
				m_dateMinute=(data>>8)&0x1F;
				publishDate();
				bHandled=true;
				break;

			case OpenThermMessageID::Date:
				m_dateMonth=data>>8;
				m_dateDay=(uint8_t)data;
				publishDate();
				bHandled=true;
				break;

			case OpenThermMessageID::Year:
				m_dateYear=data;
				bHandled=true;
				publishDate();
				break;
				
			default:
				break;
		}

		if(!bHandled)
		{
			// Define the handler helpers to publish the results to all sensors
			#define OPENTHERMGW_MESSAGE_RESPONSE_MESSAGE(msg) \
				case OpenThermMessageID::msg: \
				    ESP_LOGD(TAG, "Received %s response", #msg); \
				    bHandled=true;
			#define OPENTHERMGW_MESSAGE_RESPONSE_ENTITY(key, msg_data) \
			    	this->key->publish_state(message_data::parse_ ## msg_data(data));
			#define OPENTHERMGW_MESSAGE_RESPONSE_TEXT_ENTITY(key, msg_data) \
			    	this->key->publish_state(message_data::parse_ ## msg_data(this->key, data));
			#define OPENTHERMGW_MESSAGE_RESPONSE_POSTSCRIPT \
			    	break;

			// Then use those to create a switch statement for each thing we would want
			// to report. We use a separate switch statement for each type, because some
			// messages include results for multiple types, like flags and a number.
			switch (dataID) 
			{
				OPENTHERMGW_SENSOR_MESSAGE_HANDLERS(OPENTHERMGW_MESSAGE_RESPONSE_MESSAGE, OPENTHERMGW_MESSAGE_RESPONSE_ENTITY, , OPENTHERMGW_MESSAGE_RESPONSE_POSTSCRIPT, )			
				default: break;
			}
			
			switch (dataID) 
			{
				OPENTHERMGW_BINARY_SENSOR_MESSAGE_HANDLERS(OPENTHERMGW_MESSAGE_RESPONSE_MESSAGE, OPENTHERMGW_MESSAGE_RESPONSE_ENTITY, , OPENTHERMGW_MESSAGE_RESPONSE_POSTSCRIPT, )
				default: break;
			}

			switch (dataID) 
			{
				OPENTHERMGW_TEXT_SENSOR_MESSAGE_HANDLERS(OPENTHERMGW_MESSAGE_RESPONSE_MESSAGE, OPENTHERMGW_MESSAGE_RESPONSE_TEXT_ENTITY, , OPENTHERMGW_MESSAGE_RESPONSE_POSTSCRIPT, )
				default: break;
			}

			switch (dataID) 
			{
				OPENTHERMGW_SWITCH_MESSAGE_HANDLERS(OPENTHERMGW_MESSAGE_RESPONSE_MESSAGE, OPENTHERMGW_MESSAGE_RESPONSE_ENTITY, , OPENTHERMGW_MESSAGE_RESPONSE_POSTSCRIPT, )
				default: break;
			}
		}
		
		if(bHandled)
		{
			std::unordered_map<OpenThermMessageID, SAutoUpdateMessage>::iterator it=m_map_auto_update_messages.find(dataID);
			if(it!=m_map_auto_update_messages.end())
			{
				(*it).second.msTimeSinceLastUpdate=0;
			}
		} else {		
			ESP_LOGD(TAG, "Unhandled response [MessageType: %s, DataID: %d, Data: %x]", m_otBoiler->messageTypeToString(type), dataID, data);
		}
	}
	
	void OpenThermGateway::publishDate()
	{
		if(m_dateMinute==0xFF || m_dateHour==0xFF || m_dateDay==0xFF || m_dateMonth==0xFF || m_dateYear==0xFFFF)
			return;
			
		char szDate[64];
		snprintf(szDate, sizeof(szDate), "%02d:%02d %02d/%02d/%04d", m_dateMinute, m_dateHour, m_dateDay, m_dateMonth, m_dateYear);
		if(m_strDate!=szDate)
		{
			//this->time_date_text_sensor->publish_state(szDate);
			m_strDate=szDate;
		}			
	}


/*        void OpenThermGateway::control(const climate::ClimateCall & call) 
        {
        }

        climate::ClimateTraits OpenThermGateway::traits() 
        {
            auto traits = climate::ClimateTraits();
            return traits;
        }*/

        void OpenThermGateway::loop() 
        {        	
        	unsigned long loopStart=millis();
        	unsigned long loopTime=loopStart-m_msLastLoop;
        	m_msLastLoop=loopStart;
        	
	        if(m_bStatusReceived && m_bInitializing)
	        {	        
		    	if (m_bInitializing && m_bStatusReceived && m_otBoiler!=NULL && m_otBoiler->isReady())
		    	{
				if (m_current_message_iterator == m_initial_messages.end()) 
				{
				    m_bInitializing = false;
				} else {
					unsigned int request = build_request(*m_current_message_iterator);										
					unsigned int response = m_otBoiler->sendRequest(request);											
					if (response!=0) 
					{		
						OpenThermMessageType responseType=m_otThermostat->getMessageType(response);
						OpenThermMessageID responseDataID=m_otThermostat->getDataID(response);
						uint16_t responseData=(uint16_t)response;

						ESP_LOGD(TAG, "Boiler response (%08X) : MessageType: %s, DataID: %d, Data: %x]", response, m_otBoiler->messageTypeToString(responseType), responseDataID, responseData);					
						parseResponse(responseType, responseDataID, responseData);
					}
					m_current_message_iterator++;
				}
			}
		} else if(m_otThermostat!=NULL) {
			bool bDidProcessMessage=m_otThermostat->process();		

			for(std::unordered_map<OpenThermMessageID, SAutoUpdateMessage>::iterator it=m_map_auto_update_messages.begin(); it!=m_map_auto_update_messages.end(); ++it)
				(*it).second.msTimeSinceLastUpdate+=loopTime;
				
			// Send auto-update message during thermostat delay to avoid messing communication, and mas 1 message every 2 secs
			m_msTimeSinceLastAutoUpdate+=loopTime;			
			if(!bDidProcessMessage && m_msTimeSinceLastAutoUpdate>=2000 && m_otThermostat!=NULL && m_otThermostat->status==OpenThermStatus::DELAY && m_otBoiler->status==OpenThermStatus::READY)
			{
				while(m_auto_update_message_iterator!=m_map_auto_update_messages.end())
				{
					if((*m_auto_update_message_iterator).second.msTimeSinceLastUpdate>=(*m_auto_update_message_iterator).second.msTimeUpdate)
					{
						unsigned int request = build_request((*m_auto_update_message_iterator).first);									
						unsigned int response = m_otBoiler->sendRequest(request);
						m_msTimeSinceLastAutoUpdate=0;
						if (response!=0) 
						{		
							OpenThermMessageType responseType=m_otBoiler->getMessageType(response);
							OpenThermMessageID responseDataID=m_otBoiler->getDataID(response);
							uint16_t responseData=(uint16_t)response;

							ESP_LOGD(TAG, "Auto-update response (%08X) (%d>=%d) : MessageType: %s, DataID: %d, Data: %x]", response, (*m_auto_update_message_iterator).second.msTimeSinceLastUpdate, (*m_auto_update_message_iterator).second.msTimeUpdate, m_otBoiler->messageTypeToString(responseType), responseDataID, responseData);					
							parseResponse(responseType, responseDataID, responseData);
							m_auto_update_message_iterator++;
						}
						break;
					}
					m_auto_update_message_iterator++;
				}
				if(m_auto_update_message_iterator==m_map_auto_update_messages.end())
					m_auto_update_message_iterator=m_map_auto_update_messages.begin();
			}
		}		
        }

	void OpenThermGateway::update()
	{
	}
	
	unsigned int OpenThermGateway::build_request(OpenThermMessageID request_id) 
	{
		if(m_otBoiler==NULL)
			return 0;
			
		// First, handle the status request. This requires special logic, because we
		// wouldn't want to inadvertently disable domestic hot water, for example.
		// It is also included in the macro-generated code below, but that will
		// never be executed, because we short-circuit it here. 
		if (request_id == OpenThermMessageID::Status) 
		{
			ESP_LOGD(TAG, "Building Status request");
			bool ch_enable = 
				m_bCHEnable
				&& 
				#ifdef OPENTHERMGW_READ_ch_enable
				OPENTHERMGW_READ_ch_enable
				#else
				true
				#endif 
				&& 
				#ifdef OPENTHERMGW_READ_t_set
				OPENTHERMGW_READ_t_set > 0.0
				#else
				true
				#endif
				;
		
			bool dhw_enable = 
				m_bDHWEnable
				&& 
				#ifdef OPENTHERMGW_READ_dhw_enable
				OPENTHERMGW_READ_dhw_enable
				#else
				true
				#endif
				;

			bool cooling_enable = 
				m_bCoolingEnable
				&& 
				#ifdef OPENTHERMGW_READ_cooling_enable
				OPENTHERMGW_READ_cooling_enable
				#else
				true
				#endif 
				&& 
				#ifdef OPENTHERMGW_READ_cooling_control
				OPENTHERMGW_READ_cooling_control > 0.0
				#else
				true
				#endif
				;

			bool otc_active = 
				m_bOTCActive
				&& 
				#ifdef OPENTHERMGW_READ_otc_active
				OPENTHERMGW_READ_otc_active
				#else
				true
				#endif
				;

			bool ch2_active = 
				m_bCH2Active
				&& 
				#ifdef OPENTHERMGW_READ_ch2_active
				OPENTHERMGW_READ_ch2_active
				#else
				true
				#endif 
				&& 
				#ifdef OPENTHERMGW_READ_t_set_ch2
				OPENTHERMGW_READ_t_set_ch2 > 0.0
				#else
				true
				#endif
				;

			return m_otBoiler->buildSetBoilerStatusRequest(ch_enable, dhw_enable, cooling_enable, otc_active, ch2_active);
		}
		
		return m_otBoiler->buildRequest(OpenThermRequestType::READ, request_id, 0);
		
	}		
    } // namespace OpenThermGateway
} // namespace esphome
