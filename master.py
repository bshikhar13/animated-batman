import sys
from test import *
from SMS_USSD import *
from filtering_gprs_IMSI import *
from incoming_calls_vs_outgoing_calls_for_IMSI import *
from IMEI_IMSI import *
from home_group import *
#print sys.argv

SMS_USSD_result = SMS_USSD()

print "Unique Sims : " + str(SMS_USSD_result[0])
print "\n\n"

print "SMS_USSD Filtering"
print "Suspicious Sims : " + str(len(SMS_USSD_result[1]))
print "Unuspicious Sims : " + str(len(SMS_USSD_result[2]))
print "\n"
filtering_gprs_IMSI_result = filtering_gprs_IMSI(SMS_USSD_result[1])


print "GPRS Filtering"
print "Suspicious Sims : " + str(len(filtering_gprs_IMSI_result[0]))
print "Unuspicious Sims : " + str(len(filtering_gprs_IMSI_result[1]))
print "\n"

incoming_calls_vs_outgoing_calls_for_IMSI_result = incoming_calls_vs_outgoing_calls_for_IMSI(filtering_gprs_IMSI_result[0])

print "Incoming/Outgoing Filtering"
print "Suspicious Sims : " + str(len(incoming_calls_vs_outgoing_calls_for_IMSI_result[0]))
print "Unuspicious Sims : " + str(len(incoming_calls_vs_outgoing_calls_for_IMSI_result[1]))
print "\n"


IMEI_IMSI_result = IMEI_IMSI(incoming_calls_vs_outgoing_calls_for_IMSI_result[0])

print "IMEI vs IMSI record Filtering"
print "Suspicious Sims : " + str(len(IMEI_IMSI_result[0]))
print "Unuspicious Sims : " + str(len(IMEI_IMSI_result[1]))
print "\n"

home_group_result = home_group(IMEI_IMSI_result[0])

print "Home Group Filtering"
print "Suspicious Sims : " + str(len(home_group_result[0]))
print "Unuspicious Sims : " + str(len(home_group_result[1]))
print "\n"