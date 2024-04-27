import {useMyFetch} from "~/composable/useMyFetch";

export const loadProductList = (login: string, password: string): Promise<any> => {
    return useMyFetch('/products/',{
        method: 'get',
        body: {
            email: login,
            password
        }
    })
}
