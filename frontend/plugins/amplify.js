import { Amplify } from 'aws-amplify';
export default defineNuxtPlugin((nuxtApp) => {
    Amplify.configure({
        Auth: {
            Cognito: {
              userPoolClientId: '1mj7d2efpj8kcfmg7do0avbqda',
              userPoolId: 'eu-north-1_kx8XYWEzC',
              loginWith: { // Optional
                oauth: {
                  domain: 'https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_SvGcTQ7MA',
                  scopes: ['openid','email','profile','group'],
                  redirectSignIn: ['http://localhost:3000/redirect-login','https://sweatyduck.netlify.app/signin'],
                  redirectSignOut: ['http://localhost:3000/logout','https://sweatyduck.netlify.app/signout'],
                  responseType: 'code',
                },
                email: 'true',
                username: 'false',
              }
            }
          }        
    });  
});

