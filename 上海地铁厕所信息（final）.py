import requests
import json
import pandas as pd
from tqdm import tqdm  # 引入tqdm库

# 定义基础的API链接
base_url = 'https://m.shmetro.com/interface/metromap/metromap.aspx?func=stationInfo&stat_id='

# 上海地铁18条线路各站点ID
station_ids = ['0111', '0112', '0113', '0114', '0115', '0116', '0117', '0118', '0119', '0120', '0121', '0122', '0123', '0124', '0125', '0126', '0127', '0128', '0129', '0130', '0131', '0132', '0133', '0134', '0135', '0136', '0137', '0138', '0234', '0235', '0236', '0237', '0238', '0239', '0240', '0241', '0242', '0243', '0244', '0245', '0246', '0247', '0248', '0249', '0250', '0251', '0252', '0253', '0254', '0255', '0256', '0257', '0258', '0259', '0260', '0261', '0262', '0263', '0311', '0312', '0313', '0314', '0315', '0316', '0317', '0318', '0319', '0320', '0321', '0322', '0323', '0324', '0325', '0326', '0327', '0328', '0329', '0330', '0331', '0332', '0333', '0334', '0335', '0336', '0337', '0338', '0339', '0401', '0402', '0403', '0404', '0405', '0406', '0407', '0408', '0409', '0410', '0411', '0412', '0413', '0414', '0415', '0416', '0417', '0418', '0419', '0420', '0421', '0422', '0423', '0424', '0425', '0426', '0501', '0502', '0503', '0504', '0505', '0506', '0507', '0508', '0509', '0510', '0511', '0512', '0513', '0514', '0515', '0516', '0517', '0518', '0519', '0520', '0521', '0522', '0523', '0524', '0525', '0526', '0527', '0528', '0529', '0530', '0531', '0532', '0533', '0534', '0535', '0536', '0537', '0538', '0621', '0622', '0623', '0624', '0625', '0626', '0627', '0628', '0629', '0630', '0631', '0632', '0633', '0634', '0635', '0636', '0637', '0638', '0639', '0640', '0641', '0642', '0643', '0644', '0645', '0646', '0721', '0722', '0723', '0724', '0725', '0726', '0727', '0728', '0729', '0730', '0731', '0732', '0733', '0734', '0735', '0736', '0737', '0738', '0739', '0740', '0741', '0742', '0743', '0744', '0745', '0746', '0747', '0748', '0749', '0750', '0751', '0752', '0753', '0820', '0821', '0822', '0823', '0824', '0825', '0826', '0827', '0828', '0829', '0830', '0831', '0832', '0833', '0834', '0835', '0836', '0837', '0838', '0839', '0840', '0841', '0842', '0843', '0844', '0845', '0846', '0847', '0848', '0849', '0918', '0919', '0920', '0921', '0922', '0923', '0924', '0925', '0926', '0927', '0928', '0929', '0930', '0931', '0932', '0933', '0934', '0935', '0936', '0937', '0938', '0939', '0940', '0941', '0942', '0943', '0944', '0945', '0946', '0947', '0948', '0949', '0950', '0951', '0952', '1018', '1019', '1020', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1029', '1030', '1031', '1032', '1033', '1034', '1035', '1036', '1037', '1038', '1039', '1040', '1041', '1042', '1043', '1044', '1045', '1046', '1047', '1048', '1049', '1050', '1051', '1052', '1053', '1054', '1055', '1056', '1057', '1058', '1059', '1060', '1061', '1062', '1063', '1064', '1065', '1066', '1067', '1068', '1069', '1070', '1071', '1072', '1073', '1074', '1114', '1115', '1116', '1117', '1118', '1119', '1120', '1121', '1122', '1123', '1124', '1125', '1126', '1127', '1128', '1129', '1130', '1131', '1132', '1133', '1134', '1135', '1136', '1137', '1138', '1139', '1140', '1141', '1142', '1143', '1144', '1145', '1146', '1147', '1148', '1149', '1150', '1151', '1152', '1153', '1154', '1155', '1156', '1157', '1158', '1159', '1160', '1161', '1162', '1163', '1220', '1221', '1222', '1223', '1224', '1225', '1226', '1227', '1228', '1229', '1230', '1231', '1232', '1233', '1234', '1235', '1236', '1237', '1238', '1239', '1240', '1241', '1242', '1243', '1244', '1245', '1246', '1247', '1248', '1249', '1250', '1251', '1321', '1322', '1323', '1324', '1325', '1326', '1327', '1328', '1329', '1330', '1331', '1332', '1333', '1334', '1335', '1336', '1337', '1338', '1339', '1340', '1341', '1342', '1343', '1344', '1345', '1346', '1347', '1348', '1349', '1350', '1351', '1421', '1422', '1423', '1424', '1425', '1426', '1427', '1428', '1429', '1430', '1431', '1432', '1433', '1434', '1435', '1436', '1437', '1438', '1439', '1440', '1441', '1442', '1443', '1444', '1445', '1446', '1447', '1448', '1449', '1450', '1451', '1521', '1522', '1523', '1524', '1525', '1526', '1527', '1528', '1529', '1530', '1531', '1532', '1533', '1534', '1535', '1536', '1537', '1538', '1539', '1540', '1541', '1542', '1543', '1544', '1545', '1546', '1547', '1548', '1549', '1550', '1621', '1622', '1623', '1624', '1625', '1626', '1627', '1628', '1629', '1630', '1631', '1632', '1633', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1728', '1729', '1730', '1731', '1732', '1733', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1831', '1832', '1833', '1834', '1835', '1836', '1837', '1838', '1839', '1840', '1841', '1842', '1843', '1844', '1845', '1846', '4101', '4102', '4103', '4104', '4105', '4106']
# 存储所有站点信息的列表
all_station_info = []

# 使用tqdm包装循环，添加进度条显示
for station_id in tqdm(station_ids, desc="Processing Stations", unit="station"):
    # 构建完整的API链接
    api_url = base_url + station_id
    
    # 发送请求获取页面内容
    response = requests.get(api_url)
    
    try:
        # 检查响应内容是否为有效的JSON字符串
        if not response.text:
            raise ValueError("Empty response")
        
        # 解析JSON数据
        data = json.loads(response.text)
        
        # 提取车站名
        station_name = data[0]['name_cn']
        
        # 提取车站线路
        if len(station_id) == 4:
            station_line = station_id[:2]
        elif len(station_id) == 3:
            station_line = station_id[0]
        else:
            station_line = 'N/A'
        
        # 提取厕所信息的JSON字符串
        toilet_info_json_str = data[0]['toilet_position']
        
        # 如果厕所信息的JSON字符串为空，则将specific_description设置为'无厕所'
        if not toilet_info_json_str:
            specific_description = '无厕所'
        else:
            # 解析厕所信息的JSON字符串
            toilet_info_json = json.loads(toilet_info_json_str)
            
            # 提取特定lineno对应的厕所信息
            specific_lineno = str(int(station_line))
            specific_description = '无厕所'  # 默认值
            
            for toilet in toilet_info_json['toilet']:
                if str(toilet['lineno']) == specific_lineno:
                    specific_description = toilet['description'].split('：', 1)[-1]
                    break
    
        # 存储当前站点的信息
        current_station_info = {
            '车站路线': station_line,
            '车站名': station_name,
            '车站编号':station_id,
            '厕所信息': specific_description
        }
        
        # 将当前站点信息添加到总列表
        all_station_info.append(current_station_info)
    
    except Exception as e:
        print(f"Error processing station ID {station_id}: {e}")
        continue

# 将所有站点信息转换为DataFrame
df = pd.DataFrame(all_station_info)

# 重新排列列的顺序
df = df[['车站路线', '车站名', '车站编号', '厕所信息']]

# 输出DataFrame，包括显示"无厕所"的情况
print(df)

# 将DataFrame保存为Excel文件
df.to_excel('station_info.xlsx', index=False)
