@echo off

rem 执行单个用例脚本，日志写入指定目录
start cmd /k "pybot -d E:\robotframework\logs --test 代发询价 E:\Python27\Test\houtai\业务流程测试.txt"

rem 执行suit中所有的脚本,包括代发询价，代下单，客户询价，客户下单，客户申请售后，客户取消订单，客户下单激光切割，客户下单3D打印
rem start cmd /k "pybot -d E:\robotframework\logs E:\Python27\Test\houtai\业务流程测试.txt"