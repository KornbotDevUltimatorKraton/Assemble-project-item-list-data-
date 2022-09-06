import json
API_SBC = {}
API_features_Data = {} 
#try:          
API_features_data = open("/home/roboreactor/Backup_API_project_features.json",'r') #Getting the features json 
data_4 = json.loads(API_features_data.read()) # Getting features data of the main board 
print(data_4)
restore_4 = list(data_4)  
print(restore_4)
email = 'kornbot380@hotmail.com'
modify_project = {'kornbot380@hotmail.com': {'category': [
{'items': [{'title': 'face_recog_1  ======> 127.0.0.1,0,5080,5081,Non'}, 
{'title': 'Servo_control_2  ======> 127.0.0.1,5081,I2C,2'}, 
{'title': 'Speech_recognition_3  ======> 127.0.0.1,1.04,th'}, {'title': 'Stepper_motor_4  ======> 127.0.0.1,50,90'}], 'title': 'Meridianstar'}]}}
if restore_4 !=[]:
      for rst in restore_4:
                 #print(rst,data_4.get(rst),type(rst))
                 API_features_Data[rst] = data_4.get(rst)
      #print(API_features_Data)
      Get_items = API_features_Data.get(email).get('category')
      print('Get Items after seeking the category',Get_items) # True form of the data inside the category 
      #input json from the current new project to creat the pattern 
      Get_input_items = modify_project.get(email).get('category') # Getting the data from the list of category 
      for i in range(0,len(Get_items)):
             
              print('Extracted',i,list(Get_items)[i])
              #Assemly new data in the key 
              data_assembly = {list(Get_items)[i].get('title'):list(Get_items)[i].get('items')}
              print('Data assembly',data_assembly)
              if len(Get_items)-1 == i:
                  print("Assembly end result",i,len(Get_items)) #Get the data into index number    
                  for y in Get_input_items:
                      print('Extracted_from_input',y,list(y)) # Getting the new input of the project to assembly into the old file of the data 
                      data_input = {y.get('title'):y.get('items')} 
                      print(data_input)
                      data_assembly[list(data_input)[0]] = list(data_input.values())[0] # Getting the new project append inside the list of the data                                                           
                      print("End result new project append",data_assembly)                                            
                      Create_items_title = [] # Ggetting the data created in the form of item and title 
                      for gt in range(0,len(list(data_assembly))):
                                      print("title ",list(data_assembly)[gt]," items ",data_assembly.get(list(data_assembly)[gt]))   
                                      forming_items_data = {'title':list(data_assembly)[gt],'items':data_assembly.get(list(data_assembly)[gt])} 
                                      Create_items_title.append(forming_items_data) # Forming the list of the data 
                      print(Create_items_title)                                                                     
                      Account_project = {email:{'category':Create_items_title}}
                      print(Account_project)                          
 
