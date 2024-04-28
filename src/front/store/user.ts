import { createSharedComposable } from '@vueuse/core'
import type {User} from "~/inrefaces/interfaces";
import {clearTokenCookie, setTokenCookie} from "~/composable/useToken";
import {number} from "vue-types";

export const useUserStore = createSharedComposable(() => {
   const user = ref({});
   const token = ref('')
    const selectedGroup = ref()
    const authenticated = ref(false)
    const setUserData = (userData: User): void => {
        user.value = userData;
    }

    const setSelectedGroup = (geoupId: number)  => {
        selectedGroup.value = geoupId;
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
        setSelectedGroup,
        selectedGroup,
    }
});
