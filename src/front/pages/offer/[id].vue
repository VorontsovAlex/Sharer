<template>
    <div class="offer">
       <Offer :id="productId"/>
       <Navbar />
    </div>
</template>

<script lang="ts">
    import {loadProduct} from "~/api/product";

    export default {
        setup() {
          const route = useRoute()
          const productId = computed(() => route.params.id)

          onMounted(() => {
            loadProduct(productId)
          })

          return {
            productId
          }
        }
    }
</script>

<style lang="scss" scoped>
  @import "../styles/offer/offer";
</style>
