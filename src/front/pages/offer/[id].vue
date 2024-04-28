<template>
    <div class="offer">
       <Offer :id="productId"/>
       <Navbar />
    </div>
</template>

<script lang="ts">
    import {loadProduct} from "~/api/product";
    import {offers} from "~/components/constants/offers";

    export default {
        setup() {
          const route = useRoute()
          const productId = computed(() => route.params.id)

          const offer = unref(offers).find((itemOffer) => {
            return Number(itemOffer.id) === Number(unref(productId))
          })
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
