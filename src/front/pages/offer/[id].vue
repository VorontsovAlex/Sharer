<template>
    <div class="offer">
       <Offer />
       <Navbar />
    </div>
</template>

<script lang="ts">
    import {loadProduct} from "~/api/product";

    export default {
        setup() {
          const route = useRoute()

          onMounted(() => {
            loadProduct(route.params.id)
          })
          return {

          }
        }
    }
</script>

<style lang="scss" scoped>
  @import "../styles/offer/offer";
</style>
