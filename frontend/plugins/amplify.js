import { Amplify, Auth } from 'aws-amplify';

export default defineNuxtPlugin((nuxtApp) => {
    Amplify.configure({});

    return {
        provide: {
            auth: Auth,
        }
    }       
});

