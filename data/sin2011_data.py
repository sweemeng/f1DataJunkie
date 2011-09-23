#Fuel info - from Williams
fuel={'consumption':2.6,'penalty':0.03,'laps':61,'lapdistance':5.073,'racedistance':309, 'pitstoploss':30}

#Practice Data
fp1times=[['1', 'S. VETTEL', '1', '18:36:39', '2', '15:22.905', '3', '1:53.252', '4', '2:01.525', '5', '14:14.847', '6', '1:50.082', '7', '1:49.656', '8', '1:54.642', '9', '1:49.005', '10', '2:05.160', '11', '9:37.113', '12', '1:49.564', '13', '2:03.614'], ['2', 'M. WEBBER', '1', '18:34:39', '2', '13:29.089', '3', '1:52.869', '4', '1:52.648', '5', '2:00.855', '6', '1:54.339', '7', '15:34.618', '8', '1:51.683', '9', '1:50.930', '10', '1:58.210', '11', '1:50.308', '12', '1:50.066', '13', '9:38.676', '14', '1:59.478'], ['3', 'L. HAMILTON', '1', '18:34:48', '2', '11:04.218', '3', '9:20.157', '4', '16:06.019', '5', '1:51.961', '6', '1:53.423', '7', '1:49.515', '8', '1:55.184', '9', '1:48.599'], ['4', 'J. BUTTON', '1', '18:35:49', '2', '12:55.007', '3', '18:14.867', '4', '1:54.422', '5', '1:50.952', '6', '2:22.853', '7', '8:18.728', '8', '7:53.627', '9', '1:51.018', '10', '2:14.460'], ['5', 'F. ALONSO', '1', '18:34:02', '2', '18:41.729', '3', '11:59.510', '4', '1:59.404', '5', '2:01.881', '6', '9:31.647', '7', '1:50.596', '8', '9:05.117', '9', '1:50.847', '10', '2:02.210'], ['6', 'F. MASSA', '1', '18:34:04', '2', '13:02.281', '3', '1:53.770', '4', '1:52.043', '5', '2:05.869', '6', '1:56.689', '7', '1:53.527', '8', '21:39.315', '9', '2:00.937', '10', '9:11.790', '11', '1:52.331', '12', '2:38.641'], ['7', 'M. SCHUMACHER', '1', '18:34:01', '2', '8:38.437', '3', '1:55.827', '4', '2:07.113', '5', '22:18.346', '6', '1:53.205', '7', '2:07.764', '8', '16:01.648', '9', '1:52.416', '10', '2:04.676'], ['8', 'N. ROSBERG', '1', '18:33:03', '2', '8:16.406', '3', '1:57.351', '4', '2:14.685', '5', '11:13.690', '6', '12:10.393', '7', '1:54.382', '8', '1:56.042', '9', '1:52.815', '10', '2:12.285', '11', '14:50.913', '12', '2:13.559'], ['9', 'B. SENNA', '1', '18:33:24', '2', '10:19.331', '3', '1:59.340', '4', '1:56.682', '5', '2:02.936', '6', '1:56.577', '7', '1:54.912', '8', '2:11.024', '9', '11:05.981', '10', '1:55.424', '11', '1:53.765', '12', '1:57.713', '13', '1:54.819', '14', '2:08.906', '15', '12:50.731', '16', '1:55.112', '17', '2:21.721'], ['10', 'V. PETROV', '1', '18:33:21', '2', '11:04.568', '3', '1:59.106', '4', '1:56.693', '5', '1:55.802', '6', '1:54.736', '7', '1:54.866', '8', '2:21.685'], ['11', 'R. BARRICHELLO', '1', '18:34:46', '2', '10:48.799', '3', '2:00.000', '4', '2:01.205', '5', '2:10.422', '6', '12:51.303', '7', '1:55.481', '8', '1:53.066', '9', '2:10.464', '10', '2:47.837', '11', '1:53.215', '12', '2:08.336', '13', '1:52.991', '14', '2:08.143', '15', '8:23.187', '16', '1:53.562', '17', '2:14.058'], ['12', 'P. MALDONADO', '1', '18:34:00', '2', '12:45.317', '3', '1:58.272', '4', '1:56.441', '5', '2:06.129', '6', '1:54.965', '7', '1:54.674', '8', '13:19.627', '9', '1:54.646', '10', '1:54.205', '11', '2:06.709', '12', '1:53.399', '13', '2:09.000', '14', '9:27.465', '15', '1:54.693', '16', '2:21.223'], ['14', 'A. SUTIL', '1', '18:34:12', '2', '12:17.963', '3', '1:56.726', '4', '1:55.640', '5', '1:53.748', '6', '2:14.139', '7', '12:38.255', '8', '1:52.758', '9', '2:02.598', '10', '1:52.251', '11', '2:07.798', '12', '5:51.049'], ['15', 'P. DI RESTA', '1', '18:32:52', '2', '12:22.701', '3', '1:57.026', '4', '1:54.561', '5', '2:07.771', '6', '12:51.613', '7', '1:53.676', '8', '1:53.098', '9', '1:58.102', '10', '1:52.435', '11', '2:17.758', '12', '7:33.650'], ['16', 'K. KOBAYASHI', '1', '18:32:55', '2', '10:40.800', '3', '5:52.811', '4', '15:21.676', '5', '1:55.225', '6', '1:54.254', '7', '2:03.717', '8', '2:06.415', '9', '16:09.601', '10', '1:53.749', '11', '2:20.629'], ['17', 'S. PEREZ', '1', '18:33:49', '2', '10:45.096', '3', '2:06.526', '4', '2:00.534', '5', '1:57.594', '6', '2:03.164', '7', '1:56.033', '8', '1:56.649', '9', '14:53.396', '10', '2:02.026', '11', '1:55.418', '12', '1:53.980', '13', '1:59.106', '14', '2:10.895', '15', '7:37.313', '16', '1:53.703', '17', '2:22.310'], ['18', 'S. BUEMI', '1', '18:32:47', '2', '10:59.276', '3', '8:23.048', '4', '1:54.188', '5', '1:54.538', '6', '13:59.534', '7', '1:53.785', '8', '2:04.145', '9', '1:59.012', '10', '1:53.821', '11', '1:58.789', '12', '9:40.133', '13', '1:53.859', '14', '2:17.701'], ['19', 'J. ALGUERSUARI', '1', '18:32:36', '2', '5:28.918', '3', '13:23.200', '4', '1:56.016', '5', '1:53.952', '6', '1:57.474', '7', '11:23.194', '8', '1:53.756', '9', '1:53.050', '10', '1:53.051', '11', '2:06.764', '12', '1:53.851', '13', '1:55.190', '14', '10:03.724', '15', '2:12.911'], ['20', 'H. KOVALAINEN', '1', '18:32:58', '2', '11:58.968', '3', '1:58.192', '4', '1:56.198', '5', '2:00.546', '6', '2:01.289', '7', '2:06.162'], ['21', 'J. TRULLI', '1', '18:33:57', '2', '30:12.728', '3', '1:57.377', '4', '1:55.601', '5', '1:56.771', '6', '2:05.573', '7', '1:54.821', '8', '2:21.975'], ['22', 'D. RICCIARDO', '1', '18:33:01', '2', '14:44.281', '3', '2:07.847', '4', '2:05.330', '5', '2:03.771', '6', '2:04.397', '7', '15:02.787', '8', '2:01.018', '9', '2:02.116', '10', '1:59.871', '11', '1:59.906', '12', '1:59.622', '13', '8:09.549', '14', '1:59.169', '15', '2:23.447'], ['23', 'N. KARTHIKEYAN', '1', '18:33:09', '2', '13:08.544', '3', '2:06.952', '4', '2:03.502', '5', '2:00.090', '6', '1:59.214', '7', '2:06.462', '8', '13:08.264', '9', '1:59.530', '10', '2:08.751', '11', '2:06.927', '12', '2:00.576', '13', '2:05.602', '14', '9:10.255', '15', '2:01.488', '16', '2:17.166'], ['24', 'T. GLOCK', '1', '18:33:45', '2', '16:02.295', '3', '2:00.943', '4', '1:59.486', '5', '1:58.792'], ['25', "J. D'AMBROSIO", '1', '18:32:40', '2', '12:01.620', '3', '2:04.360', '4', '2:01.941', '5', '1:59.960', '6', '1:58.775', '7', '2:15.267', '8', '25:13.631', '9', '9:18.781', '10', '1:57.798', '11', '2:19.425']]
fp1classification=[['1', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:48.599', '168.167', '19:20:37', '10'], ['2', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:49.005', '0.406', '167.540', '19:17:35', '15'], ['3', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:50.066', '1.467', '1.061', '165.925', '19:20:44', '16'], ['4', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:50.596', '1.997', '0.530', '165.130', '19:20:07', '11'], ['5', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:50.952', '2.353', '0.356', '164.600', '19:10:44', '12'], ['6', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:52.043', '3.444', '1.091', '162.998', '18:50:53', '14'], ['7', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:52.251', '3.652', '0.208', '162.696', '19:12:56', '13'], ['8', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:52.416', '3.817', '0.165', '162.457', '19:30:56', '12'], ['9', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:52.435', '3.836', '0.019', '162.429', '19:11:43', '13'], ['10', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:52.815', '4.216', '0.380', '161.882', '19:14:39', '13'], ['11', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:52.991', '4.392', '0.176', '161.630', '19:19:19', '17'], ['12', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:53.050', '4.451', '0.059', '161.546', '19:12:25', '17'], ['13', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:53.399', '4.800', '0.349', '161.049', '19:17:44', '18'], ['14', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:53.703', '5.104', '0.304', '160.618', '19:31:00', '19'], ['15', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:53.749', '5.150', '0.046', '160.553', '19:30:53', '12'], ['16', '9', 'B. SENNA', 'BRA', 'Lotus Renault GP', '1:53.765', '5.166', '0.016', '160.530', '19:10:40', '17'], ['17', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:53.785', '5.186', '0.020', '160.502', '19:11:51', '16'], ['18', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:54.736', '6.137', '0.951', '159.172', '18:52:12', '8'], ['19', '21', 'J. TRULLI', 'ITA', 'Team Lotus', '1:54.821', '6.222', '0.085', '159.054', '19:13:59', '9'], ['20', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:56.198', '7.599', '1.377', '157.169', '18:48:51', '8'], ['21', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:57.798', '9.199', '1.600', '155.034', '19:31:32', '13'], ['22', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:58.792', '10.193', '0.994', '153.737', '18:55:47', '6'], ['23', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:59.169', '10.570', '0.377', '153.251', '19:31:21', '17'], ['24', '23', 'N. KARTHIKEYAN', 'IND', 'HRT F1 Team', '1:59.214', '10.615', '0.045', '153.193', '18:54:27', '18']]



fp2times=[]

fp2classification=[]



fp3times=[]

fp3classification=[]


#Qualifying
qualitimes=[]

qualiclassification=[]

qualisectors=[]
qualitrap=[]
qualispeeds=[]

#Race
stops=[]
analysis=[]
chart=[]
history=[]
speeds=[]
sectors=[]
trap=[]
classification=[]

#Drivers
#from GBR, 22: KAR-> RIC
driverShort={'1':"VET",'2':"WEB",'3':"HAM",'4':"BUT",'5':"ALO",'6':"MAS",'7':"SCH",'8':"ROS",'9':"HEI",'10':"PET",'11':"BAR",'12':"MAL",'14':"SUT",'15':"RES",'16':"KOB",'17':"PER",'18':"BUE",'19':"ALG",'20':"TRU",'21':"KOV",'22':"RIC",'23':"LIU",'24':"GLO",'25':"AMB"}


#Tyre data from Pirelli
tyres=[]