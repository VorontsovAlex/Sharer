import { createSharedComposable } from '@vueuse/core'
import type {User} from "~/inrefaces/interfaces";

export const useUserStore = createSharedComposable(() => {
   const user = ref({});
   const token = ref('')
    const authenticated = ref(false)
    const setUserData = (userData: User): void => {
        user.value = userData;
    }

    const setToken = (newToken: string): void => {
        token.value = newToken;
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
    }
});
