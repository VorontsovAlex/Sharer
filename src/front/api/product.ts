import {useMyFetch} from "~/composable/useMyFetch";

export const loadProductList = (): Promise<any> => {
    return useMyFetch('/products/',{
        method: 'get',
        body: {
        }
    })
}
