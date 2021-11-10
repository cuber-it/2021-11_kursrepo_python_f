# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r" ([A-Z]+) *?:"



test_str = ("03/22 08:51:01 INFO   :.main: *************** RSVP Agent started ***************\n"
	"03/22 08:51:01 INFO   :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf\n"
	"03/22 08:51:01 INFO   :.main: Using log level 511\n"
	"03/22 08:51:01 INFO   :..settcpimage: Get TCP images rc - EDC8112I Operation not supported on socket.\n"
	"03/22 08:51:01 INFO   :..settcpimage: Associate with TCP/IP image name = TCPCS\n"
	"03/22 08:51:02 INFO   :..reg_process: registering process with the system\n"
	"03/22 08:51:02 INFO   :..reg_process: attempt OS/390 registration\n"
	"03/22 08:51:02 INFO   :..reg_process: return from registration rc=0\n"
	"03/22 08:51:06 TRACE  :...read_physical_netif: Home list entries returned = 7\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #1, interface TR1 has address 9.37.65.139, ifidx 1\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #2, interface LINK11 has address 9.67.100.1, ifidx 2\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #3, interface LINK12 has address 9.67.101.1, ifidx 3\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #4, interface CTCD0 has address 9.67.116.98, ifidx 4\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #5, interface CTCD2 has address 9.67.117.98, ifidx 5\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0\n"
	"03/22 08:51:06 INFO   :....mailslot_create: creating mailslot for timer\n"
	"03/22 08:51:06 INFO   :...mailbox_register: mailbox allocated for timer\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.37.65.139, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.100.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.101.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.116.98, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.117.98, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 127.0.0.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :......mailslot_create: creating socket for querying route\n"
	"03/22 08:51:06 INFO   :.....mailbox_register: no mailbox necessary for forward\n"
	"03/22 08:51:06 INFO   :......mailslot_create: creating mailslot for route engine - informational socket\n"
	"03/22 08:51:06 TRACE  :......mailslot_create: ready to accept informational socket connection\n"
	"03/22 08:51:11 INFO   :.....mailbox_register: mailbox allocated for route\n"
	"03/22 08:51:11 INFO   :.....mailslot_create: creating socket for traffic control module\n"
	"03/22 08:51:11 INFO   :....mailbox_register: no mailbox necessary for traffic-control\n"
	"03/22 08:51:11 INFO   :....mailslot_create: creating mailslot for RSVP client API\n"
	"03/22 08:51:11 INFO   :...mailbox_register: mailbox allocated for rsvp-api\n"
	"03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for terminate\n"
	"03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for terminate\n"
	"03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for dump\n"
	"03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for dump\n"
	"03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for (broken) pipe\n"
	"03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for pipe\n"
	"03/22 08:51:11 INFO   :.main: rsvpd initialization complete\n"
	"03/22 08:52:50 INFO   :......rsvp_api_open: accepted a new connection for rapi\n"
	"03/22 08:52:50 INFO   :.......mailbox_register: mailbox allocated for mailbox\n"
	"03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 does not exist\n"
	"03/22 08:52:50 EVENT  :.....api_reader: api request SESSION\n"
	"03/22 08:52:50 TRACE  :......rsvp_event_establishSession: local node will send\n"
	"03/22 08:52:50 INFO   :........router_forward_getOI: Ioctl to get route entry successful\n"
	"03/22 08:52:50 TRACE  :........router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:52:50 TRACE  :........router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:52:50 TRACE  :........router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:52:50 TRACE  :........router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:52:50 TRACE  :.......event_establishSessionSend: found outgoing if=9.67.116.98 through forward engine\n"
	"03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:52:50 EVENT  :.....api_reader: api request SENDER\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Entering\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  papiLogFunc = 98681F0 papiUserValue = 0\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Exiting\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Entering\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Entering\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Exiting\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  ApiHandle = 98BDFB0,  connfd = 22\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Exiting\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Entering\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Writing to socket = 22\n"
	"03/22 08:52:50 INFO   :.......init_policyAPI: ReadBuffer:  Entering\n"
	"03/22 08:52:51 INFO   :.......init_policyAPI: ReadBuffer:  Exiting\n"
	"03/22 08:52:51 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Exiting\n"
	"03/22 08:52:51 INFO   :.......init_policyAPI: Policy API initialized\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Entering\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Entering\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Exiting\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Result = 0\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Exiting\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: found action name CLCat2 for flow[sess=9.67.116.99:1047:6,source=9.67.116.98:8000]\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Entering\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Entering\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Exiting\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Result = 0\n"
	"03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Exiting\n"
	"03/22 08:52:51 INFO   :.....api_reader: appl chose service type 1\n"
	"03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Entering\n"
	"03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Result = 0\n"
	"03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Exiting\n"
	"03/22 08:52:51 TRACE  :.....api_reader: new service=1, old service=0\n"
	"03/22 08:52:51 INFO   :.......rsvp_flow_stateMachine: state SESSIONED, event PATHDELTA\n"
	"03/22 08:52:51 TRACE  :........rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:52:51 TRACE  :........flow_timer_start: started T1\n"
	"03/22 08:52:51 TRACE  :.......rsvp_flow_stateMachine: entering state PATHED\n"
	"03/22 08:52:51 TRACE  :........mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:52:51 TRACE  :........mailslot_send: sending to (9.67.116.99:1698)\n"
	"03/22 08:52:51 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98\n"
	"03/22 08:52:51 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84\n"
	"03/22 08:52:51 TRACE  :.......rsvp_parse_objects: STYLE is WF\n"
	"03/22 08:52:51 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0\n"
	"03/22 08:52:51 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:52:51 INFO   :.......rsvp_flow_stateMachine: state PATHED, event RESVDELTA\n"
	"03/22 08:52:51 TRACE  :........traffic_action_oif: is to install filter\n"
	"03/22 08:52:51 INFO   :.........qosmgr_request: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6 rthdl-7f5251c8\n"
	"03/22 08:52:51 INFO   :.........qosmgr_request: [CL r=90000 b=6000 p=110000 m=1024 M=2048]\n"
	"03/22 08:52:51 INFO   :.........qosmgr_request: Ioctl to add reservation successful\n"
	"03/22 08:52:51 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Entering\n"
	"03/22 08:52:51 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Entering\n"
	"03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Exiting\n"
	"03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Result = 0\n"
	"03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Exiting\n"
	"03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: flow[sess=9.67.116.99:1047:6, source=9.67.116.98:8000] registered with CLCat2\n"
	"03/22 08:52:52 EVENT  :..........qosmgr_response: RESVRESP from qosmgr, reason=0, qoshandle=8b671d0\n"
	"03/22 08:52:52 INFO   :..........qosmgr_response: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6\n"
	"03/22 08:52:52 TRACE  :...........traffic_reader: tc response msg=1, status=1\n"
	"03/22 08:52:52 INFO   :...........traffic_reader: Reservation req successful[session=9.67.116.99:1047:6,source=9.67.116.98:8000, qoshd=8b671d0]\n"
	"03/22 08:52:52 TRACE  :........api_action_sender: constructing a RESV\n"
	"03/22 08:52:52 TRACE  :........flow_timer_stop: stopped T1\n"
	"03/22 08:52:52 TRACE  :........flow_timer_stop: Stop T4\n"
	"03/22 08:52:52 TRACE  :........flow_timer_start: started T1\n"
	"03/22 08:52:52 TRACE  :........flow_timer_start: Start T4\n"
	"03/22 08:52:52 TRACE  :.......rsvp_flow_stateMachine: entering state RESVED\n"
	"03/22 08:53:07 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:53:07 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:53:07 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:53:07 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:53:07 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:53:07 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:53:07 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:53:07 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:53:07 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:53:07 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:53:07 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:07 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:53:22 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98\n"
	"03/22 08:53:22 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84\n"
	"03/22 08:53:22 TRACE  :.......rsvp_parse_objects: STYLE is WF\n"
	"03/22 08:53:22 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0\n"
	"03/22 08:53:22 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:53:22 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV\n"
	"03/22 08:53:22 TRACE  :........flow_timer_stop: Stop T4\n"
	"03/22 08:53:22 TRACE  :........flow_timer_start: Start T4\n"
	"03/22 08:53:22 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:22 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:53:22 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:53:22 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:53:22 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:53:22 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:53:22 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:53:22 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:53:22 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:53:22 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:53:22 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:53:22 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:22 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:53:38 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:53:38 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:53:38 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:53:38 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:53:38 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:53:38 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:53:38 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:53:38 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:53:38 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:53:38 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:53:38 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:38 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:53:52 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98\n"
	"03/22 08:53:52 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84\n"
	"03/22 08:53:52 TRACE  :.......rsvp_parse_objects: STYLE is WF\n"
	"03/22 08:53:52 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0\n"
	"03/22 08:53:52 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:53:52 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV\n"
	"03/22 08:53:52 TRACE  :........flow_timer_stop: Stop T4\n"
	"03/22 08:53:52 TRACE  :........flow_timer_start: Start T4\n"
	"03/22 08:53:52 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:53 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:53:53 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:53:53 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:53:53 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:53:53 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:53:53 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:53:53 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:53:53 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:53:53 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:53:53 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:53:53 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:53:53 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:54:09 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:54:09 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:54:09 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:54:09 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:54:09 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:54:09 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:54:09 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:54:09 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:54:09 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:54:09 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:54:09 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:54:09 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:54:22 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98\n"
	"03/22 08:54:22 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84\n"
	"03/22 08:54:22 TRACE  :.......rsvp_parse_objects: STYLE is WF\n"
	"03/22 08:54:22 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0\n"
	"03/22 08:54:22 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:54:22 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV\n"
	"03/22 08:54:22 TRACE  :........flow_timer_stop: Stop T4\n"
	"03/22 08:54:22 TRACE  :........flow_timer_start: Start T4\n"
	"03/22 08:54:22 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:54:24 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
	"03/22 08:54:24 TRACE  :.....event_timerT1_expire: T1 expired\n"
	"03/22 08:54:24 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
	"03/22 08:54:24 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
	"03/22 08:54:24 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
	"03/22 08:54:24 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
	"03/22 08:54:24 TRACE  :......router_forward_getOI:         route handle:   7f5251c8\n"
	"03/22 08:54:24 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT\n"
	"03/22 08:54:24 TRACE  :.......rsvp_action_nHop: constructing a PATH\n"
	"03/22 08:54:24 TRACE  :.......flow_timer_start: started T1\n"
	"03/22 08:54:24 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED\n"
	"03/22 08:54:24 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:54:35 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists\n"
	"03/22 08:54:35 EVENT  :.....api_reader: api request SENDER_WITHDRAW\n"
	"03/22 08:54:35 INFO   :.......rsvp_flow_stateMachine: state RESVED, event PATHTEAR\n"
	"03/22 08:54:35 TRACE  :........traffic_action_oif: is to remove filter\n"
	"03/22 08:54:35 INFO   :.........qosmgr_request: Ioctl to remove reservation successful\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Entering\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Entering\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Exiting\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Result = 0\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Exiting\n"
	"03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: flow[sess=9.67.116.99:1047:6, source=9.67.116.98:8000] unregistered from CLCat2\n"
	"03/22 08:54:35 EVENT  :..........qosmgr_response: DELRESP from qosmgr, reason=0, qoshandle=0\n"
	"03/22 08:54:35 INFO   :..........qosmgr_response: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6\n"
	"03/22 08:54:35 TRACE  :...........traffic_reader: tc response msg=3, status=1\n"
	"03/22 08:54:35 TRACE  :........rsvp_action_nHop: constructing a PATHTEAR\n"
	"03/22 08:54:35 TRACE  :........flow_timer_stop: stopped T1\n"
	"03/22 08:54:35 TRACE  :........flow_timer_stop: Stop T4\n"
	"03/22 08:54:35 TRACE  :.......rsvp_flow_stateMachine: entering state SESSIONED\n"
	"03/22 08:54:35 TRACE  :........mailslot_send: sending to (9.67.116.99:0)\n"
	"03/22 08:54:35 TRACE  :......rsvp_event_propagate: flow[session=9.67.116.99:1047:6, source=9.67.116.98:8000] ceased\n"
	"03/22 08:54:35 EVENT  :.....api_reader: api request CLOSE\n"
	"03/22 08:54:35 INFO   :.......rsvp_flow_stateMachine: state SESSIONED, event PATHTEAR\n"
	"03/22 08:54:35 PROTERR:.......rsvp_flow_stateMachine: state SESSIONED does not expect event PATHTEAR\n"
	"03/22 08:54:53 EVENT  :..mailslot_sitter: process received signal SIGTERM\n"
	"03/22 08:54:53 INFO   :...check_signals: received TERM signal\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Entering\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: ReadBuffer:  Entering\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: ReadBuffer:  Exiting\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Result = 0\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Exiting\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: APITerminate:  Entering\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: APITerminate:  Exiting\n"
	"03/22 08:54:53 INFO   :......term_policyAPI: Policy API terminated\n"
	"03/22 08:54:53 INFO   :......dreg_process: deregistering process with the system\n"
	"03/22 08:54:53 INFO   :......dreg_process: attempt to dereg (ifaeddrg_byaddr)\n"
	"03/22 08:54:53 INFO   :......dreg_process: rc from ifaeddrg_byaddr  rc =0\n"
	"03/22 08:54:53 INFO   :.....terminator: process terminated with exit code 0")

matches = re.finditer(regex, test_str, re.MULTILINE)

counter = {}

import timeit
start = timeit.timeit()

for matchNum, match in enumerate(matches, start=1):
    if len(match.groups()) == 1:
        try:
            counter[match.group(1)] += 1
        except KeyError:
            counter[match.group(1)] = 0
 #       if match.group(1) in counter:
 #           counter[match.group(1)] += 1
 #       else: 
 #           counter[match.group(1)] = 1
    else: 
        print(matchNum," Nicht genau eine Gruppe")
        exit(-1)

laufzeit = (timeit.timeit() - start)*1000
print(f"Laufzeit {laufzeit} s")
print(counter)

#