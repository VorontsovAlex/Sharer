import { createSharedComposable } from '@vueuse/core'
import type {ProductList, User} from "~/inrefaces/interfaces";
import {clearTokenCookie, setTokenCookie} from "~/composable/useToken";

export const useProductsStore = createSharedComposable(() => {
    const searchQuery = ref('');
   const productList = ref<ProductList[]>([]);

    const setProductList = (newProductList: ProductList[]): void => {
        productList.value = newProductList;
    }
    const setSearchQuery = (newSearchQuery: string): void => {
        searchQuery.value = newSearchQuery
    }

    return {
        productList,
        searchQuery,
        setSearchQuery,
        setProductList
    }
});
