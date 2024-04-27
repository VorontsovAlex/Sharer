const DATA_KEY = 'access_token';

function getCookie(name: string) {
    const cookieList = document.cookie.split(';');

    return cookieList.find((cookie) => {
        const cookieName = cookie.split('=')[0];

        if (cookieName === ` ${name}` || cookieName === `${name}`) {
            return true;
        }
    });
}
export function setTokenCookie(token: string) {
    const expire = new Date();

    expire.setHours(expire.getHours() + 1);
    document.cookie = `${DATA_KEY}=${token};${expire}; path=/; secure;`;
}

export function clearTokenCookie() {
    const tokenCookie = getCookie(DATA_KEY);

    if (tokenCookie) {
        document.cookie = DATA_KEY + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
}
