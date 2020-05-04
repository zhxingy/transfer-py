# 原理流媒体transfer API列表

## 系统相关
### 系统信息
#### 功能
`获取当前系统信息`

#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=system`

##### 请求参数

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_result/result/@ret | int | 是 |  错误代码
api_result/result/@reason| string | 是 | 错误描述
api_result/system/server_id| int | 是 | 服务器ID
api_result/system/server_domain| string |是 | 服务器域
api_result/system/version | string | 是 | 系统版本
api_result/system/start_time|string |是| 启动时间
api_result/system/auth_remain| float | 是| 授权剩余天数
api_result/system/current_time | string | 是| 当前时间


#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=system`
##### 响应示例
```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_result>
  <system>
    <server_id>4011</server_id>
    <server_domain>/forcetech/group1</server_domain>
    <version>ForceLiveTransfer/May 28 2018 13:59:08</version>
    <start_time>2020-05-04 17:41:46</start_time>
    <auth_remain>16294.455359</auth_remain>
    <current_time>Mon, 04 May 2020 09:48:50 GMT</current_time>
  </system>
  <result ret="0" reason="success"/>
</api_result>
```
### 系统高级信息
#### 功能
`查看系统配置文件`
#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=conf_file`

##### 请求参数

##### 响应参数
`响应配置文件文本内容`


