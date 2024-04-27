import {useUserStore} from "~/store/user";

export const useMyFetch: typeof useFetch = (request, opts?) => {
    const config = useRuntimeConfig()
    const {token} = useUserStore()

    //TODO проработать токен
    return useFetch(request, { baseURL: 'http://172.23.128.1:8080/',
        headers:  {
            'Authorization':   `Bearer ${unref(token)}`,
        },
        ...opts
    })
}
