# Dictionaries are used to store data values in key:value pairs.

 # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Basic Syntax:
# dictionary_name = {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }

phone_dict={"brand": "poco m2 pro",
            "ram":"4 ram",
            "Camera":"48MP + 8MP + 5MP + 2MP  16MP Front",
            "Battery":"5000 mAh",
            "colour":["black","blue","red","yellow"]}
#print(phone_dict)


# Syntax to Add a Key-Value Pair:
# dictionary_name[new_key] = new_value

phone_dict={"brand": "poco m2 pro",
            "ram":"4 ram",
            "Camera":"48MP + 8MP + 5MP + 2MP  16MP Front",
            "Battery":"5000 mAh",
            "colour":["black","blue","red","yellow"]}

phone_dict["storage"]="128 gb"
#print(phone_dict)

#iddi new key nii new value nii add cheysamu..


#ippudu ila kakunda nenu oka key tisukuni aa key lo unna value kii inka values add cheydam anukuntuna...

phone_dict={"brand": "poco m2 pro",
            "ram":"4 ram",
            "Camera":"48MP + 8MP + 5MP + 2MP  16MP Front",
            "Battery":"5000 mAh",
            "colour":["black","blue","red","yellow"]}

phone_dict["colour"]=phone_dict["colour"]+["pink"]
# print(phone_dict)

#Using update() Method & syntax chudam, update cheyadam..
#dictionary_name.update({key1: value1, key2: value2})

sd_info={}
sd_info["name"]="ravi varma"
sd_info["ph.no"]="123456789"
sd_info["qualification"]="B.tech"
sd_info["city"]="kakinada"
sd_info["address"]=["rto office opt road" , "rr nagar", "renuka apratments", "gudari gunta", "kakinada"]
sd_info.update({"name":"dantuluri","qualification":"compeleted"}) #dict lo kabbati {} ee bracketes use cheyali,multiple vatiki ila assign cheyali
#sd_info["name"]="dantuluri" #ila kuda update cheyachu
# print(sd_info)

sd_info={}
sd_info["name"]="ravi varma"
sd_info["ph.no"]="123456789"
sd_info["qualification"]="B.tech"
sd_info["city"]="kakinada"
sd_info["address"]=["rto office opt road" , "rr nagar", "renuka apratments", "gudari gunta", "kakinada"]
sd_info["address"]=sd_info["address"][4] #niku address oka 4 index kavali kabbti adi ichamu, andukey assign cheysey daggara kuda ivalii, niku aa element oka index kavalo addi iavli..
print(sd_info)

#update anetey unna vatti nii tinesi kota danni add cheyadam ..

lap_dict={}
lap_dict["bike price"]=100000
lap_dict["company"]=["ns150","ns140"]
lap_dict["palce"]=["hyderabad"]
lap_dict["picode"]=500069

lap_dict["palce"]=lap_dict["palce"]+["kakinada"] #ila add cheysukovachu..
del lap_dict["company"][0] #ila delete cheyali
# print(lap_dict)

#delte cheyali antey ila cheyali..


 











