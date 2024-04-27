import {useMyFetch} from "~/composable/useMyFetch";
export const tryLogin = (login: string, password: string): Promise<any> => {
    return useMyFetch('/users/login',{
        method: 'post',
        body: {
            email: login,
            password
        }
    })
}

export const tryRegistration = (login: string, password: string): Promise<any> => {
    return useMyFetch('/users/register/',{
            method: 'post',
            body: {
                email: login,
                password
            }
    })
}

