import {useUserStore} from "~/store/user";

export default defineNuxtRouteMiddleware((to, from) => {
    const {setAuthenticated} = useUserStore();
    const token = useCookie('access_token');

    if (token.value) {
        setAuthenticated(true);
    }

    if (token.value && to?.name === 'login') {
         return navigateTo('/');
    }

    if (!token.value && to?.name !== 'login') {
        abortNavigation();
       //  return navigateTo('/login');
    }
})
