import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ph_num1 = input('Enter number here : ')
ph_num = "+91" + ph_num1

ch_num = phonenumbers.parse(ph_num, 'CH')
ctr_nm = geocoder.description_for_number(ch_num, 'en')
print("Country Name : ", ctr_nm)

srv_prd = phonenumbers.parse(ph_num, 'RO')
car_nm = carrier.name_for_number(srv_prd, 'en')
print("Carrier Name : ", car_nm)

tm_zn = phonenumbers.parse(ph_num, 'GB')
tm_zne = timezone.time_zones_for_number(tm_zn)
print("Time Zones : ", tm_zne)