#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=conf_file`
##### 响应示例
```angular2
JTIzJUI3JUZFJUNFJUYxJUM2JUY3SUQlMkMlRDMlRjIlMkMlRDQlREQlQ0ElQjElQzMlQkIlRDMlRDAlRDMlQzMlQjQlQTYlMEFzZXJ2ZXIuaWQlMjAlM0QlMjA0MDExJTBBc2VydmVyLmRvbWFpbiUyMCUzRCUyMC9mb3JjZXRlY2gvZ3JvdXAxJTBBJTIzY21zJTIwbm90aWZ5JTIwdXJsJTI4aHR0cCUzQS8vMTAuMTAuMTAuMTAvdXBkYXRlJTNGaWQlM0RfaWQlMjZuYW1lJTNEX25hbWUlMjZzdGF0dXMlM0Rfc3RhdHVzJTI2cXVldWUlM0QxJTI5JTBBc2VydmVyLmNtc19ub3RpZnlfdXJsJTNEaHR0cCUzQS8vMTIyLjExMy4yNi4zJTNBODA4MC9mb3JjZXRlY2gvdHJhbnNmZXIlMEElMEElMjMlQjclRkUlQ0UlRjElQzYlRjclQjAlRjMlQjYlQThJUCUyMDAuMC4wLjAlQjElRUQlQ0ElQkUlQjAlRjMlQjYlQTglQ0IlRjklRDMlRDAlRDMlRDAlRDAlQTclQjUlQzRJUCUyMDEyNy4wLjAuMSVCMSVFRCVDQSVCRSVCMCVGMyVCNiVBOCVCMSVCRSVCQiVGQSUyMCVENiVCQiVDNCVEQyVCMSVCRSVCQiVGQSVDQSVCOSVEMyVDMyUwQXNlcnZlci5pcCUzRDAuMC4wLjAlMEElMEElMjMlQjUlQzclQzIlQkMlQjAlRDclQzMlRkIlQjUlQTVJUCUyMCVENiVCQiVEMyVEMCVENSVFMiVCOCVGNklQJUIyJUM1JUM0JURDJUI1JUM3JUMyJUJDJTIwJUM4JUU3JUI5JUZCJUNBJUM3MC4wLjAuMCVCRSVDRCVCMiVCQiVENyVGNiVDRiVERSVENiVDNiUwQXNlcnZlci5sb2dpbi5pcCUzRDAuMC4wLjAlMEElMEElMjNrZXklMEElMjMlQkMlRDMlQzMlRENLRVklMEFzZXJ2ZXIuZW5jcnlwdF9rZXklM0RfX2ZvcmNldGVjaCUyMUAlMjMlMEElMEElMjNsaXZlJTBBJTIzJUMxJUY3JUI0JUFCJUNBJUU0JUNBJUIxJUNCJUY5JUNBJUI5JUQzJUMzJUI1JUM0JUI2JUNCJUJGJURBJTI4VURQJTI5JTBBc2VydmVyLmxpdmUucG9ydCUyMCUzRDk5MDAlMEElMjMlQzklRTglRDYlQzNUUyVCRCVEMyVDQSVENSVCQiVCQSVCNCVFNiVCNCVGMyVEMCVBMSUyMCVCNSVBNSVDRSVCQiVDQSVDN0tCJTJDJUIxJUQ4JUQwJUVCJUNBJUM3MTg4JUI1JUM0JUIxJUI2JUNBJUZEJTBBc2VydmVyLmxpdmUudHNfcGFja19sZW4lM0Q5NDAlMEElMjNkYXRhJTIwc3RvcmFnZSUwQSUyMyVDMyVCRiVCOCVGNiVDNyVEMCVDNiVBQyVCNSVDNCVDQSVCMSVCQyVFNCVCMyVBNCVCNiVDOCUwQXNlcnZlci5zdG9yYWdlLmZpbGV0aW1lJTIwJTNEJTIwMTUlMEElMEElMjMlQ0ElRkQlQkUlREQlQjUlQzQlQjElQkUlQjUlRDglQjQlRTYlQjQlQTIlQzIlQjclQkUlQjYlMEFzZXJ2ZXIubGl2ZS5wYXRoJTIwJTNEJTIwLi9kYXRhJTBBJTBBJTIzbWVkaWElMEElMjMlQ0MlRTElQjklQTklQzElRjclQjUlQzQlRDQlQUQlQ0ElQkMlQ0ElRTQlQjMlRjYlMjhUQ1AlMkNIVFRQJTI5JTIwJUIxJUM4JUM4JUU3JUMxJUY3SUQlQ0UlQUExJUI1JUM0JUNBJUU0JUIzJUY2JUNFJUFBJTIwaHR0cCUzQS8vbG9jYWxpcCUzQTk5OTEvMSUwQXNlcnZlci5tZWRpYS5wb3J0JTIwJTNEJTIwODA4MCUwQXNlcnZlci5jcHVfY29yZV9udW0lMjAlM0QlMjA0JTBBJTBBJTIzd2ViJTIwaHR0cHJlc3QlMjBhcGklMjBhbmQlMjBzaW1wbGUlMjBtYW5hZ2VyJTIwd2Vic2l0ZSUwQXNlcnZlci53ZWIucG9ydCUyMCUzRCUyMDgwOTAlMEFzZXJ2ZXIud2ViLmRvY19yb290JTIwJTNEJTIwLi93ZWIvdHJhbnNmZXIvemhfQ04lMEFzZXJ2ZXIud2ViLnVzZXIlMjAlM0QlMjBhZG1pbiUwQXNlcnZlci53ZWIucGFzc3dvcmQlMjAlM0QlMjBhZG1pbiUwQXNlcnZlci5ydHQlM0QxMDAlMEE=
```


## 直播管理
### 列出直播频道
#### 功能
`查询所有频道的详细信息`

#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_channellist`

##### 请求参数

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
channellist/result/@ret | int | 是 |  错误代码
channellist/result/@reason| string | 是 | 错误描述
channellist/channel/@id| string | 是 | 频道ID
channellist/channel/@name| string | 是 | 频道名称
channellist/channel/@url| string | 是 | 频道地址
channellist/channel/@ptl| string | 是 | 频道协议
channellist/channel/@ptlimpl| string | 是 | 频道实现
channellist/channel/@filetype| string | 是 | 格式
channellist/channel/@time_delay| int | 是 | 时延
channellist/channel/@bandw| int | 是 | 



#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_channellist`
##### 响应示例


```
<?xml version="1.0" encoding="utf-8"?>

<channellist> 
  <channel id="1" name="test" url="http://190.2.137.73:35891/bongacams/0/index.m3u8" ptl="http" ptlimpl="hls" filetype="ts" time_delay="180" bandw="2"/>  
  <result ret="0" reason="success"/>
</channellist>
```

