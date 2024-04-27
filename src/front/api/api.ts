import type {User} from "~/inrefaces/interfaces";
export const login = async (login: string, password: string): Promise<User | undefined> => {
    const { data } = await useFetch('/api/login')

    if (data) {
        return data
    }

    return undefined
}
