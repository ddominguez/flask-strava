## Info

This is a simple flask application that handles authentication to the Strava API.

It was made to be used with the front-end client(FRONTEND_APP_DOMAIN) located [here](https://github.com/ddominguez/react-strava-app).


## Requests

### Authorize access to Strava

```GET /strava_authorize```

### Request access token from Strava

```GET /strava_token```

**Params**

Name | Description
---- | -------------
code | The code parameter obtained in the strava authorization redirect.

## Run locally
```
env \
FLASK_APP=application.py \
FLASK_ENV=development \
STRAVA_CLIENT_ID=<STRAVA_CLIENT_ID> \
STRAVA_CLIENT_SECRET=<STRAVA_CLIENT_SECRET> \
REDIRECT_URI=<FRONTEND_APP_DOMAIN>/strava_redirect \
flask run
```

## Strava
To obtain a client id and a client secret you must first [create a Strava API App](https://developers.strava.com/).