### 创建直播频道
#### 功能
`新增一个直播频道`
#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_add`



##### 请求参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
id| string | 是 |  频道ID
name| string | 是 | 频道名称
url| string | 是 | 频道地址, 多个用“$”连接
ptlimpl| string | 是 | 频道实现
filetype| string | 是 | 格式
time_delay| int | 是 | 时延

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_object/result/@ret | int | 是 |  错误代码
api_object/result/@reason| string | 是 | 错误描述



#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_add&id=111&name=111&url=http://127.0.0.1:/index.m3u9&ptlimpl=hls&filetype=m3u8&time_delay=180`
##### 响应示例

```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_object>
  <result ret="0" reason="success"/>
</api_object>
```

### 删除直播频道
#### 功能
`删除一个直播频道`


#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_delete`


##### 请求参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
id| string | 是 |  频道ID

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_object/result/@ret | int | 是 |  错误代码
api_object/result/@reason| string | 是 | 错误描述




#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_delete&id=2`
##### 响应示例

```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_object>
  <result ret="0" reason="success"/>
</api_object>
```

### 修改直播频道
#### 功能
`修改一个直播频道相关信息`


#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_modify`


##### 请求参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
id| string | 是 |  频道ID
name| string |是 | 频道名称
time_delay| int |是 | 时延

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_object/result/@ret | int | 是 |  错误代码
api_object/result/@reason| string | 是 | 错误描述



#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_modify&id=2&name=111&time_delay=180`
##### 响应示例

```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_object>
  <result ret="0" reason="success"/>
</api_object>
```

### 查询直播频道
#### 功能
`查询一个直播频道的详细信息`


#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_id`


##### 请求参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
id| string | 是 |  频道ID

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_result/result/@ret | int | 是 |  错误代码
api_result/result/@reason| string | 是 | 错误描述
api_result/channel/@id| string | 是 | 频道ID
api_result/channel/@name| string | 是 | 频道名称
api_result/channel/@url| string | 是 | 频道地址
api_result/channel/@ptl| string | 是 | 频道协议
api_result/channel/@ptlimpl| string | 是 | 频道实现
api_result/channel/@filetype| string | 是 | 格式
api_result/channel/@time_delay| int | 是 | 时延
api_result/channel/@bandw| int | 是 | 
api_result/channel/stat/status | string | 是 | 是否启动
api_result/channel/stat/state | string | 是 |状态
api_result/channel/stat/run_time | string | 是 | 运行时间(秒)
api_result/channel/stat/transfer_kbps | string | 是 |  速度(kbps)
api_result/channel/stat/wait_count | string | 是 | 等待文件数
api_result/channel/stat/filename | string | 是 | 当前文件
api_result/channel/stat/current_time | string | 是 | 当前时间


#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_id&id=2`
##### 响应示例
```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_result>
  <channel id="2" name="测试" url="http://127.0.0.1:8080/122$http://127.0.0.1:8080/123$http://127.0.0.1:8080/124" ptl="http" ptlimpl="hls" filetype="ts" time_delay="180" bandw="2">
    <stat>
      <status>wait</status>
      <state>start</state>
      <run_time>2</run_time>
      <transfer_kbps>0</transfer_kbps>
      <filename/>
      <wait_count>0</wait_count>
      <current_time>20200504T095930</current_time>
    </stat>
  </channel>
  <result ret="0" reason="success"/>
</api_result>

```

### 重置直播频道
#### 功能
`重置一个直播频道(删除切片文件)`


#### HTTP请求方式
`GET`

#### URL
`http://192.168.101.222:8090/api?func=live_reset`


##### 请求参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
id| string | 是 |  频道ID

##### 响应参数
参数名称 | 类型 | 是否必须 | 描述
---|---|---|---
api_object/result/@ret | int | 是 |  错误代码
api_object/result/@reason| string | 是 | 错误描述


#### 示例
##### 请求示例
`GET http://192.168.101.222:8090/api?func=live_reset&id=2`

##### 响应示例
```angular2
<?xml version="1.0" encoding="utf-8"?>

<api_object>
  <result ret="0" reason="success"/>
</api_object>
```