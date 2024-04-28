import {useMyFetch} from "~/composable/useMyFetch";

export const loadProductList = (): Promise<any> => {
    return useMyFetch('/products/',{
        method: 'get',
        body: {
        }
    })
}


export const loadProduct = (id: number): Promise<any> => {
    return useMyFetch(`/products/${id}`,{
        method: 'get',
    })
}
