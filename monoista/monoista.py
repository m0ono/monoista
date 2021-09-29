import requests
import json
import webbrowser
from importlib import resources
import io
def login(username, password):
	url = "https://www.instagram.com/accounts/login/ajax/"
	headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "279",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
        "x-instagram-ajax": "901e37113a69",
        "x-requested-with": "XMLHttpRequest"
    }
	data = {"username": username, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + password, "queryParams": "{}",
            "optIntoOneTap": "false"}
	log = requests.session().post(url, headers=headers, data=data)
	if ('"authenticated":true') in log.text:
		print(f"Done login >> {username}:{password}")
	elif ('"authenticated":false') in log.text:
		print(f"incorrect password >> {username}:{password}")
	elif ('"message":"checkpoint_required"') in log.text:
		print("Secure >> {username}:{password}")
	elif('"error_type":"ip_block"') in log.text:
		print("You have ip block try to use vpn")
	elif ('"message":"Please wait a few minutes before you try again."') in log.text:
		print("You've blocked wait a few minutes before you tru again")
def avatar(username):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; win64; x64) AppleWebKit/537.36"
}
	if "@" in username:
		url = "https://instagram.com/" + username[1:31] +"/?__a=1"
		picdata = requests.get(url,headers=headers).json()
		picture = picdata["graphql"]["user"]["profile_pic_url_hd"]
		webbrowser.open(picture)
	else:
		url = f"https://instagram.com/{username}/?__a=1"
		picdata = requests.get(url, headers=headers).json()
		picture = picdata["graphql"]["user"]["profile_pic_url_hd"]
		webbrowser.open(picture)
def image(post):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; win64; x64) AppleWebKit/537.36"
}
	url = post[0:40] + "?__a=1"
	data = requests.get(url,headers=headers).json()
	img = data["graphql"]["shortcode_media"]["display_url"]
	webbrowser.open(img)
def video(post):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; win64; x64) AppleWebKit/537.36"
}
	url = post[0:40] + "?__a=1"
	data = requests.get(url,headers=headers).json()
	vid = data["graphql"]["shortcode_media"]["video_url"]
	webbrowser.open(vid)
def change_info(username, password, name, email, phone_number, target):
	url = "https://www.instagram.com/accounts/login/ajax/"
	headers = {
	        "accept": "*/*",
	        "accept-encoding": "gzip, deflate,br",
	        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
	        "content-length": "279",
	        "content-type": "application/x-www-form-urlencoded",
	        "origin": "https://www.instagram.com",
	        "referer": "https://www.instagram.com/",
	        "sec-fetch-dest": "empty",
	        "sec-fetch-site": "same-origin",
	        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	        "x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
	        "x-ig-app-id": "936619743392459",
	        "x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
	        "x-instagram-ajax": "901e37113a69",
	        "x-requested-with": "XMLHttpRequest"
	}
	data = {"username": username, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + password, "queryParams": "{}",
	            "optIntoOneTap": "false"}
	log = requests.session().post(url, headers=headers, data=data)
	if ('"authenticated":true') in log.text:
		print(f"Done login >> {username}:{password}")
		c = log.cookies
		c1 =c.get_dict()
		url_edit = "https://www.instagram.com/accounts/edit/"
		headers_edit = {'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '476',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie':  "sessionid="+c1['sessionid']+";ds_user_id="+c1['ds_user_id']+";csrftoken="+c1['csrftoken'],
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/edit/',
		'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
		'x-asbd-id': '437806',
		'x-csrftoken': c1['csrftoken'],
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6J7a',
		'x-instagram-ajax': 'caee87137ae9',
		'x-requested-with': 'XMLHttpRequest'
		}
		data_edit = {
			"first_name": name,
			"email": email,
			"username": target,
			"phone_number": phone_number,
			"external_url": "",
			}
		change = requests.session().post(url_edit, headers = headers_edit, data = data_edit).text
		if ('"status":"ok"') in change:
			print(f"new info : username => {target}, name => {name}, email => {email}, phone number => {phone_number}")
		elif('"error_type":"ip_block"') in change:
			print("you have ip block try to use vpn")
		elif ('"message":"Please wait a few minutes before you try again."') in change:
			print("You've blocked wait 1m")
		else:
			print("username isn't available now")
	elif ('"authenticated":false') in log.text:
		print(f"incorrect >> {username}:{password}")
	elif ('"message":"checkpoint_required"') in log.text:
		print(f"Secure >> {username}:{password}")
	elif('"error_type":"ip_block"') in log.text:
		print("You have ip block try to use vpn")
	elif ('"message":"Please wait a few minutes before you try again."') in log.text:
		print("You've blocked wait a few minutes before you tru again")
def make_acc(username, password, phone_number):
	try:
		import secrets
	except:
		import os
		os.system("pip install secrets")
		os.system("clear")
	cookie = secrets.token_hex(8)*2
	if phone_number=="":
		print("[!] Please enter a phone number")
	else:
		url_attempt = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
		headers = {
			'HOST': "www.instagram.com",
			'KeepAlive' : 'True',
			'user-agent' : "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
			'Cookie': cookie,
			'Accept' : "*/*",
			'ContentType' : "application/x-www-form-urlencoded",
			"X-Requested-With" : "XMLHttpRequest",
			"X-IG-App-ID": "936619743392459",
			"X-Instagram-AJAX" : "missing",
			"X-CSRFToken" : "missing",
			"Accept-Language" : "en-US,en;q=0.9"}
		data_attempt = {
			'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
			'phone_number': phone_number,
			'username': username,
			'first_name': "",
			'month': '1',
			'day': '1',
			'year': '1999',
			'client_id': 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9',
			'seamless_login_enabled': '1',
			'opt_into_one_tap': 'fals'
		}
		attempt = requests.session().post(url_attempt, headers = headers, data = data_attempt)
		url_code = 'https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
		data_code = {
			'client_id': 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9',
			'phone_number': phone_number,
			'phone_id': '',
			'big_blue_token': ''
		}
		code = requests.session().post(url_code, headers=headers, data=data_code).text
		if 'Looks like your phone number may be incorrect.' in code:
			print("[!] Phone Number is incorrect")
		elif 'Please wait a few minutes before you try again.' in code:
			print('[!] Please wait a few minutes before you try again.')
		elif 'true' in code:
			sms = input("[+] Enter the code : ")
			url_sms = 'https://www.instagram.com/accounts/web_create_ajax/'
			data_sms = {
				'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
				'phone_number': phone_number,
				'username': username,
				'first_name': "",
				'month': '1',
				'day': '1',
				'year': '1999',
				'sms_code': sms,
				'client_id': 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9',
				'seamless_login_enabled': '1',
				'tos_version': 'row'}
			make = requests.session().post(url_sms,headers=headers,data=data_sms).text
			if "That code isn't valid." in make:
				print("[!] Code isn't valid")
			elif 'true' in make:
				print(f"[-] Done Created Account >> {usermame} : {password}")
			elif "checkpoint_required" in make:
				print(f'[!] checkpoint required >> {username}, {password}')
			else:
				print('[!] Something wrong')
		else:
			print("[!] There is something wrong or the account has been banned")
def id(target):
	try:
		url = f"https://www.instagram.com/{target}/?__a=1"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; win64; x64) AppleWebKit/537.36"
		}
		get = requests.get(url, headers=headers).json()
		id = get["graphql"]["user"]["id"]
		print(f"Username >> {target}\nID >> {id}")
	except:
		print("[!] Not found")