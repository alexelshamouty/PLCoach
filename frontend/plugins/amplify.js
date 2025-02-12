import { Amplify } from 'aws-amplify';
export default defineNuxtPlugin((nuxtApp) => {
    Amplify.configure({
        Auth: {
            Cognito: {
              userPoolClientId: 'be2d5d9l8ofcrjr756v1asath',
              userPoolId: 'eu-north-1_SvGcTQ7MA',
              loginWith: { // Optional
                oauth: {
                  domain: 'https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_SvGcTQ7MA',
                  scopes: ['openid','email','profile'],
                  redirectSignIn: ['http://localhost:3000/signin','https://sweatyduck.netlify.app/signin'],
                  redirectSignOut: ['http://localhost:3000/signout','https://sweatyduck.netlify.app/signout'],
                  responseType: 'code',
                },
                email: 'true',
                username: 'false',
              }
            }
          }        
    });  
});

