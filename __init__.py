from facebooktoken import FacebookTokenRefresher

app_id = "261234567890"
app_secret="3hniw8u9it5ojkdlforoir"
app_access_token="EAADvIDZCA94urhxkjfllwijrflksvldijfroer8euut3ie4uhtkedjrnfekrhyeikrfnbemdrjngqoHAZD"
checked_access_token="EAADvIDZ384ihflerkjmlwudhkefhkshfy74y8347y5i3b4jnbh5tnhhvkiujfie4e7yieuh4LqoHAZD"
ftr = FacebookTokenRefresher(
	app_id=app_id,
	app_secret=app_secret,
	short_access_token=app_access_token
)

#refresh token
results = ftr.refresh()

#get token detail
results = ftr.detail(app_access_token,checked_access_token)
print ('1323423')