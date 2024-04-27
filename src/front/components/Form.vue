<template>
    <div class="form">
        <form action="#">
            <div class="form__item">
                <label
                    class="form__label"
                    for="email"
                >
                    Email:
                </label>
                <input
                    v-model="login"
                    type="text"
                    id="email"
                    name="email"
                    placeholder="Email"
                    class="form__input form__input--text"
                >
            </div>
            <div class="form__item">
                <label
                    class="form__label"
                    for="password"
                >
                    Пароль:
                </label>
              password -  {{password}}
                <input
                    v-model="password"
                    type="password"
                    id="password"
                    name="password"
                    placeholder="Пароль"
                    class="form__input form__input--text"
                >
            </div>

          {{errorMessage}}
          <div
              v-if="isRegistered"
              class="form__row"
          >
            <div>
              <input
                  type="checkbox"
                  id="remember"
                  class="form__input form__input--checkbox"
              >
              <label for="remember">Запомнить меня</label>
            </div>
            <router-link to="/registration">Зарегистрироваться</router-link>
          </div>
            <div
                v-if="!isRegistered"
                class="form__row"
            >
                <router-link to="/login">Войти</router-link>
            </div>
            <Button
                v-if="isRegistered"
                @click="onLoginClick"
                class="form__action form-action"
            >
                <span class="form-action__text">Войти</span>
            </Button>

            <Button
                v-else
                :disabled="isRegistrationDisabled"
                @click="onRegistrationClick"
                type="button"
                class="form__action form-action"
            >
                <span  class="form-action__text">Зарегистрироваться</span>
            </Button>
        </form>
    </div>
</template>

<script lang="ts">
    import { Button } from 'ant-design-vue';
    import {tryRegistration, tryLogin} from "~/api/api";
    import {useUserStore} from "~/store/user";

    export default {
        components: {
            Button,
        },
        props: {
            isRegistered: {
                type: Boolean,
                default: true,
            },
        },
        setup() {
          const router = useRouter()
          const login = ref('asd');
          const password = ref('asd');
          const errorMessage = ref('');
          const {setToken} = useUserStore();
          const onRegistrationClick = async () => {
            const response = await tryRegistration(unref(login), unref(password))

            if (response.status === 'success') {
              await router.push('/login');
            } else {
              errorMessage.value = unref(response.error)?.data?.detail;
            }
          }
          const onLoginClick = async () => {
            const response = await tryLogin(unref(login), unref(password))

            if (unref(response.data)?.access_token) {
              setToken(unref(response.data).access_token);
              await router.push('/')
            } else {
              errorMessage.value = unref(response.data).error;
            }
          }

          const isRegistrationDisabled = computed(() => unref(password).length === 0 || unref(login).length === 0)
          return {
            login,
            password,
            onRegistrationClick,
            onLoginClick,
            isRegistrationDisabled,
            errorMessage,
          }
        }
    }
</script>

<style lang="scss">
  @use "./styles/form/form";
</style>
