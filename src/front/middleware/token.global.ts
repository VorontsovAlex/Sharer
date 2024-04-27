import {useUserStore} from "~/store/user";
import {LOGIN, REGISTRATION} from "~/constants/routes";

export default defineNuxtRouteMiddleware((to, from) => {
    const {setAuthenticated} = useUserStore();
    const token = useCookie('access_token');
    const listForUnregistered = [LOGIN, REGISTRATION]

    if (token.value) {
        setAuthenticated(true);
    }

    console.log('token.value', token.value)
    if (token.value && listForUnregistered.includes(to?.name)) {
         return navigateTo('/');
    }
})
