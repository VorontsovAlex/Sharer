import type {User} from "~/inrefaces/interfaces";
import {useMyFetch} from "~/composable/useMyFetch";
export const login = async (login: string, password: string): Promise<User | undefined> => {
    const { data } = await useFetch('/api/login')

    if (data) {
        return data
    }

    return undefined
}

export const registration = async (login: string, password: string): Promise<User | undefined> => {
    const { data } = await useMyFetch('/users/register',{
            method: 'post',
            body: {
                email: login,
                password
            }
        })

    debugger
    if (data) {
        return data
    }

    return undefined
}
