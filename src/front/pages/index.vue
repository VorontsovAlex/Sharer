<template>
    <div class="index">
        <Header />
        <Directions class="index__directions" />
        <SortItems class="index__sort-items" />
        <Offers />
    </div>
</template>

<script lang="ts">
    import {useProductsStore} from "~/store/products.js";
    import {loadProductList} from "~/api/product.js";

    export default {
        setup() {
          const {productList, setProductList} = useProductsStore()
          onMounted(async () => {
            const result = await loadProductList()

            if (unref(result.data)) {
              setProductList(unref(result.data));
            }
          })

          return {
            productList,
          }
        }
    }
</script>

<style lang="scss" scoped>
  @import "./styles/index/index";
</style>
