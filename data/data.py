class data_pass():
    metadata_test_connection = [
        # testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode
        ("incorrect_databasetype", "testConnection","Service Name", False, " ", " ", "invalid", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_host", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.1764", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_port", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 15921, "metadb", "metadb", "orcl", 422),
        ("incorrect_username", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "mestadb", "metadb", "orcl", 422),
        ("incorrect_password", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadddb", "orcl", 422),
        ("incorrect_database-name", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orrtcl", 422),
        ("invalid-action", "testCottection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-connectiontype", "testConnection","Servicevd Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("Success", "testConnection","", False, " ", " ", "db2", "192.168.0.208", 25010, "db2inst1", "db2inst1", "archive", 200)
    ]

    metadata_Create_tables = [
        # testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepeted_statuscode
        ("incorrect_databasetype", "createTables","Service Name", False, " ", "drop", "invalid", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_host", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.1764", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_port", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 15921, "metadb", "metadb", "orcl", 422),
        ("incorrect_username", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "mestadb", "metadb", "orcl", 422),
        ("incorrect_password", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadddb", "orcl", 422),
        ("incorrect_database-name", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orrtcl", 422),
        ("invalid-action", "createssTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-connectiontype", "createTables","Servicevd Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-status", "createTables","Servicevd Name", False, " ", "dop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("Success", "createTables","", False, " ", "drop","db2", "192.168.0.208", 25010, "db2inst1", "db2inst1", "archive", 200)
    ]
    Super_user=[
        #testcasename,loginType,name,username,psswrd,email,excepetd_statuscode
        ("invalid-logintype","BASTC","Super","Super","Super@123","super@gmail.com",422),
        ("invalid-name","BASIC"," ","Super","Super@123","super@gmail.com",422),
        ("invalid-Username","BASIC","Super"," ","Super@123","super@gmail.com",422),
        ("invalid-passwrd","BASIC","Super","Super","Super**&^#$","super@gmail.com",422),
        ("invalid-email","BASIC","Super","Super","Super@123","super@gmail_com",422),
        ("valid-details","BASIC","Super","Super","Super@123","super@gmail.com",200)

    ]

    Storesuperseturl=[
        #testcasename,superseturl,skip,excepetd_statuscode
        ("invalid-superseturl"," ","false",400),
        ("invalid-superseturl"," ","true",200)
    ]

    add_storgae=[
        # "testcasename,storageType,name,locationType,mountPath,path,UNC_path,storageProtocol,saveFlag,excepetd_statuscode"
        ("all_empty","","","","","","","","",422),
        ("invalid_storageType","window","Archive_files","archiveFileLocation","mountPath","/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","False",422),
        ("empty_storagename","local"," ","archiveFileLocation","mountPath","/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","False",422),
        ("Invalid_locationType","local","Archive_files","archive_FileLocation","mountPath","/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","False",422),
        ("Invalid_path","local","Archive_files","archiveFileLocation","mountPath","__/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","False",422),
        ("saveflas_true","local","Archive_files","archiveFileLocation","mountPath","/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","False",200),
        ("valid_archive","local","Archive_files","archiveFileLocation","mountPath","/home/archive/API_Automation/Archive_files/","UNC_path","storageProtocol","True",200),
        ("valid_csv","local","Csv_storage","csvFileLocation","mountPath","/home/archive/API_Automation/Csv_storage/","UNC_path","storageProtocol","True",200),
        ("valid_parquet","local","Parquet_storage","parquetFileLocation","mountPath","/home/archive/API_Automation/Parquet_storage/","UNC_path","storageProtocol","True",200)
    ]

    fetch_storage=[
        # testcasename,storageId,excepetd_statuscode
        ("invalid_storageId"," ",422),
        ("valid_storageId","1",200)
    ]


    convert_server=[
        #testcasename,platformType,optimServerName, optimDirectory, psthomePath, defaultQualifier, storageId, excepetd_statuscode
        ("invalid-platformType","conver","server208 ","OPTIMDIR223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRC223.optimsrc","2",422),
        ("invalid-optimServerName","linux",56842,"OPTIMDIR223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRC223.optimsrc","2",422),
        ("invalid-optimDirectory","linux","server208 ","OPTIMDIRde3q223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRC223.optimsrc","2",422),
        ("invalid-psthomePath","linux","server208 ","OPTIMDIR223 ","/home/postgres/IBM/InfoSphere//Optim/rt/","OPTIMSRC223.optimsrc","2",422),
        ("invalid-defaultQualifier","linux","server208 ","OPTIMDIR223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRCs356223.optimsrc","2",422),
        ("invalid-storageId","linux","server208 ","OPTIMDIR223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRC223.optimsrc",24,422),
        ("invalid-platformType","linux","server208 ","OPTIMDIR223 ","/home/archive/IBM/InfoSphere/Optim/rt/","OPTIMSRC223.optimsrc",2,422)
       
    ]

    query_server=[
        #testcasename,catalogType,skip,ssl,queryServerName,databaseName,host,port,username,psswrd,excepetd_statuscode
        ("invalid_catalogtype","invald",False,False,"Server208","databaseName","192.168.0.208","10000","anything","anything",422),
        ("invalid_skip","spark","hyiue",False,"Server208","databaseName","192.168.0.208","10000","anything","anything",422),
        ("invalid_queryServerName","spark",False,False,4543,"databaseName","192.168.0.208","10000","anything","anything",422),
        ("invalid_host","spark",False,False,"Server208","databaseName","192.168.0.2098","10000","anything","anything",404),
        ("invalid_port","spark",False,False,"Server208","databaseName","192.168.0.208","150000","anything","anything",404),
        ("skip true","spark",True,False,"Server208","databaseName","192.168.0.208","10000","anything","anything",200),
        ("add_spark","spark",False,False,"Server208","databaseName","192.168.0.208","10000","anything","anything",200)
        ]


        
    


