import { createSharedComposable } from '@vueuse/core'
import type {User} from "~/inrefaces/interfaces";
import {clearTokenCookie, setTokenCookie} from "~/composable/useToken";

export const useUserStore = createSharedComposable(() => {
   const user = ref({});
   const token = ref('')
    const authenticated = ref(false)
    const setUserData = (userData: User): void => {
        user.value = userData;
    }

    const setToken = (newToken: string): void => {
        token.value = newToken;
        setTokenCookie(newToken)
    }
    const clearToken = (): void => {
        token.value = '';
        clearTokenCookie()
    }

    const setAuthenticated = (isAuthenticated: boolean): void => {
       authenticated.value = isAuthenticated
    }

    return {
        user,
        token,
        setUserData,
        setToken,
        authenticated,
        setAuthenticated,
        clearToken,
    }
});
