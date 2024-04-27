<template>
    <div class="sort-items">
        <div
            v-for="sortItem in sortItems"
            :key="sortItem.id"
            class="sort-items__item"
        >
            <!-- TODO @programm1st: @click & :src -->
            <button
                @click="selectSort(sortItem)"
                type="button"
                class="sort-items-item-element"
                :class="sortItem.class"
            >
                <span class="sort-items-item-element__text">
                    {{ sortItem.text }}
                </span>
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        setup() {
            // TODO @programm1st
            const sortItems = ref([
                {
                    id: 0,
                    text: 'Топ',
                    class: 'sort-items-item-element--is-selected',
                },
                {
                    id: 1,
                    text: 'Рекомендации',
                    class: '',
                },
                {
                    id: 2,
                    text: 'Рядом',
                    class: '',
                },
            ]);

            const selectSort = (item) => {
                item.class = 'sort-items-item--is-selected';
            };

            return {
                sortItems,
                selectSort,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/sortItems/sort-items";
</style>
