# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xml.etree.ElementTree as ET 
import time

# Create your views here.
@csrf_exempt
def erduo(request):
	if request.method == "GET":
		signature = request.GET.get('signature',None)
		timestamp = request.GET.get('timestamp',None)
		nonce = request.GET.get('nonce',None)
		echostr = request.GET.get('echostr',None)
		token = 'nx5bw'

		hashlist = [token,timestamp,nonce]
		hashlist.sort()
		print(hashlist)
		hashstr = "".join([s for s in hashlist])
		hashstr = hashlib.sha1(hashstr).hexdigest()
		if hashstr == signature:
			return HttpResponse(echostr)
		else:
			return HttpResponse("field")

	else:
		othercontent =autoreply(request)
		return HttpResponse(othercontent)



def autoreply(request):
	try:
		webData = request.body
		xmlData = ET.fromstring(webData)

		msg_type = xmlData.find("MsgType").text
		ToUserName = xmlData.find('ToUserName').text
		FromUserName = xmlData.find('FromUserName').text
		CreateTime = xmlData.find('CreateTime').text
		MsgType = xmlData.find('MsgType').text
		MsgId = xmlData.find('MsgId').text

		toUser = FromUserName
		fromUser = ToUserName

		if msg_type == "text":

			content = "您好，欢迎关注Erduo1928！"
			replyMsg = TextMsg(toUser,fromUser,content)
			print("成功了！！！！！！！")
			print(replyMsg)
			return replyMsg.send()

		elif msg_type =="image" :
			content = "图片消息！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()

		elif msg_type =="voice" :
			content = "语音消息！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()

		elif msg_type =="video" :
			content = "视频消息！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()

		elif msg_type =="shortvideo" :
			content = "小视频！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		elif msg_type =="location" :
			content = "位置消息！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()


		else:
			msg_type =="link" 
			content = "链接消息！"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()

	except Exception as Argment:
		return Argment


class Msg(object):

	def __init__(self,xmlData):
		self.ToUserName = xmlData.find()
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
	def __init__(self, toUserName, fromUserName, content):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content

	def send(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[text]]></MsgType>
		<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		return XmlForm.format(**self.__dict)

	