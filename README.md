Fortune_Form

1. What happens when you press the “submit” button? Paste the full URL you are sent to on submit.
When you press the submit button you're redirected to a new url, with a "Your file was not found" message. file:///fortune_results?name=Joanelly&gender=female&Bunny=Bunny&favcolor=%23663fff
2. What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?
They are the names in the form.
3. What are the values of the URL query string? How do they correspond to what the user entered or typed?
The values in the URL string are the options the user submitted.
----
OpenWeather API:

1. Describe the data contained in the API response. What can we discern about the weather in the specified city?

It provides things such as weather, describing things such as "clouds", including the timezones as well.

2. How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)

request.args.get(temp)
